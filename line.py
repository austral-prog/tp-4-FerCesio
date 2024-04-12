def line():
    import math
    A = float(input("Ingrese el coeficiente A: "))
    B = float(input("Ingrese el coeficiente B: "))
    x1 = float(input("Ingrese el coeficiente X1: "))
    x2 = float(input("Ingrese el coeficiente X2: "))
    y1 = float(A*x1+B)
    y2 = float(A*x2+B)
    print(f"""
    El coeficiente A de su ecuación de la recta es: {A}
    El coeficiente B de su ecuación de la recta es: {B}
    El coeficiente X1 de su ecuación de la recta es: {x1}
    El coeficiente X2 de su ecuación de la recta es: {x2}
    
    Para la siguiente ecuación:
            Y = {A}x + {B}
    
    Dados los siguientes puntos:
            P1 ({x1}, {y1})
            P2 ({x2}, {y2})
    
    La distancia entre ellos es: {math.dist([x1, y1], [x2, y2])}
    """)
    
