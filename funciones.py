def CalcularResultado(num1, num2, op):
    """Funcion que recibe dos numeros reales y un operador aritmetico en
    forma de string, y segun cual es, retorna la cuenta que corresponda """


    if op == "+":
        res = num1 + num2
    
    elif op == "*":

        res = num1 * num2
    
    elif op == "-":
        res = num1 - num2
    
    elif op == "/":
        
        #Manejar el error de division por cero
        if num2 != 0:
            res = num1 / num2
        else:
            return "ERROR"


    if '.' in str(res):
        res = RemoverDecimalNulo(str(res))
    


    return res


def RemoverDecimalNulo(num):

    """ 
        Esta funcion recibe un numero flotante en forma de string y, si tiene un decimal nulo lo elimina y retorna como int,
            SI EL DECIMAL NO ES NULO LO RETORNA COMO FLOAT
        por ejemplo:    INPUT: 4.0  OUTPUT: 4       INPUT: 16.000   OUTPUT: 16      INPUT:  50.015     OUTPUT: 50.015
    """
    DecimalNulo = True

    #Si algun digito de la parte decimal NO es cero, entonces el decimal no es NULO

    for digito in num.split(".")[1]:
        if digito != "0":
            DecimalNulo = False

    #Si el decimal es nulo, quedarse solo con la parte entera
    if DecimalNulo:
        return int(num.split(".")[0])

    return float(num)