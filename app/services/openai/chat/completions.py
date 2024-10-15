# -*- coding: utf-8 -*-
from typing import AsyncGenerator, List, Optional
import httpx
import os
import asyncio
from pydantic import BaseModel
from app.log import log
from langchain_community.tools import BingSearchRun
from langchain_community.utilities import BingSearchAPIWrapper

logger = log.set_log()


class Message(BaseModel):
    role: str
    content: str
    name: Optional[str] = None


class ChatCompletionsRequest(BaseModel):
    model: str
    messages: List[Message]
    temperature: Optional[float] = 1.0
    top_p: Optional[float] = 1.0
    n: Optional[int] = 1
    stream: Optional[bool] = False
    max_tokens: Optional[int] = None
    presence_penalty: Optional[float] = 0
    frequency_penalty: Optional[float] = 0


class Choice(BaseModel):
    index: int
    message: Message
    finish_reason: Optional[str]


class Usage(BaseModel):
    prompt_tokens: int
    completion_tokens: int
    total_tokens: int


class ChatCompletionsResponse(BaseModel):
    id: str
    object: str
    created: int
    model: str
    choices: List[Choice]
    usage: Usage


class ChatCompletionsService:
    def __init__(self, request: ChatCompletionsRequest):
        self.request = request
        self.bing_search = BingSearchRun(api_wrapper=BingSearchAPIWrapper())
        self.search_result = None

    async def get_completion(self) -> AsyncGenerator[str, None]:
        try:
            if search_result := await self.search():
                self.search_result = search_result
                yield search_result

            if self.request.stream:
                async for response in self.stream_request():
                    yield response
            else:
                yield await self.normal_request()

        except httpx.HTTPError as e:
            raise ValueError(f"Failed to get completion: {str(e)}")

    async def stream_request(self):
        if self.search_result:
            self.request.messages.append(Message(
                role="assistant",
                content=self.search_result
            ))
        openai_response = await self.call_openai_api(self.request)
        return openai_response

    async def normal_request(self):
        if self.search_result:
            self.request.messages.append(Message(
                role="assistant",
                content=self.search_result
            ))
        openai_response = await self.call_openai_api(self.request)
        return openai_response

    async def call_openai_api(self, request: ChatCompletionsRequest):
        async with httpx.AsyncClient() as client:
            response = await client.post(
                "https://api.gezhishirt.club/v1/chat/completions",
                headers={"Authorization": f"Bearer {os.getenv('OPENAI_API_KEY')}"},
                json=request.model_dump()
            )
            return response.json()

    async def search(self):
        if self.request.messages and self.request.messages[-1].content.startswith("@search"):
            query = self.request.messages[-1].content[7:].strip()  # 移除"@search"前缀
            search_result = await asyncio.to_thread(self.bing_search.run, query)
            return ChatCompletionsResponse(
                id="search-result",
                object="chat.completion",
                created=int(asyncio.get_event_loop().time()),
                model=self.request.model,
                choices=[
                    Choice(
                        index=0,
                        message=Message(
                            role="assistant",
                            content=f"搜索结果：\n\n{search_result}"
                        ),
                        finish_reason="stop"
                    )
                ],
                usage=Usage(
                    prompt_tokens=len(query),
                    completion_tokens=len(search_result),
                    total_tokens=len(query) + len(search_result)
                )
            ).model_dump_json()
        return None


async def create_chat_completion(
    request: ChatCompletionsRequest
) -> AsyncGenerator[str, None]:
    service = ChatCompletionsService(request)
    async for response in service.get_completion():
        yield response
