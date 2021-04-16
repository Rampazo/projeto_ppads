#!/usr/bin/python3
# coding: utf-8

import psycopg2


PGHOST = 'localhost'
PGDATABASE = 'db_ppads'
PGUSER = 'postgres'
PGPASSWORD = 'admin'


def create_user_db(data_user):
    conn_string = f'host={PGHOST} port=5432 dbname={PGDATABASE} user={PGUSER} password={PGPASSWORD}'

    conn = psycopg2.connect(conn_string)

    cursor = conn.cursor()

    query = f"""INSERT INTO users
        (name, username, password, birth_date, city, state)
        values ('{data_user.name}', '{data_user.username}', '{data_user.password}', '{data_user.birth_date}',
        '{data_user.city}', '{data_user.state}')"""

    cursor.execute(query)
    # print(cursor.statusmessage)
    conn.commit()

    # d = cursor.fetchall()

    cursor.close()

    return True
