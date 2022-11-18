from django.db import models
from django.db.models import Model, Manager, QuerySet, Q
from django.utils import timezone


class PostQuerySet(QuerySet):
    def for_user(self, user=None):
        if user.is_staff:
            return self.all()
        elif user.is_authenticated:
            return self.filter(
                Q(published_date_lte=timezone.now() | Q(author=user))
            )
        else:
            return self.filter(published_date_lte=timezone.now())


class PostManager(Manager):
    def get_queryset(self):
        return PostQuerySet(self.model, using=self._db)

    def for_user(self, user=None):
        return self.get_queryset().for_user(user=user)


class PostPublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_quetyset().filter(
            published_date_lte=timezone.now())