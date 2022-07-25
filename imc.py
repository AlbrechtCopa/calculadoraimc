# UTEL - UCAMP
# Jose Albrecht Copa
# Proyecto 1 - Caculadora de IMC

#   En este proyecto la especificacion de apellido paterno o materno fue reemplazado por primer y segundo apellido ya que existen personas que pueden tener un unico apellido

bandera = 1
bandera = bool(bandera)

while (bandera):

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
            print ('No es numero')

        if(res and edad > 0):
            auxiliar = False
        else:
            print ('* NO ES UN NUMERO ENTERO')
    
    #   While para el ingreso y validacion de peso

    auxiliar = True
    while(auxiliar):
        try:
            peso = float(input('INGRESE SU PESO EN KG.: '))
            res = True
        except ValueError:
            res = False
            print ('No es numero')

        if(res and peso > 0):
            auxiliar = False
        else:
            print ('* NO ES UN NUMERO ENTEROD')

    bandera = 0