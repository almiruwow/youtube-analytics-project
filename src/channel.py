import os
from googleapiclient.discovery import build
import json

api_key = os.getenv('YT_API_KEY')
youtube = build('youtube', 'v3', developerKey=api_key)


class Channel:
    """Класс для ютуб-канала"""

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self._channel_id = channel_id
        self.data_chanel = youtube.channels().list(id=self._channel_id, part='snippet, statistics').execute()
        self.title = self.data_chanel["items"][0]["snippet"]['title']
        self.video_count = self.data_chanel["items"][0]["statistics"]['videoCount']
        self.url = 'https://www.youtube.com/channel/' + channel_id

    @property
    def channel_id(self):
        return self._channel_id

    @staticmethod
    def get_service():
        return youtube

    def to_json(self, filename):
        with open(f'{filename}', 'w', encoding='utf-8') as file:
            json.dump(self.data_chanel, file, indent=2)
