from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Task
from .serializers import TaskSerializer
from .tasks import enviar_email
from django.http import JsonResponse

# class TaskViewSet(viewsets.ModelViewSet):
#     queryset = Task.objects.all()
#     serializer_class = TaskSerializer
#     permission_classes = [IsAuthenticated]

#     def perform_create(self, serializer):
#         # Asignar automáticamente la tarea al usuario que la crea
#         serializer.save(assigned_to=self.request.user)
#         #tareas de celery ( cada vez que se crea una tarea )
        
#         tarea_id = 123
#         enviar_email.delay(tarea_id)  # Llamada asíncrona
#         return JsonResponse({"mensaje": "El email está siendo enviado en segundo plano"})

from rest_framework import viewsets
from .models import Task, Team, Comment
from .serializers import TaskSerializer, TeamSerializer, CommentSerializer
from .services import send_task_notification  # Importar el servicio

class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def perform_create(self, serializer):
        # Guardar la tarea
        task = serializer.save()
        # Llamar al servicio para enviar notificación
        send_task_notification(f'Tarea "{task.title}" creada chinwenwencha.')

    def perform_update(self, serializer):
        # Guardar la tarea actualizada
        task = serializer.save()
        # Llamar al servicio para enviar notificación
        #send_task_notification(f'Tarea "{task.title}" actualizada.')

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
