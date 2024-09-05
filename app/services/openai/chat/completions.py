# -*- coding: utf-8 -*-
from typing import AsyncGenerator
import asyncio
import httpx
from pydantic import BaseModel, Field
from app.log import log

logger = log.set_log()

class ChatCompletionsRequest(BaseModel):
    name: str = Field(..., description="Name for the chat completion")

class ChatCompletionsResponse(BaseModel):
    text: str = Field(..., description="Response text from the chat completion")

class ChatCompletionsService:
    def __init__(self, request: ChatCompletionsRequest):
        self.request = request

    async def get_completion(self) -> AsyncGenerator[ChatCompletionsResponse, None]:
        try:
            for i in range(1, 11):
                response = f"Number {i}"
                logger.info(f"Response: {response}")
                yield ChatCompletionsResponse(
                    text=f"{response} {self.request.name}"
                )
                await asyncio.sleep(1)  # 等待1秒
        except httpx.HTTPError as e:
            # 这里可以根据需要进行更详细的错误处理
            raise ValueError(f"Failed to get completion: {str(e)}")


async def create_chat_completion(request: ChatCompletionsRequest) -> AsyncGenerator[ChatCompletionsResponse, None]:
    service = ChatCompletionsService(request)
    async for response in service.get_completion():
        yield response
