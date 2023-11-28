import sys, os
sys.path.insert(1, '././')


import logging
import json

from aiogram import Bot, Dispatcher, executor, types
import insta


with open('_configs.json', 'r') as file:

    '''
    crie um arquivo "_configs.json"
    {
        "token": "BOT DO SEU TOKEN AQUI"
    }
    '''

    API_TOKEN = json.loads(file.read())['token']


# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    logging.info(f"@{message.from_user.username} = {message.text}")

    await message.reply("🤖 Estou pronto para baixar seus Vídeos\n\n✅ Por enquanto suportamos apenas vídeos do instagram\n\n👉 Me envie o link do reels para baixar:")


@dp.message_handler()
async def echo(message: types.Message):

    url = message.text

    logging.info(f"@{message.from_user.username} = {url}")

    # por enquanto só insta
    if 'instagram.com/reel' in url:

        new_msg = await message.answer('🔄 Verificando URL')

        media = insta.GetOriginalMedia(url)

        # acho o reels
        if media.success:
            # edita a mensagem de verificando para baixando
            await bot.edit_message_text(f'✅ Vídeo encontrado\n\n🔄 Baixando...', message.chat.id, new_msg.message_id)

            # envia o video baixado
            await message.reply_video(media.media_url, caption='👍Obrigado por usar nosso Bot🫶\n\n⭐️ Contribua com o desenvolvimento: https://github.com/joaoporth/video_downloader')

            logging.info(f"@{message.from_user.username} = vídeo baixado")

            # apaga a mensagem de baixando
            return await bot.delete_message(message.chat.id, new_msg.message_id)



        # não acho o reels
        else:

            return await bot.edit_message_text(f'❌ Ops\n\n{media.message}', message.chat.id, new_msg.message_id)

    else:
        await message.reply('❕ Por enquanto suportamos apenas reels do instagram\n\n👉 Me envie o link do reels para baixar:')

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=False)