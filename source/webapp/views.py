from webapp.models import Course, Order
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse, reverse_lazy
from webapp.forms import CourseForm




class OrderDetailView(DetailView):
    model = Order
    template_name = 'order_detail.html'

class OrderListView(ListView):
    model = Order
    template_name = 'order_list.html'

class CourseDetailView(DetailView):
    model = Course
    template_name = 'course_detail.html'


class CourseListView(ListView):
    model = Course
    template_name = 'course_list.html'

class CourseCreateView(CreateView):
    model = Course
    template_name = 'course_create.html'
    form_class = CourseForm

    def get_success_url(self):
        return reverse('course_detail', kwargs={'pk': self.object.pk})

class CouseUpdateView(UpdateView):
    model = Course
    template_name = 'course_update.html'
    form_class = CourseForm
    success_url = reverse_lazy('course_list')

class CourseDeleteView(DeleteView):
    model = Course
    template_name = 'course_delete.html'
    success_url = reverse_lazy('course_list')



