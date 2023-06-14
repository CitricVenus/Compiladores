# Erick Alfonso Montan Lopez - A01379766
"""Nuestras tablas salen despues de hacer nuestra maquina de estados para el lenguaje, de igual forma
Nuestra tabla de transiciones, tabla de errores y tabla de estados aceptores, salen de nuestra maquina de estados"""
# Tabla de nuestros tokens, para el reconocimiento de tokens
tokens = {
    "int": "1",
    "if": "2",
    "read": "3",
    "float": "4",
    "read": "5",
    "write": "6",
    "string": "7",
    "while": "8",
    "void": "9",
    "for": "10",
    "return": "11",
    "+": "12",
    "-": "13",
    "*": "14",
    "/": "15",
    "<": "16",
    "<=": "17",
    ">": "18",
    ">=": "19",
    "==": "20",
    "!=": "21",
    "=": "22",
    ";": "23",
    ",": "24",
    "(": "25",
    ")": "26",
    "[": "27",
    "]": "28",
    "{": "29",
    "}": "30",
    "identifier": "31",
    "string_value": "32",
    "float_number": "33",
    "int_number": "34"
}
# list con nuestras letras validas
letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
          'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
# list con nuestros valores numericos validos
numeros = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
# list con nuestros delimitadores validos
delimitadores = ['+', '-', '*', '/', '>', '<', '!', '=', ';',
                 ',', '"', '.', '(', ')', '[', ']', '{', '}', ' ', '\n', '\t']
# Nuestra tabla de transicione
tabla_de_transicion = [
    [2, 3, 20, 21, 22, 6, 9, 10, 12, 11, 23, 24,
        1, 38, 25, 26, 27, 28, 29, 30, 0, 38, 13,],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 14, 1, 1, 1, 1, 1, 1, 1, 1, 1, 39],
    [2, 2, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15,
        38, 38, 15, 15, 15, 15, 15, 15, 15, 38, 39],
    [17, 3, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17,
        38, 4, 17, 17, 17, 17, 17, 17, 17, 38, 39],
    [40, 5, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40,
        40, 40, 40, 40, 40, 40, 40, 40, 40, 38, 39],
    [16, 5, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16,
        38, 38, 16, 16, 16, 16, 16, 16, 16, 38, 39],
    [18, 18, 18, 18, 7, 18, 18, 18, 18, 18, 18, 18,
        38, 38, 18, 18, 18, 18, 18, 18, 18, 38, 39],
    [7, 7, 7, 7, 8, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 39],
    [7, 7, 7, 7, 7, 19, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 39],
    [31, 31, 31, 31, 31, 31, 31, 31, 31, 32, 31, 31,
        38, 38, 31, 31, 31, 31, 31, 31, 31, 38, 39],
    [33, 33, 33, 33, 33, 33, 33, 33, 33, 34, 33, 33,
        38, 38, 33, 33, 33, 33, 33, 33, 33, 38, 39],
    [35, 35, 35, 35, 35, 35, 35, 35, 35, 36, 35, 35,
        38, 38, 35, 35, 35, 35, 35, 35, 35, 38, 39],
    [41, 41, 41, 41, 41, 41, 41, 41, 41, 37, 41, 41,
        41, 41, 41, 41, 41, 41, 41, 41, 41, 38, 39]
]
# Los estados aceptores
estados_aceptados = [13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23,
                     24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37]
# Estados de error
estados_de_error = [38, 39, 40, 41]
# Diccionarios que nos ayudaran al manejo y almacenamiento de nuestros identificadores, strings, integers y floats
tabla_identifieres = {}
tabla_strings = {}
tabla_integers = {}
tabla_floats = {}
# Nuestras tablas de salida
reconocimiento_de_tokens = []
escaner_output = []

current_token = ""
current_token_cont = 0


