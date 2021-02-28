from collections import deque

n = int(input())
array = deque()
command_list = []

for i in range(n) :
    command = input()
    command_list.append(command)

for command in command_list :
    cmd = command.split()

    if cmd[0] == "push_front" :
        array.appendleft(cmd[1])

    elif cmd[0] == "push_back" :
        array.append(cmd[1])

    elif cmd[0] == "pop_front" :
        if len(array) != 0 :
            print(array.popleft())
        else :
            print(-1)
    elif cmd[0] == "pop_back" :
        if len(array) != 0 :
            print(array.pop())
        else :
            print(-1)
    
    elif cmd[0] == "size" :
        print(len(array))

    elif cmd[0] == "empty" :
        if len(array) == 0 :
            print(1)
        else :
            print(0)

    elif cmd[0] == "front" :
        if len(array) != 0 :
            print(array[0])
        else :
            print(-1)
    elif cmd[0] == "back" :
        if len(array) != 0 :
            print(array[-1])
        else :
            print(-1)

