def run(data):
    sources,quorum=data.get("sources"),data.get("quorum")
    if not isinstance(sources,list) or not 1<=len(sources)<=128 or type(quorum) is not int or not 1<=quorum<=len(sources):
        raise ValueError("1..128 sources and valid quorum required")
    intervals={}
    for source in sources:
        if not isinstance(source,dict) or set(source)!={"id","lower","upper"}:
            raise ValueError("source fields: id, lower, upper")
        ident,lo,hi=source["id"],source["lower"],source["upper"]
        if not isinstance(ident,str) or not ident or len(ident)>128 or ident in intervals or type(lo) is not int or type(hi) is not int or abs(lo)>2**63-1 or abs(hi)>2**63-1 or lo>hi:
            raise ValueError("unique source IDs and ordered integer bounds required")
        intervals[ident]=(lo,hi)
    points=sorted({v for bounds in intervals.values() for v in bounds})
    pieces,trace=[],[]
    for i,p in enumerate(points):
        ids=sorted(k for k,(lo,hi) in intervals.items() if lo<=p<=hi)
        trace.append({"kind":"point","lower":p,"upper":p,"sources":ids})
        if len(ids)>=quorum:
            pieces.append([p,p])
        if i+1<len(points):
            nxt=points[i+1]
            ids=sorted(k for k,(lo,hi) in intervals.items() if lo<=p and hi>=nxt)
            trace.append({"kind":"open_interval","lower":p,"upper":nxt,"sources":ids})
            if len(ids)>=quorum:
                pieces.append([p,nxt])
    windows=[]
    for lo,hi in sorted(pieces):
        if windows and lo<=windows[-1][1]:
            windows[-1][1]=max(hi,windows[-1][1])
        else:
            windows.append([lo,hi])
    return {"quorum":quorum,"windows":windows,"ambiguous":len(windows)>1,"trace":trace}
