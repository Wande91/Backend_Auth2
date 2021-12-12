from parametros.models.account   import Account
from parametros.models.user      import user
from rest_framework              import serializers

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Account
        fields = ['balance', 'last_change_date', 'is_active']
    
    def to_representation(self, obj):
        accountData = Account.objects.get(id=obj.id)
        userData    = user.objects.get(id=obj.user_id)
        return {
           'id'             : accountData.id,
           'balance'        : accountData.balance,
           'lastChangeDate' : accountData.last_change_date,
           'user' : {
               'name': userData.name,
               'email': userData.email,
           }
        }
