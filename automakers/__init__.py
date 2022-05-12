from cars.models import CarModel
from owners.models import OwnerModel
from users.models import UserModel
import uuid
import factory
from faker import Faker
from factory.django import DjangoModelFactory


fake = Faker('pt_BR')

class OwnerFactory(DjangoModelFactory):
    class Meta:
        model = OwnerModel

    name = factory.LazyAttribute(lambda x: fake.name())
    doc_number = factory.LazyAttribute(lambda x: fake.company_id())


class CarFactory(DjangoModelFactory):
    class Meta:
        model = CarModel
    
    owner = OwnerModel()
    color = "Y"
    car_model = "SE"


class UserFactory(DjangoModelFactory):
    class Meta:
        model = UserModel

    username = factory.LazyAttribute(lambda x: fake.name())
    password = factory.LazyAttribute(lambda x: fake.password())
