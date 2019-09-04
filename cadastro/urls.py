from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from rest_framework import routers

from landing.views import AlunoViewSet

router = routers.DefaultRouter()
router.register('alunos', AlunoViewSet)

from professor.views import ProfessorViewSet

router.register('professores', ProfessorViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('admin/', admin.site.urls),
]