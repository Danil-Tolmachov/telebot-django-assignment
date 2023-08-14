from django.urls import path
import bot.views as views

urlpatterns = [
    path('accumulation/', views.AccumulationView.as_view()),
    path('statistics/', views.get_statistics, name='statistics')
]
