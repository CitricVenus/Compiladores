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
    '"': '25',
    '.': '26',
    "(": "27",
    ")": "28",
    "[": "29",
    "]": "30",
    "{": "31",
    "}": "32",
    "identifier": "33",
    "string_value": "34",
    "float_number": "35",
    "int_number": "36"
}
letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
          'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numeros = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
delimitadores = ['+', '-', '*', '/', '>', '<', '!', '=', ';',
                 ',', '"', '.', '(', ')', '[', ']', '{', '}', ' ', '\n', '\t']

tabla_de_transicion = [
    [2, 3, 20, 21, 22, 6, 9, 10, 12, 11, 23, 24,
        1, 31, 25, 26, 27, 28, 29, 30, 0, 41, 13],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
     14, 1, 1, 1, 1, 1, 1, 1, 1, 1, 40],
    [2, 2, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15,
     15, 15, 15, 15, 15, 15, 15, 15, 15, 41, 40],
    [17, 3, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17,
     17, 4, 17, 17, 17, 17, 17, 17, 17, 41, 40],
    [42, 5, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42,
     42, 42, 42, 42, 42, 42, 42, 42, 42, 41, 40],
    [16, 5, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16,
     16, 16, 16, 16, 16, 16, 16, 16, 16, 41, 40],
    [18, 18, 18, 18, 7, 18, 18, 18, 18, 18, 18, 18,
     18, 18, 18, 18, 18, 18, 18, 18, 18, 41, 40],
    [7, 7, 7, 7, 8, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 40],
    [7, 7, 7, 7, 7, 19, 7, 7, 7, 7, 7, 7,
     7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 40],
    [33, 33, 33, 33, 33, 33, 33, 33, 33, 34, 33, 33,
     33, 33, 33, 33, 33, 33, 33, 33, 33, 41, 40],
    [35, 35, 35, 35, 35, 35, 35, 35, 35, 36, 35, 35,
     35, 35, 35, 35, 35, 35, 35, 35, 35, 41, 40],
    [37, 37, 37, 37, 37, 37, 37, 37, 37, 38, 37, 37,
     37, 37, 37, 37, 37, 37, 37, 37, 37, 41, 40],
    [43, 43, 43, 43, 43, 43, 43, 43, 43, 39, 43, 43,
     43, 43, 43, 43, 43, 43, 43, 43, 43, 41, 40]
]
estados_aceptados = [13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23,
                     24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39]
estados_de_error = [40, 41, 42, 43]

tabla_identifieres = {}
tabla_strings = {}
tabla_integers = {}
tabla_floats = {}
reconocimiento_de_tokens = []
escaner_output = []


def analizador():
    file = open("code.txt", 'r')
    estado_actual = 0
    string_aux = ""
    cont_string = 1
    cont_int_num = 1
    cont_float_num = 1
    cont_identifier = 1
    numero_aux = 0
    nuevo_estado = 0
    while 1:
        char = file.read(1)
        if (char != ' ' and char != '\t' and char != '\n'):
            estado_actual = 0
            string_aux = ""
            if not char:
                break
            while (not estado_actual in estados_aceptados and not estado_actual in estados_de_error):
                nuevo_estado = nuevoEstado(estado_actual, char)
                if (avanza(estado_actual, char)):
                    if (char == ''):
                        nuevo_estado = 40
                    else:
                        string_aux = string_aux + char
                        char = file.read(1)
                estado_actual = nuevo_estado
            if (estado_actual in estados_aceptados):
                if (estado_actual == 36):
                    numero_aux = tokens.get(">=")
                    escaner_output.append(numero_aux)
                    reconocimiento_de_tokens.append(">=")
                    continue
                if (estado_actual == 34):
                    numero_aux = tokens.get("<=")
                    escaner_output.append(numero_aux)
                    reconocimiento_de_tokens.append("<=")
                    continue
                if (estado_actual == 38):
                    numero_aux = tokens.get("==")
                    escaner_output.append(numero_aux)
                    reconocimiento_de_tokens.append("==")
                    continue
                if (estado_actual == 39):
                    numero_aux = tokens.get("!=")
                    escaner_output.append(numero_aux)
                    reconocimiento_de_tokens.append("!=")
                    continue
                if (string_aux in tokens):
                    numero_aux = tokens.get(string_aux)
                    escaner_output.append(numero_aux)
                    reconocimiento_de_tokens.append(string_aux)
                else:
                    if (estado_actual == 13):
                        return print("Fin de archivo")
                    if (estado_actual == 14):
                        if (not string_aux in tabla_strings):
                            if (char in tokens):
                                numero_aux = tokens.get(char)
                                escaner_output.append(numero_aux)
                                reconocimiento_de_tokens.append(char)
                            tabla_strings[string_aux.replace(
                                '"', '')] = cont_string
                            reconocimiento_de_tokens.append(
                                string_aux.replace('"', ''))
                            numero_aux = tokens.get("string_value")
                            out_aux = str(numero_aux) + ','+str(cont_string)
                            escaner_output.append(out_aux)
                            cont_string += 1
                        else:
                            reconocimiento_de_tokens.append(string_aux)
                            int_num = tabla_strings.get(string_aux)
                            numero_aux = tokens.get("string_value")
                            out_aux = str(numero_aux) + "," + str(int_num)
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
                    if (estado_actual == 19):
                        continue

            if (estado_actual in estados_de_error):
                if estado_actual == 40:
                    print("EOF error")
                    break
                if estado_actual == 41:
                    print(
                        "Error, caracter no aceptado o hace falta delimitador despues de " + '"' + string_aux+'"')
                    break
                if estado_actual == 42:
                    print("Error al crear valor flotante" +
                          string_aux + "No es un numero")
                    break
                if estado_actual == 43:
                    print("Error al crear el token" + ' "!=" ,' +
                          '"'+char + '"' + " es diferente a " + '"="')
                    break
            if (char in tokens):
                numero_aux = tokens.get(char)
                escaner_output.append(numero_aux)
                reconocimiento_de_tokens.append(char)

    file.close()
# Revisa si el siguiente estado es un estado de error, estado final o si sigue leyendo mas caracteres


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


# regresa el estado dependiendo el caracter leido y el estado en el que estaba
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


analizador()
print(reconocimiento_de_tokens)
print("----------------------\n")
print(escaner_output)
print("----------------------\n")
print(tabla_identifieres)
print("----------------------\n")
print(tabla_floats)
print("----------------------\n")
print(tabla_integers)
print("----------------------\n")
print(tabla_strings)
