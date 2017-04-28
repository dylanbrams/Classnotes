from rest_framework import permissions
from KilnData.models import jt_Kiln_Admin, jt_Program_Admin, KilnAdminType
from django.db.models import Q

class CanModifyObject(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        # Modifying Administration / Ownership is only allowed if the user is Owner of the object.
        admin_type_ids = KilnAdminType.objects.filter(kilnadmintype_name__in=('Owner', 'Manager')).values_list('kilnadmintype_id')
        if ('/kilnedits/' in request.path):
            Admin_rights = jt_Kiln_Admin.objects.filter(user=request.user, kiln_id=obj.kiln_id, kilnadmintype__in=admin_type_ids).count()
            if Admin_rights > 0:
                return True
            else:
                return False
        if ('/programedits/' in request.path):
            Admin_rights = jt_Program_Admin.objects.filter(user=request.user, program_id=obj.program_id,
                                                           kilnadmintype__in=admin_type_ids).count()
            if Admin_rights > 0:
                return True
            else:
                return False
        # Other write permissions are only allowed if the user is an Admin or Owner of the object.
        owner_type_id = KilnAdminType.objects.filter(kilnadmintype_name__in=('Owner')).values_list('kilnadmintype_id')
        return False