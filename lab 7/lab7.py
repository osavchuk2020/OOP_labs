'''
a = input("Введіть число: ")
assert a.isdigit(), "Потрібно ввести число!"
print(f"введене число: {a}")
'''

'''
class Figure:
    def __init__(self, type, length) -> None:
        assert length > 0, "Довжина має бути більшою за 0!"
        assert type in ["квадрат", "прямокутник", "трикутник"], "Дозволені фігури: квадрат, прямокутник, трикутник"
        self.type = type
        self.length = length

#a = Figure("трапеція", 12)
b = Figure("квадрат", 0)
#c = Figure("квадрат", 1)
'''

class Name:
    def __init__(self, name, age=None) -> None:
        if name not in ["Богдан", "Анонім", "Олександр"]:
            raise ValueError("Дозволені імена: Богдан, Анонім")
        if age is None:
            raise ValueError("Потрібно вказати вік")
        elif age.isdigit() is False:
                 raise ValueError("Вік має бути вказаний цифрами") 
        self.name = name

a = Name("Олександр", "12")