from django.urls import path
from webapp.views import CourseDetailView, OrderDetailView, CourseListView, OrderListView, CourseCreateView, CouseUpdateView, \
    CourseDeleteView, OrderCreateView, OrderUpdateView, CourseOrderCreateView, CourseOrderUpdateView, CourseOrderDeleteView, \
    StatusUpdateView, OrderCancelView, CourseOrderAjaxCreateView, CourseOrderAjaxUpdateView

app_name = 'webapp'

urlpatterns = [
    path('order/<int:pk>', OrderDetailView.as_view(), name='order_detail'),
    path('course/<int:pk>', CourseDetailView.as_view(), name='course_detail'),
    path('', OrderListView.as_view(), name='order_list'),
    path('courses', CourseListView.as_view(), name='course_list'),
    path('courses/create', CourseCreateView.as_view(), name='course_create'),
    path('courses/<int:pk>/update', CouseUpdateView.as_view(), name='course_update'),
    path('courses/<int:pk>/delete', CourseDeleteView.as_view(), name='course_delete'),
    path('orders/create', OrderCreateView.as_view(), name='order_create'),
    path('orders/<int:pk>/update', OrderUpdateView.as_view(), name='order_update'),
    path('order/<int:pk>/courses/add', CourseOrderCreateView.as_view(), name='add_course'),
    path('order/<int:pk>/courses/update', CourseOrderUpdateView.as_view(), name='change_course'),
    path('order/<int:pk>/courses/delete', CourseOrderDeleteView.as_view(), name='delete_course'),
    path('orders/<int:pk>/status_update', StatusUpdateView.as_view(), name='order_status_update'),
    path('orders/<int:pk>/cancel', OrderCancelView.as_view(), name='order_cancel'),
    path('order/<int:pk>/course/create', CourseOrderAjaxCreateView.as_view(), name='order_course_create'),
    path('order/course/<int:pk>/update', CourseOrderAjaxUpdateView.as_view(), name='order_course_update'),
]