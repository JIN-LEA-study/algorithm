



'''

숫자의 합 11720

N개의 숫자가 공백 없이 쓰여있다. 이 숫자를 모두 합해서 출력하는 프로그램을 작성하시오.

'''

#1
num=int(input())
nums = input()
sum = 0

for i in range(num):
    sum += int(nums[i])
print(sum)

#2

# n = input()
# print(sum(map(int, input())))