#!/usr/bin/python3
# coding: utf-8

from modules.User.repository.db import create_user_db


async def registration_user(data_user):
    create_user_db(data_user)
