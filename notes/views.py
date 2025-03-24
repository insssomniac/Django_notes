from django.shortcuts import render
from django.http import Http404

from .models import Notes

def list(request):
    notes = Notes.objects.all()
    return render(request, 'notes/list.html', {'notes': notes})

def detail(request, pk):
    try:
        note = Notes.objects.get(pk=pk)
    except Notes.DoesNotExist:
        raise Http404('Note does not exist')
    return render(request, 'notes/detail.html', {'note': note})
