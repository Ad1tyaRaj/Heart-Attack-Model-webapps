from . import views
from django.urls import path


urlpatterns = [
    path('Student-Placement-model/',views.Student_placement),
]