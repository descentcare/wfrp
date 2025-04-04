#!/usr/bin/env python3
import sys
engrus = dict(zip("qwertyuiop[]asdfghjkl;'zxcvbnm,.`",
                  "йцукенгшщзхъфывапролджэячсмитьбюё"))
query = ''
if len(sys.argv) > 1:
    query = ''.join(map(lambda c: engrus[c] if c in engrus else c, sys.argv[1].lower()))

outlines = []

for filename in ["characteristics.csv", "skills.csv"]:
    with open(filename, "r") as f:
        outlines += [l for l in f.readlines() if query in l.lower()]
print(*outlines)

