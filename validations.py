
def validate_string(data):
    words  = str(data) 
   
    try:
        number = int(words)
        #print('Se pudo convertir a int lo siguiente {}'.format(number))
        print('Solo esta permitido cadenas y usted ha ingresado un numero')
        return False           
    except ValueError:
        pass   
        #print('La entrada {} no se pudo convertir a int'.format(words))

    #largo del input
    lenght = len(data) 

    #try to convert characters into numbers
    for i in range(lenght):
        try:
            character = int(words[i])
            #print('El caracter {} es un numero'.format(character))
            print('Todos los caracteres de la data deben ser letras y no numeros')
            return False
        except ValueError:
           # print('todo ok con el caracter ')
            continue

    return True 


def validate_varchar(data,maximum_length):
    
    words  = str(data) 
   
    try:
        number = int(words)
        #print('Se pudo convertir a int lo siguiente {}'.format(number))
        print('Solo esta permitido cadenas y usted ha ingresado un numero')
        return False           
    except ValueError:
        pass   
        #print('La entrada {} no se pudo convertir a int'.format(words))

    #largo del input
    lenght = len(data) 
    if (lenght > maximum_length):
        print('La longitud de la entrada no debe ser mayor a {}'.format(maximum_length))
        return False

    #try to convert characters into numbers
    for i in range(lenght):
        try:
            character = int(words[i])
            #print('El caracter {} es un numero'.format(character))
            print('Todos los caracteres de la data deben ser letras y no numeros')
            return False
        except ValueError:
           # print('todo ok con el caracter ')
            continue

    return True 

def validate_int(data):

    try:
        number = int(data)
        print('Se pudo convertir a int lo siguiente {}'.format(number))
        
        return True           
    except ValueError:
          
        print('La entrada {} no se pudo convertir a int'.format(data))
        return False
        
def validate_char(data):
    words  = str(data) 
   
    try:
        number = int(words)
        #print('Se pudo convertir a int lo siguiente {}'.format(number))
        print('Solo esta permitido cadenas y usted ha ingresado un numero')
        return False           
    except ValueError:
        pass   
        #print('La entrada {} no se pudo convertir a int'.format(words))

    #largo del input
    lenght = len(data) 
    if (lenght > 1):
        print('La longitud de la entrada no debe ser mayor a {}'.format(1))
        return False

    #try to convert characters into numbers
    for i in range(lenght):
        try:
            character = int(words[i])
            #print('El caracter {} es un numero'.format(character))
            print('Todos los caracteres de la data deben ser letras y no numeros')
            return False
        except ValueError:
           # print('todo ok con el caracter ')
            continue

    return True 

if __name__ == "__main__":
    
    while True:
        flag=1
        while flag:
            tusu_desc = input(' Ingrese el char: ')
            if (tusu_desc != ''):
                flag = 0


        boolean =validate_char(tusu_desc)
        print('La respuesta sale {}',format(boolean))

    

    # print('El tipo de dato es de {} \n'.format(type(tusu_desc)))

    # tusu_estado = int(input(' Ingrese el tusu_estado: '))
    # print('El tipo de dato es de {} \n'.format(type(tusu_estado)))

    # tusu_id = int(input(' Ingrese el tusu_id: '))
    # print('El tipo de dato es de {} \n'.format(type(tusu_id)))

    
