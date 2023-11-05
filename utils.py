# import csv
# import click

# from models import db, Opinion
# from opinions_app import app


# @app.cli.command('load_opinions')
# def load_opinions_command():
#     """Функция загрузки мнений в базу данных."""
#     # Открывается файл
#     with open('opinions.csv', encoding='utf-8') as f:
#         # Создаётся итерируемый объект, который отображает каждую строку
#         # в качестве словаря с ключами из шапки файла
#         reader = csv.DictReader(f)
#         # Для подсчёта строк добавляется счётчик
#         counter = 0
#         for row in reader:
#             # Распакованный словарь можно использовать
#             # для создания объекта мнения
#             opinion = Opinion(**row)
#             # Изменения нужно зафиксировать
#             db.session.add(opinion)
#             db.session.commit()
#             counter += 1
#     click.echo(f'Загружено мнений: {counter}')
