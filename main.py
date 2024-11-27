import math


class Matrix:
    def __init__(self, data):
        self.data = data

    def __sub__(self, other):
        return Matrix([
            [self.data[i][j] - other.data[i][j]
                for j in range(len(self.data[0]))]
            for i in range(len(self.data))
        ])

    def __str__(self):
        return '\n'.join([' '.join(map(str, row)) for row in self.data])

    @staticmethod
    def sort_rows_decorator(func):
        def wrapper(self, *args, **kwargs):
            for row in self.data:
                n = len(row)
                for i in range(n):
                    for j in range(0, n - i - 1):
                        if row[j] > row[j + 1]:
                            row[j], row[j + 1] = row[j + 1], row[j]
            print("Оновлена матриця:")
            for row in self.data:
                print(row)
            return func(self, *args, **kwargs)
        return wrapper

    @sort_rows_decorator
    def calculate_f_and_F(self):
        n = len(self.data)

        fi = [0] * len(self.data[0])
        for i in range(n):
            for j in range(n):
                if i + j >= n:
                    fi[j] += self.data[i][j]

        positive_fi = [val for val in fi if val > 0]
        if len(positive_fi) > 0:
            F = math.pow(math.prod(positive_fi), 1 / len(positive_fi))
        else:
            F = 0

        return fi, F


matrix = Matrix([
    [87, 98, 57, 29, 95],
    [-8, 59, -2, 9, -11],
    [6, 10, 20, 59, -23],
    [12, 13, 51, 46, -7],
    [-2, 87, 69, 90, -3],
])

fi, F = matrix.calculate_f_and_F()

print("\nСуми елементів під допоміжною діагоналлю (fi):", fi)
print("Середнє геометричне значення (F):", F)


A = Matrix([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

B = Matrix([
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]
])

C = A - A

print("\nРезультат віднімання матриць A і B:")
print(C)
