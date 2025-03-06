import factory
from django.utils import timezone
from tasks.models import Task
from django.contrib.auth.models import User
from .team_factory import TeamFactory

class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Sequence(lambda n: f'user{n}')
    email = factory.LazyAttribute(lambda obj: f'{obj.username}@example.com')
    password = factory.PostGenerationMethodCall('set_password', 'testpass123')

class TaskFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Task

    title = factory.Sequence(lambda n: f'Task {n}')
    description = factory.Faker('text')
    status = 'todo'
    assigned_to = factory.SubFactory(UserFactory)
    team = factory.SubFactory(TeamFactory)
    due_date = factory.LazyFunction(lambda: timezone.now() + timezone.timedelta(days=7))