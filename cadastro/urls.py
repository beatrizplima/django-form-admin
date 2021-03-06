from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token
from landing.views import AlunoViewSet, AlunoList, AlunoDetails

router = routers.DefaultRouter()
router.register('alunos', AlunoViewSet)

from professor.views import ProfessorViewSet

router.register('professores', ProfessorViewSet)

urlpatterns = [
    path('alunos', AlunoList.as_view()),
    path('alunos/<int:id>', AlunoDetails.as_view()),
    path('api/', include(router.urls)),
    path('admin/', admin.site.urls),
    path('auth-api/', obtain_auth_token),
]