def analizador():
    # se especifica que archivo es el que se va a leer
    file = open("code.txt", 'r')
    estado_actual = 0
    string_aux = ""
    cont_string = 1
    cont_int_num = 1
    cont_float_num = 1
    cont_identifier = 1
    numero_aux = 0
    nuevo_estado = 0
    imprime = True
# El while termina asta que encuentre el EOF del archivo leido
    while 1:
        # Obtiene caracter por caracter del archivo que se está leyendo
        char = file.read(1)
        # Si el caracter leido no es un "Blank" va a entrar  a revisar si tiene continuidad el caracter leido
        # Si el caracter leido es un "Blank" lo ignora y sigue con el siguiente caracter
        if (char != ' ' and char != '\t' and char != '\n'):
            estado_actual = 0
            # String auxiliar nos va a ayudar guardar los caracteres leidos.
            string_aux = ""
            # Si esse termina el archivo, termina el while
            if not char:
                break
            # Se revisa que el estado en el nos encontramos no sea un estado aceptado o un estado de error
            # Si no es un estado de error o estado aceptado va a continuar moviendose dentro de la tabla de transiciones
            while (not estado_actual in estados_aceptados and not estado_actual in estados_de_error):
                # Se obtiene el siguiente estado dependiendo el caracter leido y el estado en el que nos encontrabamos
                nuevo_estado = nuevoEstado(estado_actual, char)
                # Si el estado en el que estamos y el caracter leido entran en un estado no aceptor y no terminal, nos regresa un true
                # El true nos dice que el estado en el que estamos se mueve a otro estado no terminal ni de error
                if (avanza(estado_actual, char)):
                    # Verificamos que no sea fin del archivo
                    if (char == ''):
                        # Si es fin del archivo, nos movemos al estado de error numero 39 EOF
                        nuevo_estado = 39

                    else:
                        # Se va contruyendo un string con los caracteres leidos
                        string_aux = string_aux + char
                        char = file.read(1)
                # Nos movemos al estado siguiente
                estado_actual = nuevo_estado
            # Se revisa si el estado actual es un estado de los compuestos >= ,<= , == , !=
            # Se almacena el numero del token en el output del escanner y se guarda en el reconocimiento de tokens
            if (estado_actual in estados_aceptados):
                if (estado_actual == 33):
                    numero_aux = tokens.get(">=")
                    escaner_output.append(numero_aux)
                    reconocimiento_de_tokens.append(">=")
                    continue
                if (estado_actual == 32):
                    numero_aux = tokens.get("<=")
                    escaner_output.append(numero_aux)
                    reconocimiento_de_tokens.append("<=")
                    continue
                if (estado_actual == 36):
                    numero_aux = tokens.get("==")
                    escaner_output.append(numero_aux)
                    reconocimiento_de_tokens.append("==")
                    continue
                if (estado_actual == 37):
                    numero_aux = tokens.get("!=")
                    escaner_output.append(numero_aux)
                    reconocimiento_de_tokens.append("!=")
                    continue
                if (string_aux in tokens or string_aux.lower() in tokens):
                    numero_aux = tokens.get(string_aux.lower())
                    escaner_output.append(numero_aux)
                    reconocimiento_de_tokens.append(string_aux.lower())
                # Si no es un estado con caracteres compuestos, revisa si es un identificador, un string, numero entero o un numero flotante
                else:
                    if (estado_actual == 13):
                        # El archivo esta vacio
                        return print("Fin de archivo")
                    # Este estado guarda los strings
                    if (estado_actual == 14):
                        # Revisamos pprimero que no este almacenado el valor
                        if (not string_aux in tabla_strings):
                            # se usa para los strings, si char existe en la tabla de tokens, sigue
                            # Esto para poder sacar los tokens "
                            # se agrega el string en un diccionario
                            # se guarda el valor y el numero que le corresponde
                            # cont_string guarda el valor numerico de la posicion en el diccionario
                            tabla_strings[string_aux.replace(
                                '"', '')] = cont_string
                            # se guarda el string en el reconocimiento de tokens
                            reconocimiento_de_tokens.append(
                                string_aux.replace('"', ''))
                            # se saca el numero del token String
                            numero_aux = tokens.get("string_value")
                            # Se crea un string que se guardara en el escaner output
                            out_aux = str(numero_aux) + \
                                ','+str(cont_string)
                            # se guarda el valor en el escaner output
                            escaner_output.append(out_aux)
                            # como ya se guardo un valor, nuestro contador se aumenta en uno para el siguiente que sea diferente al ya guardado
                            cont_string += 1
                        # Si el string ya esta guardado, solo guardamos valores en el reconocimiento de tokens y en el output
                        # Se van a guardar con los valores del ya creado
                        else:
                            # Se guarda el token reconocido
                            reconocimiento_de_tokens.append(string_aux)
                            # Se saca el numero del valor de la tabla que le corresponde, en este caso de la tabla de strings
                            int_num = tabla_strings.get(string_aux)
                            # se saca el numero de token que le corresponde
                            numero_aux = tokens.get("string_value")
                            # Se crea el string con los dos valores sacados anteriormente
                            out_aux = str(numero_aux) + "," + str(int_num)
                            # se guarda en el escaner output
                            escaner_output.append(out_aux)

                    if (estado_actual == 15):
                        if (not string_aux in tabla_identifieres):
                            tabla_identifieres[string_aux] = cont_identifier
                            reconocimiento_de_tokens.append(string_aux)
                            numero_aux = tokens.get("identifier")
                            out_aux = str(numero_aux) + ',' + \
                                str(cont_identifier)
                            escaner_output.append(out_aux)
                            cont_identifier += 1
                        else:
                            reconocimiento_de_tokens.append(string_aux)
                            int_num = tabla_identifieres.get(string_aux)
                            numero_aux = tokens.get("identifier")
                            out_aux = str(numero_aux) + "," + str(int_num)
                            escaner_output.append(out_aux)
                    if (estado_actual == 16):
                        if (not string_aux in tabla_floats):
                            tabla_floats[string_aux] = cont_float_num
                            reconocimiento_de_tokens.append(string_aux)
                            numero_aux = tokens.get("float_number")
                            out_aux = str(numero_aux) + ',' + \
                                str(cont_float_num)
                            escaner_output.append(out_aux)
                            cont_float_num += 1
                        else:
                            reconocimiento_de_tokens.append(string_aux)
                            int_num = tabla_floats.get(string_aux)
                            numero_aux = tokens.get("float_number")
                            out_aux = str(numero_aux) + "," + str(int_num)
                            escaner_output.append(out_aux)
                    if (estado_actual == 17):
                        if (not string_aux in tabla_integers):
                            tabla_integers[string_aux] = cont_int_num
                            reconocimiento_de_tokens.append(string_aux)
                            numero_aux = tokens.get("int_number")
                            out_aux = str(numero_aux) + ',' + str(cont_int_num)
                            escaner_output.append(out_aux)
                            cont_int_num += 1
                        else:
                            reconocimiento_de_tokens.append(string_aux)
                            int_num = tabla_integers.get(string_aux)
                            numero_aux = tokens.get("int_number")
                            out_aux = str(numero_aux) + "," + str(int_num)
                            escaner_output.append(out_aux)
                    # Si el estado es 19, significa que es un comentario, este lo ignoramos
                    if (estado_actual == 19):
                        continue

