import pytest
from pytest_factoryboy import register
from rest_framework.test import APIClient
from .factories.task_factory import UserFactory, TaskFactory
from .factories.team_factory import TeamFactory

# Registrar factories
register(UserFactory)
register(TaskFactory)
register(TeamFactory)

@pytest.fixture
def api_client():
    return APIClient()

@pytest.fixture
def authenticated_client(api_client, user_factory):
    user = user_factory()
    api_client.force_authenticate(user=user)
    return api_client, user

@pytest.fixture
def task_with_user(task_factory, user_factory):
    user = user_factory()
    task = task_factory(assigned_to=user)
    return task, user