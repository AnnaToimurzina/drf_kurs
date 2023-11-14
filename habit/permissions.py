from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    """
        Пользователи могут редактировать только свои объекты.
        """

    def has_object_permission(self, request, view, obj):
        # Разрешения только для чтения разрешены для любого запроса
        if request.method in permissions.SAFE_METHODS:
            return True

        # Редактирование разрешено только владельцам объекта
        return obj.user == request.user


class ReadOnlyIfPublic(permissions.BasePermission):
    """
    Разрешение на только чтение, если привычка публичная.
    """

    def has_permission(self, request, view):
        # Разрешения на чтение разрешены для любого запроса
        if request.method in permissions.SAFE_METHODS:
            return True

        # Редактирование и удаление разрешено только для администраторов
        return request.user and request.user.is_staff