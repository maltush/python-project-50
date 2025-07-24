### Hexlet tests and linter status:
[![Actions Status](https://github.com/maltush/python-project-50/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/maltush/python-project-50/actions)

# gendiff

Библиотека для сравнения двух плоских JSON-файлов и вывода различий в удобочитаемом формате.

## Установка

Просто скопируйте файлы в ваш проект или установите как пакет (если подготовите дистрибутив).

## Использование

```python
from gendiff import generate_diff

diff = generate_diff('file1.json', 'file2.json')
print(diff)