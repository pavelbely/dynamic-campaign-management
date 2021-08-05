from itertools import chain


def create_reducer(field_name):
    def reducer(acc, e):
        field_val = wrap_list(e[field_name])
        for event_type in field_val:
            acc[event_type].append(e)
        return acc
    return reducer


def wrap_list(x):
    if isinstance(x, list):
        return x
    return [x]


def get_with_generic(sources, field_name):
    res = []
    for s in wrap_list(sources):
        res.extend(wrap_list(s[field_name]))
        res.extend(wrap_list(s['*']))
    return res
