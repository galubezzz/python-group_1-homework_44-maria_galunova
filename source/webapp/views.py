from webapp.models import Course, Order, CourseOrder
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse, reverse_lazy
from webapp.forms import CourseForm, OrderForm, CourseOrderForm, StatusForm, OrderUpdateForm
from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin



class OrderDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = Order
    template_name = 'order_detail.html'
    permission_required = 'webapp.view_order'


class OrderListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Order
    template_name = 'order_list.html'
    permission_required = 'webapp.view_order'


class CourseDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = Course
    template_name = 'course_detail.html'
    permission_required = 'webapp.view_course'


class CourseListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Course
    template_name = 'course_list.html'
    permission_required = 'webapp.view_course'


class CourseCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Course
    template_name = 'course_create.html'
    form_class = CourseForm
    permission_required = 'webapp.add_course'

    def get_success_url(self):
        return reverse('webapp:course_detail', kwargs={'pk': self.object.pk})


class CouseUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Course
    template_name = 'course_update.html'
    form_class = CourseForm
    success_url = reverse_lazy('webapp:course_list')
    permission_required = 'webapp.change_course'


class CourseDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Course
    template_name = 'course_delete.html'
    success_url = reverse_lazy('webapp:course_list')
    permission_required = 'webapp.delete_course'


class OrderCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Order
    template_name = 'order_create.html'
    form_class = OrderForm
    permission_required = 'webapp.view_order'

    def form_valid(self, form):
        form.instance.status = 'new'
        form.instance.operator = self.request.user
        return super().form_valid(form)


    def get_success_url(self):
        return reverse('webapp:order_detail', kwargs={'pk': self.object.pk})


class OrderUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Order
    template_name = 'order_update.html'
    form_class = OrderUpdateForm
    permission_required = 'webapp.change_order'

    def get_success_url(self):
        return reverse('webapp:order_detail', kwargs={'pk': self.object.pk})


class OrderCancelView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Order
    template_name = 'order_cancel.html'
    form_class = StatusForm
    permission_required = 'webapp.change_order'

    def get(self, request, pk):
        order = get_object_or_404(Order, pk=pk)
        if order.status in ('new', 'preparing'):
            order.status = 'canceled'
        else:
            print("Заказ нельзя отменить")
        order.save()
        return redirect('webapp:order_list')

    def get_success_url(self):
        return reverse('webapp:order_detail', kwargs={'pk': self.object.pk})


class StatusUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Order
    form_class = StatusForm
    permission_required = 'webapp.can_take_and_deliver_orders'

    def get(self, request, pk):
        order = get_object_or_404(Order, pk=pk)
        if order.status == 'in progress':
            order.status = 'beeing delivered'
            order.courier = self.request.user
        elif order.status == 'beeing delivered' and order.courier == self.request.user:
            order.status = 'done'
        order.save()
        return redirect('webapp:order_list')


class CourseOrderCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = CourseOrder
    template_name = 'course_order_create.html'
    form_class = CourseOrderForm
    permission_required = 'webapp.view_courseorder'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['order_pk'] = self.kwargs.get('pk')
        return context

    def form_valid(self, form):
        form.instance.order = Order.objects.get(pk=self.kwargs.get('pk'))
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('webapp:order_detail', kwargs={'pk': self.object.order.pk})


class CourseOrderUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = CourseOrder
    template_name = 'course_order_update.html'
    form_class = CourseOrderForm
    permission_required = "webapp.change_courseorder"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['order_pk'] = self.kwargs.get('pk')
        return context

    def form_valid(self, form):
        form.instance.order = Order.objects.get(pk=self.kwargs.get('pk'))
        return super().form_valid(form)


    def get_success_url(self):
        return reverse('webapp:order_detail', kwargs={'pk': self.object.order.pk})


class CourseOrderDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = CourseOrder
    template_name = 'course_order_delete.html'
    permission_required = 'webapp.delete_courseorder'

    def get_success_url(self):
        return reverse('webapp:order_detail', kwargs={'pk': self.object.order.pk})

