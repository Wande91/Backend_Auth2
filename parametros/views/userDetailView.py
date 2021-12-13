from rest_framework                        import status, generics
from django.conf                           import settings

from parametros.models.user                import user
from parametros.serializers.userSerializer import UserSerializer

class UserDetailView(generics.RetrieveAPIView):
    querySet           = user.objects.all()
    serializer_class   = UserSerializer
    def get(self, request, *args, **kwargs):        
        return super().get(self, request, *args, **kwargs)    


class UserUpdateView(generics.UpdateAPIView):
    querySet           = user.objects.all()
    serializer_class   = UserSerializer
    def update(self, request, *args, **kwargs):        
        return super().update(self, request, *args, **kwargs)

class UserDeleteView(generics.DestroyAPIView):
    querySet           = user.objects.all()
    serializer_class   = UserSerializer
    def delete(self, request, *args, **kwargs):  
        return super().destroy(self, request, *args, **kwargs)
