# import queue
from collections import deque

q = deque() #双端队列
q.append(1)
q.append(2)
result = q.popleft() #队列：先进先出

print(result)