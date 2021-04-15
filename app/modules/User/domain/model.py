#!/usr/bin/python3
# coding: utf-8

import datetime

from pydantic import BaseModel, Field


class User(BaseModel):

    name: str = Field(title='Name')
    username: str = Field(title='Username')
    password: str = Field(title='Password')
    birth_date: str = Field(title='Birth Date')
    city: str = Field(title='City')
    state: str = Field(title='State')
