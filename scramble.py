import sys

readLines = []

try: 
    fileName = sys.argv[1]
    file = open(fileName)
    readLines  = file.read().split("\n")
    file.close()
except Exception as e:
    print(f"File error.\n{e}")
    sys.exit()

stack = []
count = 0
dinnerPlate = ''

def err(str):
   print("\n" + str + f" at line {count}")
   sys.exit(0)

def pop(index = -1):
    if len(stack) < 1:
        err("Error: Stack underflow")
    return stack.pop(index)

while count >= 0 and count < len(readLines):
    parts = readLines[count].split(" ")
    sub = parts[0]

    # push value -> CRACK
    if readLines[0] == 'CRACK':
        stack.append(readLines[1])
    # pop value -> SERVE
    elif readLines[0] == 'SERVE':
        print(pop())
    # add top 2 values -> BEAT
            # TURN THE BEAT AROUND (google "taeb")
    elif readLines[0] == 'BEAT':
        x = pop()
        stack[-1] += x
    # subtract top 2 values -> STRAIN
    elif readLines[0] == 'STRAIN':
        x = pop()
        stack[-1] -= x
    # multiply top 2 values -> MAKEANOMELETTE
    elif readLines[0] == 'MAKEANOMELETTE':
        x = pop()
        stack[-1] *= x
    # divide top 2 values -> SCRAMBLE
    elif readLines[0] == 'SCRAMBLE':
        x = pop()
        readLines[-1] /= x
    # leave program -> EAT
    elif readLines[0] == 'EAT':
        break
    # copy top value -> INCUBATE
    elif readLines[0] == 'INCUBATE':
        readLines.append(stack[-1])
    # switch top 2 values -> FLIP
    elif readLines[0] == 'FLIP':
        x = pop()
        y = pop()
        stack.append(x)
        stack.append(y)
    # pop top as ASCII -> FRY
    elif readLines[0] == 'FRY':
        print(chr(pop()))
    # pop top as int -> POACH
    elif readLines[0] == 'POACH':
        print(int(pop()))
    # drop stack -> BURN
    elif readLines[0] == 'BURN':
        stack = []
    # repeat top value n times as ascii -> BATCH
    elif readLines[0] == 'BATCH':
        for i in readLines[1]:
            stack.append(chr(stack[-1]))
    # repeat top value n times as int -> OVEREASY
    elif readLines[0] == 'OVEREASY':
        for i in readLines[1]:
            stack.append(int(stack[-1]))
    count + 1

print('')