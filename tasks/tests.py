


from django.test import TestCase
from django.contrib.auth.models import User
from .models import Task, Team, Comment

class TaskModelTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.team = Team.objects.create(name='Test Team')
        self.task = Task.objects.create(
            title='Test Task',
            description='Test Description',
            status='todo',
            assigned_to=self.user,
            team=self.team,
            due_date='2025-12-31'
            
        )

    def test_task_creation(self):
        self.assertEqual(self.task.title, 'Test Task')
        self.assertEqual(self.task.description, 'Test Description')
        self.assertEqual(self.task.status, 'todo')
        self.assertEqual(self.task.assigned_to, self.user)
        self.assertEqual(self.task.team, self.team)

    def test_task_str_representation(self):
        self.assertEqual(str(self.task), 'Test Task')

class TeamModelTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.team = Team.objects.create(name='Test Team')
        self.team.members.add(self.user)

    def test_team_creation(self):
        self.assertEqual(self.team.name, 'Test Team')
        self.assertEqual(self.team.members.count(), 1)
        self.assertTrue(self.user in self.team.members.all())

    def test_team_str_representation(self):
        self.assertEqual(str(self.team), 'Test Team')

class CommentModelTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.team = Team.objects.create(name='Test Team')
        self.task = Task.objects.create(
            title='Test Task',
            description='Test Description',
            status='pending',
            assigned_to=self.user,
            team=self.team,
            due_date='2025-12-31'
        )
        self.comment = Comment.objects.create(
            task=self.task,
            author=self.user,
            content='Test Comment'
        )

    def test_comment_creation(self):
        self.assertEqual(self.comment.task, self.task)
        self.assertEqual(self.comment.author, self.user)
        self.assertEqual(self.comment.content, 'Test Comment')

    def test_comment_str_representation(self):
        expected_str = f'Comment by {self.user.username} on {self.task.title}'
        self.assertEqual(str(self.comment), expected_str)

# from django.urls import reverse
# from rest_framework import status
# from rest_framework.test import APITestCase
# from .models import Team
# from django.contrib.auth.models import User

# class TeamViewSetTests(APITestCase):

#     def setUp(self):
#         self.user = User.objects.create_user(username='testuser', password='testpass')
#         self.client.force_authenticate(user=self.user)

#     def test_team_viewset_list(self):
#         Team.objects.create(name='Team A')
#         Team.objects.create(name='Team B')
        
#         url = reverse('team-list')
#         response = self.client.get(url)
        
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.assertEqual(len(response.data), 2)
#         self.assertEqual(response.data[0]['name'], 'Team A')
#         self.assertEqual(response.data[1]['name'], 'Team B')

#     def test_team_viewset_create(self):
#         url = reverse('team-list')
#         data = {'name': 'New Team', 'members': [self.user.id]}
#         response = self.client.post(url, data, format='json')
        
#         self.assertEqual(response.status_code, status.HTTP_201_CREATED)
#         self.assertEqual(Team.objects.count(), 1)
#         self.assertEqual(Team.objects.get().name, 'New Team')

#     def test_team_viewset_retrieve_nonexistent(self):
#         url = reverse('team-detail', args=[999])
#         response = self.client.get(url)
        
#         self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)