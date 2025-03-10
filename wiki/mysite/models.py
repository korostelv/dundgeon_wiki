from django.db import models
from django.urls import reverse


class Race(models.Model):
    name = models.CharField(max_length=20, blank=False, null=True, verbose_name='Раса')

    class Meta:
        verbose_name = "Раса"
        verbose_name_plural = "Расы"

    def get_absolute_url(self):
        return reverse('mysite:personages_filter',kwargs={'pk': self.pk})

    def __str__(self):
        return self.name


class Personage(models.Model):
    name = models.CharField(max_length=30, blank=False, null=True, verbose_name='Имя персонажа')
    race = models.ForeignKey('Race', blank=True, null=True, on_delete=models.CASCADE, verbose_name='Раса')
    description = models.TextField(blank=True, null=True, verbose_name='Описание')
    power = models.IntegerField(blank=False, null=True, verbose_name='Сила')
    dexterity = models.IntegerField(blank=False, null=True, verbose_name='Ловкость')
    endurance = models.IntegerField(blank=False, null=True, verbose_name='Выносливость')
    wisdom = models.IntegerField(blank=False, null=True, verbose_name='Мудрость')
    intellect = models.IntegerField(blank=False, null=True, verbose_name='Интеллект')
    charisma = models.IntegerField(blank=False, null=True, verbose_name='Харизма')
    gamer = models.ForeignKey('Gamer', blank=True, null=True, on_delete=models.CASCADE, verbose_name='Игрок',
                              related_name='personages_list')
    image = models.ImageField(upload_to='personages', blank=True, null=True, verbose_name='Изображение персонажа')

    class Meta:
        verbose_name = "Персонаж"
        verbose_name_plural = "Персонажи"

    def get_absolute_url(self):
        return reverse('mysite:personage_detail',kwargs={'pk': self.pk})

    def __str__(self):
        return self.name


class Gamer(models.Model):
    name = models.CharField(max_length=40, blank=False, verbose_name='Имя игрока')
    personages = models.ManyToManyField('Personage', blank=True, verbose_name='Персонажи', related_name='gamers')
    image = models.ImageField(upload_to='gamers', blank=True, null=True, verbose_name='Фото игрока')

    class Meta:
        verbose_name = "Игрок"
        verbose_name_plural = "Игроки"

    def get_absolute_url(self):
        return reverse('mysite:gamer_detail',kwargs={'pk': self.pk})

    def __str__(self):
        return self.name

    def display_personages(self):
        return ", ".join([personage.name for personage in self.personages.all()])

    display_personages.short_description = 'Персонажи'


class Storyline(models.Model):
    line = models.CharField(max_length=50, blank=False, verbose_name='Сюжетная линия')

    class Meta:
        verbose_name = "Сюжетная линия"
        verbose_name_plural = "Сюжетные линии"

    def get_absolute_url(self):
        return reverse('mysite:releases_filter',kwargs={'pk': self.pk})

    def __str__(self):
        return self.line


class Release(models.Model):
    number = models.IntegerField(blank=False, verbose_name='Номер выпуска')
    title = models.CharField(max_length=50, blank=False, verbose_name='Название выпуска')
    annotation = models.TextField(blank=True, verbose_name='Аннотация')
    gamers = models.ManyToManyField('Gamer', verbose_name='Игроки')
    personages = models.ManyToManyField('Personage', verbose_name='Персонажи')
    line = models.ForeignKey('Storyline', blank=True, null=True, on_delete=models.CASCADE,
                             verbose_name='Сюжетная линия')
    url = models.URLField(max_length=150, blank=True, verbose_name='Ссылка')
    image = models.ImageField(upload_to='releases', blank=True, null=True, verbose_name='Афиша')
    created_at = models.DateTimeField(auto_now_add=True,null=True, verbose_name="Дата создания")

    class Meta:
        verbose_name = "Выпуск"
        verbose_name_plural = "Выпуски"

    def get_absolute_url(self):
        return reverse('mysite:release_detail',kwargs={'pk': self.pk})

    def __str__(self):
        return f'{self.number}. {self.title}'

    def display_gamers(self):
        return ", ".join([gamer.name for gamer in self.gamers.all()])

    def display_personages(self):
        return ", ".join([personage.name for personage in self.personages.all()])

    display_gamers.short_description = 'Игроки'
    display_personages.short_description = 'Персонажи'


def picture_upload_to(instance, filename):
    if instance.personage is not None and instance.personage.name:
        return f'gallery/{instance.personage.name}/{filename}'
    elif instance.release is not None and instance.release.title:
        return f'gallery/{instance.release.title}/{filename}'
    return f'gallery/unknown/{filename}'


class Picture(models.Model):
    personage = models.ForeignKey('Personage',  blank=True,null=True, on_delete=models.CASCADE,verbose_name='Персонаж' )
    release = models.ForeignKey('Release',  blank=False,null=True, on_delete=models.CASCADE,verbose_name='Выпуск' )
    image = models.ImageField(upload_to=picture_upload_to, blank=False, null=True, verbose_name='Рисунок')
    title = models.CharField(max_length=50, blank=True, verbose_name='Описание фото')
    in_release = models.BooleanField(default=False, verbose_name='Показывать в выпусках')

    class Meta:
        verbose_name = "Рисунок"
        verbose_name_plural = "Рисунки"

    def __str__(self):
        return self.title
