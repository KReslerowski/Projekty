def podwoj(x):
    return x * 2

print(podwoj(4))

# print((lambda x: x * 2) (4))

my_List = [2, 14, 22, 7, 6, 4, 5, 17]

my_List_filtered = list(filter(lambda x: x % 2 == 0, my_List))

print(my_List_filtered)