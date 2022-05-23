
'''
회문 문자열 검사

N개의 문자열 데이터를 입력받아 앞에서 읽을 때나 뒤에서 읽을 때나 같은 경우(회문 문자열) 이면 YES를 출력하고 회문 문자열이 아니면 NO를 출력하는 프로그램을 작성한다.
단 회문을 검사할 때 대소문자를 구분하지 않습니다.

입력
첫 줄에 정수 N(1<=N<=20)이 주어지고, 그 다음 줄부터 N개의 단어가 입력된다. 각 단어의 길이는 100을 넘지 않는다.

출력
각 줄에 해당 문자열의 결과를 YES 또는 NO로 출력한다.

입력예제
5
level
moon
abcba
soon
gooG

출력예제
#1 YES
#2 NO
#3 YES
#4 NO
#5 YES


'''

#%d 정수, %f 실수, %s 문자열

#방법1
n = int(input()) #정수로 받음
for i in range(n):
  string = input() #문자열 받음
  string = string.upper() #대문자화
  size = len(string) #a문자열의 길이
  for j in range(size//2):
    if string[j] != string[-1-j]:
      print('#%d No' %(i+1))
      break
  else:
    print('#%d YES' %(i+1))


#방법2 (내가 푼 방법)
n= int(input())
for i in range(n):
  string = input()
  string = string.upper() #모든 문자 대문자로 변경
  # 맨 뒷자리부터 한단계씩 작아짐
  if string == string[::-1]:
    print('#%d YES' %(i+1))
  else:
    print('#%d No' %(i+1))
