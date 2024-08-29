a = 1
b = 2
c = a + b

for x in range(10):
    y = x * c
#1 the debugger stops before executing the line of the breakpoint not after
#2 because the debugger is inside the loop, it will rerun until the loop is over (until 9 for this one) then go to next break point

message = "Hello World!"

print(message)
