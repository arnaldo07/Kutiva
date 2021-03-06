from django.shortcuts import render
from .models import Screencast

def screencasts(request):
    screencasts = Screencast.objects.all()
    return render(request, 'screencast/screencasts.html', {"screencasts":screencasts})



def watch(request, id):
    try:
    	screencasts = Screencast.get(id=id)
    except Screencast.DoesNotExist:
        raise Http404('This item does not exist')
    return render(request, 'kutiva/watch.html', {
        'lesson': lesson,
    })
    