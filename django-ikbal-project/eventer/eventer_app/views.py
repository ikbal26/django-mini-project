from django.shortcuts import render
from .events import events
from datetime import datetime
def index_view(request,):
    current_day = datetime.now().day
    current_event = events[current_day]
    client_ip = request.META.get('REMOTE_ADDR')

    context = {
        'current_day': current_day,
        'current_event': current_event,
        'client_ip': client_ip,
        'events': events
    }

    return render(request, 'index.html', {})