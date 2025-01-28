from django.db import models

class Race(models.Model):
    name = models.CharField(max_length=20, blank=False, null=True, verbose_name='Раса')

    def __str__(self):
        return self.name




class Personage(models.Model):
    name = models.CharField(max_length=30, blank=False,null=True, verbose_name='Имя персонажа')
    race = models.ForeignKey('Race', blank=True, null=True, on_delete=models.CASCADE, verbose_name='Раса')
    description = models.TextField(blank=False,null=True, verbose_name='Описание')
    power = models.IntegerField( blank=False,null=True, verbose_name='Сила')
    dexterity = models.IntegerField( blank=False,null=True, verbose_name='Ловкость')
    endurance = models.IntegerField(blank=False,null=True, verbose_name='Выносливость')
    wisdom = models.IntegerField( blank=False,null=True, verbose_name='Мудрость')
    intellect = models.IntegerField(blank=False,null=True, verbose_name='Интеллект')
    charisma= models.IntegerField(blank=False,null=True, verbose_name='Харизма')
    image = models.ImageField(upload_to='personages', blank=True, null=True, verbose_name='Изображение персонажа')

    def __str__(self):
        return self.name


class Gamer(models.Model):
    name = models.CharField(max_length=40, blank=False, verbose_name='Имя игрока')
    personages = models.ManyToManyField('Personage', verbose_name='Персонажи')
    image = models.ImageField(upload_to='gamers', blank=True, null=True, verbose_name='Фото игрока')

    def __str__(self):
        return self.name

    def display_personages(self):
        return ", ".join([personage.name for personage in self.personages.all()])

    display_personages.short_description = 'Персонажи'


class Storyline(models.Model):
    line = models.CharField(max_length=50,blank=False, verbose_name='Сюжетная линия')

    def __str__(self):
        return self.line


class Release(models.Model):
    number = models.IntegerField(blank=False, verbose_name='Номер выпуска')
    title = models.CharField(max_length=50, blank=False, verbose_name='Название выпуска')
    gamers = models.ManyToManyField('Gamer', verbose_name='Игроки')
    personages = models.ManyToManyField('Personage', verbose_name='Персонажи')
    line = models.ForeignKey('StoryLine', blank=True, null=True, on_delete=models.CASCADE, verbose_name='Сюжетная линия')
    url = models.URLField(max_length=150, blank=False, verbose_name='Ссылка')
    image = models.ImageField(upload_to='releases', blank=True, null=True, verbose_name='Афиша')

    def __str__(self):
        return f'{self.number}. {self.title}'

    def display_gamers(self):
        return ", ".join([gamer.name for gamer in self.gamers.all()])

    def display_personages(self):
        return ", ".join([personage.name for personage in self.personages.all()])

    display_gamers.short_description = 'Игроки'
    display_personages.short_description = 'Персонажи'


