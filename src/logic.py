import json
import dateparser
from calendar import TextCalendar
from telegram_api.api import CALENDAR_DOC_ID
import uuid

class Handler:
    def handle(self, msg):
        date_text = msg['inline_query']['query']
        if not date_text:
            date_text = 'now'
        date = dateparser.parse(date_text)
        cal = 'Not recognized'
        if date:
            cal = '```{}```'.format(TextCalendar().formatmonth(date.year, date.month))
        parsed_str = date.strftime('%Y-%m-%d') if date else 'WAT?'

        return {
            'inline_query_id': msg['inline_query']['id'],
            'results': json.dumps([
                {
                    'type': 'article',
                    'id': uuid.uuid4().hex,
                    'gif_file_id': CALENDAR_DOC_ID,
                    'title': date_text,
                    # 'caption': parsed_str,
                    'description': parsed_str,
                    'url': 'sorseg.ru',
                    'hide_url': True,
                    'thumb_url': 'sorseg.ru/c.jpg',
                    'input_message_content': {
                        'message_text': cal,
                        'parse_mode': 'Markdown'
                    }
                }
            ])
        }
