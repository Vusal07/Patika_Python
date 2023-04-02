def flatten(lst):
    result = []
    for item in lst:
        if type(item) == list:
            result += flatten(item)
        else:
            result.append(item)
    return result

user_input = input()

user_list = eval(user_input)
flattened_list = flatten(user_list)
print( flattened_list)
