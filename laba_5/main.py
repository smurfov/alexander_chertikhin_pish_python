# Парсинг CSV
print("Задача №1")
data = "Иванов Иван, 20, Математика; Петров Петр, 21, Физика; Сидоров Сидор, 22, Химия"

students = data.split("; ")
formatted = []


for student in students:
	info = student.split(", ")
	formatted.append(f"Имя: {info[0]}\nВозраст: {info[1]}\nФакультет: {info[2]}")

result = "\n\n".join(formatted)
print(result)

# Извлечение email-адресов
print("\nЗадача №2")
text = "Контакты: ivanov@example.com, petrov@work.net, sid@mail.ru"

formatted = text.replace(",", " ").split()

result = []

for email in formatted:
	if "@" in email:
		result.append(email)

print(", ".join(result))

# Подсчет количества слов
print("\nЗадача №3")
sentence = "Python is a powerful and easy-to-learn programming language."
formatted = sentence.replace(".", "").split()
print(len(formatted))

# Удаление дубликатов символов
print("\nЗадача №4")
s = "aaabbbcccaaadddd"
new_stroke = ""

for char in s:
	if char not in new_stroke:
		new_stroke += char

print(new_stroke)

# Извлечение чисел
print("\nЗадача №5")
text = "Сегодня 20 градусов, завтра будет 18 градусов, а вчера было 22 градуса."

result = []
current_number = ""

for char in text:
    if char.isdigit():
        current_number += char
    elif current_number:
        result.append(int(current_number))
        current_number = ""

if current_number:
	result.append(int(current_number))

print(result)