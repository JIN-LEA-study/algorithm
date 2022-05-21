
'''
최소힙은 완전이진트리로 구현된 자료구조입니다. 그 구성은 부모 노드값이 왼쪽자식과 오른 쪽 자식노드의 값보다 작게 트리를 구성하는 것입니다. 그렇게 하면 트리의 루트(root)노드는 입력된 값들 중 가장 작은 값이 저장되어 있습니다. 예를 들어 5 3 2 1 4 6 7순으로 입력되 면 최소힙 트리는 아래와 같이 구성됩니다.
'''

import heapq as hq

a = []
while True:
  n = int(input())
  if n == 1:
    break
  if n == 0:
    if len(a) == 0:
      print(-1)
    else:
      print(hq.heappop(a))
  else:
    hq.heappush(a,n)