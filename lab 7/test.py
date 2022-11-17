import unittest
from random import choice, randint

from app import Figure # назва файлу з нашим класом повинна бути app.py

class TestFigure(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """Виконається лише раз на початку тестів
        """
        pass
    
    def setUp(self) -> None:
        """Виконується кожного разу коли запускається тест
        """
        self.figure = choice(Figure.FIGURES)
        self.сolor = choice(Figure.COLORS)
        self.length = randint(1, 10)
        self.obj = Figure(self.figure, self.length, self.сolor)
        return super().setUp()

    def tearDown(self) -> None:
        del self.obj
        return super().tearDown()

    def test_figure_type(self):
        print(f"Тестуємо вивід типу фігури, має бути: {self.figure} == {self.obj.get_figure_type}")
        self.assertEqual(self.figure, self.obj.get_figure_type, "Властивість get_figure_type повертає непривильну фігуру!")

    def test_figure_lengh(self):
        print(f"Тестуємо вивід довжини, має бути: {self.length} == {self.obj.get_figure_length}")
        self.assertEqual(self.length, self.obj.get_figure_length, "Властивість get_figure_length повертає непривильну довжину!")

    def test_figure_color(self):
        print(f"Тестуємо вивід кольору, має бути: {self.сolor} == {self.obj.get_figure_color}")
        self.assertEqual(self.сolor, self.obj.get_figure_color, "Властивість get_figure_color повертає непривильний колір!")

if __name__ == '__main__':
    unittest.main() # unittest.main(verbosity=2) щоб був більш детальний вивід