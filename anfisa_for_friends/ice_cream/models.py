from django.db import models

from core.models import PublishedModel


class Category(PublishedModel):
    title = models.CharField(max_length=256, verbose_name='Название')
    slug = models.SlugField(max_length=64, unique=True, verbose_name='Слаг')
    output_order = models.PositiveSmallIntegerField(
        default=100,
        verbose_name='Порядок отображения')

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.title


class Topping(PublishedModel):
    title = models.CharField(max_length=256, verbose_name='Название')
    slug = models.SlugField(max_length=64, unique=True, verbose_name='Слаг')

    class Meta:
        verbose_name = 'топинг'
        verbose_name_plural = 'Топинги'

    def __str__(self):
        return self.title


class Wrapper(PublishedModel):
    title = models.CharField(max_length=256, verbose_name='Название',
                             help_text='Уникальное название обёртки, не более 256 символов')

    class Meta:
        verbose_name = 'обертка'
        verbose_name_plural = 'Обертки'

    def __str__(self):
        return self.title


class IceCream(PublishedModel):
    title = models.CharField(max_length=256, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    wrapper = models.OneToOneField(
        Wrapper,
        on_delete=models.SET_NULL,
        related_name='ice_cream',
        verbose_name='Обертка',
        null=True,
        blank=True,
    )
    output_order = models.PositiveSmallIntegerField(
        default=100,
        verbose_name='Порядок отображения')
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='ice_creams',
        verbose_name='Категория'
    )
    price = models.DecimalField(max_digits=5, decimal_places=2)
    toppings = models.ManyToManyField(Topping, verbose_name='топинги')
    is_on_main = models.BooleanField(default=False, verbose_name='На главную')

    class Meta:
        verbose_name = 'мороженное'
        verbose_name_plural = 'Мороженное'
        ordering = ('output_order', 'title')

    def __str__(self):
        return self.title
