from django.db import models
from django.conf import settings
from django.utils import timezone
from django.urls import reverse

from .managers import PostPublishedManager, PostManager


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL,
                               on_delete=models.CASCADE)
    title = models.CharField(max_length=200, verbose_name="Заголовок")
    text = models.CharField(max_length=400, verbose_name="Текст статьи")
    created_date = models.DateTimeField(default=timezone.now,
                                        verbose_name="Дата создания")
    published_date = models.DateTimeField(blank=True,
                                          null=True,
                                          verbose_name="Дата публикации")
    is_published = models.BooleanField(default=False,
                                       verbose_name="Запись опубликована?")

    objects = PostManager()
    published = PostPublishedManager()

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def is_publish(self):
        return True if self.published_date else False

    #def get_absolute_url(self):
    #    return reverse('post_detail', args=[str(self.id)])


    class Meta:
        verbose_name = "Запись в блоге"
        verbose_name_plural = "Запись в блоге"


    def __str__(self):
        return self.title