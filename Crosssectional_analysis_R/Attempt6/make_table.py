#!/usr/bin/env python

# import built-in modules below

# import own modules below

with open('output2.csv', 'r') as readfile:
    lines = readfile.readlines()
    lines = [i.strip() for i in lines]
    lines = [i.split() for i in lines]
    lines = [list(map(float, i)) for i in lines]

coff = []
error = []
Ps = []
table = []

t = 1
for line in lines:
    if len(line)==0:
        t += 1
    elif len(line)==1:
        coff.append(line[0])
        error.append('--')
        Ps.append('--')
        table.append(t)
    else:
        coff.append(line[0])
        error.append(line[1])
        Ps.append(line[2])
        table.append(t)
coff = [c if c!=0 else 0.0001 for c in coff]

Ps2 = []
for p in Ps:
    if p == '--':
        Ps2.append('')
    elif p<0.01:
        Ps2.append('***')
    elif p<0.05:
        Ps2.append('**')
    elif p<0.1:
        Ps2.append('*')
    else:
        Ps2.append('')

entries = []        
for i in range(96):
    entry = '${:.4}^{{{:.4}}}$\\\$({:.4})$'
    entry = entry.format(coff[i], Ps2[i], error[i])
    entry = '\\begin{tabular}[c]{@{}l@{}}' + entry + '\end{tabular}'
    entries.append(entry)

lines = [[] for i in range(12)]
for i in range(96):
    lines[i%12].append(entries[i])
lines = ['\t'.join(i) for i in lines]
[print(i) for i in lines]






















