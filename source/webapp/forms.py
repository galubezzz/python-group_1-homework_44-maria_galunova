from django import forms
from webapp.models import Course, Order, CourseOrder

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        exclude =[]

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        exclude = []


class CourseOrderForm(forms.ModelForm):
    class Meta:
        model = CourseOrder
        exclude = ['order']

