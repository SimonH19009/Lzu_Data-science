def list_max(int_list):
    int_list.sort(reverse=True)
    return int_list[0]

print(list_max([1, 2, 8, 3, 10, 5]))