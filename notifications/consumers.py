import json
from channels.generic.websocket import AsyncWebsocketConsumer

class NotificationConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        # Grupo para notificaciones globales
        await self.channel_layer.group_add('notifications', self.channel_name)
        await self.accept()
        await self.send( text_data= json.dumps({
            'type': 'connection established',
            'message': 'you are connected now'
        }) )

    async def disconnect(self, close_code):
        # Salir del grupo al desconectar
        await self.channel_layer.group_discard('notifications', self.channel_name)

    async def receive(self, text_data):
        # Recibir mensajes del frontend (opcional)
        data = json.loads(text_data)
        print('message:',data)
        await self.channel_layer.group_send(
            'notifications',
            {
                'type': 'send_notification',
                'message': data['message']
            }
        )

    async def send_notification(self, event):
        # Enviar notificación al frontend
        await self.send(text_data=json.dumps(event))