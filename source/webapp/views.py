from webapp.models import Course, Order
from django.views.generic import DetailView, ListView


class CourseDetailView(DetailView):
    model = Course
    template_name = 'course_detail.html'


class OrderDetailView(DetailView):
    model = Order
    template_name = 'order_detail.html'

class OrderListView(ListView):
    model = Order
    template_name = 'order_list.html'


class CourseListView(ListView):
    model = Course
    template_name = 'course_list.html'