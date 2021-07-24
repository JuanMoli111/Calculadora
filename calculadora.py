from funciones import CalcularResultado

import PySimpleGUI as sg

#Definimos los elementos divididos en secciones segun su funcion
#una para los operandos, otra para los operadores, y una seccion para la operacion y el resultado

seccion_numeros = [

    [sg.Button("0",size = (2,2),key = "0")],

    [sg.Button("1",size = (2,2),key = "1"), sg.Button("2",size = (2,2),key = "2"), sg.Button("3",size = (2,2),key = "3")],

    [sg.Button("4",size = (2,2),key = "4"), sg.Button("5",size = (2,2),key = "5"), sg.Button("6",size = (2,2),key = "6")],

    [sg.Button("7",size = (2,2),key = "7"), sg.Button("8",size = (2,2),key = "8"), sg.Button("9",size = (2,2),key = "9")],

]


seccion_operadores = [

    [sg.Button("+",size = (3,3),key = "+"), sg.Button("-",size = (3,3),key = "-")],

    [sg.Button("*",size = (3,3),key = "*"), sg.Button("/",size = (3,3),key = "/")],
    
    [sg.Button("=",size = (4,4), key = "=")]
]



operacion = [


    [sg.Text("" , key = "-OPERACION-", font='Courier 14',size = (20,2))],

    #[sg.HSeparator()],


    [sg.Text("Num1")],

    [sg.Text("" , key = "-NUM1-", font='Courier 10',size = (10,5))],

    [sg.Text("Num2")],
    [sg.Text("" , key = "-NUM2-", font='Courier 10',size = (10,5))],


    [sg.Text("RESULTADO")],
    [sg.Text("", key = "-RESULTADO-", font = 'Courier 12',size = (15,8))]

]

#Creamos el layout

layout = [


    [
        sg.Column(operacion),

        sg.Column(seccion_numeros),

        sg.VSeparator(),

        sg.Column(seccion_operadores)
    ]
]

#Creamos la ventana
window = sg.Window("Calculadora", layout, margins=(150,100))



strDigs = ["0","1","2","3","4","5","6","7","8","9"]

strOperadores = ["+","-","*","/"]

#Un booleano que es falso si el usuario no ha seleccionado el primer numero
IngresoPrimerNro = False
#IngresoSegundoNro = False

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


            Num1 = int(StrNum1)
        else:
            Num1 = 0

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
                    
                    print(StrNum2)



                Num2 = int(StrNum2)
            else:
                Num2 = 0
                
            #Update del resultado, llama a la funcion que calcula el resultado
            window["-RESULTADO-"].update(CalcularResultado(Num1,Num2,Op))

            # resetea la variable de control
            
            EligioOperador = False

        #Si no eligio operador es por que solo selecciono un numero, este sera el resultado 
        # (si solo ingreso 3 y doy a igual, deberia decirme que es = 3)
        else:

            #Si no ha ingresado ni siquiera un numero, el resultado es cero
            if StrNum1 == "":
                Num1 = 0
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
        


    window["-NUM2-"].update(value = StrNum2)
    window["-NUM1-"].update(value = StrNum1)


   
    
window.close()    

