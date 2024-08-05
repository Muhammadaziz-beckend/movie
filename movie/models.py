from django.db import models
from django.contrib.auth.models import User

# Кино
class Movie(models.Model):
    vidio_file = models.FileField(verbose_name='Загрузите видео',upload_to='movi_vidio/',)
    title = models.CharField(verbose_name='Названея кино',max_length=120) 
    desctiption = models.TextField(verbose_name='Описания',)
    cauntry = models.ForeignKey(to='Cauntry',verbose_name='Страна производства',related_name='country',on_delete=models.SET_NULL,null=True)
    release_date = models.DateField(verbose_name='Дата выпуска кино',)
    premiere_ru = models.DateField(verbose_name='Премьера (РФ)')
    many = models.PositiveBigIntegerField(verbose_name='Сборы по миру $')
    tegline = models.CharField(verbose_name='Слоган фильма',max_length=25)
    reting = models.FloatField(verbose_name='Рейтинг',max_length=5,default=0)
    genre = models.ManyToManyField(to='Genre',verbose_name='Жанр фильма',related_name='genres',)
    director = models.CharField(verbose_name='Режиссер',max_length=35,)
    writer = models.CharField(verbose_name='Сценарист',max_length=35,)
    producer = models.CharField(verbose_name='Продюсер',max_length=35,)
    age = models.PositiveBigIntegerField(verbose_name='Возрастное ограничение',default=16)
    actors = models.ManyToManyField(to='Actor',verbose_name='Актёры каторые участвовали',)
    
    def __str__(self) -> str:
        return f'{self.title} ({self.release_date})'
    
    class Meta:
        verbose_name = 'Кино'
        verbose_name_plural = 'Кино'

class Poster(models.Model):
    movie = models.ForeignKey(to=Movie,verbose_name='Постер связен',on_delete=models.CASCADE,)
    poster = models.ImageField(upload_to='poster/',verbose_name='Постер филема',)

    def __str__(self) -> str:
        return f'{self.movie__title}'
    
    class Meta:
        verbose_name = 'Постер'
        verbose_name_plural = 'Постеры'

# catigori
    #  director,writer,producer,age

# Жаннер кино
class Genre(models.Model):
    name = models.CharField(verbose_name='Жанр фильма',max_length=50)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = 'Жанр фильма'
        verbose_name_plural = 'Жанры фильмов'

# Отзыв
class Review(models.Model):
    movie = models.ForeignKey(to=Movie,verbose_name='Кино',on_delete=models.CASCADE,) 
    # user = models.ForeignKey(to='',verbose_name='Пользователь который добавил',on_delete=models.CASCADE,null=True)
    user = models.CharField(verbose_name='Имя коментатора',max_length=50)
    like = models.PositiveBigIntegerField(verbose_name='Лайк',default=0)
    dislike = models.PositiveBigIntegerField(verbose_name='Дислайк',default=0)
    catigori_review = models.ForeignKey(to='Catigori_review',verbose_name='Отзыв (ха-й,плохой , нетральный)',related_name='catigori',on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f'{self.movie__titel} Отзыв'
    
    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'

class Catigori_review(models.Model):
    name = models.CharField(("Катигория отзыва"), max_length=50)

    def __str__(self) -> str:
        return f'{self.name} отзыв'
    
    class Meta:
        verbose_name = 'Катигория отзыва'
        verbose_name_plural = 'Катигории отзывов'

# catigoti user

# Актёр
class Actor(models.Model):
    name = models.CharField(verbose_name='Имя',max_length=35)
    career = models.ManyToManyField(to='Career',verbose_name='Карера',related_name='career')
    heght = models.PositiveBigIntegerField(verbose_name='Рост',)
    date_fo_birth = models.DateField(verbose_name='Дата родждения',)
    birthplace = models.ForeignKey(to='Cauntry',verbose_name='Место рождения',on_delete=models.CASCADE,related_name='birthplace')
    genres = models.ManyToManyField(to=Genre,verbose_name='Жанры',related_name='genre')
    total_movis = models.PositiveBigIntegerField(verbose_name='Всего филемов',default=0)
    active_years = models.PositiveIntegerField(verbose_name='Cтаж',)
    movies = models.ManyToManyField(to=Movie,verbose_name='Кино которых учавствовал')
    total_save = models.PositiveBigIntegerField(verbose_name='Количество избранном',default=0)

    def __str__(self) -> str:
        return f'{self.name} актёр'
    
    class Meta:
        verbose_name = 'актёр'
        verbose_name_plural = 'актёры'


class Career(models.Model):
    name = models.CharField(verbose_name=("Карера"), max_length=90)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = 'Карера'
        verbose_name_plural = 'Кареры'


# Фтот актёра
class Photos_actor(models.Model):
    actor = models.ForeignKey(to=Actor,verbose_name='Актёр',related_name='actor',on_delete=models.CASCADE,)
    photo = models.ImageField(upload_to='actor_photo/',verbose_name='Фото')

    def __str__(self) -> str:
        return f'{self.actor__name} актёр'
    
    class Meta:
        verbose_name = 'Фтот актёра'
        verbose_name_plural = 'Фтографии актёрав'

# Стана
class Cauntry(models.Model):
    name = models.CharField(verbose_name=("Страна"), max_length=80)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = 'Страна'
        verbose_name_plural = 'Страны'


# class UserModel(User):
#     User.