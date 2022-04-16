'''
셀프 넘버 #4673번

셀프 넘버는 1949년 인도 수학자 D.R. Kaprekar가 이름 붙였다. 양의 정수 n에 대해서 d(n)을 n과 n의 각 자리수를 더하는 함수라고 정의하자. 예를 들어, d(75) = 75+7+5 = 87이다.

양의 정수 n이 주어졌을 때, 이 수를 시작해서 n, d(n), d(d(n)), d(d(d(n))), ...과 같은 무한 수열을 만들 수 있다.

예를 들어, 33으로 시작한다면 다음 수는 33 + 3 + 3 = 39이고, 그 다음 수는 39 + 3 + 9 = 51, 다음 수는 51 + 5 + 1 = 57이다. 이런식으로 다음과 같은 수열을 만들 수 있다.

33, 39, 51, 57, 69, 84, 96, 111, 114, 120, 123, 129, 141, ...

n을 d(n)의 생성자라고 한다. 위의 수열에서 33은 39의 생성자이고, 39는 51의 생성자, 51은 57의 생성자이다. 생성자가 한 개보다 많은 경우도 있다. 예를 들어, 101은 생성자가 2개(91과 100) 있다.

생성자가 없는 숫자를 셀프 넘버라고 한다. 100보다 작은 셀프 넘버는 총 13개가 있다.
1, 3, 5, 7, 9, 20, 31, 42, 53, 64, 75, 86, 97

10000보다 작거나 같은 셀프 넘버를 한 줄에 하나씩 출력하는 프로그램을 작성하시오.'''


# 생성자가 있는 숫자 = 숫자 + 숫자의 각 자리 수 # n(39) = 33+3+3=39 #33은 39의 생성자
# 생성자가 없는 숫자 = 셀프 넘버, 100보다 작은 셀프 넘버는 1, 3, 5, 7, 9, 20, 31, 42, 53, 64, 75, 86, 92

# numbers_set = set(range(1, 10001)) #1부터 10000까지 숫자
# self_numbers_set = set() #생성자가 없는 숫자



#생성자 구하는 함수 만들기

def d(n): #숫자 33
    num_sum = 0
    num_str = list(str(n)) #값을 한자리씩 나눠주기 [3, 3]

    for i in num_str:
        num_sum += int(i) #3

    return n + num_sum # 33 + 6 = 39


# line 30 : n = 33
# line 31 : n = 33, num_sum = 0
# line 32 : n = 33, num_sum = 0, num_str = [3, 3]
# line 34 : n = 33, i = 3, num_str = [3, 3]
# line 35 : num_sum = 3




non_self_numbers = set()
self_numbers_set = set()
all_number = set(range(1, 10001))



#생성자가 있는 숫자
for j in range(1, 10001): #1부터 10000까지
    non_self_numbers.add(d(j)) #set 함수는 append X add O

#모든 숫자들 - 생성자가 있는 숫자 빼주기
self_numbers_set = all_number - non_self_numbers
# list(self_numbers_set)
# self_numbers_set.sort()

#셀프 넘버 하나씩 출력하기
for self_number in sorted(self_numbers_set):
    print(self_number)
