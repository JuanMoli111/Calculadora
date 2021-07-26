from funciones import CalcularResultado

import PySimpleGUI as sg

#Definimos los elementos divididos en secciones segun su funcion
#una para los digitos, otra para los operadores, y una seccion para la operacion y el resultado
seccion_numeros = [

    [sg.Button("",visible = False)],

                                    [sg.Button("0",size = (2,2), key = "0", pad = (39,0,0,0), focus = False)],

    [sg.Button("1",size = (2,2),key = "1"), sg.Button("2",size = (2,2),key = "2"), sg.Button("3",size = (2,2),key = "3")],

    [sg.Button("4",size = (2,2),key = "4"), sg.Button("5",size = (2,2),key = "5"), sg.Button("6",size = (2,2),key = "6")],

    [sg.Button("7",size = (2,2),key = "7"), sg.Button("8",size = (2,2),key = "8"), sg.Button("9",size = (2,2),key = "9")],

]


seccion_operadores = [

    [sg.Button("+",size = (3,3),key = "+"), sg.Button("-",size = (3,3),key = "-")],

    [sg.Button("*",size = (3,3),key = "*"), sg.Button("/",size = (3,3),key = "/")],
    
    [sg.Button("=",size = (4,4), key = "=")]
]

resultado = [


    [sg.Text("", key = "-RESULTADO-", font = 'Courier 12',size = (15,8))]

]

operacion = [

    [sg.Text("" , key = "-OPERACION-", font='Courier 14',size = (20,2))],
    [sg.Frame("RESULTADO",resultado)],

]


#Creamos el layout

layout = [

    [
        sg.Frame("Cuenta",operacion),


        sg.Column(seccion_numeros),

        sg.VSeparator(),

        sg.Column(seccion_operadores)
    ]
]

#Creamos la ventana
window = sg.Window("Calculadora", layout, margins=(100,50))


strDigs = ["0","1","2","3","4","5","6","7","8","9"]

strOperadores = ["+","-","*","/"]


#Un booleano que es falso si el usuario no ha seleccionado el operador 
#Dependiendo de esto sabemos si el usuario esta seleccionando el primero o el segundo operando
EligioOperador = False


StrNum1, StrNum2, Op = "","",""



#Loop de la ventana
while True:

    event, values = window.read()


    if event == "Exit" or event == sg.WIN_CLOSED:
        break
    

    #Si el boton apretado es un digito
    if (event in strDigs):
    
        #Concatenar el digito al operando que corresponda,
        if not(EligioOperador):
            StrNum1 += event
        else:
            StrNum2 += event

        #Update de los elementos que muestran la operacion, y cada uno de los operandos seleccionados
        window["-OPERACION-"].update(value = StrNum1 + " " + Op + " " + StrNum2)



    #Si el boton apretado es un operador
    if event in strOperadores and not(EligioOperador):

        #Guarda el primer operando, si no se ingresó se supone cero
        if StrNum1 != "":


            while(StrNum1[0] == "0") and (len(StrNum1) > 1):
                StrNum1 = StrNum1[1:]
                    
                print(StrNum1)

        else:
            StrNum1 = str(window["-RESULTADO-"].get())

        #Guarda el operador seleccionado
        Op = event

        #Setear en true la variable de control
        EligioOperador = True

        #Update de los elementos que muestran la operacion, y cada uno de los operandos seleccionados
        window["-OPERACION-"].update(value = StrNum1 + " " + Op + " " + StrNum2)



    #Si el boton es el igual, resolver el calculo y resetear las variables de string 
    if (event == "="): 
    
        #Si eligio el operador calcular el resultado
        if (EligioOperador):
     
            if StrNum2 != "":

                #Quitar ceros a la izquierda

                while (StrNum2[0] == "0") and (len(StrNum2) > 1):
                    StrNum2 = StrNum2[1:]

                #Num2 = int(StrNum2)
            else:
                StrNum2 = "0"
                
            #Convertir los strings a flotantes o a enteros segun corresponda
            Num1 = float(StrNum1) if '.' in StrNum1 or 'e' in StrNum1.lower() else int(StrNum1)
            Num2 = float(StrNum2) if '.' in StrNum2 or 'e' in StrNum2.lower() else int(StrNum2)

            #Update del resultado, llama a la funcion que calcula el resultado
            window["-RESULTADO-"].update(CalcularResultado(Num1,Num2,Op))

            # resetea la variable de control
            EligioOperador = False


        #Si no eligio operador es por que solo selecciono un numero, este sera el resultado 
        # (si solo ingreso 3 y doy a igual, deberia decirme que es = 3)
        else:

            #Si no ha ingresado ni siquiera un numero, este se supone cero
            if StrNum1 == "":
                StrNum1 = "0"
            else:
                #Quitar ceros a la izq en caso de que el numero los tenga
                while(StrNum1[0] == "0") and (len(StrNum1) > 1):
                    StrNum1 = StrNum1[1:]

            #Actualizar el resultado
            window["-RESULTADO-"].update(value = StrNum1)
        

        #Update de los elementos que muestran la operacion, y cada uno de los operandos seleccionados
        window["-OPERACION-"].update(value = StrNum1 + " " + Op + " " + StrNum2)
        
        #Resetea los strings,
        StrNum1, StrNum2, Op = "","",""

   
    
window.close()    



""""    

    BUGS A CORREGIR


    * AL PRODUCIR UN ERROR EN EL RESULTADO, SI SELECCIONAMOS OTRO OPERADOR EL RESULTADO 'ERROR' SERA EL PRIMER OPERANDO DE ESTA NUEVA CUENTA
        AL PRESIONAR = NO PUEDE OPERAR CON EL STRING 'ERROR' Y LEVANTA ValueError
    DE ALGUNA MANERA SETEAR EL OPERANDO A CERO CUANDO ESTE SEA 'ERROR'


    * AL OBTENER UN RESULTADO FLOTANTE DEL TIPO 1.0, 1.000, 3.0 ETC, SI SELECCIONAMOS OTRO OPERADOR Y UN OPERANDO ENTERO, EL RESULTADO
        MANTENDRA ESE DECIMAL NULO, POR EJEMPLO DESDE UN RESULTADO 4.0, SI SELECCIONAMOS LA SUMA Y LUEGO EL NUMERO 2:

        4.0 + 2 = 6.0   EN VEZ DE :     4.0 + 2 = 6


"""