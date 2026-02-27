def modify(num_list):
    num_list[1] = 99
    print("Inside modify function:", num_list)


my_list = [10, 20, 30]
modify(my_list)

print("Outside modify function:", my_list)
