"""
Advance Quiz Bot — Open Source Project
This project was originally developed by Gagan (github.com/devgaganin).
Reference: https://t.me/advance_quiz_bot
The codebase has been reviewed and verified with the assistance of Claude AI.
"""

from __future__ import annotations

import functools
import logging
from typing import Callable

from pyrogram import Client
from pyrogram.types import Message

from quizbot.shared import config

logger = logging.getLogger(__name__)

UNAUTHORIZED_MESSAGE = (
    "Please Join @cuetchampion for more updates on cuet and quizzes.\n"
    "This is a private bot hence only students of @cuetchampion can access the quizzes in official group."
)


def _is_authorized(user_id: int) -> bool:
    """Check if a user is authorized (owner or admin)."""
    return user_id == config.OWNER_ID or user_id in config.ADMIN_IDS


def require_auth(func: Callable) -> Callable:
    """Decorator to ensure only authorized users (owner/admins) can execute a command.
    
    Sends the unauthorized message to non-authorized users.
    Usage:
        @require_auth
        async def my_command(c: Client, m: Message) -> None:
            ...
    """
    @functools.wraps(func)
    async def wrapper(c: Client, m: Message) -> None:
        user_id = m.from_user.id
        if not _is_authorized(user_id):
            await m.reply(UNAUTHORIZED_MESSAGE)
            logger.debug(f"Unauthorized access attempt by user {user_id} to {func.__name__}")
            return
        await func(c, m)
    return wrapper