# Si el estado actual es un estado de error , imprime cual fue el error
# Si entra algun error, no se imprime las tablas
            if (estado_actual in estados_de_error):
                if estado_actual == 39:
                    print("EOF error")
                    imprime = False
                    # imprimeTablas(True)
                    break
                if estado_actual == 38:
                    print(
                        "Error, caracter no aceptado o hace falta delimitador " + "'" + char+"'")
                    imprime = False
                    # imprimeTablas(True)
                    break
                if estado_actual == 40:
                    print("Error al crear valor flotante ")
                    imprime = False
                    # imprimeTablas(True)
                    break
                if estado_actual == 41:
                    print("Error al crear el token" + ' "!=" ,' +
                          '"'+char + '"' + " es diferente a " + '"="')
                    imprime = False
                    # imprimeTablas(True)
                    break
            # Si char tiene el valor de un token, aqui revisamos que sea un token valido y lo agregamos al escaner output y al reconocimiento de tokens
            if (char in tokens or char.lower() in tokens):
                numero_aux = tokens.get(char.lower())
                escaner_output.append(numero_aux)
                reconocimiento_de_tokens.append(char.lower())

    # Se cierra el archivo leido
    file.close()
    # Si no hubo errores, se imprime las tablas
    if imprime:
        imprimeTablas(True)
    else:
        imprimeTablas(False)

