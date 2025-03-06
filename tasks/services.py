# tasks/services.py
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

def send_task_notification(message):
    """
    Envía una notificación a través de WebSockets.
    """
    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_send)(
        'notifications',  # Nombre del grupo
        {
            'type': 'send_notification',  # Método del consumidor
            'message': message
        }
    )