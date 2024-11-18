from rest_framework import permissions

from rest_framework import permissions

class IsOwnerOrAdmin(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # Check if the object is a Loan and the user is the owner or admin
        if hasattr(obj, 'user'):
            return obj.user == request.user or request.user.is_staff
        
        # Check if the object is a Repayment and the user is the owner of the related loan
        if hasattr(obj, 'loan') and hasattr(obj.loan, 'user'):
            return obj.loan.user == request.user or request.user.is_staff
        
        return False

