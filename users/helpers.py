from uuid import uuid4


class Roles(object):
    ADMIN = 1
    MARKETING_ADMIN = 2
    RECTOR_ADMIN = 3

    ROLE_CHOICES = (
        (ADMIN, 'Admin'),
        (MARKETING_ADMIN, 'Marketing admin'),
        (RECTOR_ADMIN, 'Rector admin')
    )


class FilePaths(object):

    def get_photo_path(instance, filename):
        extension = filename.split('.')[-1]
        return f"protected_files/user_admin_photos/{uuid4()}.{extension}"
