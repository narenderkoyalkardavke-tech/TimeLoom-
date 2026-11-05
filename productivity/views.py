from django.shortcuts import render

def dashboard(request):
    context = {
        'total_tasks': 12,
        'completed_tasks': 8,
        'pending_tasks': 4,
        'focus_hours': 4.5,
        'productivity': 85,
    }

    return render(request, 'productivity/dashboard.html', context)
