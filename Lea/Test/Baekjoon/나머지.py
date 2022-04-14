
'''

나머지 3052번

두 자연수 A와 B가 있을 때, A%B는 A를 B로 나눈 나머지 이다. 예를 들어, 7, 14, 27, 38을 3으로 나눈 나머지는 1, 2, 0, 2이다.

수 10개를 입력받은 뒤, 이를 42로 나눈 나머지를 구한다. 그 다음 서로 다른 값이 몇 개 있는지 출력하는 프로그램을 작성하시오.

'''

# nums = []

# for i in range(10): #10개 한줄씩
#     num = int(input()) % 42 #입력 받는다.
#     nums.append(num) #리스트에 담아준다.
#     #리스트 안에 있는 인덱스끼리 서로 같은지 비교하기
#     if num[i]


# nums = []

# for i in range(10):
#     num = int(input()) % 42
#     if num in nums:
#         continue #참이면 그냥 위로 올라가, 거짓이면 내려가
#     nums.append(num) #배열에 없을 경우 (중복되지 않을 경우 )






a = []
for i in range(10): #10개를 한줄씩
    num = int(input()) #입력받기
    a.append(num) #입력값을 list에 남아주기
a = set(a) #중복삭제
print(len(a)) #길이







