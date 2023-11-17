from django.urls import path
from . import views

urlpatterns = [
    path('formateurs/', views.members, name='formateurs'),
    path('Training/', Training.site.urls),
    ]