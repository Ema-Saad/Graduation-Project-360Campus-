from rest_framework.permissions import BasePermission

class IsProfessor(BasePermission):

    def has_permission(self, req, view):
        return req.user.person_type == 'P'

