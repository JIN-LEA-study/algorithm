

'''
나는 요리사다

"나는 요리사다"는 다섯 참가자들이 서로의 요리 실력을 뽐내는 티비 프로이다. 각 참가자는 자신있는 음식을 하나씩 만들어오고, 서로 다른 사람의 음식을 점수로 평가해준다. 점수는 1점부터 5점까지 있다.

각 참가자가 얻은 점수는 다른 사람이 평가해 준 점수의 합이다. 이 쇼의 우승자는 가장 많은 점수를 얻은 사람이 된다.

각 참가자가 얻은 평가 점수가 주어졌을 때, 우승자와 그의 점수를 구하는 프로그램을 작성하시오.

'''


human = [list(map(int, input().split())) for _ in  range(5)]
human_score = [0]*5
score = 0

for i in range(5):
    sum=0
    for j in range(4):
        sum+=human[i][j]
        human_score[i]=sum
        score=max(score, sum)

for i in range(5):
    if human_score[i] == score:
        print(i+1, score)
        break