# Revisa si el siguiente estado es un estado de error, estado final o si es un estado no final. Esto dependiendo el caracter leido
# Si no es un estado final, regresa True que significa que va a seguir leyendo mas caracteres


def avanza(estado, char):
    siguiente_estado = 0
    if (char in letras):
        siguiente_estado = tabla_de_transicion[estado][0]
        if (siguiente_estado in estados_aceptados or siguiente_estado in estados_de_error):
            return False
        else:
            return True
    if (char in numeros):
        siguiente_estado = tabla_de_transicion[estado][1]
        if (siguiente_estado in estados_aceptados or siguiente_estado in estados_de_error):
            return False
        else:
            return True
    if (char == '+'):
        siguiente_estado = tabla_de_transicion[estado][2]
        if (siguiente_estado in estados_aceptados or siguiente_estado in estados_de_error):
            return False
        else:
            return True
    if (char == '-'):
        siguiente_estado = tabla_de_transicion[estado][3]
        if (siguiente_estado in estados_aceptados or siguiente_estado in estados_de_error):
            return False
        else:
            return True
    if (char == '*'):
        siguiente_estado = tabla_de_transicion[estado][4]
        if (siguiente_estado in estados_aceptados or siguiente_estado in estados_de_error):
            return False
        else:
            return True
    if (char == '/'):
        siguiente_estado = tabla_de_transicion[estado][5]
        if (siguiente_estado in estados_aceptados or siguiente_estado in estados_de_error):
            return False
        else:
            return True
    if (char == '<'):
        siguiente_estado = tabla_de_transicion[estado][6]
        if (siguiente_estado in estados_aceptados or siguiente_estado in estados_de_error):
            return False
        else:
            return True
    if (char == '>'):
        siguiente_estado = tabla_de_transicion[estado][7]
        if (siguiente_estado in estados_aceptados or siguiente_estado in estados_de_error):
            return False
        else:
            return True
    if (char == '!'):
        siguiente_estado = tabla_de_transicion[estado][8]
        if (siguiente_estado in estados_aceptados or siguiente_estado in estados_de_error):
            return False
        else:
            return True
    if (char == '='):
        siguiente_estado = tabla_de_transicion[estado][9]
        if (siguiente_estado in estados_aceptados or siguiente_estado in estados_de_error):
            return False
        else:
            return True
    if (char == ';'):
        siguiente_estado = tabla_de_transicion[estado][10]
        if (siguiente_estado in estados_aceptados or siguiente_estado in estados_de_error):
            return False
        else:
            return True
    if (char == ','):
        siguiente_estado = tabla_de_transicion[estado][11]
        if (siguiente_estado in estados_aceptados or siguiente_estado in estados_de_error):
            return False
        else:
            return True
    if (char == '"'):
        siguiente_estado = tabla_de_transicion[estado][12]
        if (siguiente_estado in estados_aceptados or siguiente_estado in estados_de_error):
            return False
        else:
            return True
    if (char == '.'):
        siguiente_estado = tabla_de_transicion[estado][13]
        if (siguiente_estado in estados_aceptados or siguiente_estado in estados_de_error):
            return False
        else:
            return True
    if (char == '('):
        siguiente_estado = tabla_de_transicion[estado][14]
        if (siguiente_estado in estados_aceptados or siguiente_estado in estados_de_error):
            return False
        else:
            return True
    if (char == ')'):
        siguiente_estado = tabla_de_transicion[estado][15]
        if (siguiente_estado in estados_aceptados or siguiente_estado in estados_de_error):
            return False
        else:
            return True
    if (char == '['):
        siguiente_estado = tabla_de_transicion[estado][16]
        if (siguiente_estado in estados_aceptados or siguiente_estado in estados_de_error):
            return False
        else:
            return True
    if (char == ']'):
        siguiente_estado = tabla_de_transicion[estado][17]
        if (siguiente_estado in estados_aceptados or siguiente_estado in estados_de_error):
            return False
        else:
            return True
    if (char == '{'):
        siguiente_estado = tabla_de_transicion[estado][18]
        if (siguiente_estado in estados_aceptados or siguiente_estado in estados_de_error):
            return False
        else:
            return True
    if (char == '}'):
        siguiente_estado = tabla_de_transicion[estado][19]
        if (siguiente_estado in estados_aceptados or siguiente_estado in estados_de_error):
            return False
        else:
            return True
    if (char == ' ' or char == '\t' or char == '\n'):
        siguiente_estado = tabla_de_transicion[estado][20]
        if (siguiente_estado in estados_aceptados or siguiente_estado in estados_de_error):
            return False
        else:
            return True
    if (not char in letras and not char in numeros and not char in delimitadores):
        siguiente_estado = tabla_de_transicion[estado][21]
        if (siguiente_estado in estados_aceptados or siguiente_estado in estados_de_error):
            return False
        else:
            return True
    if (char == ''):
        siguiente_estado = tabla_de_transicion[estado][22]
        if (siguiente_estado in estados_aceptados or siguiente_estado in estados_de_error):
            return False
        else:
            return True


