list1 = ([5, 1, 2, 3], [3, 4, 5, 5])
list2 = ([1, 1], [2, 2, 3])
list3 = (["tomato", "mango", "kiwi"], ["eggplant", "tomato", "broccoli"])



def get_unique_values_from_two_lists(input):
  print(set(input))

get_unique_values_from_two_lists([5, 1, 2, 3] + [3, 4, 5, 5])
get_unique_values_from_two_lists([1,1] + [2,2,3])
get_unique_values_from_two_lists(["tomato", "mango", "kiwi"] + ["eggplant", "tomato", "broccoli"])
