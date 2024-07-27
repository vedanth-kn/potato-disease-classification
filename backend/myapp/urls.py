from django.urls import path
from myapp import views

urlpatterns = [
    path('hello/', views.hello, name='hello'),
    path('predict/', views.predict, name='predict'),
    path('test/', views.test_view, name='test_view'),
]