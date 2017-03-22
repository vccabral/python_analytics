

BIG_SIZE = 100000000

long_list = [i for i in range(BIG_SIZE)]

print("array created")
print(BIG_SIZE in long_list)
print(BIG_SIZE-1 in long_list)

long_dict = {i:True for i in range(BIG_SIZE)}

print("dict created")
print(BIG_SIZE in long_dict)
print(BIG_SIZE-1 in long_dict)

long_set = set([i for i in range(BIG_SIZE)])

print("set created")
print(BIG_SIZE in long_set)
print(BIG_SIZE-1 in long_set)
