# Звіт до роботи
## Тема: Знайомство з ООП
### Мета роботи: Знайомство з ООП
---
### Виконання роботи
1. Перевірка assert
    1. Створив власний крок `assert` для перевірки введених даних, зробив декілька тестів
        - код програми:
            ```python
            a = input("Введіть число: ")
            assert a.isdigit(), "Потрібно ввести число!"
            print(f"введене число: {a}")
            ```
        - результат роботи при введені `5`:
            ```text
            введене число: 5
            ```
        - результат роботи при введені `f`:
            ```text
            AssertionError: Потрібно ввести число!
            ```
    1. Створив класс, у якому за допомогою `assert` здійснюю перевірку аргументів при ініціалізації обєкту. Виконав код для перевірки створення декількох обєктів, з різними данними
        - код програми:
            ```python
            class Figure:
                def __init__(self, type, length) -> None:
                    assert length > 0, "Довжина має бути більшою за 0!"
                    assert type in ["квадрат", "прямокутник", "трикутник"], "Дозволені фігури: квадрат, прямокутник, трикутник"
                    self.type = type
                    self.length = length
            ```
        - результат роботи при створенні обєкту  `a = Figure("трапеція", 12)`:
            ```text
            AssertionError: Дозволені фігури: квадрат, прямокутник, трикутник
            ```
        - результат роботи при створенні обєкту  `b = Figure("квадрат", 0)`:
            ```text
            AssertionError: Довжина має бути більшою за 0!
            ```
        -  при створенні обєкту  `c = Figure("квадрат", 1)` виконується без помилок;
    1. Створив класс у якому перевірка виконується за допомогою умовного розгалудження. Виконав декілька перевірок
        - код програми:
            ```python
            class Name:
                def __init__(self, name) -> None:
                    if name not in ["Богдан", "Анонім"]:
                        raise ValueError("Дозволені імена: Богдан, Анонім")
                    self.name = name            
            ```
        - результат роботи при створенні обєкту  `a = Name("Бодько")`:
            ```text
            ValueError: Дозволені імена: Богдан, Анонім
            ```
    1. Додав своє імя до списку дозволених імен. Додав новий атрибут `age`, зробив перевірку `isdigit` для ноього
        - код програми:
            ```python
            class Name:
            def __init__(self, name, age=None) -> None:
                if name not in ["Богдан", "Анонім", "Олександр"]:
                    raise ValueError("Дозволені імена: Богдан, Анонім")
                if age is None:
                    raise ValueError("Потрібно вказати вік")
                elif age.isdigit() is False:
                        raise ValueError("Вік має бути вказаний цифрами") 
                self.name = name          
            ```
        - результат роботи при створенні обєкту  `a = Name("Олександр")`:
            ```text
            ValueError: Потрібно вказати вік
            ```
        - результат роботи при створенні обєкту  `a = Name("Олександр", "дванадцять")`:
            ```text
            ValueError: Вік має бути вказаний цифрами
            ```
        -  при створенні обєкту  `a = Name("Олександр", "12")` виконується без помилок;
