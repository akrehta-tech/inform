def markdown_to_html(md: str) -> str:
    if md == "":
        return ""

    result_lines = []

    for line in md.split("\n"):
        # Правило 1: заголовок — 1–6 решёток, затем пробел
        if line.startswith("#"):
            level = 0
            while level < len(line) and line[level] == "#":
                level += 1

            if 1 <= level <= 6 and level < len(line) and line[level] == " ":
                content = line[level + 1:]
                content = inline_format(content)
                result_lines.append(f"<h{level}>{content}</h{level}>")
                continue

        # Правило 4: обычная строка — абзац
        result_lines.append(f"<p>{inline_format(line)}</p>")

    return "\n".join(result_lines)


def inline_format(text: str) -> str:
    """Применяет правила 2 (**жирный**) и 3 (`код`) внутри строки."""
    text = replace_pairs(text, "**", "<b>", "</b>")
    text = replace_pairs(text, "`", "<code>", "</code>")
    return text


def replace_pairs(text: str, marker: str, open_tag: str, close_tag: str) -> str:
    """Заменяет пары marker...marker на open_tag...close_tag."""
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


# ==================== ПРОВЕРКА ====================

if __name__ == "__main__":
    # --- Обязательные тесты из условия ---
    assert markdown_to_html("# Привет") == "<h1>Привет</h1>"
    assert markdown_to_html("### Тема") == "<h3>Тема</h3>"
    assert markdown_to_html("###### Мелкий") == "<h6>Мелкий</h6>"
    assert markdown_to_html("Это **важно**") == "<p>Это <b>важно</b></p>"
    assert markdown_to_html("Код `x`") == "<p>Код <code>x</code></p>"
    assert markdown_to_html("") == ""

    # --- Пример из условия ---
    md = """# Заголовок
## Подзаголовок
Это **жирный** текст и `код`."""

    expected = """<h1>Заголовок</h1>
<h2>Подзаголовок</h2>
<p>Это <b>жирный</b> текст и <code>код</code>.</p>"""

    got = markdown_to_html(md)
    print("=== Пример из условия ===")
    print(got)
    print()
    assert got == expected, f"Ожидалось:\n{expected}\nПолучено:\n{got}"

    # --- Дополнительные крайние случаи ---
    assert markdown_to_html("#") == "<p>#</p>"                    # нет пробела
    assert markdown_to_html("####### x") == "<p>####### x</p>"     # 7 решёток
    assert markdown_to_html("# ") == "<h1></h1>"                   # пустой заголовок
    assert markdown_to_html("**a** и **b**") == "<p><b>a</b> и <b>b</b></p>"
    assert markdown_to_html("**незакрытый") == "<p>**незакрытый</p>"
    assert markdown_to_html("**a `b` c**") == "<p><b>a <code>b</code> c</b></p>"
    assert markdown_to_html("строка1\nстрока2") == "<p>строка1</p>\n<p>строка2</p>"

    print("Все тесты пройдены ✅")
