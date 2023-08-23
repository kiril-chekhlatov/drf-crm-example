from uuid import uuid4


class Genders(object):
    MAN = 1
    FEMALE = 2

    GENDER_CHOICES = ((MAN, "Man"), (FEMALE, "Female"))


class Contracts(object):
    TYPE_B = 1
    TYPE_BG = 2
    TYPE_M = 3
    TYPE_MG = 4

    CONTACT_TYPE_CHOICES = (
        (TYPE_B, "B"),
        (TYPE_BG, "BG"),
        (TYPE_M, "M"),
        (TYPE_MG, "MG"),
    )


class Statues(object):
    RECENTLY_ADDED = 1
    MARKETING_CONSIDERATION = 2
    RECTOR_CONSIDERATION = 3
    ACCEPTED = 4
    NOT_ACCEPTED = 5
    DELETED = 6

    STATUS_CHOICES = (
        (RECENTLY_ADDED, "Recently Added"),
        (MARKETING_CONSIDERATION, "For consideration from marketing admin"),
        (RECTOR_CONSIDERATION, "For consideration from rector admin"),
        (ACCEPTED, "Accepted"),
        (NOT_ACCEPTED, "Not accepted"),
        (DELETED, "Deleted"),
    )


class FilePaths(object):
    def get_passport_document_path(instance, filename):
        extension = filename.split(".")[-1]
        return f"protected_files/passports/{uuid4()}.{extension}"

    def get_IELTS_document_path(instance, filename):
        extension = filename.split(".")[-1]
        return f"protected_files/IELTS/{uuid4()}.{extension}"

    def get_contract_document_path(instance, filename):
        extension = filename.split(".")[-1]
        return f"protected_files/contracts/{uuid4()}.{extension}"
