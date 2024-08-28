# l1 = [1,2,3,4,4,5,5,5,5,5,5,6,7]
# s1 = set(l1)
# l2 = list(s1)
# print(l2)

s1 = set()
s1.add('pedro')
s1.add(1)
s1.update(('ola mundo', 1, 2, 3, 4,))
# s1.clear()
s1.discard('ola mundo')
s1.discard('pedro')
print(s1)

s1 = {1,2,3}
s2 = {2,3,4}
s3 = s1 | s2
s3 = s1 & s2
s3 = s1 - s2
s3 = s1 ^ s2
print(s3)