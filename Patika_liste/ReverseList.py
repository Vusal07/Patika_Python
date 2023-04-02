def reverse_list(lst):
    reversed_lst=lst[::-1]
    for i in range(len(reversed_lst)):
        if type(reversed_lst[i])==list:
            reversed_lst[i]=reverse_list(reversed_lst[i])
    return reversed_lst

input_list=input()
parsed_list=eval(input_list)
reversed_list=reverse_list(parsed_list)
print(reversed_list)
