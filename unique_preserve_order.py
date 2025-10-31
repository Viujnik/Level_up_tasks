def unique_preserve_order(data_lst):
    """Возвращает всё, кроме повторных значений"""
    seen_trash = set()
    result = []
    for item in data_lst:
        if item not in seen_trash:
            seen_trash.add(item)
            result.append(item)
    return result

def unique_without_trash(data_lst):
    """Возвращает только уникальные значения"""
    count = {}
    # подсчет
    for item in data_lst:
        count[item] = count.get(item, 0) + 1

    # Сбор уникальных значений
    result = []
    for item in data_lst:
        if count[item] == 1:
            result.append(item)
    return result

if __name__ == "__main__":
    lst = [int(i) for i in input().split()]
    down_mode = int(input("How are you?(1 or 2): "))
    if down_mode == 1:
        print(unique_preserve_order(lst))
    elif down_mode == 2:
        print(unique_without_trash(lst))