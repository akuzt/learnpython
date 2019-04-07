checkmates = [a for a in range(1,65)]
print(checkmates)
checkmates_two = []
for b in checkmates:
	checkmates_two.append(2**(b-1))
print(checkmates_two)
print(sum(checkmates_two))