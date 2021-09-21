from django.shortcuts import render
from django.views.generic import (TemplateView, DetailView,
                                    ListView, CreateView,
                                    UpdateView,DeleteView,FormView,)
from .models import Standard, Subject, Lesson
from .forms import LessonForm
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy

# Create your views here.
class StandardListView(ListView):
    context_object_name = 'standards'
    model = Standard
    template_name = 'courses/standard_list_view.html'



class SubjectListView(DetailView):
    context_object_name = 'standards'
    model = Standard
    template_name = 'courses/subject_list_view.html'



class LessonListView(DetailView):
    context_object_name = 'subjects'
    model = Subject
    template_name = 'courses/lesson_list_view.html'


class LessonDetailView(DetailView):
    context_object_name = 'lessons'
    model = Lesson
    template_name = 'courses/lesson_detail_view.html'









##########create

class LessonCreateView(CreateView):
    form_class = LessonForm
    context_object_name = 'subject'
    model= Subject
    template_name = 'courses/lesson_create.html'

    def get_success_url(self):
        self.object = self.get_object()
        standard = self.object.standard
        return reverse_lazy('courses:lesson_list',kwargs={'standard':standard.slug,
                                                             'slug':self.object.slug})


    def form_valid(self, form, *args, **kwargs):
        self.object = self.get_object()
        fm = form.save(commit=False)
        fm.created_by = self.request.user
        fm.Standard = self.object.standard
        fm.subject = self.object
        fm.save()
        return HttpResponseRedirect(self.get_success_url())
    


class LessonUpdateView(UpdateView):
    fields = ('name','position','video','ppt','Notes')
    model= Lesson
    template_name = 'courses/lesson_update.html'
    context_object_name = 'lessons'



class LessonDeleteView(DeleteView):
    model= Lesson
    context_object_name = 'lessons'
    template_name = 'courses/lesson_delete.html'

    def get_success_url(self):
        print(self.object)
        standard = self.object.Standard
        subject = self.object.subject
        return reverse_lazy('courses:lesson_list',kwargs={'standard':standard.slug,'slug':subject.slug})





#def classesView(request,apple):
    