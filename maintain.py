from telethon import TelegramClient, events
import aiohttp

# أدخل بياناتك هنا
api_id = '29147240'
api_hash = '0fe85fc806f0e22291b804262404d273'
bot_token = '7420366841:AAFaS9oOBdYP6AXF3kdUyHVkQFIbEwqkvsw'

# إنشاء عميل لتسجيل الدخول
client = TelegramClient('bot', api_id, api_hash).start(bot_token=bot_token)

@client.on(events.NewMessage(pattern='/start'))
async def start(event):
    await event.respond('مرحبًا! أنا بوتك الشخصي.')
    await event.respond('أرسل لي رسالة وسأرد عليك.')

    await event.respond('ارسل /help أو /start')
    raise events.StopPropagation
@client.on(events.NewMessage(pattern='/help'))
async def help_command(event):
    raise events.StopPropagation

@client.on(events.NewMessage)
async def echo(event):
    user_message = event.message.text.lower()

    # الردود التلقائية
    if user_message == 'مرحبا':
        response = 'أهلاً وسهلاً!'
    elif user_message == 'شلونك':
        response = 'زين وانت شلونك؟'
    elif user_message == "زين" or "الحمدالله":
    	response = "دوومك ياعمري انت❤️"
    elif user_message == "شسمك":
    	response = "انا نموذج ذكاء اصطناعي تم تدريبي بواسطة المطور ياسين"
    elif user_message == 'وينك':
    	response = 'أنا هنا، شنو تحتاج؟'
    elif user_message == "سلامتك"   or "سلامتك والله":
    	response = "الله يسلمك يا ورده"
    else:
        # الرد عبر API للذكاء الاصطناعي إذا لم تكن الرسالة تتطابق مع الردود التلقائية
        response = await get_ai_response(user_message)
    
    await event.respond(response)

async def get_ai_response(message: str) -> str:
    url = 'https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent'  # استبدل بـ URL الخاص بـ API
    headers = {'Authorization': 'AIzaSyCXDmv-UKrKO1mqNbtEqmzUWXZfM1zj_bg'}  # استبدل بـ API Key الخاص بك

    async with aiohttp.ClientSession() as session:
        async with session.post(url, json={'message': message}, headers=headers) as response:
            data = await response.json()
            return data.get('response', 'أعتذر، لم أفهم ما تقصده.')

# بدء العميل
client.run_until_disconnected()