# Using list as queues
# While appends and pops from the end of list are fast,
# doing inserts or pops from the beginning of a list is slow (because all of the other elements have to be shifted by one).
# from collections import deque
# queue = deque(["Eric", "John", "Michael"])
# queue.append("Terry")           # Terry arrives
# queue.append("Graham")          # Graham arrives
# print(queue.popleft())          # The first to arrive now leaves
# print(queue.popleft())          # The second to arrive now leaves
# print(queue)
# print()

# List comprehensions
# squares = []
# for x in range(11):
#     squares.append(x**2)
# print(squares)
# print()


squares1 = list(map(lambda x: x**2, range(10)))
# print(squares1)
# print()

# squares2 = [x**2 for x in range(10)]
# print(squares2)
# print()

print([(x, y) for x in [1,2,3] for y in [3,1,4] if x != y])
print()

combs = []
for x in [1,2,3]:
    for y in [3,1,4]:
        if x != y:
            combs.append((x, y))
print(combs)
print()
