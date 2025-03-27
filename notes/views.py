from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.views.generic.edit import DeleteView
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse

from .forms import NotesForm
from .models import Notes

class NotesListView(ListView):
    model = Notes
    context_object_name = 'notes'
    template_name = 'notes/notes_list.html'

class PopularNotesListView(ListView):
    model = Notes
    context_object_name = 'notes'
    template_name = 'notes/notes_list.html'
    queryset = Notes.objects.filter(likes__gt=0).order_by('-likes')

class NotesDetailView(DetailView):
    model = Notes
    context_object_name = 'note'
    template_name = 'notes/notes_detail.html'

class NotesCreateView(CreateView):
    model = Notes
    form_class = NotesForm
    success_url = '/smart/notes'
    template_name = 'notes/notes_form.html'

class NotesUpdateView(UpdateView):
    model = Notes
    form_class = NotesForm
    success_url = '/smart/notes'
    template_name = 'notes/notes_form.html'

class NotesDeleteView(DeleteView):
    model = Notes
    success_url = '/smart/notes'
    template_name = 'notes/notes_delete.html'

def add_like_view(request, pk):
    if request.method == 'POST':
        note = get_object_or_404(Notes, pk=pk)
        note.likes += 1
        note.save()
        return HttpResponseRedirect(reverse('notes.detail', args=(pk,)))
    else:
        raise Http404
