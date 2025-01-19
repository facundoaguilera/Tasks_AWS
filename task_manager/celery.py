from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

# Establece el módulo de configuración predeterminado de Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'task_manager.settings')

# Crea una instancia de Celery
app = Celery('task_manager')

# Usamos el string aquí para que Celery pueda descubrir la configuración
# de Django automáticamente usando el archivo settings.py.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Carga tareas de todos los módulos de tareas registrados
app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))
