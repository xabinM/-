import sys
input = sys.stdin.readline

def solution():
    string = [i for i in input().strip()]

    left_stack = string
    right_stack = []
    M = int(input())

    for _ in range(M):
        command = input().split()
        if command[0] == 'L':
            if left_stack:
                right_stack.append(left_stack.pop())
        elif command[0] == 'D':
            if right_stack:
                left_stack.append(right_stack.pop())
        elif command[0] == 'B':
            if left_stack:
                left_stack.pop()
        elif command[0] == 'P':
            left_stack.append(command[1])

    print(''.join(left_stack + list(reversed(right_stack))))

solution()