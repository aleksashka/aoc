# https://pastebin.com/3Y2S8yUW
with open('input.txt') as f:
    inputs = f.readlines()
 
Wires = {}
done = list()
 
i = 0
 
for x in range(0,len(inputs)):
    done.append(False)
 
while i < len(inputs):
    if done[i] == False:
 
        currentTask = inputs[i].replace("\n","")
        splitTask = currentTask.split(" -> ")
        targetId = splitTask[1]
 
        if "AND" in splitTask[0]: #AND OPERATION
            invwires = splitTask[0].split(" AND ")
            if invwires[0] == "1" and invwires[1] in Wires:
                Wires[targetId] = 1 & Wires[invwires[1]]
                done[i] = True
            elif invwires[0] in Wires and invwires[1] in Wires:
                #print "Starting AND OPERATION"
                Wires[targetId] = Wires[invwires[0]] & Wires[invwires[1]]
                done[i] = True
        elif "OR" in splitTask[0]: #OR OPERATION
            invwires = splitTask[0].split(" OR ")
            if invwires[0] in Wires and invwires[1] in Wires:
                #print "Starting OR OPERATION"
                Wires[targetId] = Wires[invwires[0]] | Wires[invwires[1]]
                done[i] = True
        elif "LSHIFT" in splitTask[0]:
            lshift = splitTask[0].split(" LSHIFT ")
            if lshift[0] in Wires:
                Wires[targetId] = Wires[lshift[0]] << int(lshift[1])
                done[i] = True
        elif "RSHIFT" in splitTask[0]:
            rshift = splitTask[0].split(" RSHIFT ")
            if rshift[0] in Wires:
                Wires[targetId] = Wires[rshift[0]] >> int(rshift[1])
                done[i] = True
        elif "NOT" in splitTask[0]:
            notwire = splitTask[0].replace("NOT ", "")
            if notwire in Wires:
                Wires[targetId] = 65535 - Wires[notwire]
                done[i] = True
 
        else:
            try:
                Wires[targetId] = int(splitTask[0])
                done[i] = True
            except ValueError:
                if splitTask[0] in Wires:
                    Wires[targetId] = Wires[splitTask[0]]
 
    if "a" in Wires:
        print("FOUND IT!!!! " + str(Wires["a"]))
        break
 
    elif i+1 == len(inputs):
        executed = 0
        for x in range(0,len(inputs)):
            if done[x] == True:
                executed += 1
        print("executed " + str(executed) + " instructions")
        i = 0
 
    else:
        i += 1
