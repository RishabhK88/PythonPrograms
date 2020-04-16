# FIFO - First In First Out
# For example there are 1001 elements in list if we remove the first one, 1000 elements
# will have to change their position in memory. to avoid this we use deque.
from collections import deque
queue = deque([])
queue.append(1)
queue.append(2)
queue.append(3)
queue.popleft()
print(queue)
if not queue:
    print("Empty")
