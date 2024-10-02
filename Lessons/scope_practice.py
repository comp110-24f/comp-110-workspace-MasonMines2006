def remove_chars(msg: str, char: str) -> str:
    copy: str = ""
    for i in range(len(msg)):
        if msg[i] != char:
            copy = copy + msg[i]
    return copy


print(remove_chars("football", "o"))