# regresa el estado dependiendo el caracter leido y el caracter en el que nos encontramos
# Esta parte la hacemos con nuestra tabla de transiciones
def nuevoEstado(estado, char):
    if (char in letras):
        return tabla_de_transicion[estado][0]
    if (char in numeros):
        return tabla_de_transicion[estado][1]
    if (char == '+'):
        return tabla_de_transicion[estado][2]
    if (char == '-'):
        return tabla_de_transicion[estado][3]
    if (char == '*'):
        return tabla_de_transicion[estado][4]
    if (char == '/'):
        return tabla_de_transicion[estado][5]
    if (char == '<'):
        return tabla_de_transicion[estado][6]
    if (char == '>'):
        return tabla_de_transicion[estado][7]
    if (char == '!'):
        return tabla_de_transicion[estado][8]
    if (char == '='):
        return tabla_de_transicion[estado][9]
    if (char == ';'):
        return tabla_de_transicion[estado][10]
    if (char == ','):
        return tabla_de_transicion[estado][11]
    if (char == '"'):
        return tabla_de_transicion[estado][12]
    if (char == '.'):
        return tabla_de_transicion[estado][13]
    if (char == '('):
        return tabla_de_transicion[estado][14]
    if (char == ')'):
        return tabla_de_transicion[estado][15]
    if (char == '['):
        return tabla_de_transicion[estado][16]
    if (char == ']'):
        return tabla_de_transicion[estado][17]
    if (char == '{'):
        return tabla_de_transicion[estado][18]
    if (char == '}'):
        return tabla_de_transicion[estado][19]
    if (char == ' ' or char == '\t' or char == '\n'):
        return tabla_de_transicion[estado][20]
    if (not char in letras and not char in numeros and not char in delimitadores):
        return tabla_de_transicion[estado][21]
    if (char == ''):
        return tabla_de_transicion[estado][22]


