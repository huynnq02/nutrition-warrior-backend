from rest_framework.decorators import api_view
from rest_framework.response import Response
from background_task.models import Task

@api_view(['GET'])
def get_scheduled_tasks(request):
    """
    List all currently scheduled tasks.

    Returns:
    Response: The HTTP response with the list of scheduled tasks.
    """
    try:
        tasks = Task.objects.all()
        task_list = [
            {
                'id': task.id,
                'task_name': task.task_name,
                'run_at': task.run_at,
                'kwargs': task.kwargs,
            }
            for task in tasks
        ]

        return Response({'scheduled_tasks': task_list}, status=200)

    except Exception as e:
        return Response({'success': False, 'message': str(e)}, status=500)
