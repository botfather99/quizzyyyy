"""
Advance Quiz Bot — Open Source Project
This project was originally developed by Gagan (github.com/devgaganin).
Reference: https://t.me/advance_quiz_bot
The codebase has been reviewed and verified with the assistance of Claude AI.

Authorization middleware to protect all bot commands.
Only authorized users, admins, and the owner can access commands.
"""

from __future__ import annotations

import logging
from typing import Optional

from telegram import Update
from telegram.constants import ChatType, ParseMode
from telegram.ext import ContextTypes

from quizbot.shared import config

logger = logging.getLogger(__name__)

# Unauthorized message for private users
UNAUTHORIZED_MESSAGE = (
    "Please Join @cuetchampion for more updates on cuet and quizzes. "
    "This is a private bot hence only students of @cuetchampion can access the quizzes in official group."
)


async def is_authorized(update: Update, ctx: ContextTypes.DEFAULT_TYPE) -> bool:
    """
    Check if the user is authorized to execute a command.
    
    Authorization hierarchy:
    1. Owner (OWNER_ID from config)
    2. Admins (ADMIN_IDS from config)
    3. In groups: Group admins/creators
    4. In private chats: Authorized users only (future expansion with database)
    
    Args:
        update: The Telegram update object
        ctx: The bot context
        
    Returns:
        True if authorized, False otherwise (and sends denial message)
    """
    try:
        # Determine user and chat info
        user_id = None
        chat_id = None
        chat_type = None
        message = update.message or update.callback_query.message if update.callback_query else None
        
        if not message:
            return False
        
        user_id = message.from_user.id if message.from_user else None
        chat_id = message.chat.id
        chat_type = message.chat.type
        
        if not user_id:
            await _send_unauthorized_message(ctx, chat_id)
            return False
        
        # Owner has full access
        if config.OWNER_ID and user_id == config.OWNER_ID:
            return True
        
        # Admins have full access
        if user_id in config.ADMIN_IDS:
            return True
        
        # In groups: only admins and creators can use commands
        if chat_type in (ChatType.GROUP, ChatType.SUPERGROUP):
            if await _is_group_admin(ctx, chat_id, user_id):
                return True
            else:
                await _send_unauthorized_message(ctx, chat_id)
                return False
        
        # In private chats: only owner and admins
        if chat_type == ChatType.PRIVATE:
            await _send_unauthorized_message(ctx, chat_id)
            return False
        
        # Default: deny access
        await _send_unauthorized_message(ctx, chat_id)
        return False
        
    except Exception as e:
        logger.error("Authorization check error: %s", e, exc_info=True)
        return False


async def require_admin_or_authorized(update: Update, ctx: ContextTypes.DEFAULT_TYPE) -> bool:
    """
    Stricter authorization check - requires admin status or authorization.
    Used for sensitive operations.
    
    Args:
        update: The Telegram update object
        ctx: The bot context
        
    Returns:
        True if authorized as admin/owner, False otherwise
    """
    try:
        user_id = update.message.from_user.id if update.message and update.message.from_user else None
        chat_id = update.message.chat.id if update.message else None
        
        if not user_id or not chat_id:
            return False
        
        # Owner has full access
        if config.OWNER_ID and user_id == config.OWNER_ID:
            return True
        
        # Admins have full access
        if user_id in config.ADMIN_IDS:
            return True
        
        # Group admins
        if await _is_group_admin(ctx, chat_id, user_id):
            return True
        
        await _send_unauthorized_message(ctx, chat_id)
        return False
        
    except Exception as e:
        logger.error("Admin authorization check error: %s", e, exc_info=True)
        return False


async def _is_group_admin(ctx: ContextTypes.DEFAULT_TYPE, chat_id: int, user_id: int) -> bool:
    """
    Check if user is an admin or creator in the group.
    
    Args:
        ctx: The bot context
        chat_id: The group chat ID
        user_id: The user ID to check
        
    Returns:
        True if user is admin or creator, False otherwise
    """
    try:
        member = await ctx.bot.get_chat_member(chat_id, user_id)
        return member.status in ("administrator", "creator")
    except Exception as e:
        logger.debug("Could not determine admin status for user %s in chat %s: %s", user_id, chat_id, e)
        return False


async def _send_unauthorized_message(ctx: ContextTypes.DEFAULT_TYPE, chat_id: int) -> None:
    """
    Send the unauthorized access message to the user.
    
    Args:
        ctx: The bot context
        chat_id: The chat ID to send message to
    """
    try:
        await ctx.bot.send_message(
            chat_id=chat_id,
            text=UNAUTHORIZED_MESSAGE,
            parse_mode=ParseMode.HTML,
        )
    except Exception as e:
        logger.error("Failed to send unauthorized message to chat %s: %s", chat_id, e)


def is_owner(user_id: int) -> bool:
    """Quick synchronous check if user is the owner."""
    return config.OWNER_ID is not None and user_id == config.OWNER_ID


def is_admin(user_id: int) -> bool:
    """Quick synchronous check if user is in admin list."""
    return user_id in config.ADMIN_IDS


def is_owner_or_admin(user_id: int) -> bool:
    """Quick synchronous check if user is owner or admin."""
    return is_owner(user_id) or is_admin(user_id)
