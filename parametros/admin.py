from django.contrib  import admin
from .models.user    import user
from .models.account import Account

# Register your models here.
admin.site.register(user)