# imprime las tablas
def imprimeTablas(error_aux):
    if (error_aux == True):
        
            print("---------------------------Reconocimiento de tokens----------------------\n")
            print(reconocimiento_de_tokens)
            print("---------------------------Output de escaner----------------------\n")
            print(escaner_output)
            print("------------------------Tabla de identificadores-------------------------\n")
            print(tabla_identifieres)
            print("-----------Tabla de numeros con punto flotante-----------\n")
            print(tabla_floats)
            print("-----------Tabla de numeros enteros-----------\n")
            print(tabla_integers)
            print("---------Tabla de strings-------------\n")
            print(tabla_strings)
        
       

# se llama la funcion del analizador
analizador()

def match(terminal):
    if current_token == terminal:
        current_token = reconocimiento_de_tokens[current_token_cont + 1]
    else:
        print("Error")
        exit(1)
        
def syntax_analysis():
    reconocimiento_de_tokens.append('$')
    current_token = reconocimiento_de_tokens[current_token_cont]
    program()
    if(current_token == '$'):
        print("Syntax_Analysis_OK")
    else:
        print("Syntax_Analysis_Error")
        exit(1)
    

def program():
    declaration()
    if current_token == 'void':
        match('void')
        match('ID')
        match('(')
        match('void')
        match(')')
        match('{')
        local_declarations()
        statement_list()
        match('return')
        match(';')
        match('}')
    else:
        print("Syntax_Analysis_Error")
        exit(1)

def declaration_list():
    declaration()
    declaration_list()
    if current_token == 'void':
        match('void')
        return
    else:
      print("Syntax_Analysis_Error")
      exit(1)  

def declaration():
    type_specifer()
    if current_token == 'ID':
        match('ID')
        declaration_prime()
        
    if current_token == 'void':
        match('void')
        match('ID')
        match('(')
        params()
        match(')')
        match('{')
        local_declarations()
        statement_list()
        match('return')
        return_stmt_prime()
        match('}')  
        
def declaration_prime():
    if current_token == ';':
        match(';')
    elif current_token == '[':
        match('[')
        match('integer_constant')
        match(']')
        match(';')
    elif current_token == '(':
        params()
        match(')')
        match('{')
        local_declarations()
        statement_list()
        match('return')
        return_stmt_prime()
        match('}') 
    
        
def type_specifer():
    if current_token == 'int':
          match('int')
    elif current_token == 'float':
          match('float')
    elif current_token == 'string':
        match('string')
    else:
        print("Syntax_Analysis_Error")
        exit(1)        
        
def params():
    param()
    param_list_prime()
    
    if current_token == 'void':
        match('void')
        return

def param_list_prime():
    if current_token == ',':
        match(',')
        param()
        param_list_prime()
    
    elif current_token == ',' or current_token == ')':
        return
    
    else:
        print("Syntax_Analysis_Error")
        exit(1)      

def param():
    type_specifer()
    if current_token == 'ID':
        match('ID')
        param_prime()

def param_prime():
    if current_token == '[':
        match('[')
        match(']')
    elif current_token == ',' or current_token == ')':
        return
    else:
        print("Syntax_Analysis_Error")
        exit(1) 

def local_declarations():
    type_specifer()
    if current_token == 'ID':
        match('ID')
        declaration_prime()
        local_declarations()
    elif current_token == 'ID' or current_token == '{' or current_token == 'if' or current_token == 'while' or current_token == 'return' or current_token == 'input' or current_token == 'output' or current_token == 'return' or current_token == '}':
        return
    else:
        print("Syntax_Analysis_Error")
        exit(1) 
    
def statement_list():
    statement()
    statement_list()
    if current_token == 'return' or current_token == '}':
        return
    else:
        print("Syntax_Analysis_Error")
        exit(1) 

def statement():
    if current_token == 'ID':
        match('ID')
        statement_prime()
    elif current_token == '{':
        match('{')
        local_declarations()
        statement_list()
        match('}')
    elif current_token == 'if':
        match('if')
        match('(')
        expression()
        match(')')
        statement()
        selection_stmt_prime()
    elif current_token == 'while':
        match('while')
        match('(')
        expression()
        match(')')
        statement()
    elif current_token == 'return':
        match('return')
        return_stmt_prime()
    elif current_token == 'input':
        match('input')
        match('ID')
        var_prime()
        match(';')
    elif current_token == 'output':
        match('output')
        expression()
        match(';')
    
