my_dict = {'a': 500, 'b': 5874, 'c': 560, 'd': 400, 'e': 5874, 'f': 20}

# for key in my_dict:
#     print(key, ':', my_dict[key])
#
# list1 = [1, 2, 3]
# list2 = ['a', 'b', 'c']
# dict = zip(list1, list2)
# print(list(dict))
# max1=max2=max3=None
#
# for key in my_dict:
#     value = my_dict[key]
#
#     if max1 is None or value > my_dict[max1]:
#         max3 = max2
#         max2 = max1
#         max1 = key
#     elif max2 is None or value > my_dict[max2]:
#         max3 = max2
#         max2 = key
#     elif max3 is None or value > my_dict[max3]:
#         max3 = key
# print("3 ключа с самыми высокими значениями\n", max1, "-", my_dict[max1], "\n", max2, "-", my_dict[max2], "\n", max3,
#       "-", my_dict[max3])

top_keys = sorted(my_dict, key = my_dict.get, reverse = True)[:3]
print("3 ключа с самыми высокими значениями\n", top_keys)