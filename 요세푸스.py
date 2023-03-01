# N,K =map(int,input().split())
# lst = []
# lst2 =[]
# sp = 0
# for i in range(1,N+1):
#     lst.append(i)
# #처음 수 뺄때
# del(lst[K-1])
# lst2.append(lst[K-1])
# lst[K-1] = -1
# sp = K
# cnt = 1
# print(lst)
# #리스트가 빌때까지 과정 반복
# while lst:
#     if lst[K]!= -1:
#         sp +=1
#         if sp > N:
#             sp = sp%7
#         cnt += 1
#         if cnt ==3:
#             del(lst[sp])
#             lst2.append(lst[sp])
#     else:
#         sp += 1
#         if sp > N:
#             sp = sp%7
#         cnt += 0
#         if cnt == 3:
#             del(lst[sp-1])
#             lst2.append(lst[sp])
# print(lst2)


# from collections import deque
# n, k = map(int, input().split())
# queue = deque(range(1, n + 1))
# answer = []
# print(queue)
# while queue:
#     for _ in range(k-1):
#         queue.append(queue.popleft())
#         print(queue)
#     answer.append(queue.popleft())

N,K =map(int,input().split())
lst = []
ans =[]
sp = 0
for i in range(1,N+1):
    lst.append(i)

while len(lst):
    sp = (sp+(K-1)) % len(lst) #K만큼 이동을 했을때 인덱스를 넘어버릴 수 있기때문
    ans.append(lst.pop(sp)) 

#출력포맷 변경해줄 것
#ans 출력시 [3, 6, 2, 7, 5, 1, 4]로 나옴
# ans.replace('[', '<')
# print(ans)

print("<", ', '.join(str(i) for i in ans), ">", sep = '')


