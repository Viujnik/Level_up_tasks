def unique_by(iterable, key):
    seen = set()
    for item in iterable:
        k = key(item)
        if k not in seen:
            seen.add(k)
            yield item

items = [
    {'name': 'Masha', 'iq': 99},
    {'name': 'Dima', 'iq': 113},
    {'name': 'Masha', 'iq': 89},
    {'name': 'Oleg', 'iq': 127},
    {'name': 'Dima', 'iq': 107},
]

for item in unique_by(items, lambda item: item['name']):
    print(item)