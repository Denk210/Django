from jinja2 import Template
import csv

with open('books_template.j2') as file:
    template = Template(file.read())

language = input("Выберите язык: ")
books = []
with open('books.csv', newline='', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        if len(row) > 1 and row[6] == language:
            books.append(row[1])

output = template.render(language=language, books=books)

with open('books_output.html', 'w', encoding='utf-8') as html_file:
    html_file.write(output)

print(output)