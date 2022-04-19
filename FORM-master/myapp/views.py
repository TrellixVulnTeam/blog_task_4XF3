from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, ListView
from .forms import StudentForm
from myapp.models import Student


class StudentCreateView(CreateView):
    model = Student
    form_class = StudentForm
    template_name = 'myapp/home.html'
    success_url = reverse_lazy('display')

    def form_valid(self, form):
        print(form, 'Valid')
        pass

    def form_invalid(self, form):
        print(form, 'Invalid')
        pass


# class StudentCreateView(View):
#     def get(self, request):
#         form = StudentForm()
#         # candidates = Student.objects.all()
#         return render(request, 'myapp/home.html', {'form': form})
#
#     def post(self, request):
#         form = StudentForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return render(request, 'myapp/home.html', {'form': form})


class DisplayView(ListView):
    model = Student
    template_name = 'myapp/display.html'
    context_object_name = 'students'
