# Лабораторная работа 1
## Задание:
1) Нужно было написать 3 абстрактных класса, описывающих любой объект
2) Для каждого класса выделить 2-3 характеристики и записать их в виде атрибутов.
3) Сформировать для каждого класса 2-3 метода, которые будет описывать возможные действия с объектом.
4) Каждый метод должен содержать документацию с описанием аргумментов и возвращаемого результата
5) Все аргументы методов и возвращаемые результаты должны содержать аннотацию типов.
6) В документации должен содержаться как минимум один doctest пример как пользоваться методом.

## Реализация:
- [x] Были созданы классы ```User```, ```Contacts``` и ```Group```
Каждый из этих классов содержит различные методы, реализующие действия, которые может выполнять пользователь
Например, добавлять других пользователей, отправлять сообщения пользователям, формировать группы и диалоги ...

## То, что не понял (не получилось):
- При создании тестов внутри документации к методу ```show_info``` возникла проблема, связанная с тем, что в ожидаемых результатах должно выводиться конкретное значение, а в данном методе используется метод ```datetime()```, с помощью которго возвращается текущее время. Таким образом, при запуске теста программа каждый раз будет выводить различный результат. В качестве решения проблемы было решено сделать "метку времени", задав своё время на входе:

```python
with patch('main.datetime') as mock_datetime:
  mock_datetime.now.side_effect = [
  datetime(2023, 12, 3, 0, 40, 58),
  ]
```

- Таким образом, при запуске теста происходит считывание временной метки и будет выводиться информация о том, что сообщение было получено 2023-12-03 00:40:58 и тест проходит успешно:

![Test show_info()](https://github.com/MatNepo/PythonCourseOOP/blob/Lab1/Screenshot%201.png)
![Test show_info()](https://github.com/MatNepo/PythonCourseOOP/blob/Lab1/Screenshot%202.png)

### Запуск тестов

Чтобы запустить все тесты, необходимо:
- нажать и запустить ```Run 'Doctest in main'``` в правом верхнем углу экрана:

![Test show_info()](https://github.com/MatNepo/PythonCourseOOP/blob/Lab1/Screenshot%203.png)

- нажать ПКМ в любой части кода после:
```python
doctest.testmod()
```
на ```581``` и запустить ```Run 'Doctest in main'```:

![Test show_info()](https://github.com/MatNepo/PythonCourseOOP/blob/Lab1/Screenshot%204.png)

В этом случае тесты пройдкт успешно!

Однако, если запустить ```Run 'main'``` (нажать ```Run``` около блока ```if __name__ == "__main__":```), то не сработает один тест, описанный в методе ```show_info()```, т.к. он выведет текущее время:

![Test show_info()](https://github.com/MatNepo/PythonCourseOOP/blob/Lab1/Screenshot%205.png)

![Test show_info()](https://github.com/MatNepo/PythonCourseOOP/blob/Lab1/Screenshot%206.png)


**Именно эту проблему не получилось решить**


## Запуск тестов c использованием файла ```tests.txt```

Для запуска тестов в этом режиме необходимо раскомментировать строки с 574 по 577 включительно (а них подключается файл с тестами) и заменить все символы ```>>>``` в документации на ```***``` или другие (это необходимо, чтобы тесты, описанные в документации не запускались автоматически)
