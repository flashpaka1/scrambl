import sys

readLines = []

try: 
    fileName = sys.argv[1]
    file = open(fileName)
    readLines = file.read().split("\n")
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

def pop(index=-1):
    if len(stack) < 1:
        err("Error: Stack underflow")
    return stack.pop(index)

while count >= 0 and count < len(readLines):
    parts = readLines[count].split(" ")
    cmd = parts[0]

    if cmd == 'CRACK':
        stack.append(int(parts[1]))  # push value
    elif cmd == 'SERVE':
        print(pop())  # pop value
    elif cmd == 'BEAT':
        x = pop()
        stack[-1] += x  # add top 2 values
    elif cmd == 'STRAIN':
        x = pop()
        stack[-1] -= x  # subtract top 2 values
    elif cmd == 'MAKEANOMELETTE':
        x = pop()
        stack[-1] *= x  # multiply top 2 values
    elif cmd == 'SCRAMBLE':
        x = pop()
        stack[-1] /= x  # divide top 2 values
    elif cmd == 'CRY':
        break  # leave program
    elif cmd == 'INCUBATE':
        stack.append(stack[-1])  # copy top value
    elif cmd == 'FLIP':
        x = pop()
        y = pop()
        stack.append(x)
        stack.append(y)  # switch top 2 values
    elif cmd == 'FRY':
        print(chr(pop()))  # pop top as ASCII
    elif cmd == 'POACH':
        print(int(pop()))  # pop top as int
    elif cmd == 'BURN':
        stack = []  # drop stack
    elif cmd == 'BATCH':
        for i in range(int(parts[1])):
            stack.append(chr(stack[-1]))  # repeat top value n times as ASCII
    elif cmd == 'OVEREASY':
        for i in range(int(parts[1])):
            stack.append(int(stack[-1]))  # repeat top value n times as int
    elif cmd == "EAT":
      try:
         stack.append(ord(input("")[0]))   
      except IndexError:
         stack.append(0)

    count += 1

print('')