1. Юніт тести
    1. Створив класс з двома методами. У одному з методів навмисно допущено помилку. Провів декілька тестів створення обєкту
        - код програми:
            ```python
            class Figure:
                FIGURES = ["квадрат", "прямокутник", "трикутник"]
                def __init__(self, type, length) -> None:
                    assert length > 0, "Довжина має бути більшою за 0!"
                    assert type in self.FIGURES, "Дозволені фігури: квадрат, прямокутник, трикутник"
                    self.type = type
                    self.length = length

                @property
                def get_figure_type(self):
                    return self.type

                @property
                def get_figure_length(self):
                    return self.type # робимо помилку

            a = Figure("квадрат", 12)
            print(a.get_figure_type)
            print(a.get_figure_length)         
            ```
        - результат роботи при створенні обєкту  `a = Figure("коло", 12)`:
            ```text
            AssertionError: Дозволені фігури: квадрат, прямокутник, трикутник
            ```
        - результат роботи при створенні обєкту  `a = Figure("квадрат", 12)`:
            ```text
            Фігура: квадрат
            Довжина: квадрат
            ```
    1. Створив окремий файл, у якому за допомгою юніт тестів відтворив перевірку обєктів створеного раніше класу. Провів перевірку
        - результат виконання тестів:
            ```text
            test_figure_lengh (__main__.TestFigure.test_figure_lengh) ... Тестуємо вивід довжини, має бути: прямокутник == прямокутник
            FAIL
            test_figure_type (__main__.TestFigure.test_figure_type) ... Тестуємо вивід типу фігури, має бути: прямокутник == прямокутник
            ok
            test_obj (__main__.TestFigure.test_obj) ... FAIL

            ======================================================================
            FAIL: test_figure_lengh (__main__.TestFigure.test_figure_lengh)
            ----------------------------------------------------------------------
            Traceback (most recent call last):
            File "c:\OOP_labs\lab 7\test.py", line 31, in test_figure_lengh
                self.assertEqual(self.length, self.obj.get_figure_length, "Властивість get_figure_length повертає непривильну довжину!")
            AssertionError: 8 != 'прямокутник' : Властивість get_figure_length повертає непривильну довжину!

            ======================================================================
            FAIL: test_obj (__main__.TestFigure.test_obj)
            ----------------------------------------------------------------------
            Traceback (most recent call last):
            File "c:\OOP_labs\lab 7\test.py", line 34, in test_obj
                Figure("коло", 1) # Спробуємо створити обєкт з недозволеними параметрими, в нас має бути помилка AssertionError
                ^^^^^^^^^^^^^^^^^
            File "c:\OOP_labs\lab 7\app.py", line 5, in __init__
                assert type in self.FIGURES, "Дозволені фігури: квадрат, прямокутник, трикутник"
            AssertionError: Дозволені фігури: квадрат, прямокутник, трикутник

            ----------------------------------------------------------------------
            Ran 3 tests in 0.018s

            FAILED (failures=2)
            ```
        - перший тест на тип обєкту пройдено
        - другий тест на довжину провалено, неправильний вивід 
        - третій тест на створення обєкту провалено, введено непривильні атрибути
    1. Додав до классу фігури новий атрибут `color` та додав перевірки для нього. Провів тести
        - код класу
            ```python
            class Figure:
                COLORS = ["чорний", "білий"]
                FIGURES = ["квадрат", "прямокутник", "трикутник"]
                def __init__(self, type, length, color) -> None:
                    assert length > 0, "Довжина має бути більшою за 0!"
                    assert type in self.FIGURES, "Дозволені фігури: квадрат, прямокутник, трикутник"
                    assert color in self.COLORS, "Дозволені кольори: {}.".format(", ".join(self.COLORS))
                    self.type = type
                    self.length = length
                    self.color = color

                @property
                def get_figure_type(self):
                    return self.type

                @property
                def get_figure_length(self):
                    return self.length

                @property
                def get_figure_color(self):
                    return self.color
            ```
        - код тесту для перевірки кольору
            ```python
            def test_figure_color(self):
                print(f"Тестуємо вивід кольору, має бути: {self.сolor} == {self.obj.get_figure_color}")
                self.assertEqual(self.сolor, self.obj.get_figure_color, "Властивість get_figure_color повертає непривильний колір!")
            ```
        - результати 
            ```text
            Тестуємо вивід кольору, має бути: чорний == чорний
            .Тестуємо вивід довжини, має бути: 4 == 4
            .Тестуємо вивід типу фігури, має бути: трикутник == трикутник
            .
            ----------------------------------------------------------------------
            Ran 3 tests in 0.001s

            OK
            ```
