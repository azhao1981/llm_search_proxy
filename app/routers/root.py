# -*- coding: utf-8 -*-

from fastapi import APIRouter, Query
from app.services import hello

router = APIRouter()

@router.get("/")
def read_root(name: str = Query(...)):
    request = hello.dao.HelloRequest(name=name)
    return hello.do.get_ip(request)