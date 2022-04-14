
# #문자열과 내장함수

# #upper, lower

msg="It is Time"
print(msg.upper()) #대문자
print(msg.lower()) #소문자
print(msg) #원본은 그대로 유지

# #find, count

tmp=msg.upper()
print(tmp)
print(tmp.find('T')) #T가 있는 index 리턴 #처음 나온 index 번호만 출력 #1
print(tmp.count('T')) #T가 몇개가 있는가? #2


print(msg)
print(msg[:2]) #처음부터 2번 전까지 추출 (부분 문자열) #IT
print(msg[3:5]) #3번부터 4번까지 #is
print(len(msg)) #문자열 길기 (공백포함)

for i in range(len(msg)):
    print(msg[i], end=" ")
print() #I t   i s   T i m e

for x in msg:
    print(x, end=" ") #I t   i s   T i m e
print()


#isupper

for x in msg:
    if x.isupper():
        print(x, end=" ")  #대문자일 경우 참
print()


#islower

for x in msg:
    if x.islower():
        print(x, end=" ")  #대문자일 경우 참
print()

#isalpha (알파벳)

for x in msg:
    if x.isalgha():
        print(x, end="")
print()


#문자 -> 아스키넘버 ord

tmp="AZ"
for x in tmp:
    print(ord(x)) #65, 90

tmp="az"
for x in tmp:
    print(ord(x)) #97, 122


# 아스키넘버 -> 문자 chr

tmp=65
print(chr(tmp)) #A