def statement_prime():
    
    if current_token == '(':
        match('(')
        call_prime()
        match(';')
    else:
        var_prime()
        match('=')
        assignment_stmt_prime()
    
    
def assignment_stmt_prime():
 
    
    if current_token == 'string_constant':
        match('string_constant')
        match(';')
    
    else:
        expression()
        match(';')
        
def selection_stmt_prime():
    if current_token == 'else':
        match('else')
        statement()
    elif current_token == 'ID' or current_token == '{' or current_token == 'if' or current_token == 'while' or   current_token == 'return' or current_token =='input' or current_token == 'output'or current_token == '}' or current_token == 'else':
         return
    else:
        print("Syntax_Analysis_Error")
        exit(1) 
    
def return_stmt_prime():
    if current_token == ';':
        match(';')
    else:
        expression()
        match(';')

def var_prime():
    if current_token == '[':
        match('[')
        arithmetic_expression()
        match(']')
    elif current_token == ';' or current_token == '=' or current_token == '*' or current_token == '/' or current_token == '+' or current_token == '-' or current_token == ']'or current_token == ']' or current_token == '<=' or current_token == '<' or current_token == '>' or current_token == '>=' or current_token == '==' or current_token == '!=' or current_token == ')' or current_token == ',':
        return

def expression():
    arithmetic_expression()
    expression_prime()

def expression_prime():
    
    relop()
    arithmetic_expression()
    
    if current_token == ')' or current_token == ';':
         return
        
    else:
        print("Syntax_Analysis_Error")
        exit(1)    
    
def relop():
    if current_token == '<=':
        match('<=')
    elif current_token == '<':
        match('<')
    elif current_token == '>':
        match('>')
    elif current_token == '>=':
        match('>=')
    elif current_token == '==':
        match('==')
    elif current_token == '!=':
        match('!=')
    
    
def arithmetic_expression():
    term()
    arithmetic_expression_prime()

def arithmetic_expression_prime():
    if current_token == '+':
        match('+')
        term()
        arithmetic_expression_prime()
    elif current_token == '-':
        match('-')
        term()
        arithmetic_expression_prime()
    elif current_token == ']' or current_token == '<=' or current_token == '<' or current_token == '>' or current_token == '>=' or current_token == '==' or current_token == '!=' or current_token == ')' or current_token == ';' or current_token == ',':
        return
    else:
        print("Syntax_Analysis_Error")
        exit(1)   



def term():
    factor()
    term_prime()

def term_prime(): 
    if current_token == '*':
        match('*')
        factor()
        term_prime()
    elif current_token == '/':
        match('/')
        factor()
        term_prime()
    elif  current_token == '+' or current_token == '-' or current_token == ']' or current_token == '<=' or current_token == '<' or current_token == '>' or current_token == '>=' or current_token == '==' or current_token == '!=' or current_token == ')' or current_token == ';' or current_token == ',':
        return
    else:
        print("Syntax_Analysis_Error")
        exit(1)  

def factor():
    if current_token == '(':
        match('(')
        arithmetic_expression()
        match(')')
    elif current_token == 'ID':
        match('ID')
        factor_prime()
    elif current_token == 'float_constant':
        match('float_constant')
    elif current_token == 'integer_constant':
        match('integer_constant')

def factor_prime():
    if current_token == '(' :
        call_prime()
    else:
        var_prime()
    
def call_prime():
    if current_token == ')':
        match(')')
    else:
        arithmetic_expression()
        arg_list_prime()
        match(')')
        
def arg_list_prime():
    if current_token == ',':
        arithmetic_expression()
        arg_list_prime()
    elif current_token == ')':
        return
    else:
        print("Syntax_Analysis_Error")
        exit(1)  
        
         


syntax_analysis()