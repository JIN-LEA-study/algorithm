

'''

1. 문제를 나눠쓰기
2. 하루 3문제를 못풀면 잘못된 것 (두호가 내준 숙제 기준)


대표값

N명의 학생의 수학점수가 주어집니다. N명의 학생들의 평균(소수 첫째자리 반올림)을 구하고, N명의 학생 중 평균에 가장 가까운 학생은 몇 번째 학생인지 출력하는 프로그램을 작성하세요.

평균과 가장 가까운 점수가 여러 개일 경우 먼저 점수가 높은 학생의 번호를 답으로 하고,
높은 점수를 가진 학생이 여러 명일 경우 그 중 학생번호가 빠른 학생의 번호를 답으로 합니다.

▣ 입력설명
첫줄에 자연수 N(5<=N<=100)이 주어지고, 두 번째 줄에는 각 학생의 수학점수인 N개의 자연 수가 주어집니다. 학생의 번호는 앞에서부터 1로 시작해서 N까지이다.

▣ 출력설명
첫줄에 평균과 평균에 가장 가까운 학생의 번호를 출력한다. 평균은 소수 첫째 자리에서 반올림합니다.

▣ 입력예제 1
10
45 73 66 87 92 67 75 79 75 80

▣ 출력예제
74 7


예제설명)
평균이 74점으로 평균과 가장 가까운 점수는 73(2번), 75(7번), 75(9번)입니다.
여기서 점수가 높은 75(7번), 75(9번)이 답이 될 수 있고, 75점이 두명이므로 학생번호가 빠른 7번이 답이 됩니다.'''




#인프런코드

num = int(input())
scores = list(map(int, input().split()))
ave = round(sum(scores))

for idx, x in enumerate(scores):
    tmp = abs(x-ave)
    if tmp < min:
        min = tmp
        score = x
        res = idx + 1
    elif tmp == min :
        if x > score:
            score = x
            res = idx + 1





#1

n = int(input())
scores = list(map(int, input().split()))
average = round(sum(scores)/n) #평균값 구하기
min_value = 999999999
min_index = -1


#2 평균값과 점수 거리 구하기

# x = 70
# average = 60

# if x > average:
#     result = x-average
# else:
#     result = average-x

for i in range(len(scores)):
    if scores[i] > average:
        diff = scores[i] - average
    else:
        diff = average-scores[i]
    if min_value > diff:
        min_value = diff
        min_index = i #최소값일 때 i(인덱스)
    elif min_value == diff and scores[min_index] < scores[i]:
        min_index = i

print(min_index+1)


# print(min_index+1) #인덱스는 0부터 시작하니까, 번째의 값을 구할 경우 +1




