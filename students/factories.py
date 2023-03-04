import factory
from factory import fuzzy
from students.helpers import Genders, Contracts
from django.core.files.base import ContentFile
import datetime

from students.models import Student, Comment, Major, Region
from users.factories import AdminUserFactory


class CommentFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Comment

    author = factory.SubFactory(AdminUserFactory)
    title = factory.Sequence(lambda n: 'title %d' % n)
    message = factory.Sequence(lambda n: 'message %d' % n)


class MajorFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Major

    name = factory.Sequence(lambda n: 'name %d' % n)
    price = fuzzy.FuzzyInteger(low=1)
    description = factory.Sequence(lambda n: 'description %d' % n)


class RegionFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Region

    name = factory.Sequence(lambda n: 'name %d' % n)


class StudentFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Student

    contract_type = fuzzy.FuzzyInteger(
        low=1, high=len(Contracts.CONTACT_TYPE_CHOICES))
    name = factory.Faker('name')
    surname = factory.Faker('name')
    middle_name = factory.Faker('name')
    birth_of_date = fuzzy.FuzzyDate(datetime.date.today())
    email = factory.Faker('email')
    address = factory.Faker('address')
    phone = '+998919191919'
    passport_series = 'QQ'
    passport_number = fuzzy.FuzzyInteger(low=1)
    PIN = '21312312'
    region = factory.SubFactory(RegionFactory)
    authority = factory.Faker('address')
    major = factory.SubFactory(MajorFactory)
    gender = fuzzy.FuzzyInteger(low=1, high=len(Genders.GENDER_CHOICES))
    discount = True
    percent = fuzzy.FuzzyFloat(low=1)
    discount_from = fuzzy.FuzzyDate(datetime.date.today())
    discount_to = factory.LazyAttribute(
        lambda o: o.discount_from + datetime.timedelta(days=2)
    )
    super_contract = True
    super_contract_sum = fuzzy.FuzzyInteger(low=1)
    passport_document = factory.LazyAttribute(
        lambda _: ContentFile(b'...', name="passport_document.pdf")
    )
    IELTS_document = factory.LazyAttribute(
        lambda _: ContentFile(b'...', name="IELTS_document.pdf")
    )
    status = 1
    # comments = factory.SubFactory(CommentFactory)
