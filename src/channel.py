from googleapiclient.discovery import build
import os
import json

api_key: str = os.getenv('YT_API_KEY')

youtube = build('youtube', 'v3', developerKey=api_key)


class Channel:
    """Класс для ютуб-канала"""

    def __init__(self, channel_id: str):
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.__channel_id = channel_id
        self.channel = youtube.channels().list(id=self.__channel_id, part='snippet,statistics').execute()
        self.content = json.dumps(self.channel, indent=2, ensure_ascii=False)
        self.file = json.loads(self.content)
        self.title = dict(self.file)['items'][0]['snippet']['title']
        self.video_count = dict(self.file)['items'][0]['statistics']['videoCount']
        self.url = f"https://www.youtube.com/channel/{dict(self.file)['items'][0]['id']}"

    def print_info(self):
        """Выводит в консоль информацию о канале."""
        self.channel = youtube.channels().list(id=self.__channel_id, part='snippet,statistics').execute()
        return json.dumps(self.channel, indent=2, ensure_ascii=False)

    @property
    def channel_id(self):
        """Делаеи channel_id не изменяемым"""
        return self.__channel_id

    @staticmethod
    def get_service():
        """получаем объект для работы с API вне класса"""
        return build('youtube', 'v3', developerKey=api_key)

    def to_json(self, file_name: str):
        """сохроняем данные каналла в в файле"""
        with open(file_name, 'w') as f:
            json.dump(self.channel, f, indent=2, ensure_ascii=False)

# two_drots = Channel("UCOIRN19VunfPaW7ZfmOKeoQ")
# # print(two_drots.print_info())
# # print(two_drots.url)
# # two_drots.channel_id = 'Новое название'
# # print(two_drots.channel_id)
# two_drots.to_json('two_drots.json')
