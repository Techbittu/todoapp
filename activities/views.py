from django.shortcuts import (
    render,
    redirect
)
from datetime import datetime
from django.contrib.auth.models import User
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Activity
from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    UserPassesTestMixin
)
from .forms import (
    ActivityForm,
    RawActivityForm
)
from django.views import View


class ActivityListView(LoginRequiredMixin, ListView):
    login_url = '/login/'
    model = Activity
    template_name = 'activity.html'
    context_object_name = 'activities'
    ordering = ['-to_do_date']

    def get_queryset(self):
        return super().get_queryset().filter(user=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        grouped_activities = []
        current_date = None
        current_activities = []
        for activity in context['activities']:
            if activity.to_do_date.date() != current_date:
                if current_date is not None:
                    grouped_activities.append((current_date, current_activities))
                    current_activities = []
                current_date = activity.to_do_date.date()
            current_activities.append(activity)
            pass
        grouped_activities.append((current_date, current_activities))
        context['grouped_activities'] = grouped_activities
        return context


class ActivityDetailView(DetailView):
    model = Activity
    template_name = 'activity_detail.html'


class ActivityCreateView(LoginRequiredMixin, CreateView):
    form_class = ActivityForm
    template_name = 'activity_form.html'
    success_url = '/activities'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class ActivityDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Activity
    template_name = 'activity_delete.html'
    success_url = '/'

    def test_func(self):
        activity = self.get_object()
        if self.request.user == activity.user:
            return True
        return False


class ActivityUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Activity
    template_name = 'activity_form.html'
    fields = ['activity', 'to_do_date', 'is_done']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def test_func(self):
        activity = self.get_object()
        return self.request.user == activity.user



class DeleteManyActivieties(LoginRequiredMixin, UserPassesTestMixin, View):
    model = Activity

    def post(self, request):
        list_ids = request.POST.getlist('id')
        for object_id in list_ids:
            Activity.objects.get(id=object_id).delete()
        return redirect('activity')

    def test_func(self):
        for pk in self.request.POST.getlist('id'):
            if self.request.user != Activity.objects.get(id=pk).user:
                return False
        return True


class ChangeStatusActivieties(LoginRequiredMixin, UserPassesTestMixin, View):
    model = Activity

    def get(self, request, pk):
        activity = Activity.objects.get(id=pk)
        activity.is_done = not activity.is_done
        activity.save()
        return redirect(f'/activities/#activity-{pk}')

    def test_func(self):
        pk = self.kwargs.get('pk')
        return self.request.user == Activity.objects.get(id=pk).user