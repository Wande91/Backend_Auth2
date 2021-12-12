from parametros.models.account   import Account
from parametros.models.user      import user
from .accountSerializer          import AccountSerializer
from rest_framework              import serializers

class UserSerializer (serializers.ModelSerializer):
    class Meta:
        model = user
        fields = ['id', 'username', 'password', 'name', 'email', 'account']

        def create(self, validated_data):
            accountData = validated_data.pop('account')
            userInstance = user.objects.create(**validated_data)
            Account.objects.create(user=userInstance, **accountData)
            return userInstance

        def to_representation(self, obj):
            user     = user.objects.get(id=obj.id)
            account  = Account.objects.get(user=obj.id)
            return {
                'id'       : user.id,
                'username' : user.balance,
                'name'     : user.name,
                'email'    : user.email,
                'account'  : {
                    'id'                : account.id,
                    'balance'           : account.balance,
                    'lastChangeDate'    : account.lastChangeDate,
                    'isActive'          : account.isActive
           }
        }
