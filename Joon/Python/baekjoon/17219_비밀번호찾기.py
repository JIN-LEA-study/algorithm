import sys
input = sys.stdin.readline;

N, M = map(int,input().split())

hashMap = {}

for i in range(N):
    password = input().split()
    hashMap[password[0]] = password[1]


for j in range(M):
    password2 = input().split()
    print(hashMap[password2[0]])