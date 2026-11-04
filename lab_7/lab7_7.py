students = [
    ("Аня", 5), ("Борис", 3), ("Вера", 4),
    ("Глеб", 5), ("Дина", 2), ("Егор", 4),
    ("Жанна", 5), ("Зоя", 3)
]
filtered = list(filter(lambda s: s[1] >= 4, students))
sorted_students = sorted(filtered, key=lambda s: (-s[1], s[0]))
for name, grade in sorted_students:
    print(f"{name} - {grade}")
average = sum(grade for _, grade in filtered) / len(filtered)
print(f"Средний балл: {average:.2f}")
