def merge(a: dict[str, float], b: dict[str, float]):
    result: dict[str, float] = {}
    for key in a:
        if key in b:
            result[key] = a[key] + b[key]
    return result


a: dict[str, float] = {
    "a": 1.0,
    "b": 2.0,
    "c": 3.0,
}

b: dict[str, float] = {
    "a": 1.0,
    "b": 2.0,
    "d": 3.0,
}

if __name__ == "__main__":
    print(merge(a, b))
