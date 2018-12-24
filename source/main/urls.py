"""main URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings


from webapp.views import CourseDetailView, OrderDetailView, CourseListView, OrderListView, CourseCreateView, CouseUpdateView, \
    CourseDeleteView, OrderCreateView, OrderUpdateView, CourseOrderCreateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('order/<int:pk>', OrderDetailView.as_view(), name='order_detail'),
    path('course/<int:pk>', CourseDetailView.as_view(), name='course_detail'),
    path('', OrderListView.as_view(), name='order_list'),
    path('courses', CourseListView.as_view(), name='course_list'),
    path('courses/create', CourseCreateView.as_view(), name='course_create'),
    path('courses/<int:pk>/update', CouseUpdateView.as_view(), name='course_update'),
    path('courses/<int:pk>/delete', CourseDeleteView.as_view(), name='course_delete'),
    path('orders/create', OrderCreateView.as_view(), name='order_create'),
    path('orders/<int:pk>/update', OrderUpdateView.as_view(), name='order_update'),
    path('order/<int:pk>/courses/add', CourseOrderCreateView.as_view(), name='add_courses'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

