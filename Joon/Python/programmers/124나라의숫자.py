def solution(n):
    answer = ''
    onetwofour = [1,2,4]
    
    while n:
        n -= 1
        answer += str(onetwofour[n%3])
        n //= 3
    
    return answer[::-1]