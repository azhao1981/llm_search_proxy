# -*- coding: utf-8 -*-
from fastapi import FastAPI
from dotenv import load_dotenv, find_dotenv
from app.web import uvicorn
from app.log import log
from app.routers import router
load_dotenv(find_dotenv(), override=True)
logger = log.set_log()

app = FastAPI()
# 将路由包含到主应用中
app.include_router(router)

if __name__ == "__main__":
    uvicorn.run_server()
