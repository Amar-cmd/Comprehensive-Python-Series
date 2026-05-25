# from collections import Counter
#
# data = ["a", "b", "a", "c", "a", "b"]
# c = Counter(data)
#
# # Basic
# print(c)
# print(c["a"])
# print(c["z"])
#
# # 1. Most common
# print(c.most_common(2))
#
# # 2. Update counts
# c.update(["a", "d", "d"])
# print(c)
#
# # 3. Convert to normal dict
# print(dict(c))
#
# # 4. Count characters
# print(Counter("banana"))
#
# # 5. Count words
# print(Counter("I love love python".split()))
from collections import namedtuple

#! 2. DEQUE

# from collections import deque
#
# dq = deque([1, 2, 3, 4, 5])
# print(dq)
#
# # add right
# dq.append(6)
# print(dq)
#
# # add left
# dq.appendleft(0)
# print(dq)
#
# # remove left
# dq.popleft()
# print(dq)
#
# # remove right
# dq.pop()
# print(dq)
#
# # Rotate
# # [5, 1, 2, 3, 4]
#
# dq.rotate(2)
# print(dq)
#
# # [3, 4, 5, 1, 2]
# dq.rotate(-2)
# dq.rotate(-2)
#
# print(dq)
#
# # Fixed size deque → gives only the latest N items
# dqe = deque([1, 2, 3, 4, 5], maxlen=3)
# print(dqe)



#! 3. DefaultDict

# from collections import defaultdict
#
# d = defaultdict(int)
# d1 = defaultdict(list)
# d2 = defaultdict(set)
#
# print(d)
#
# d['a'] = 1
# print(d)
#
# d['b'] = 2
# print(d)
#
# d['a'] += 5
# print(d)


#! 4. namedtuple

# from collections import namedtuple
#
# d = namedtuple("Person", ["name", "age"])
# p = d("Amar", 24)
# print(p)
# print(p.age)


#! 4. chainmap

from collections import ChainMap

defaults = {"theme": "light", "lang": "en"}
user = {"theme": "dark"}

chg = ChainMap(user, defaults)
print(chg["theme"])
print(chg["lang"])

chg = ChainMap(defaults, user)
print(chg["theme"])
print(chg["lang"])
















