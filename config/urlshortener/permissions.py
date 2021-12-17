from rest_framework import permissions


class IsPremiumClient(permissions.BasePermission):
    """
    Allows access only to users who has PREMIUM_CLIENT status.
    """

    def has_permission(self, request, view) -> bool:
        return bool(request.user and request.user.is_premium_client)
