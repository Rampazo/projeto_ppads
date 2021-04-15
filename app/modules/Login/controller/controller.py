#!/usr/bin/python3
# coding: utf-8

from fastapi import APIRouter, HTTPException, Request, status
from fastapi.templating import Jinja2Templates

from modules.Login.domain.model import Authentication
from modules.Login.service.service import validate_login

router_login = APIRouter()
templates = Jinja2Templates(directory="./modules/Login/template")


@router_login.post("/auth", status_code=201, description='Get Authentication')
async def make_login(auth: Authentication):

    try:
        query = await validate_login(auth)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e)
        )
    return query


@router_login.get("", description='Login Page')
async def login_page(request: Request):
    return templates.TemplateResponse(
        "login.html",
        {'request': request}
    )
