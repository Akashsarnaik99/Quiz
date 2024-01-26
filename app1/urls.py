from django.urls import path
from . import views


urlpatterns= [
    path('',views.home, name='home'),
    path('result',views.result,name='result'),
    path('quiz',views.quiz,name='quiz'),
    path('evaluate',views.evaluate,name='evaluate'),
    path('result2',views.result2,name='result2'),

]