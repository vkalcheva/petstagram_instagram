import datetime

from django.contrib.auth import get_user_model
from django.db import models

UserModel = get_user_model()

class Pet(models.Model):
    CAT = 'Cat'
    DOG = 'Dog'
    BUNNY = 'Bunny'
    PARROT = 'Parrot'
    FISH = 'Fish'
    OTHER = 'Other'

    TYPES = [(x, x) for x in (CAT, DOG, BUNNY, PARROT, FISH, OTHER)]

    NAME_MAX_LENGTH = 30

    # MIN_DATE = datetime.date(1920, 1, 1)

    name = models.CharField(
        max_length=NAME_MAX_LENGTH,
    )
    type = models.CharField(
        max_length=max(len(x) for (x, _) in TYPES),
        choices=TYPES,

    )
    date_of_birth = models.DateField(
        null=True,
        blank=True,
        # validators=MinDateValidator(),
    )
    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
    )

    @property
    def age(self):
        return datetime.datetime.now().year - self.date_of_birth.year

    class Meta:
        unique_together = ('user', 'name')


class PetPhoto(models.Model):
    photo = models.ImageField(
        # validators=ValidateMaxSizeInMB(5),

    )

    description = models.TextField(
        null=True,
        blank=True,
    )
    publication_date = models.DateTimeField(
        auto_now_add=True,
    )
    likes = models.IntegerField(
        default=0,
    )

    tagged_pets = models.ManyToManyField(
        Pet,
    )
    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
    )