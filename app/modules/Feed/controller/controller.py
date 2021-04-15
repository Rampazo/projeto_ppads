#!/usr/bin/python3
# coding: utf-8

from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates

router_feed = APIRouter()
templates = Jinja2Templates(directory="./modules/Feed/template")


@router_feed.get("", description='Feed Page')
async def feed_page(request: Request):
    return templates.TemplateResponse(
        "feed.html",
        {'request': request}
    )
