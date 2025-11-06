from collections import Counter

lst = ["abc", "a", "xy", "z", "abc", "xy", "xy", "xyz"]

print(sorted(lst, key=lambda s: (-len(s), s), reverse=True))

print([item for item, _ in Counter(lst).most_common(3)])

compose = lambda f, g: lambda x: f(g(x))
print(compose(lambda x: x*3, lambda x: x**2)(5))