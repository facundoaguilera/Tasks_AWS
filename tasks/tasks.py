from celery import shared_task
import time

@shared_task
def enviar_email(tarea_id):
    print(f"Enviando email para la tarea {tarea_id}")
    time.sleep(10)  # Simulando una tarea larga
    print(f"Email enviado para la tarea {tarea_id}")
