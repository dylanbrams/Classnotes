from django.contrib import admin
from KilnData.models import KilnUserProfile
from KilnData.models import Program
from KilnData.models import Kiln
from KilnData.models import KilnAdminType
from KilnData.models import ProgramStep
from KilnData.models import jt_Kiln_Admin
from KilnData.models import jt_Kiln_Program

#Kiln Data Models.

class KilnUserProfileAdmin(admin.ModelAdmin):
    pass
admin.site.register(KilnUserProfile, KilnUserProfileAdmin)

class ProgramAdmin(admin.ModelAdmin):
    pass
admin.site.register(Program, ProgramAdmin)

class KilnAdmin(admin.ModelAdmin):
    pass
admin.site.register(Kiln, KilnAdmin)

class KilnAdminTypeAdmin(admin.ModelAdmin):
    pass
admin.site.register(KilnAdminType, KilnAdminTypeAdmin)

class ProgramStepAdmin(admin.ModelAdmin):
    pass
admin.site.register(ProgramStep, ProgramStepAdmin)

class jt_Kiln_AdminAdmin(admin.ModelAdmin):
    pass
admin.site.register(jt_Kiln_Admin, jt_Kiln_AdminAdmin)

class jt_Kiln_ProgramAdmin(admin.ModelAdmin):
    pass
admin.site.register(jt_Kiln_Program, jt_Kiln_ProgramAdmin)
