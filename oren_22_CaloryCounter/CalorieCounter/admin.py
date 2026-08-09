from django.contrib import admin
from CalorieCounter.models import *

admin.site.register([UserModel,BasicInfoModel,ConsumedCalories])
