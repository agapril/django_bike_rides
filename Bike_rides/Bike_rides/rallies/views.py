from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Rally, ParticipantsList
from django.views.generic import ListView, DetailView, FormView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .forms import RallyRegisterForm
from django.contrib.admin.widgets import AdminDateWidget, AdminTimeWidget
from datetime import date
from django.contrib.auth.mixins import LoginRequiredMixin


def hello_world(request):
    return HttpResponse('Hello world')


def intro(request):
   return render(request, 'rallies/intro.html')


class RallyList(ListView):
    paginate_by = 3
    model = Rally
    template_name = 'rallies/rally_list.html'

    def get_queryset(self):
        # print(Rally.objects.filter(date__gt=datetime.today()) == True)
        return Rally.objects.all().order_by('-date')
        # return Rally.objects.filter(date__gt=datetime.today()).order_by('-date')

    def get_context_data(self, **kwargs):
        flag = []
        for Obj in Rally.objects.all():

            if Obj.date > date.today():
                flag.append(True)
                # print(Obj.date)
                print(flag)
            else:
                flag.append(False)
                print(flag)

        context = {
            'flag': flag,
        }
        kwargs.update(context)
        return super().get_context_data(**kwargs)


class RallyDetail(LoginRequiredMixin, DetailView):
    model = Rally


class RallyCreate(LoginRequiredMixin, CreateView):
    model = Rally
    fields = ('description', 'date', 'time', 'level', 'place')
    success_url = reverse_lazy('rallies:list')

    def get_form(self, form_class=None):
        form = super(RallyCreate, self).get_form(form_class)
        form.fields['date'].widget = AdminDateWidget(attrs={'type': 'date'})
        form.fields['time'].widget = AdminTimeWidget(attrs={'type': 'time'})
        return form


class RallyUpdate(LoginRequiredMixin, UpdateView):
    permission_required = 'update.rally'
    model = Rally
    fields = ('description', 'date', 'level', 'place')
    success_url = reverse_lazy('rallies:list')


class RallyDelete(LoginRequiredMixin, DeleteView):
    permission_required = 'delete.rally'
    model = Rally
    success_url = reverse_lazy('rallies:list')


class RallyConfirmedDetail(LoginRequiredMixin, DetailView):
    template_name = 'rallies/rally_confirmed.html'
    model = Rally
    fields = ('description', 'date', 'level', 'place')


class RallyRegisterView(LoginRequiredMixin, FormView):
    template_name = 'rallies/rally_register.html'
    success_url = reverse_lazy('rallies:rally_confirmed')
    form_class = RallyRegisterForm
    model = ParticipantsList

    def form_valid(self, form):
        # print(form.cleaned_data['id_rally'].pk)
        form.cleaned_data['id_participant'] = self.request.user.id
        # print(form.cleaned_data)

        ParticipantsList.objects.create(
            id_participant=self.request.user,
            id_rally=form.cleaned_data['id_rally']
        )

        return redirect('rallies:rally_confirmed', pk=form.cleaned_data['id_rally'].pk)


# class UploadFileView(FormView):
#     template_name = 'rallies/upload_file.html'
#     form_class = UploadFileForm
#     model = Ride
#
#     def form_valid(self, form):
#         handle_uploaded_file(self.request.FILES["file"])
#
#         start_time, total_time, max_speed, distance, moving_time = read_gpx(self.request.FILES["file"])
#
#         ride = Ride.objects.create(
#             name=form.cleaned_data['title'],
#             distance=distance,
#             start_date=start_time,
#             total_time=total_time,
#             max_speed=max_speed,
#             moving_time=moving_time,
#             user=self.request.user,
#         )
#
#         return redirect('rallies:file_uploaded_summary', pk=ride.pk)
#         # return HttpResponse("File uploaded successfuly")
#
#
# class FileUploadedSummary(DetailView):
#     template_name = 'rallies/file_uploaded_summary.html'
#     model = Ride
#     fields = ('name', 'distance')
#
#
# class RidesListView(ListView):
#     template_name = 'rallies/ride_list.html'
#     model = Ride
#
#     def get_queryset(self):
#         return Ride.objects.all().order_by('-start_date')
#
# # def upload_file(request):
# #     if request.method == "POST":
# #         form_upload = UploadFileForm(request.POST, request.FILES)
# #         if form_upload.is_valid():
# #             handle_uploaded_file(request.FILES["file"])
# #             return HttpResponse("File uploaded successfuly")
# #     else:
# #         form_upload = UploadFileForm()
# #     return render(request, "rallies/upload_file.html", {"form": form_upload})