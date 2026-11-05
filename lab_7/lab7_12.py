def markdown_to_html(md: str) -> str:
    if md == "":
        return ""

    result_lines = []

    for line in md.split("\n"):
        if line.startswith("#"):
            level = 0
            while level < len(line) and line[level] == "#":
                level += 1

            if 1 <= level <= 6 and level < len(line) and line[level] == " ":
                content = line[level + 1:]
                content = inline_format(content)
                result_lines.append(f"<h{level}>{content}</h{level}>")
                continue


        result_lines.append(f"<p>{inline_format(line)}</p>")

    return "\n".join(result_lines)


def inline_format(text: str) -> str:
    text = replace_pairs(text, "**", "<b>", "</b>")
    text = replace_pairs(text, "`", "<code>", "</code>")
    return text


def replace_pairs(text: str, marker: str, open_tag: str, close_tag: str) -> str:
    result = []
    i = 0
    n = len(text)
    while i < n:
        if text.startswith(marker, i):
            end = text.find(marker, i + len(marker))
            if end != -1:
                inner = text[i + len(marker):end]
                result.append(open_tag + inner + close_tag)
                i = end + len(marker)
                continue
        result.append(text[i])
        i += 1
    return "".join(result)




assert markdown_to_html("# Привет") == "<h1>Привет</h1>"
assert markdown_to_html("### Тема") == "<h3>Тема</h3>"
assert markdown_to_html("###### Мелкий") == "<h6>Мелкий</h6>"
assert markdown_to_html("Это **важно**") == "<p>Это <b>важно</b></p>"
assert markdown_to_html("Код `x`") == "<p>Код <code>x</code></p>"
assert markdown_to_html("") == ""

md = """# Заголовок
## Подзаголовок
Это **жирный** текст и `код`."""

expected = """<h1>Заголовок</h1>
<h2>Подзаголовок</h2>
<p>Это <b>жирный</b> текст и <code>код</code>.</p>"""

got = markdown_to_html(md)
print("Выход")
print(got)
print()

print("Все тесты пройдены")
