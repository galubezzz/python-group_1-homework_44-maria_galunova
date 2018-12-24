from webapp.models import Course, Order, CourseOrder
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse, reverse_lazy
from webapp.forms import CourseForm, OrderForm, CourseOrderForm




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


class OrderCreateView(CreateView):
    model = Order
    template_name = 'order_create.html'
    form_class = OrderForm

    def get_success_url(self):
        return reverse('order_detail', kwargs={'pk': self.object.pk})

class OrderUpdateView(UpdateView):
    model = Order
    template_name = 'order_update.html'
    form_class = OrderForm

    def get_success_url(self):
        return reverse('order_detail', kwargs={'pk': self.object.pk})

class CourseOrderCreateView(CreateView):
    model = CourseOrder
    template_name = 'course_order_create.html'
    form_class = CourseOrderForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['order_pk'] = self.kwargs.get('pk')
        return context

    def form_valid(self, form):
        form.instance.order = Order.objects.get(pk=self.kwargs.get('pk'))
        return super().form_valid(form)


    def get_success_url(self):
        return reverse('order_detail', kwargs={'pk': self.object.order.pk})