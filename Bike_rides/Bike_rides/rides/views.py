from django.shortcuts import render, redirect
from .models import Ride
from django.views.generic import ListView, DetailView, FormView
from .forms import UploadFileForm
from .functions import handle_uploaded_file, read_gpx
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


class UploadFileView(LoginRequiredMixin, FormView):
    template_name = 'rides/upload_file.html'
    form_class = UploadFileForm
    model = Ride

    def form_valid(self, form):
        handle_uploaded_file(self.request.FILES["file"])

        start_time, total_time, max_speed, distance, moving_time = read_gpx(self.request.FILES["file"])

        ride = Ride.objects.create(
            name=form.cleaned_data['title'],
            distance=distance,
            start_date=start_time,
            total_time=total_time,
            max_speed=max_speed,
            moving_time=moving_time,
            user=self.request.user,
        )

        return redirect('rides:file_uploaded_summary', pk=ride.pk)
        # return HttpResponse("File uploaded successfuly")


class FileUploadedSummary(LoginRequiredMixin, DetailView):
    template_name = 'rides/file_uploaded_summary.html'
    model = Ride
    fields = ('name', 'distance')

    def get_queryset(self):
        return Ride.objects.all().filter(user=self.request.user)


class RidesListView(LoginRequiredMixin, ListView):
    paginate_by = 3
    template_name = 'rides/ride_list.html'
    model = Ride

    def get_queryset(self):

        if self.request.user.is_superuser:
            return Ride.objects.all() \
                .order_by('-start_date')
        else:
            return Ride.objects.all().filter(user=self.request.user)\
                .order_by('-start_date')


# def upload_file(request):
#     if request.method == "POST":
#         form_upload = UploadFileForm(request.POST, request.FILES)
#         if form_upload.is_valid():
#             handle_uploaded_file(request.FILES["file"])
#             return HttpResponse("File uploaded successfuly")
#     else:
#         form_upload = UploadFileForm()
#     return render(request, "rallies/upload_file.html", {"form": form_upload})
