from . import views
from django.urls import path


urlpatterns = [
    path('Heart-Attack-model/',views.Heart_Attack),
]