#!/usr/bin/python3
# coding: utf-8

from pydantic import BaseModel, Field


class Authentication(BaseModel):

    username: str = Field(title='Username')
    password: str = Field(title='Password')
