from faker import Factory
import factory
from factory import Sequence
from core import models

factory_ru = Factory.create('ru-Ru')


class ProductCategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.ProductCategory

    name = Sequence(lambda n: f"Category {n}")
    description = factory_ru.text()


class ProductFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Product

    name = Sequence(lambda n: f"Product {n}")
    description = factory_ru.text()
    price = Sequence(lambda n: n * 10)
    category = factory.SubFactory(ProductCategoryFactory)


class ClientFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Client

    name = factory_ru.name()
    email = factory_ru.email()
    phone = factory_ru.phone_number()



