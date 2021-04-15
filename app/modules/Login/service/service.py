#!/usr/bin/python3
# coding: utf-8

from modules.Login.repository.db import query_user


async def validate_login(data_login):
    query = query_user(data_login)
    if not query:
        raise ModuleNotFoundError
    return query
