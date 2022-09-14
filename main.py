# Problem 1: Remove Duplicates from Sorted Array
# You are given a sorted list (non-decreasing). There can be multiple occurrence of an element. Remove all duplicates from the sorted array.

def remove_duplicate(my_list):
  # TODO: Add your code here!
  return my_list


if __name__ == "__main__":
  print(remove_duplicate([])) # []
  print(remove_duplicate([-1, -1, 0])) # [-1, 0]
  print(remove_duplicate([1, 1, 2, 8, 11, 11, 14, 14, 17]))
