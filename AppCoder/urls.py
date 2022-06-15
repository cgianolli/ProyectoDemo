from django.urls import path
from AppCoder.views import curso, profesores # Asi estaba en el proyecto 
from AppCoder.views import mi_plantilla # la que cree con los bootstrap
urlpatterns = [
    path('curso/', curso),
    path('profesores/', profesores),
    path('mi_plantilla/', mi_plantilla),
]
