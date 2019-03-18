# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import RegistrationDatas,master,DistrictModel,BloodModel,UserProfileModel,project_employee
# Register your models here.

admin.site.register(RegistrationDatas)

admin.site.register(master)
admin.site.register(DistrictModel)
admin.site.register(BloodModel)
admin.site.register(UserProfileModel)
admin.site.register(project_employee)



