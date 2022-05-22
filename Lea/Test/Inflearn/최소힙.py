
'''
최소힙은 완전이진트리로 구현된 자료구조입니다.
그 구성은 부모 노드값이 왼쪽자식과 오른 쪽 자식노드의 값보다 작게 트리를 구성하는 것입니다.
그렇게 하면 트리의 루트(root)노드는 입력된 값들 중 가장 작은 값이 저장되어 있습니다.
예를 들어 5 3 2 1 4 6 7순으로 입력되 면 최소힙 트리는 아래와 같이 구성됩니다.
'''

import heapq as hq

a = []
while True:
  n = int(input())
  if n == -1:
    break
  if n == 0:
    if len(a) == 0:
      print(-1)
    else:
      print(hq.heappop(a))
  else:
    hq.heappush(a,n)


# anthoer code 내장함수 안쓰고 코드 구현

class Heap: # min heap
    def __init__(self):
        self.values = [0]

    def is_empty(self):
        return len(self.values) == 1

    def push(self, value):
        index = len(self.values)
        self.values.append(value)
        while index > 1:
            if self.values[index // 2] > self.values[index]:
                self.swap(index, index // 2)
            else:
                break
            index = index // 2

    def swap(self, index1, index2):
        self.values[index1], self.values[index2] = self.values[index2], self.values[index1]

    def pop(self):
        min_value = self.values[1]
        self.values[1] = self.values.pop()
        index = 1
        n = len(self.values) - 1
        while True:
            if n < index * 2: # no child
                break
            elif n < index * 2 + 1: # only left child
                if self.values[index] > self.values[index * 2]:
                    self.swap(index, index * 2)
                    index = index * 2
                else:
                    break
            else: # have both children
                if self.values[index] > self.values[index * 2] or self.values[index] > self.values[index * 2 + 1]:
                    if self.values[index * 2] < self.values[index * 2 + 1]:
                        self.swap(index, index * 2)
                        index = index * 2
                    else:
                        self.swap(index, index * 2 + 1)
                        index = index * 2 + 1
                else:
                    break

        return min_value

heap = Heap()

while True:
    n = int(input())
    if n == -1:
        break
    elif n == 0:
        if heap.is_empty():
            print(-1)
        else:
            print(heap.pop())
    else:
        heap.push(n)