1. Юніт тести з використання бібліотеки PyTest
    1. У файл `app.py` у якому знаходиться клас фігури, дописав функцію `pytest` для тестування обєкту класу
        - код функції
            ```python
            def test_app_triangle():
            """Test if we create triangle figure.
            """
            fig = "трикутник"
            col = "білий"
            triangle = Figure(fig, 4, col)
            assert triangle.type == fig, f"Фігура має бути {fig}"
            ```
        - результат виконання
            ```text
            C:\OOP_labs\lab 7>pipenv run pytest app.py
            ================================================= test session starts =================================================
            platform win32 -- Python 3.11.0, pytest-7.2.0, pluggy-1.0.0
            rootdir: C:\OOP_labs\lab 7
            collected 1 item

            app.py .                                                                                                         [100%]

            ================================================== 1 passed in 0.02s ==================================================
            ```
1. Візуалізація результатів та покриття коду Coverage (pytest-cov)
    1. Для візуалізації тестів встановив додаткову біблотеку `coverage`
    1. Запуск тестів
        - команда 
            ```bash
            python -m unittest discover
            ```
        - результат виконання
            ```bash
            Фігура: квадрат
            Довжина: квадрат
            Колір: білий
            Тестуємо вивід кольору, має бути: чорний == чорний
            .Тестуємо вивід довжини, має бути: 8 == прямокутник
            FТестуємо вивід типу фігури, має бути: трикутник == трикутник
            .
            ======================================================================
            FAIL: test_figure_lengh (test.TestFigure.test_figure_lengh)
            ----------------------------------------------------------------------
            Traceback (most recent call last):
            File "C:\OOP_labs\lab 7\test.py", line 32, in test_figure_lengh
                self.assertEqual(self.length, self.obj.get_figure_length, "Властивість get_figure_length повертає непривильну довжину!")
            AssertionError: 8 != 'прямокутник' : Властивість get_figure_length повертає непривильну довжину!

            ----------------------------------------------------------------------
            Ran 3 tests in 0.003s

            FAILED (failures=1)
            ```
        - виклик `coverage`
            ```bash
            pipenv run coverage run -m pytest test.py
            ```
        - результат виконання
            ```bash
            ================================================= test session starts =================================================
            platform win32 -- Python 3.11.0, pytest-7.2.0, pluggy-1.0.0
            rootdir: C:\OOP_labs\lab 7
            collected 3 items

            test.py .F.                                                                                                      [100%]

            ====================================================== FAILURES =======================================================
            ____________________________________________ TestFigure.test_figure_lengh _____________________________________________

            self = <test.TestFigure testMethod=test_figure_lengh>

                def test_figure_lengh(self):
                    print(f"Тестуємо вивід довжини, має бути: {self.length} == {self.obj.get_figure_length}")
            >       self.assertEqual(self.length, self.obj.get_figure_length, "Властивість get_figure_length повертає непривильну довжину!")
            E       AssertionError: 7 != 'трикутник' : Властивість get_figure_length повертає непривильну довжину!

            test.py:32: AssertionError
            ------------------------------------------------ Captured stdout call -------------------------------------------------
            Тестуємо вивід довжини, має бути: 7 == трикутник
            =============================================== short test summary info ===============================================
            FAILED test.py::TestFigure::test_figure_lengh - AssertionError: 7 != 'трикутник' : Властивість get_figure_length повертає непривильну довжину!
            ============================================= 1 failed, 2 passed in 0.12s =============================================
            ```
    1. Для візуалізації тестів через бразуер викликав команду для створення звіту у форматі `.html`
        - команда
            ```bash
            pipenv run python -m coverage html
            ```
        - у результаті виконання було створено `.html` [документ](/htmlcom/index.html) з реузльтатами тестів    

### Висновок: 
-  В ході роботи я ознаймився та навчився використовувати `assert` тести, для виявлення то попередження можливих помилок, тестів за допомогою умовних розгалуджень, створення та налаштування юніт тестів, візуалізації та покриттю коду за допомогою бібліотеки `сovorege` та плагіну `pytest-cov`
- Так, мету роботи досягнуто.
- Всі, згідно вищезазначених завдань
- У даній роботі питання відсутні)
- Так, вдалось
- Ні, не виникало.
- Так, подобається.
- Зменшити кількість питань у висновку)
---