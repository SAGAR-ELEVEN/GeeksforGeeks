class Solution:
    def calculate(self, a: int, b: int, optr: int) -> None:
        # code here
        #if optr == 1:
            #print(a+b)
        #elif optr == 2:
            #print(a-b)
        #elif optr == 3:
            #print(a*b)
        #else:
            #print("Invalid Input")
        
        if optr in (1, 2, 3):
            print((None, a + b, b - a, a * b)[optr], end="")
        else:
            print("Invalid Input", end="")