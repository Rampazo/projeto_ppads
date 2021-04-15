#!/usr/bin/python3
# coding: utf-8

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from modules.Feed.controller.controller import router_feed
from modules.Login.controller.controller import router_login
from modules.User.controller.controller import router_user

origins = [
    "http://localhost",
]

app = FastAPI(
    title='API Recomenda',
    version='1.0.0'
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/src", StaticFiles(directory="./static/src"), name="source")

app.include_router(router_feed, prefix="/feed")
app.include_router(router_login, prefix="/login")
app.include_router(router_user, prefix="/user")
