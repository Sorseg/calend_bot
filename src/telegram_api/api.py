import aiohttp
import json


class Api:
    url = 'https://api.telegram.org/bot{token}/{method}'

    def __init__(self, token):
        self.token = token
        self.aio_session = aiohttp.ClientSession()
        self.last_update_id = None

    async def make_request(self, url, params=None, method='GET'):
        async with self.aio_session.request(method, url, params=params) as response:
            return await response.text()

    async def get_updates(self):
        url = self.url.format(token=self.token, method='getUpdates')
        params = {'timeout': '10'}
        if self.last_update_id:
            params['offset'] = int(self.last_update_id) + 1
        response = json.loads(await self.make_request(url, params))
        messages = response['result']
        if messages:
            self.last_update_id = max((m['update_id'] for m in messages))
        return messages

    async def send_inline_response(self, response):
        url = self.url.format(token=self.token, method='answerInlineQuery')
        result = await self.make_request(url, response)
        print(result)

    def iterate_messages(self):
        return UpdateIterator(self)

    def __del__(self):
        self.aio_session.close()


class UpdateIterator:

    def __init__(self, api):
        self.api = api
        self.messages = []

    async def __aiter__(self):
        return self

    async def __anext__(self):
        while not self.messages:
            self.messages = await self.api.get_updates()
        return self.messages.pop(0)
