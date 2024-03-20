from rest_framework import viewsets
from .permissions import RoleBasedPermissionMixin, HasPermissionByAuthenticatedUserRole


class HospitalGenericViewset(
    RoleBasedPermissionMixin,
    viewsets.GenericViewSet
):
    permission_classes = [HasPermissionByAuthenticatedUserRole, ]