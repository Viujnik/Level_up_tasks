def flatten(iterable):
    result = []
    for item in iterable:
        if isinstance(item, (list, tuple)):
            result.extend(flatten(item))
        else:
            result.append(item)
    return result

# Прикинь чё питон вытворяет:
# flatten_alt = lambda nested: [item for sublist in nested for item in (flatten(sublist) if isinstance(sublist, (list, tuple)) else [sublist])]