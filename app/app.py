from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from controller.controller import router
from controller.template_controller import router_template

app = FastAPI(title='API Recomenda',
              version='1.0.0',)

app.mount("/src", StaticFiles(directory="./templates/src"), name="source")

app.include_router(
    router, prefix=""
)

app.include_router(
    router_template, prefix=""
)
