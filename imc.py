# UTEL - UCAMP
# Jose Albrecht Copa
# Proyecto 1 - Caculadora de IMC

#   En este proyecto la especificacion de apellido paterno o materno fue reemplazado por primer y segundo apellido ya que existen personas que pueden tener un unico apellido

from pickle import TRUE


bandera = 1
bandera = bool(bandera)

while (bandera == 1):

    # Menu de inicio

    print ('*'*32)
    print ('*'+' '*30+'*')
    print ('*'+' '*10+'BIENVENIDO'+' '*10+'*')
    print ('*'+' '*4+'INGRESE LOS SIGUIENTES'+' '*4+'*')
    print ('*'+' '*12+'DATOS:'+' '*12+'*')
    print ('*'+' '*30+'*')
    print ('*'*32)

    auxiliar = True
    
    #  Ingreso de informacion

    #   Un while para validar la exisencia del dato nombre, que sea mayor a un caracter y que no sea un numero

    while (auxiliar):
        nombre = str(input('INGRESE SU/S NOMBRE/S: ')) 
        if ((len(nombre)) >= 2):
            #   usamos variables auxiliares para manejar el error al momento de validar si es un numero
            try:
                #   Se convierte la variable a numero para saber si no da error
                #   La variable res es otro auxiliar para almacenar el valor 
                int(nombre)
                res = True
            except ValueError:
                res = False

            if(res):
                #   En caso de detectarse que sea numero se da un mensaje y se solicita la informacion nuevamente
                print('INTRODUJO UN NUMERO.')
            else:
                #   En caso que la variable no sea numero se la cambia a tipo string y se termina el bucle
                str(nombre)
                auxiliar = False
    
    #   While para ingreso de primer apellido
    #   Se repite la misma estructura que se uso para el nombre
    auxiliar = True
    while (auxiliar):
        pri_apellido = str(input('INGRESE SU PRIMER APELLIDO: ')) 
        if ((len(pri_apellido)) >= 2):
            try:
                int(pri_apellido)
                res = True
            except ValueError:
                res = False

            if(res):
                print('INTRODUJO UN NUMERO.')
            else:
                str(pri_apellido)
                auxiliar = False

    #   While para ingreso de segundo apellido
    #   Si bien la estructura es similar a las anteriores, en este caso puede ser que la persona no tenga un segundo apellido por lo que este puede quedar vacio
    auxiliar = True
    while (auxiliar):
        seg_apellido = str(input('INGRESE SU SEGUNDO APELLIDO: ')) 
        if ((len(seg_apellido)) >= 1):
            try:
                int(seg_apellido)
                res = True
            except ValueError:
                res = False
        if(res):
            print('INTRODUJO UN NUMERO.')
        else:
            str(pri_apellido)
            auxiliar = False

    #   While para el ingreso y validacion de edad

    auxiliar = True
    while(auxiliar):
        try:
            edad = int(input('INGRESE SU EDAD: '))
            res = True
        except ValueError:
            res = False
            print ('NO ES UN VALOR VALIDO.')

        if(res and edad > 0):
            auxiliar = False
        else:
            print ('* NO ES UN NUMERO ENTERO.')
            print ('* LOS VALORES NO DEBEN SER NEGATIVOS.')
    
    #   While para el ingreso y validacion de peso

    auxiliar = True
    while(auxiliar):
        try:
            peso = float(input('INGRESE SU PESO EN KG.: '))
            res = True
        except ValueError:
            res = False
            print ('NO ES UN VALOR VALIDO.')

        if(res and peso > 0):
            auxiliar = False
        else:
            print ('* REVISE QUE USE PUNTO EN LUGAR DE COMA.')
            print ('* LOS VALORES NO DEBEN SER NEGATIVOS.')

    #   While para el ingreso y validacion de talla

    auxiliar = True
    while(auxiliar):
        try:
            talla = float(input('INGRESE SU TALLA EN MTS.: '))
            res = True
        except ValueError:
            res = False
            print ('NO ES UN VALOR VALIDO.')

        if(res and talla > 0):
            auxiliar = False
        else:
            print ('* REVISE QUE USE PUNTO EN LUGAR DE COMA.')
            print ('* LOS VALORES NO DEBEN SER NEGATIVOS.')

    #Procesando de informacion
    #Valores tomados de Wikipedia

    imc = peso / talla**2
    imc = float(imc)
    if(imc >= 0 and imc <= 15.99):
        resultado = ' DELGADEZ SEVERA '
    elif(imc >= 16 and imc <= 16.99):
        resultado = 'DELGADEZ MODERADA'
    elif(imc >= 17 and imc <= 18.49):
        resultado = '  DELGADEZ LEVE  '
    elif(imc >= 18.5 and imc <= 24.99):
        resultado = '     NORMAL      '
    elif(imc >= 25 and imc <= 29.99):
        resultado = '   PREOBESIDAD   '
    elif(imc >= 30 and imc <= 34.99):
        resultado = '  OBESIDAD LEVE  '
    elif(imc >= 35 and imc <= 39.99):
        resultado = ' OBESIDAD MEDIA  '
    elif(imc >= 40):
        resultado = 'OBESIDAD MÓRBIDA '

    #Emision de resultado
    print('*'*33)
    print('*\t\t'+'RESULTADO'+'\t\t*')
    print('*'*33+'\n\n')

    print('ESTIMAD@',nombre.upper(),pri_apellido.upper(),seg_apellido.upper(),'.\nUSTED TIENE',edad,'AÑOS.\nUSTED MIDE',talla,'MTS.\nSU PESO ES DE',peso,'KG.')
    print (f'SU IMC ES: {imc:.2f}, - {resultado}')

    fin = True
    while(fin):
        print('''
        ***********************************************************
        *                                                         *
        *               DESEA REALIZAR OTRO CALCULO               *
        *                        INGRESE SI                       *
        *                                                         *
        ***********************************************************
        ''')
        valor = str(input('VALOR:'))
        valor = valor.upper()
        if(valor == 'SI'):
            fin = False
        else:
            bandera = 0