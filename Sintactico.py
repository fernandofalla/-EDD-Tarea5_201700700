from Lexico import tokens

from ClaseEstudiante import Estudiante
from ClaseTarea import Tarea
from ClaseControl import Control

cnt = Control()



ls = []
lt = []

names = {}

def p_statement_group(t):
    'statement : LQUESTION TELEMENTS RQUESTION elementos LQUESTION DOLAR TELEMENTS RQUESTION'


def p_elementos_group(t):
    """elementos : elementos elemento
                 | elemento
    """

def p_elemento(t):
    'elemento : LQUESTION TELEMENT  tipoElemento RQUESTION items LQUESTION DOLAR TELEMENT RQUESTION'

    # if user.carne != None and user.dpi != None and user.nombre != None and user.carrera != None and user.password != None and user.credito != None and user.edad != None and user.correo != None:
    #     cnt.ListaEstudiantes.append(user)
    
    # cnt.carne = ""
    # user = Estudiante()
    # if cnt.carne != "":
    #     user.carne = cnt.carne
    # cnt.ListaEstudiantes.append(user)

def p_tipoElemento(t):
    """tipoElemento : TTYPE EQUALS NORMSTRING
    """
    if t[3] == '"user"':
        cnt.tipo = "user"
    elif t[3] == '"task"':
        cnt.tipo = "task"

def p_items(t):
    """items : items item
             | item
    """
    # if cnt.tipo == "user":
    #     cnt.user = Estudiante()
    # elif cnt.tipo == "task":
    #     cnt.task = Tarea()
    
    # if cnt.user.carne != None and cnt.user.dpi != None and cnt.user.nombre != None and cnt.user.carrera != None and cnt.user.password != None and cnt.user.credito != None and cnt.user.edad != None and cnt.user.correo != None:
    #     cnt.ListaEstudiantes.append(cnt.user)
    #     cnt.user = None

def p_item(t):
    """item : LQUESTION TITEM tipeItem EQUALS valueItem DOLAR RQUESTION
    """
    user = Estudiante()
    task = Tarea()

    if cnt.tipo == "user":
        if t[3].lower() == "carnet":
            user.carne = t[5]
            cnt.cadenaF += t[5].replace('"',"",2) + ' '
        elif t[3].lower() == "dpi":
            user.dpi = t[5]
            cnt.cadenaF += t[5].replace('"',"",2) + ' '
        elif t[3].lower() == "nombre":
            user.nombre = t[5]
            cnt.cadenaF += t[5].replace('"',"",2) + ' '
        elif t[3].lower() == "carrera":
            user.carrera = t[5]
            cnt.cadenaF += t[5].replace('"',"",2) + ' '
        elif t[3].lower() == "password":
            user.password = t[5]
            cnt.cadenaF += t[5].replace('"',"",2) + ' '
        elif t[3].lower() == "creditos":
            user.credito = t[5]
            cnt.cadenaF += str(t[5]) + ' '
        elif t[3].lower() == "edad":
            user.edad = t[5]
            cnt.cadenaF += str(t[5]) + ' '
        elif t[3].lower() == "correo":
            user.correo = t[5]
            cnt.cadenaF += t[5].replace('"',"",2) + '\n'
    elif cnt.tipo == "task":
        if t[3].lower() == "carnet":
            cnt.cadenaT += t[5].replace('"',"",2) + ' '
        elif t[3].lower() == "nombre":
            cnt.cadenaT += t[5].replace('"',"",2) + ' '
        elif t[3].lower() == "descripcion":
            cnt.cadenaT += t[5].replace('"',"",2) + ' '
        elif t[3].lower() == "materia":
            cnt.cadenaT += t[5].replace('"',"",2) + ' '
        elif t[3].lower() == "fecha":
            cnt.cadenaT += t[5].replace('"',"",2) + ' '
        elif t[3].lower() == "hora":
            cnt.cadenaT += t[5].replace('"',"",2) + ' '
        elif t[3].lower() == "estado":
            cnt.cadenaT += t[5].replace('"',"",2) + '\n'
    
    # cnt.ListaEstudiantes.append(user)
    # if user.carne != None and user.dpi != None and user.nombre != None and user.carrera != None and user.password != None and user.credito != None and user.edad != None and user.correo != None:
    

def p_valueItem(t):
    """valueItem : NORMSTRING
                 | NUMBER
                 """
    t[0] = t[1]

def p_tipeItem(t):
    """tipeItem : TCARNET
                | TDPI
                | TNOMBRE
                | TCARRERA
                | TPASSWORD
                | TCREDITOS
                | TEDAD
                | TCORREO
                | TDESCRIPCION
                | TMATERIA
                | TFECHA
                | THORA
                | TESTADO
                """

    t[0] = t[1]

def p_error(t):
    print("Syntax error at '%s'" % t.value)

import ply.yacc as yacc
parser = yacc.yacc()