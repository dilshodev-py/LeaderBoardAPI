import json
from channels.generic.websocket import AsyncWebsocketConsumer

from apps.models import Student


class LeaderBoardConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.group_name = "leader_bord_group"
        await self.channel_layer.group_add(
            self.group_name,
            self.channel_name
        )
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.group_name,
            self.channel_name
        )


    async def leaderboard_update(self, event):
        # Guruhdagi barcha klientlarga yangilangan ma'lumotni yuborish
        await self.send(text_data=json.dumps({
            'type': 'leaderboard_update',
            'data': event['data']
        }))