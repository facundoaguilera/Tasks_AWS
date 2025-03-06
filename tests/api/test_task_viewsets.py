import pytest
from django.urls import reverse
from rest_framework import status

pytestmark = pytest.mark.django_db

class TestTaskViewSet:
    def test_list_tasks(self, authenticated_client, task_factory):
        """Test that authenticated users can list tasks"""
        client, user = authenticated_client
        task_factory.create_batch(3, assigned_to=user)
        
        url = reverse('task-list')
        response = client.get(url)
        
        assert response.status_code == status.HTTP_200_OK
        assert len(response.data) == 3

    def test_create_task(self, authenticated_client, team_factory):
        """Test that authenticated users can create tasks"""
        client, user = authenticated_client
        team = team_factory()
        
        url = reverse('task-list')
        data = {
            'title': 'New Task',
            'description': 'Task Description',
            'status': 'todo',
            'team': team.id,
            'due_date': '2025-12-31'
        }
        
        response = client.post(url, data)
        assert response.status_code == status.HTTP_201_CREATED
        assert response.data['title'] == 'New Task'

    def test_update_task(self, authenticated_client, task_with_user):
        """Test that users can update their own tasks"""
        client, user = authenticated_client
        task, task_user = task_with_user
        
        url = reverse('task-detail', kwargs={'pk': task.pk})
        data = {'title': 'Updated Task'}
        
        response = client.patch(url, data)
        assert response.status_code == status.HTTP_200_OK
        assert response.data['title'] == 'Updated Task'