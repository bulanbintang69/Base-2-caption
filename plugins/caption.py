import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

import asyncio
import datetime
from pyrogram import filters
from bot import autocaption
from config import Config
from database.database import *
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.errors import FloodWait


@autocaption.on_message(~filters.edited, group=-1)
async def editing(bot, message):
    if (message.chat.type == "private"):
        if ("/set_cap" in message.text) and ((len(message.text.split(' ')) == 2) or (len(message.text.split(' ')) == 1)):
            await message.reply_text("♦️ 𝙲𝚘𝚗𝚏𝚒𝚐𝚞𝚛𝚊çã𝚘 𝚍𝚎 𝙻𝚎𝚐𝚎𝚗𝚍𝚊 \n\nUse o comando para definir legenda personalizada para qualquer um de seus canais.\n\n👉 `/set_cap -100(o id do seu canal) exemplo: -1001234567890 com a legenda que você quer definir... EXEMPLO: /set_cap -100273783838 Boa noite vossos admin`", quote = True)
        elif ("/set_cap" in message.text) and (len(message.text.split(' ')) != 2) and (len(message.text.split(' ')) != 1):
            caption = message.text.markdown.split(' ', 2)[2]
            channel = message.text.split(' ', 2)[1].replace("-100", "")
            try:
                a = await get_caption(channel)
                b = a.caption
            except:
                await update_caption(channel, caption)
                return await message.reply_text(f"**--Sua legenda--:**\n\n{caption}", quote=True)
            await message.reply_text("⚠️\n\nUma legenda já definida para este canal, você deve primeiro usar /rmv_cap + o id do canal para remover a legenda atual e, em seguida, tentar definir novo.", quote=True)
           
        if ("/set_btn" in message.text) and ((len(message.text.split(' ')) == 2) or (len(message.text.split(' ')) == 1)):
            await message.reply_text("😴 C͟o͟n͟f͟i͟g͟u͟r͟a͟ção͟ d͟e͟ B͟o͟t͟õe͟s \n\nUse o comando para definir o botão para qualquer um de seus canais.\nEnvie um nome de botão e URL(separados por ' | ').\n\n👉 `/set_btn -1001448973320 Nome do canal | https://t.me/canal`", quote = True)
        elif ("/set_btn" in message.text) and (len(message.text.split(' ')) != 2) and (len(message.text.split(' ')) != 1):
            button = message.text.split(' ', 2)[2]
            channel = message.text.split(' ', 2)[1].replace("-100", "").replace("1", "")
            try:
                a = await get_button(channel)
                b = a.button
            except:
                await update_button(channel, button)
                return await message.reply_text(f"**--Seu botão como ficou--:**\n\n{button}", quote=True, reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(button.split(' | ')[0], url=f"{button.rsplit(' ', 1)[1]}")]]))
            await message.reply_text("⚠️\n\nUm botão já configurado para este canal, você deve primeiro usar /rmv_btn e o id do canal para remover o botão atual e, em seguida, tentar definir novo.", quote=True)
           
        if (message.text == "/rmv_cap"):
            await message.reply_text("Use este comando para remover a legenda atual de qualquer um de seus canais.\n\n👉 `/rmv_cap -1001448973320`", quote = True)
        elif ("/rmv_cap" in message.text) and (len(message.text.split(' ')) != 1):
            channel = message.text.split(' ', 1)[1].replace("-100", "")
            try:
                a = await get_caption(channel)
                b = a.caption
            except:
                return await message.reply_text("Legenda ainda não definida!", quote=True)     
            await del_caption(channel)
            await message.reply_text("♦️✔️ A legenda removida com sucesso.", quote=True)

        if (message.text == "/rmv_btn"):
            await message.reply_text("Use este comando para remover o botão atual de qualquer um de seus canais.\n\n👉 `/rmv_btn -1001524177283`", quote = True)
        elif ("/rmv_btn" in message.text) and (len(message.text.split(' ')) != 1):
            channel = message.text.split(' ', 1)[1].replace("-100", "").replace("1", "")
            try:
                a = await get_button(channel)
                b = a.button
            except:
                return await message.reply_text("Botão ainda não definido!", quote=True)     
            await del_button(channel)
            await message.reply_text("♦️✔️ O botão removido com sucesso.", quote=True)

    if (message.chat.type == "channel") and (message.video or message.document or message.audio):
        m = message.video or message.document or message.audio
        try:
            channel = str(message.chat.id).replace('-100', '').replace('1', '')
            btn = await get_button(int(channel))
            button = btn.button
        except:
            button = None
            pass
        try:
            channel = str(message.chat.id).replace('-100', '')
            cap = await get_caption(int(channel))
            if message.audio:
                caption = cap.caption.replace("{duration}", str(datetime.timedelta(seconds = m.duration))).replace("{mime_type}", m.mime_type).replace("{filename}", m.file_name).replace("{artist}", m.performer).replace("{title}", m.title).replace("{ext}", "." + m.file_name.rsplit('.', 1)[1])
            elif message.video:
                caption = cap.caption.replace("{duration}", str(datetime.timedelta(seconds = m.duration))).replace("{mime_type}", m.mime_type).replace("{filename}", m.file_name).replace("{width}", str(m.width)).replace("{height}", str(m.height)).replace("{ext}", "." + m.file_name.rsplit('.', 1)[1])
            elif message.document:
                caption = cap.caption.replace("{mime_type}", m.mime_type).replace("{filename}", m.file_name).replace("{ext}", "." + m.file_name.rsplit('.', 1)[1])
        except:
            caption = None
            pass
       
        if button is not None:
            Url = button.rsplit(' ', 1)[1]
            Name = button.split(' | ')[0]
            if caption is not None:
                try:
                    await bot.edit_message_caption(chat_id = message.chat.id, message_id = message.message_id, caption = caption, parse_mode = "markdown", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(Name, url=f"{Url}")]]))
                except Exception as e:
                    print(e)
            elif caption is None:
                try:
                    await bot.edit_message_caption(chat_id = message.chat.id, message_id = message.message_id, reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(Name, url=f"{Url}")]]))
                except Exception as e:
                    print(e)
        elif (button is None) and (caption is not None):
            try:
                await bot.edit_message_caption(chat_id = message.chat.id, message_id = message.message_id, caption = caption, parse_mode = "markdown")
            except Exception as e:
                print(e)
