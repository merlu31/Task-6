#Write a Python program to find the first non-repeating elements in a given list of integers?
arr = [4,7,3,7,4, 8, 2, 8, 9]
def odd_occurring_num(arr):
    return [i for i in arr if arr.count(i) < 2]
print(odd_occurring_num(arr))