#!/usr/bin/python3
# coding: utf-8

from repository.db import query_user


async def validate_login(data_login):
    query = query_user(data_login)
    if not query:
        raise ModuleNotFoundError
    return query


async def create_session(data_token):
    a = 1
    # try:
    #     token_id = query_token(data_token)
    #     if token_id:
    #         update_token(token_id.ID_TOKEN, data_token.date)
    #     else:
    #         create_token(data_token)
    # except Exception as err:
    #     raise err