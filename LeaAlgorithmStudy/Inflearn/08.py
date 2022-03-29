
#리스트와 내장함수

#random 모듈을 r로 쓰겠다는 뜻
import random as r

#list 하나의 변수에 값을 여러개 모아둔 것

a=[] #빈 list
b=list()

a=[1, 2, 3, 4, 5] #list안에 값을 저장
# print(a) #[1, 2, 3, 4, 5]
# print(a[0]) #1

b=list(range(1, 11))
# print(b) #[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

c=a+b
# print(c) #[1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


#list 내장함수

#append() list 뒤에 값 추가

print(a)
a.append(6)
print(a)

#insert() 해당 인텍스에 추가

print(a)
a.insert(3, 7)
print(a)

#pop() list 맨 뒤에 값을 제거
a.pop()
print(a)
a.pop(3) #해당 인텍스 값이 제거
print(a)

#remove list 안에 특정값을 제거
a.remove(4)
print(a) #[1, 2, 3, 5]

#index 해당값의 인덱스를 출력
print(a.index(5)) #3

a=list(range(1, 11))
print(a)

#sum 모든 합을 출력
print(sum(a)) #55

#max 제일 큰 값 출력
print(max(a)) #10

#min 제일 작은 값 출력
print(min(a)) #1

print(min(7, 5)) #5 인자값 중 최솟값

print(a)

#shuffle(무작위로 섞음) 게임 만들때 많이 씀
r.shuffle(a)
print(a)

#sort() 오름차순
a.sort()
print(a)

# reverse=True  내림차순
a.sort(reverse=True)
print(a)

#clear() 리스트를 다시 빈리스트로 만듦
a.clear()
print(a)



