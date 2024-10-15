# -*- coding: utf-8 -*-
from .chat.completions import create_chat_completion, ChatCompletionsRequest

__all__ = [
    "ChatCompletionsRequest",
    "create_chat_completion",
]
