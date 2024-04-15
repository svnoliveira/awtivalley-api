from django.shortcuts import get_object_or_404
from .models import UserCurso
from users.models import User
from cursos.models import Curso
from .serializers import UserCursoSerializer
from rest_framework.generics import UpdateAPIView
from rest_framework_simplejwt.authentication import JWTAuthentication


class UserCursoUpdateView(UpdateAPIView):
    authentication_classes = [JWTAuthentication]

    serializer_class = UserCursoSerializer
    queryset = UserCurso.objects.all()

    def get_object(self):
        user = get_object_or_404(User, pk=self.kwargs["user_id"])
        curso = get_object_or_404(Curso, pk=self.kwargs["curso_id"])

        obj, created = UserCurso.objects.get_or_create(user=user, curso=curso)
        self.check_object_permissions(self.request, obj)
        return obj
