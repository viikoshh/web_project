from django.db import models
from django.conf import settings
from django.utils import timezone
from django.urls import reverse
from django.template.defaultfilters import truncatewords

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
        self.is_published = True
        self.save()

    def is_publish(self):
        return self.is_published
        #return True if self.published_date else False

    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.id)])

    def get_preview_text(self):
        return truncatewords(self.text, 10)

    class Meta:
        verbose_name = "Запись в блоге"
        verbose_name_plural = "Запись в блоге"

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey('blog.Post',
                             on_delete=models.CASCADE,
                             related_name='comments')
    author = models.CharField(max_length=200)
    text = models.TextField(verbose_name="Комментарий")
    created_date = models.DateTimeField(default=timezone.now,
                                        verbose_name="Одобрен?")
    approved_comments = models.BooleanField(default=False,
                                            verbose_name="Одобрен?")

    def approve(self):
        self.approved_comments = True
        self.save()

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарий"
