import pytest
from django.core.exceptions import ValidationError

pytestmark = pytest.mark.django_db

class TestTaskModel:
    def test_task_creation(self, task_factory):
        """Test that a task can be created with valid data"""
        task = task_factory()
        assert task.title.startswith('Task')
        assert task.status == 'todo'
        assert task.assigned_to is not None
        assert task.team is not None

    def test_task_str_representation(self, task_factory):
        """Test the string representation of a task"""
        task = task_factory(title="Test Task")
        assert str(task) == "Test Task"

    def test_task_status_validation(self, task_factory):
        """Test that invalid status raises ValidationError"""
        with pytest.raises(ValidationError):
            task = task_factory(status='invalid_status')
            task.full_clean()

    def test_task_due_date_validation(self, task_factory):
        """Test that past due dates are not allowed"""
        from django.utils import timezone
        import datetime

        with pytest.raises(ValidationError):
            task = task_factory(
                due_date=timezone.now() - datetime.timedelta(days=1)
            )
            task.full_clean()