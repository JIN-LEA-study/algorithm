import sys
input = sys.stdin.readline
 
n, m = map(int, input().split())
pocket_books = {}
 
for i in range(1, n+1):
    name = input().strip()
    pocket_books[name] = i
 
pocket_books_keys = list(pocket_books.keys())
 
for _ in range(m):
    name_or_number = input().strip()
    if name_or_number.isdigit():
        print(pocket_books_keys[int(name_or_number) - 1])
    else:
        print(pocket_books[name_or_number])