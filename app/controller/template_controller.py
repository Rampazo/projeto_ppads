#!/usr/bin/python3
# coding: utf-8

from fastapi import APIRouter, Request, HTTPException, status
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.templating import Jinja2Templates

router_template = APIRouter()

templates = Jinja2Templates(directory="./templates")


@router_template.get("/login")
async def manager(request: Request):
    return templates.TemplateResponse(
        "login.html",
        {'request': request}
    )


@router_template.get("/login/success")
async def get_login_success(request: Request):
    return templates.TemplateResponse(
        "login_success.html",
        {'request': request}
    )
    # return FileResponse('app/templates/login_success.html')
