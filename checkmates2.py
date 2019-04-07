checkmates = [a for a in range(1,65)]
print(checkmates)
for b in checkmates:
	checkmates[b-1] = (2**(b-1))
print(checkmates)
print(sum(checkmates))