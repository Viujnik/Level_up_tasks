def flatten(user_list):
    nested_flag = True
    while nested_flag:
        stack = []
        nested_flag = False
        for item in user_list:
            if isinstance(item, list):
                stack.extend(item)
                nested_flag = True
            else:
                stack.append(item)
        user_list = stack

    return user_list


user_list = [1, [2, [3, [4, [5, 6]]]]]
if __name__ == "__main__":
    print(flatten(user_list))
