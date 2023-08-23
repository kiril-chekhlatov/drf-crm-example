from django.core.validators import FileExtensionValidator
from django.db import models
from django.db.models import Count, Q

from core.models import ModelTimeTracking
from students.helpers import Contracts, FilePaths, Genders, Statues


class Student(ModelTimeTracking):
    contract_type = models.PositiveSmallIntegerField(
        verbose_name="Contact Type", choices=Contracts.CONTACT_TYPE_CHOICES
    )
    name = models.CharField(verbose_name="Name", max_length=30)
    surname = models.CharField(verbose_name="Surname", max_length=30)
    middle_name = models.CharField(verbose_name="Middle Name", max_length=30)
    birth_of_date = models.DateField(verbose_name="Birth Of Date")
    email = models.EmailField(verbose_name="Email")
    address = models.TextField(verbose_name="Address")
    phone = models.CharField(verbose_name="Phone", max_length=17)
    passport_series = models.CharField(verbose_name="Passport Series", max_length=2)
    passport_number = models.CharField(verbose_name="Passport Number", max_length=7)
    PIN = models.CharField(verbose_name="PIN", max_length=14)
    region = models.ForeignKey(
        to="students.Region", verbose_name="Region", on_delete=models.PROTECT
    )
    authority = models.TextField(verbose_name="Authority")
    major = models.ForeignKey(
        to="students.Major", verbose_name="Major", null=True, on_delete=models.SET_NULL
    )
    gender = models.PositiveSmallIntegerField(
        verbose_name="Gender", choices=Genders.GENDER_CHOICES
    )

    discount = models.BooleanField(verbose_name="Discount")
    percent = models.FloatField(verbose_name="Percent", blank=True, null=True)
    discount_from = models.DateField(
        verbose_name="Discount From", blank=True, null=True
    )
    discount_to = models.DateField(verbose_name="Discount To", blank=True, null=True)

    super_contract = models.BooleanField(verbose_name="Super Contract")
    super_contract_sum = models.PositiveBigIntegerField(
        verbose_name="Super Contract Sum", blank=True, null=True
    )

    passport_document = models.FileField(
        verbose_name="Passport Document",
        upload_to=FilePaths.get_passport_document_path,
        validators=[FileExtensionValidator(allowed_extensions=["pdf", "heif", "hevc"])],
    )
    IELTS_document = models.FileField(
        verbose_name="IELTS Document",
        upload_to=FilePaths.get_IELTS_document_path,
        validators=[FileExtensionValidator(allowed_extensions=["pdf", "heif", "hevc"])],
    )

    contract_document = models.FileField(
        verbose_name="Contract Document",
        upload_to=FilePaths.get_contract_document_path,
        blank=True,
        null=True,
    )
    status = models.PositiveSmallIntegerField(
        verbose_name="Status",
        choices=Statues.STATUS_CHOICES,
        default=Statues.RECENTLY_ADDED,
        blank=True,
    )

    comments = models.ManyToManyField(
        to="students.Comment", verbose_name="Comments", blank=True
    )

    class Meta:
        verbose_name = "Student"
        verbose_name_plural = "Students"

    def __str__(self) -> str:
        return f"(Student ID: {self.id})"

    @staticmethod
    def get_statistics():
        return Student.objects.aggregate(
            all_students=Count("id", distinct=True),
            approved_students=Count(
                "id", filter=Q(status=Statues.ACCEPTED), distinct=True
            ),
            recently_added=Count(
                "id", filter=Q(status=Statues.RECENTLY_ADDED), distinct=True
            ),
            male=Count("id", filter=Q(gender=Genders.MAN), distinct=True),
            female=Count("id", filter=Q(gender=Genders.FEMALE), distinct=True),
        )


class Comment(ModelTimeTracking):
    author = models.ForeignKey(
        verbose_name="Author",
        to="users.AdminUser",
        on_delete=models.SET_NULL,
        null=True,
    )
    title = models.TextField(verbose_name="Title")
    message = models.TextField(verbose_name="Message")

    class Meta:
        verbose_name = "Comment"
        verbose_name_plural = "Comments"

    def __str__(self) -> str:
        return f"(Comment ID: {self.id})"


class Major(ModelTimeTracking):
    name = models.TextField(verbose_name="Name")
    price = models.PositiveBigIntegerField(verbose_name="Price")
    description = models.TextField(verbose_name="Description")

    class Meta:
        verbose_name = "Major"
        verbose_name_plural = "Majors"

    def __str__(self) -> str:
        return f"Major {self.name}"


class Region(ModelTimeTracking):
    name = models.TextField(verbose_name="Name")

    class Meta:
        verbose_name = "Region"
        verbose_name_plural = "Regions"

    def __str__(self) -> str:
        return f"Region {self.name}"
