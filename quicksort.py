# def quick_sort(s):
#     if len(s) <= 1:
#         return s
#
#     element = s[0]
#     left = list(filter(lambda x: x < element, s))
#     center = [i for i in s if i == element]
#     right = list(filter(lambda x: x > element, s))
#
#     return quick_sort(left) + center + quick_sort(right)
#
# print(quick_sort([7,6,10,5,9,8,3,4]))

def quick_sort(array):
    if len(array) < 2:
        return array
    else:
        pivot = array[0]
        less = [i for i in array[1:] if i <= pivot]
        greater = [i for i in array[1:] if i >= pivot]
        return quick_sort(less) + [pivot] + quick_sort(greater)
print(quick_sort([2, 4432, 67, 323, 12, 7842, 88, 1, 783]))
