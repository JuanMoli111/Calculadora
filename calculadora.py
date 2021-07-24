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


    [sg.Text("" , key = "-OPERACION-", font='Courier ',size = (5,5))],

    #[sg.HSeparator()],


    [sg.Text("Num1")],
    [sg.Text("" , key = "-NUM1-",size = (5,5), font='Courier 10')],
    [sg.Text("Num2")],
    [sg.Text("" , key = "-NUM2-", font='Courier 10',size = (5,5))],


    [sg.Text("RESULTADO")],
    [sg.Text("", key = "-RESULTADO-",size = (5,5))]

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
window = sg.Window("Calculadora",layout,margins=(300,200))



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
            print("NUM UNO ES:  " + StrNum1)

            
            #window("-NUM1-").update(value = StrNum1)

        else:
            StrNum2 += event
            print(StrNum2)
            #window["-NUM2-"].update(value = StrNum2)


    #Si el boton apretado es un operador
    if event in strOperadores and not(EligioOperador):

        #Guarda el primer operando, si no se ingresó se supone cero
        if StrNum1 != "":
            Num1 = int(StrNum1)
        else:
            Num1 = 0

        #Guarda el operador seleccionado
        Op = event
        print(EligioOperador)

        #Setear en true la variable de control
        EligioOperador = True

        print(EligioOperador)
    #Si el boton es el igual, resolver el calculo y resetear las variables de string
    if (event == "=") and (EligioOperador):

        if StrNum2 != "":
            Num2 = int(StrNum2)
            print(Num2)
        else:
            Num2 = 0
            
        window["-RESULTADO-"].update(CalcularResultado(Num1,Num2,Op))

        StrNum1, StrNum2, Op = "","",""


        
    window["-OPERACION-"].update(value = StrNum1 + " " + Op + " " + StrNum2)
    window["-NUM2-"].update(value = StrNum2)

    #window("-NUM1-").update(value = StrNum1)

    window["-NUM1-"].update(StrNum1)
    #window["-NUM2-"].update(StrNum2)



        #No logro hacer un update que muestre el nuevo nro
        







   
    
window.close()    



"""     
    if event in strDigs and not(EligioPrimerNro):

        if not(EligioPrimerDig):
   

            PrimerNro = event

            EligioPrimerDig = True


            print("Acaba de elegir primer dig y fue " + PrimerNro)

        else:

            PrimerNro += event

            print("Acaba de elegir siguiente dig y resulto " + PrimerNro)
    if not(EligioPrimerNro) and event == "-IGUAL-":
        
        EligioPrimerNro = True

        PrimerOperando = int(PrimerNro)
 """