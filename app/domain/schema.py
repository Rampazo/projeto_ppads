#!/usr/bin/python3
# coding: utf-8

from pydantic import BaseModel, Field


class DefaultResponse(BaseModel):
    message: str = Field(alias="message", title="Mensagem", description="Mensagem de erro ou descrição do retorno",
                         example="Internal Server Error!")
