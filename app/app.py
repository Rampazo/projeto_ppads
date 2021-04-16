#!/usr/bin/python3
# coding: utf-8

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from modules.Feed.controller.controller import router_feed
from modules.Login.controller.controller import router_login
from modules.User.controller.controller import router_user

app = FastAPI(
    title='API Recomenda',
    version='1.0.0'
)

app.mount("/src", StaticFiles(directory="./static/src"), name="source")

app.include_router(router_feed, prefix="/feed")
app.include_router(router_login, prefix="/login")
app.include_router(router_user, prefix="/user")
