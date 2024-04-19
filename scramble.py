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
        length = len(stack)
        for i in range(length):
            print(chr(pop()), end='')
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
        x = input()
        for char in reversed(x):  # Reverse the input here to push it in correct order
            stack.append(ord(char))
    elif cmd == 'FRY':
        print(chr(pop()))  # pop top as ASCII
    elif cmd == 'POACH':
        print(int(pop()))  # pop top as int
    elif cmd == 'BURN':
        stack = []  # drop stack
    elif cmd == 'BITE': # take input as int
        stack.append(int(input()))
    elif cmd == 'BATCH': # This will push `x` onto the stack `n` times
        if len(stack) < 2:
            err("Error: Stack underflow at BATCH command")
        n = int(pop())
        if not isinstance(n, int):
            err("Error: Non-integer value for repetition count")
        x = pop()
        for _ in range(n):
            stack.append(x)
    elif cmd == 'OVEREASY': # repeat top value n times as int
        for i in range(int(parts[1])):
            stack.append(int(stack[-1]))  
    elif cmd == "EAT": # take input as ASCII
      try:
         stack.append(ord(input("")[0]))   
      except IndexError:
         stack.append(0)
    elif cmd == 'ORDER':
        x = input("")
        for char in x:
            stack.append(ord(char)) # get string input
    elif cmd == 'DEVILLE':
        for i in range((int(stack[-1]))):
            print(chr(pop()))  # pop all as ASCII
    elif cmd == 'BOIL':
        length = len(stack)
        for i in range(length):
            print(chr(pop()), end='')  # Print without newline and space between characters

    count += 1

print('')
