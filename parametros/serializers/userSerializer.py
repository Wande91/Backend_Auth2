from parametros.models.user      import user
from rest_framework              import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = user
        fields = ['id', 'username', 'password', 'name', 'email']

 
        def to_representation(self, obj):
            user     = user.objects.get(id=obj.id)            
            return {
                'id'       : user.id,
                'username' : user.balance,
                'name'     : user.name,
                'email'    : user.email,                
           }
            