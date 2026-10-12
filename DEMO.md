# Synthetic demo

Use the installed command with `example.json`; the expected deterministic output is:

```json
{
  "ambiguous": true,
  "quorum": 2,
  "trace": [
    {
      "kind": "point",
      "lower": 0,
      "sources": [
        "a"
      ],
      "upper": 0
    },
    {
      "kind": "open_interval",
      "lower": 0,
      "sources": [
        "a"
      ],
      "upper": 2
    },
    {
      "kind": "point",
      "lower": 2,
      "sources": [
        "a",
        "b"
      ],
      "upper": 2
    },
    {
      "kind": "open_interval",
      "lower": 2,
      "sources": [
        "a",
        "b"
      ],
      "upper": 4
    },
    {
      "kind": "point",
      "lower": 4,
      "sources": [
        "a",
        "b"
      ],
      "upper": 4
    },
    {
      "kind": "open_interval",
      "lower": 4,
      "sources": [
        "a"
      ],
      "upper": 6
    },
    {
      "kind": "point",
      "lower": 6,
      "sources": [
        "a",
        "c"
      ],
      "upper": 6
    },
    {
      "kind": "open_interval",
      "lower": 6,
      "sources": [
        "a",
        "c"
      ],
      "upper": 8
    },
    {
      "kind": "point",
      "lower": 8,
      "sources": [
        "a",
        "c"
      ],
      "upper": 8
    },
    {
      "kind": "open_interval",
      "lower": 8,
      "sources": [
        "a"
      ],
      "upper": 10
    },
    {
      "kind": "point",
      "lower": 10,
      "sources": [
        "a"
      ],
      "upper": 10
    }
  ],
  "windows": [
    [
      2,
      4
    ],
    [
      6,
      8
    ]
  ]
}
```

This proves the documented example only, not production efficacy or adoption.

Independent exhaustive check: run `python oracle.py` from the repository root. It compares output membership against direct source-interval counting for 648 combinations, including closed boundary points and interior half-unit probes. It is a finite regression check, not a general proof.
