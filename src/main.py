from telegram_api import Api, UpdateIterator
import asyncio
import settings
from pprint import pprint as pp

def sync(coro):
    t = asyncio.Task(coro)
    asyncio.get_event_loop().run_until_complete(t)
    return t.result()

api = Api(settings.TELEGRAM_API_KEY)

async def read_messages():
    async for m in UpdateIterator(api):
        pp(m)


sync(read_messages())




