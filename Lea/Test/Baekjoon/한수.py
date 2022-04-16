'''

한수 1065번

어떤 양의 정수 X의 각 자리가 등차수열을 이룬다면,

(일정한 규칙을 가진 수의 나열)

그 수를 한수라고 한다.




등차수열은 연속된 두 개의 수의 차이가 일정한 수열을 말한다.

ex :
number가 있다고 치면 355
number[0] - number[1] == number[1] - number[2] 같으면 등차수열

3-5 == 5-5

N이 주어졌을 때, 1보다 크거나 같고,
N보다 작거나 같은 한수의 개수를 출력하는 프로그램을 작성하시오.



#방법 2 n = 1000,000

# 몫으로 구하기..? 몫으로 구한 값들을 변수에 각각 담아주고 == 를 이용한다. 하지만 숫자가 커지면 커질 수록 식이 길어짐
















입력
첫째 줄에 1,000보다 작거나 같은 자연수 N이 주어진다.

출력
첫째 줄에 1보다 크거나 같고, N보다 작거나 같은 한수의 개수를 출력한다.


'''


# ex :
# number가 있다고 치면
# number[0] - number[1] == number[1] - number[2] 같으면 등차수열








# n = 1000000 이하



n = int(input())
hansoo_cnt = 0

# def is_hansoo(n):
#     if n < 100:
#         return True
#     else:
#         hansoo_true = list(map(int, str(n)))
#         if hansoo_true[0] - hansoo_true[1] == hansoo_true[1] - hansoo_true[2]:
#             return True
#         else:
#             return False


def is_hansoo(n):
    if n < 100:
        return True
    else:
        hansoo_true = list(map(int, str(n)))
        for i in range(1, len(hansoo_true)-1): #인덱스+1이 없기 때문에
            if hansoo_true[0] - hansoo_true[1] != hansoo_true[i] - hansoo_true[i+1]:
                return False
        return True



for i in range(1, n+1): #1부터 n까지
    # 함수 안에 넣어서 True 이면 cnt +1
    if is_hansoo(i):
        hansoo_cnt += 1

print(hansoo_cnt)