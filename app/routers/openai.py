# -*- coding: utf-8 -*-
from fastapi import HTTPException
from fastapi import APIRouter
from fastapi.responses import StreamingResponse
from app.services.openai.chat.completions import ChatCompletionsRequest, create_chat_completion

router = APIRouter()


@router.post("/openai/v1/chat/completions")
async def completions(request: ChatCompletionsRequest):
    try:
        async def generate():
            async for response in create_chat_completion(request):
                yield f"{response.text}\n"
        
        return StreamingResponse(generate(), media_type="text/plain")

    except ValueError as e:
        raise HTTPException(status_code=500, detail=str(e))
