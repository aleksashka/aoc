# https://www.reddit.com/r/adventofcode/comments/3vr4m4/comment/cxq0omv/
import sys, string

def value(n):
    if n.isdigit():
        return int(n)
    else:
        return gates[n]

instructions = []
gates = {}
for c1 in string.ascii_lowercase:
    gates[c1] = 0
    for c2 in string.ascii_lowercase:
        gates[c1 + c2] = 0
        
for line in sys.stdin:
    if (line == '\n'):
        break
    instructions.append(line.rstrip())

for i in range(0, 26*26): # brute force rerun until guaranteed stability
    for line in instructions:
        word = line.split(' ');
        if len(word) == 3: # basic input
            gates[word[2]] = value(word[0])
        elif len(word) == 4: # can only be not
            gates[word[3]] = ~ value(word[1])
        elif word[1] == 'AND':
            gates[word[4]] = value(word[0]) & value(word[2])
        elif word[1] == 'OR':
            gates[word[4]] = value(word[0]) | value(word[2])
        elif word[1] == 'LSHIFT':
            gates[word[4]] = value(word[0]) << value(word[2])
        elif word[1] == 'RSHIFT':
            gates[word[4]] = value(word[0]) >> value(word[2])
    
print(gates[sys.argv[1]])
