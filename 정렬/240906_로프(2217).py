N = int(input())
ropes = [int(input()) for _ in range(N)]

ropes.sort()

max_weight = 0

for i in range(N):
    max_weight = max(max_weight, ropes[i] * (N - i))

print(max_weight)