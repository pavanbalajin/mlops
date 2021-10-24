from django.urls import path
from apicalling.views import Test

urlpatterns = [
    path('test', Test.as_view(), name = 'test'),
    
]