
# 최솟값 구하기

arr = [5, 3, 7, 2, 5, 2, 6]
arrMin=float('inf') #무한대값

for i in range(len(arr)): #arr의 길이
    if arr[i] < arrMin:
        arrMin=arr[i]
print(arrMin)


arr = [5, 3, 7, 2, 5, 2, 6]
arrMin=arr[0] #무한대값

for i in range(1, len(arr)): #arr의 길이
    if arr[i] < arrMin:
        arrMin=arr[i]
print(arrMin)
