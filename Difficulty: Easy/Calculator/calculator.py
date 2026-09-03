class Solution:
    def calculate(self, a: int, b: int, operator: int) -> None:
        if operator in (1, 2, 3):
            print((None, a + b, b - a, a * b)[operator], end="")
        else:
            print("Invalid Input", end="")