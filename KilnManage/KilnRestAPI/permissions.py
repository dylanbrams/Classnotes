from rest_framework import permissions
from KilnData.models import jt_Kiln_Admin, jt_Program_Admin, KilnAdminType

class CanViewModifyObject(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """

    def has_object_permission(self, request, view, obj):
        """
        This permissions subclass checks whether the user has rights to perform certain functions on an object.
        It's very wordy for what it does, and should be refactored to fill a dictionary then check for rights to
        the given entry point.  For real efficiency combining the queries into one query is a good idea.
        
        That said, none of this really matters much except that it's mediocre programming.
        :param request: 
        :param view: 
        :param obj: 
        :return: 
        """
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        # Modifying Administration / Ownership is only allowed if the user is Owner of the object.
        admin_type_ids = KilnAdminType.objects.filter(kilnadmintype_name__in=('Owner', 'Manager'))\
            .values_list('kilnadmintype_id')
        if ('/kilnedits/' in request.path):
            return (jt_Kiln_Admin.objects.filter(user=request.user, kiln_id=obj.kiln_id,
                                                 kilnadmintype__in=admin_type_ids).count() > 0)
        if ('/programedits/' in request.path):
            return (jt_Program_Admin.objects.filter(user=request.user, program_id=obj.program_id,
                                                           kilnadmintype__in=admin_type_ids).count() > 0)

        # Changing permissions are only allowed if the user is Owner of the object.xxx
        owner_type_id = KilnAdminType.objects.filter(kilnadmintype_name__in=('Owner')).values_list('kilnadmintype_id')
        if ('/kilnadminedits/' in request.path):
            return (jt_Kiln_Admin.objects.filter(user=request.user, kiln_id=obj.kiln_id,
                                                        kilnadmintype__in=owner_type_id).count > 0)
        if ('/programadminedits/' in request.path):
            return (jt_Program_Admin.objects.filter(user=request.user, program_id=obj.kiln_id,
                                                        kilnadmintype__in=owner_type_id).count > 0)
        return False

