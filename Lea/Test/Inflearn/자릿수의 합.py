'''

자릿수의 합

N개의 자연수가 입력되면 각 자연수의 자릿수의 합을 구하고,
그 합이 최대인 자연수를 출력 하는 프로그램을 작성하세요.
각 자연수의 자릿수의 합을 구하는 함수를 def digit_sum(x)를 꼭 작성해서 프로그래밍 하세요.


▣ 입력설명

첫 줄에 자연수의 개수 N(3<=N<=100)이 주어지고,
그 다음 줄에 N개의 자연수가 주어진다,
각 자연수의 크기는 10,000,000를 넘지 않는다.


▣ 출력설명

자릿수의 합이 최대인 자연수를 출력한다.
자릿수의 합이 같을 경우 입력순으로 먼저인 숫자 를 출력합니다.


▣ 입력예제 1

3
125 15232 97


▣ 출력예제 1
97

'''


# 자릿수의 합 구하기

def digit_sum(x):
    sum = 0
    for i in str(x): #123 -> 1 2 3 이렇게 문자열로
        sum+=int(i) #다시 숫자로 변환해서 다 더해준다
    return sum #sum의 값을 반환해준다.

n = int(input()) #자연수 갯수
numbers = list(map(int, input().split())) #n개의 자연수







#최댓값 구하기

nums_max = 0 #최대값을 넣어줄 변수만들기

for x in numbers: #number 리스트 안에 있는 값 하나씩 가져오기
    if digit_sum(x) > nums_max:
        nums_max = digit_sum(x) #최대값이 된다.
        answer = x #리스트 안에 있는 x의 값
print(answer)


# sum_of_digits = 최대값 구하는 변수





#다른방법



