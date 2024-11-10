import libClass
def consult(a,b,c):
    try:
        libClass.CRUD.read(f"SELECT {a} FROM {b} WHERE {a} = '{c}' ")
        x= libClass.CRUD.curl.fetchone()[0]
    except:
        return True
def colector(client, room, calendar, periodo):
    try:
        libClass.CRUD.read(f"SELECT date FROM scheduling WHERE (date = '{calendar}') AND (period = '{periodo}') ")
        consultarData= libClass.CRUD.curl.fetchone()[0]
        return True

    except:
        libClass.CRUD.create((f"INSERT INTO scheduling(id_client, id_room, date, period) VALUES('{client}', '{room}', '{calendar}', '{periodo}')"))
def validar(psw, user):
    try:
        libClass.CRUD.read(f"SELECT * FROM user WHERE (username = '{user}') and (password = '{psw}')")
        x= libClass.CRUD.curl.fetchone()[0]
    except:
        return True
def armazenar(sql):
    libClass.CRUD.create(sql)
def sql(client, room, period):


    matriz= []
    cont = False
    sql = "SELECT * FROM scheduling WHERE ("
    if client != "":
        sql += f"id_client = '{client}' "
        cont = True
    if room != "":
        cont = True
        if cont:
            sql += f" AND id_room = '{room}' "
        else:
            ql += f"id_room = '{room}' "
    if period != "":
        if cont:
            sql += f" AND period = '{period}'"
        else:
            sql += f"period = '{period}'"
    sql += ")"
    libClass.CRUD.read(sql)
    matriz = libClass.CRUD.curl.fetchall()
    return matriz

def readAll(sql):
    matriz= []
    libClass.CRUD.read(sql)
    matriz= libClass.CRUD.curl.fetchall()
    return matriz
