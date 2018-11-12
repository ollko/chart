from django.db import models
from django.db.models.signals import pre_save

from .utils import unique_slug_generator


YEARS   =   (
                ('2017', 2017,),('2018', 2018,),('2019', 2019,),('2020', 2020,),('2021', 2021,),
                ('2022', 2022,),('2023', 2023,),('2024', 2024,),('2025', 2025,),('2026', 2026,),
                ('2027', 2027,),('2028', 2028,),('2029', 2029,),('2030', 2030,),('2031', 2031,),
                ('2032', 2032,),('2033', 2033,),('2034', 2034,),('2035', 2035,),('2036', 2036,),
                ('2037', 2037,),('2038', 2038,),('2039', 2039,),('2040', 2040,),('2041', 2041,),
                ('2042', 2042,),('2043', 2043,),('2044', 2044,),('2045', 2045,),('2046', 2046,),
                ('2047', 2047,),('2048', 2048,),('2049', 2049,),('2050', 2050,),('2051', 2051,),
                ('2052', 2052,),('2053', 2053,),('2054', 2054,),
)

class Loko(models.Model):
    name = models.CharField("Серия локомотива", max_length=30)
    slug = models.SlugField(max_length=30, db_index=True, default='page-slug', blank=True)
    rate = models.DecimalField("Ставка за км", max_digits=10, decimal_places=2,)
    
    def __str__(self):              # __unicode__ on Python 2
        return self.name

    class Meta:
        ordering = ('name',)
        verbose_name = 'Локомотив'
        verbose_name_plural = 'Локомотивы со ставками за км'


class Filial(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, db_index=True, default='page-slug', blank=True)


    def __str__(self):              # __unicode__ on Python 2
        return self.name

    class Meta:
        ordering = ('name',)
        verbose_name = 'Филиал'
        verbose_name_plural = 'Филиалы'


class Mileage(models.Model):
    filial  = models.ForeignKey(Filial, on_delete=models.CASCADE, verbose_name=u"Филиал",)
    year = models.CharField('Год пробега', choices = YEARS, max_length=10,)
    loko    = models.ForeignKey(Loko, on_delete=models.CASCADE, verbose_name=u"Серия локомотива",)
    mileage = models.IntegerField("Пробег в км",)

    def __str__(self):              # __unicode__ on Python 2
        return 'Регион - {}, марка локомотива - {}, год - {} '.format(self.filial, self.loko, str(self.year))

    class Meta:
        ordering = ('year',)
        verbose_name = 'Пробег'
        verbose_name_plural = 'Пробеги'


def pre_save_receiver_page_model(sender, instance, *args, **kwargs):
    if instance.slug == 'page-slug' or instance.slug == '':
        instance.slug = unique_slug_generator(instance)

pre_save.connect(pre_save_receiver_page_model, sender=Loko)
pre_save.connect(pre_save_receiver_page_model, sender=Filial)