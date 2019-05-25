import random

def config(app):
    app.config['MYSQL_DATABASE_USER'] = 'root'
    app.config['MYSQL_DATABASE_PASSWORD'] = 'root'
    app.config['MYSQL_DATABASE_DB'] = 'url'


def get_db(mysql):
    conn = mysql.connect()
    cursor = conn.cursor()

    return conn, cursor

def cadastrar(cursor, conn, url):
    numero = random.randint(10000, 99999)
    cursor.execute(f'INSERT INTO baseurl (baseurls, codigos, newurl) values ("{url}", "{numero}", "http://127.0.0.1:5000/")')
    conn.commit()

def url_curt(cursor, teste):
    cursor.execute(f'SELECT baseurls, codigos, newurl from baseurl where baseurls="{teste}"')
    consulta = cursor.fetchall()
    cursor.close()
    return consulta


def getRegistros(cursor):

    cursor.execute(f'SELECT baseurls, codigos, newurl from baseurl')
    consultar = cursor.fetchall()
    cursor.close()
    return consultar

