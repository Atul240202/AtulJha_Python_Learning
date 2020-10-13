#integration using sympy
#sympy is pre-installed libraray in anaconda
#by - Atul Jha

import sympy as sp
def main():
    x = sp.symbols('x')
    
    eq1 = x * sp.log(x)
    eq2 = x ** 2
    eq3 = sp.tan(sp.sin(x))
    
    itg1 = sp.integrate(eq1, x)
    itg2 = sp.integrate(eq2, x)
    itg3 = sp.integrate(eq3, x)
    
    print("Intergration of " , eq1 , " is: " ,itg1)
    print("Intergration of " , eq2 , " is: " ,itg2)
    print("Intergration of " , eq3 , " is: " ,itg3)
    
if __name__ == '__main__':
    main()

    
