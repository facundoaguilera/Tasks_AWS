from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Task
from .serializers import TaskSerializer
from .tasks import enviar_email
from django.http import JsonResponse

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        # Asignar automáticamente la tarea al usuario que la crea
        serializer.save(assigned_to=self.request.user)
        #tareas de celery ( cada vez que se crea una tarea )
        
        tarea_id = 123
        enviar_email.delay(tarea_id)  # Llamada asíncrona
        return JsonResponse({"mensaje": "El email está siendo enviado en segundo plano"})


