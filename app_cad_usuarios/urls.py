from django.urls import path
from .views import home, contato, produto

urlpatterns = [
    path('', home, name='home'),
    path('contato', contato, name='contato'),
    path('produto/<int:pk>/', produto, name='produto'),
]

handler500 = 'app_cad_usuarios.views.error500'
