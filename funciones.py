def CalcularResultado(num1, num2, op):
    """Funcion que recibe dos numeros reales y un operador aritmetico en
    forma de string, y segun cual es, retorna la cuenta que corresponda """

    if op == "+":
        return num1 + num2
    
    elif op == "*":
        return num1 * num2
    
    elif op == "-":
        return num1 - num2
    
    elif op == "/":
        return num1 / num2


