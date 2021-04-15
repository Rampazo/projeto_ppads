#!/usr/bin/python3
# coding: utf-8

from fastapi import APIRouter, HTTPException, Request, status
from fastapi.templating import Jinja2Templates

from modules.User.domain.model import User
from modules.User.service.service import registration_user

router_user = APIRouter()
templates = Jinja2Templates(directory="./modules/User/template")


@router_user.post("/create", status_code=201, description='Create User')
async def create_user(user: User):

    try:
        query = await registration_user(user)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e)
        )
    return query


@router_user.get("/registration", description='Create User Page')
async def login_page(request: Request):
    return templates.TemplateResponse(
        "create_user.html",
        {'request': request}
    )
