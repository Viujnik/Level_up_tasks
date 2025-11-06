def solve_none():
    """Проблема в том, что при попытке заменить один элемент во вложенном списке,
    мы заменяем сразу три элемента (в данном случае).
    Использование генератора списков помогает нам в этом, поскольку он создаёт списки несколько раз,
    в то время как «*» просто «умножает» ссылки на объект.
    - Чисто моё грубое понимание данного 3.1415956535..."""
    return [[None for __ in range(3)] for __ in range(3)]


if __name__ == "__main__":
    change = input(
        "Select the position of the element to be changed: row(1-3) and line(1-3) separated by spaces: ").split()
    none_lst: list[list] = solve_none()
    none_lst[int(change[0]) - 1][int(change[1]) - 1] = "Hello, Samir!"
    print(none_lst)
