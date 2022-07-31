
def common_member(a, b):
	a_set = set(a)
	b_set = set(b)
  
  
	if (a_set & b_set):
		print(a_set & b_set)
	else:
		print("No common values")
		

a = [3, 4, 5, 5]
b = [3, 6, 7, 5]
common_member(a, b)

a = [1, 2]
b = [2, 2, 3]
common_member(a, b)

a = ["tomato", "mango", "kiwi"]
b = ["eggplant", "tomato", "broccoli"]
common_member(a, b)