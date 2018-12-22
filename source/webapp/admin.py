from django.contrib import admin
from webapp.models import Employee, Order, Course, CourseOrder
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin

# Register your models here.
class EmployeeInline(admin.StackedInline):
    model = Employee


class EmployeeAdmin(UserAdmin):
    inlines = [EmployeeInline]


class CourseOrderInline(admin.TabularInline):
    model = CourseOrder
    fields = ['food', 'amount']


class OrderAdmin(admin.ModelAdmin):
    model = Order
    inlines = [CourseOrderInline]


admin.site.unregister(User)
admin.site.register(User, EmployeeAdmin)
admin.site.register(Course)
admin.site.register(Order, OrderAdmin)