#!/usr/bin/python3
# coding: utf-8

import psycopg2


PGHOST = 'localhost'
PGDATABASE = 'db_ppads'
PGUSER = 'postgres'
PGPASSWORD = 'admin'


def query_user(data_login):
    conn_string = f'host={PGHOST} port=5432 dbname={PGDATABASE} user={PGUSER} password={PGPASSWORD}'

    conn = psycopg2.connect(conn_string)

    cursor = conn.cursor()

    query = f"""SELECT * FROM users WHERE username = '{data_login.username}' AND password = '{data_login.password}'"""

    cursor.execute(query)
    # print(cursor.statusmessage)
    # conn.commit()

    d = cursor.fetchone()

    cursor.close()

    return d
