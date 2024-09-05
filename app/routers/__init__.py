# -*- coding: utf-8 -*-
from fastapi import APIRouter
from .root import router as root_router
from .openai import router as openai_router
# 导入其他路由模块...

router = APIRouter()

router.include_router(root_router)
router.include_router(openai_router)
