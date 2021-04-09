#!/usr/bin/python3
# coding: utf-8

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.responses import JSONResponse, Response
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

from service.service import validate_login, create_session
from domain.model import Authentication
from domain.schema import DefaultResponse

router = APIRouter()


@router.post("/auth", status_code=201, description='Get Authentication')
async def make_login(auth: Authentication):

    try:
        query = await validate_login(auth)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e)
        )
    return query
