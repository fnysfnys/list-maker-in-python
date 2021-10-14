def add_five(my_list):
    for i in range(len(my_list)):
        my_list[i]+=5
    
    return my_list
my_list = [1,2,3,4,5]

my_list = add_five(my_list)

print(my_list)