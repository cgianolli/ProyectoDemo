from django.contrib import admin
from django.urls import path, include #sumo include para poder usarlo abajo
# from AppCoder.views import curso, profesores


urlpatterns = [
    path('admin/', admin.site.urls),
    # path('curso/', curso),
    path('appCoder/', include('AppCoder.urls')),
]
