from django.views.generic import ListView, DetailView

from .models import Notes

class NotesListView(ListView):
    model = Notes
    context_object_name = 'notes'
    template_name = 'notes/list.html'

class PopularNotesListView(ListView):
    model = Notes
    context_object_name = 'notes'
    template_name = 'notes/list.html'
    queryset = Notes.objects.filter(likes__gt=0).order_by('-likes')

class NotesDetailView(DetailView):
    model = Notes
    context_object_name = 'note'
    template_name = 'notes/detail.html'
