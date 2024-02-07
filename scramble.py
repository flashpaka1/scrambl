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
pc = 0

# push value -> CRACK
# pop value -> SERVE
# add top 2 values -> BEAT
# subtract top 2 values -> STRAIN
# multiply top 2 values -> MAKEANOMELETTE
# divide top 2 values -> SCRAMBLE
# leave program -> EAT
# copy top value -> INCUBATE
# switch top 2 values -> FLIP
# pop top as ASCII -> FRY
# pop top as int -> POACH
# drop stack -> BURN
# repeat top value n times as ascii -> BATCH
# repeat top value n times as int -> CARTON