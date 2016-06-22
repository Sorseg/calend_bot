from logic import Handler
from telegram_api import Api, UpdateIterator
import asyncio
import settings
from pprint import pprint as pp


def sync(coro):
    t = asyncio.Task(coro)
    asyncio.get_event_loop().run_until_complete(t)
    return t.result()

h = Handler()
api = Api(settings.TELEGRAM_API_KEY)

async def read_messages():
    async for msg in UpdateIterator(api):
        pp(msg)
        if 'inline_query' in msg:
            await api.send_inline_response(h.handle(msg))


sync(read_messages())




