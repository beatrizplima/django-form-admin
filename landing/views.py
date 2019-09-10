from django.shortcuts import render

from rest_framework import viewsets, views
from rest_framework.filters import SearchFilter
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.authentication import TokenAuthentication
from landing.models import Aluno
from landing.serializers import AlunoSerializer


class AlunoViewSet(viewsets.ModelViewSet):
    filter_backends = [SearchFilter]
    search_fields = ['^nome', '=idade']
    queryset = Aluno.objects.all()
    # permission_classes = (IsAuthenticatedOrReadOnly,)
    # authentication_classes = (TokenAuthentication,)
    serializer_class = AlunoSerializer

class AlunoList(views.APIView):
    def get(self, request):
            alunos = Aluno.objects.all()
            serializer = AlunoSerializer(alunos, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = AlunoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)

class AlunoDetails(views.APIView):

    def get_object(self, id):
        try:
            return Aluno.objects.get(id=id)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, id):
        aluno = self.get_object(id)
        serializer = AlunoSerializer(aluno)
        return Response(serializer.data, status = status.HTTP_200_OK)
