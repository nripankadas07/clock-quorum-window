"""Independent exhaustive membership oracle; run from repository root."""
import itertools
from clock_quorum_window import core as m
intervals=[(a,b) for a in range(-1,2) for b in range(a,2)]
count=0
for triple in itertools.product(intervals,repeat=3):
    for quorum in [1,2,3]:
        data={'sources':[{'id':str(i),'lower':a,'upper':b} for i,(a,b) in enumerate(triple)],'quorum':quorum}
        result=m.run(data)
        for twice in range(-3,4):
            expected=sum(2*a<=twice<=2*b for a,b in triple)>=quorum
            actual=any(2*a<=twice<=2*b for a,b in result['windows'])
            assert expected==actual,(data,result,twice)
        count+=1
print(count,'membership cases pass')
