def safe_get(dictionary, *path_keys, default='Wrong path of keys'):
    for key in path_keys:
        try:
            dictionary = dictionary[key]
        except KeyError:
            return default
    return dictionary


dct = {'a': {'b': {'c': 1}}}
print(safe_get(dct, 'a', 'b', 'c'))