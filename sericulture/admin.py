from django.contrib import admin
from .models import Farmer
from .models import MulberryFarm
from .models import SilkwormBatch

admin.site.register(Farmer)
admin.site.register(MulberryFarm)
admin.site.register(SilkwormBatch)

