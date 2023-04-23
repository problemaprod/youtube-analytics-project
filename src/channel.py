from googleapiclient.discovery import build
import os
import json

api_key: str = os.getenv('YT_API_KEY')
print(api_key)

youtube = build('youtube', 'v3', developerKey=api_key)


class Channel:
    """Класс для ютуб-канала"""

    def __init__(self, channel_id: str):
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.channel_id = channel_id

    def print_info(self):
        """Выводит в консоль информацию о канале."""
        channel = youtube.channels().list(id=self.channel_id, part='snippet,statistics').execute()
        print(json.dumps(channel, indent=2, ensure_ascii=False))
        # return channel


# two_drots = Channel("UCOIRN19VunfPaW7ZfmOKeoQ")
#
#
# # two_drots.print_info()



