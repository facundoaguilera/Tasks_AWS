# import pytest
# from tasks.services import TaskService  # Asumiendo que tienes una capa de servicios

# pytestmark = pytest.mark.django_db

# class TestTaskService:
#     def test_assign_task_to_team(self, task_factory, team_factory, user_factory):
#         """Test task assignment to team with notifications"""
#         team = team_factory()
#         users = user_factory.create_batch(3)
#         for user in users:
#             team.members.add(user)
        
#         task = task_factory(team=None)
        
#         TaskService.assign_to_team(task, team)
        
#         assert task.team == team
#         # Aquí podrías verificar que las notificaciones fueron enviadas, etc.

#     def test_task_status_workflow(self, task_factory):
#         """Test task status transitions"""
#         task = task_factory(status='todo')
        
#         TaskService.start_task(task)
#         assert task.status == 'in_progress'
        
#         TaskService.complete_task(task)
#         assert task.status == 'done'