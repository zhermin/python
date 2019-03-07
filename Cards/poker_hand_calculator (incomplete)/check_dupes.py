from collections import Counter

ans = ['e', 'b', 'b', 'c', 'd', 'd']
ges = ['b', 'b', 'c', 'b', 'e', 'e']
res = ans.copy()

c1 = Counter(ans)
c2 = Counter(ges)
diff = c1 - c2
list_of_diff = list(diff.elements())

for i in range (len(list_of_diff)):
	res.remove(list_of_diff[i])

print(res)
print(len(res))
input()