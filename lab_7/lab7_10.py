def tokenize(text):
    razdel = set(" \t\n.,;:!?()[]{}\"«»…—–")
    tokens = []
    buffer = []
    def flush():
        if buffer:
            tokens.append("".join(buffer))
            buffer.clear()
    n = len(text)
    for i, ch in enumerate(text):
        if ch == ".":
            left_is_digit = i > 0 and text[i - 1].isdigit()
            right_is_digit = i + 1 < n and text[i + 1].isdigit()
            if left_is_digit and right_is_digit:
                buffer.append(ch)
            else:
                flush()
        elif ch in razdel:
            flush()
        else:
            buffer.append(ch)
    flush()
    return tokens

print(tokenize("Привет, мир! Как дела?"))
print(tokenize("Жили-были 3.14 раза"))
print(tokenize('s = "don\'t"'))
print(tokenize("A...B"))
print(tokenize(""))
print(tokenize("Цена 12.5 руб.; скидка 3.14%!"))
