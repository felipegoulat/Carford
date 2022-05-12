from django.db import models
from owners.models import OwnerModel
from django.utils.translation import gettext_lazy as _


class CarsType(models.TextChoices):
    SEDAN = 'SE', _('Sedan Model')
    CONVERTIBLE = 'CO', _('Convertible Model')
    HATCH = 'HA', _('Hatch Model')


class CarsColors(models.TextChoices):
        YELLOW = 'Y', _('Yellow Color')
        BLUE = 'B', _('Blue Color')
        GREY = 'G', _('Grey Color')


class CarModel(models.Model):
    car_model = models.CharField(
        max_length=2,
        choices=CarsType.choices
    )

    color = models.CharField(
        max_length=1,
        choices=CarsColors.choices
    )


    owner = models.ForeignKey(OwnerModel, models.CASCADE)