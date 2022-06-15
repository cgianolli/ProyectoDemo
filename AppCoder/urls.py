from django.urls import path
from AppCoder.views import curso, profesores # Asi estaba en el proyecto 

urlpatterns = [
    path('curso/', curso),
    path('profesores/', profesores),
    
]
