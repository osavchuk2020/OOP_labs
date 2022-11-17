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
        return self.type

    @property
    def get_figure_color(self):
        return self.color

a = Figure("квадрат", 12, "білий")
print(f"Фігура: {a.get_figure_type}")
print(f"Довжина: {a.get_figure_length}")
print(f"Колір: {a.get_figure_color}")

def test_app_triangle():
    """Test if we create triangle figure.
    """
    fig = "трикутник"
    col = "білий"
    triangle = Figure(fig, 4, col)
    assert triangle.type == fig, f"Фігура має бути {fig}"