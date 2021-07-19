# Calls Music 1 - Telegram bot for streaming audio in group calls
# Copyright (C) 2021  Roj Serbest

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.


from asyncio import QueueEmpty
from pyrogram import Client 
from pyrogram import filters
from pyrogram.types import Message

from DaisyXMusic.config import que
from DaisyXMusic.function.admins import set
from DaisyXMusic.helpers.channelmusic import get_chat_id
from DaisyXMusic.helpers.decorators import authorized_users_only
from DaisyXMusic.helpers.decorators import errors
from DaisyXMusic.helpers.filters import command
from DaisyXMusic.helpers.filters import other_filters
from DaisyXMusic.services.callsmusic import callsmusic
from DaisyXMusic.services.queues import queues


@Client.on_message(filters.command("adminreset"))
async def update_admin(client, message: Message):
    chat_id = get_chat_id(message.chat)
    set(
        chat_id,
        [
            member.user
            for member in await message.chat.get_members(filter="administrators")
        ],
    )
    await message.reply_text("❇️ Yönetici önbelleği yenilendi!")


@Client.on_message(command("durdur") & other_filters)
@errors
@authorized_users_only
async def durdur(_, message: Message):
    chat_id = get_chat_id(message.chat)
    if (chat_id not in callsmusic.active_chats) or (
        callsmusic.active_chats[chat_id] == "durduruldu"
    ):
        await message.reply_text("❗ Durdurulcak Bi Müzik Gözükmüyor!")
    else:
        callsmusic.durdur(chat_id)
        await message.reply_text("▶️ duraklatıldı!")


@Client.on_message(command("devam") & other_filters)
@errors
@authorized_users_only
async def devam(_, message: Message):
    chat_id = get_chat_id(message.chat)
    if (chat_id not in callsmusic.active_chats) or (
        callsmusic.active_chats[chat_id] == "devamediyor"
    ):
        await message.reply_text("❗ Duraktılan Müzik Devam Ediyor!")
    else:
        callsmusic.devam(chat_id)
        await message.reply_text("⏸Devam ediyor!")


@Client.on_message(command("bitir") & other_filters)
@errors
@authorized_users_only
async def durdur(_, message: Message):
    chat_id = get_chat_id(message.chat)
    if chat_id not in callsmusic.active_chats:
        await message.reply_text("❗ Durdurulacak Müzik Yok!")
    else:
        try:
            queues.clear(chat_id)
        except QueueEmpty:
            pass

        await callsmusic.durdur(chat_id)
        await message.reply_text("❌ Müzik durduruldu!")


@Client.on_message(command("atla") & other_filters)
@errors
@authorized_users_only
async def atla(_, message: Message):
    global que
    chat_id = get_chat_id(message.chat)
    if chat_id not in callsmusic.active_chats:
        await message.reply_text("❗ Atlamak İçin Hiçbir Şey Oynamıyor!")
    else:
        queues.task_done(chat_id)
        if queues.is_empty(chat_id):
            await callsmusic.durdur(chat_id)
        else:
            await callsmusic.set_stream(
                chat_id, 
                queues.get(chat_id)["file"]
            )

    qeue = que.get(chat_id)
    if qeue:
        atla = qeue.pop(0)
    if not qeue:
        return
    await message.reply_text(f"- Atlandı **{atla[0]}**\n- Simdi Oynatılıyor **{qeue[0][0]}**")


@Client.on_message(filters.command("admincache"))
@errors
async def admincache(client, message: Message):
    set(
        message.chat.id,
        [
            member.user
            for member in await message.chat.get_members(filter="administrators")
        ],
    )
    await message.reply_text("❇️ Yönetici önbelleği yenilendi!")
