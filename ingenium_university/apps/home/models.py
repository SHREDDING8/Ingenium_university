from colorfield.fields import ColorField
from django.core.files.storage import default_storage
from django.db import models
from django.db.models.signals import pre_delete
from django.dispatch import receiver


# Create your models here.
class LendingHome(models.Model):
    name = models.CharField(max_length=50, help_text='имя',
                            verbose_name="имя", )
    phone = models.CharField(max_length=12, help_text='телефон',
                             verbose_name="телефон", )
    email = models.EmailField(help_text='email',
                              verbose_name="email", )
    date = models.DateTimeField(auto_now=True, help_text='дата',
                                verbose_name="дата", )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Лендинг'
        verbose_name_plural = 'Лендинг'


class Course(models.Model):
    type_study_list = (
        ('Profession', 'Profession'),
        ('Profession', 'Course')
    )
    lvl_hard_list = (
        ("Easy", 'Easy'),
        ("Hard", 'Hard')
    )

    direction = models.ForeignKey('Direction', on_delete=models.PROTECT, help_text='Выбери направление',
                                  verbose_name='Направление')
    # color_direction = ColorField(default='#4d4d4d', max_length=7,
    #                              help_text='Введи цвет текста направления. Например: #4d4d4d',
    #                              verbose_name="Цвет текста направления")

    name = models.CharField(max_length=100,
                            help_text='Название курса',
                            verbose_name="Название курса")
    name_2 = models.CharField(max_length=100,
                              help_text='Вторая строка названия курса',
                              verbose_name="Название курса вторая строка", null=True, blank=True)
    image_course = models.ImageField(verbose_name='Картинка для курса', help_text='Выбери картинку для курса',
                                     upload_to='courses_images')
    how_long = models.CharField(max_length=50, help_text='Введи длительность курса. Например: 3 месяца',
                                verbose_name="Длительность курса")
    min_price = models.BigIntegerField(help_text='Введи минимкльную цену. Например: 1990',
                                       verbose_name='Минимальная цена', default=1990)
    standart_price = models.BigIntegerField(help_text='Введи цену стандартного курса. Например: 4990',
                                            verbose_name='Стандартная цена', default=4990)
    vip_price = models.BigIntegerField(help_text='Введи  VIP цену. Например: 9490',
                                       verbose_name='VIP цена', default=9490)

    type_study = models.CharField(verbose_name='Тип обучения', max_length=50, choices=type_study_list)
    lvl_hard = models.CharField(verbose_name='Уровень сложности', max_length=50, choices=lvl_hard_list)
    background_color = ColorField(default='#fff', max_length=7, help_text='Введи цвет фона курса. Например: #b4e682',
                                  verbose_name="Фоновый Цвет курса")
    color_2 = ColorField(default='#fff', max_length=7, help_text='второй цвет', verbose_name="второй Цвет курса")
    # text_color = ColorField(default='#000', max_length=7, help_text='Введи цвет текста. Например: #b4e682',
    #                         verbose_name="Цвет текста")

    teachers = models.ManyToManyField('Teacher', related_name='courses')

    search_keys = models.TextField(verbose_name="Ключи для поиска", )
    recommend = models.BooleanField(verbose_name='Рекомендовано?', default=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'


# class CourseRecommend(models.Model):
#     course = models.ForeignKey(Course, on_delete=models.PROTECT, null=True, help_text='Выбери рекомендованный курс',
#                                verbose_name='рекомендованный курс')
#
#     def __str__(self):
#         return self.course.name
#
#     class Meta:
#         verbose_name = 'Рекомендованный курс'
#         verbose_name_plural = 'Рекомендованные курсы'


class Direction(models.Model):
    name = models.CharField(max_length=100,
                            help_text='Название направления',
                            verbose_name="Название направления")
    name_English = models.CharField(max_length=100,
                                    help_text='Название направления на английском языке',
                                    verbose_name="Название направления  на английском языке", unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Направление'
        verbose_name_plural = 'Направления'


# about

class Teacher(models.Model):
    first_name = models.CharField(max_length=150, verbose_name="Имя")
    second_name = models.CharField(max_length=150, verbose_name="Фамилия")
    profession = models.CharField(max_length=300, verbose_name="Профессия")
    photo = models.ImageField(upload_to='teachers', verbose_name='Фотография',
                              help_text='Желательно загружать изображения в соотношении 1:1')

    def __str__(self):
        r = self.first_name + " " + self.second_name
        return r

    class Meta:
        verbose_name = 'Преподаватель'
        verbose_name_plural = 'Преподаватели'


class Review(models.Model):
    first_name = models.CharField(max_length=50, verbose_name="Имя", default='Гость')
    second_name = models.CharField(max_length=150, verbose_name="Фамилия", blank=True)
    photo = models.ImageField(upload_to='Reviews/%Y.%M.%D', blank=True)
    review = models.TextField(verbose_name="Отзыв")
    date = models.DateTimeField(verbose_name='Время добавления', auto_now_add=True)

    def __str__(self):
        r = self.first_name + " " + self.second_name
        return r

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
        ordering = ['-date']


class Webinar(models.Model):
    name = models.CharField(max_length=200, verbose_name="Название")
    direction = models.ForeignKey(Direction, verbose_name='Направление', on_delete=models.PROTECT)
    teacher = models.ForeignKey(Teacher, on_delete=models.PROTECT, verbose_name='Учитель')
    datetime = models.DateTimeField(verbose_name='Дата и время')
    link = models.CharField(max_length=200, verbose_name='Ссылка', null=True, blank=True)
    description = models.TextField(verbose_name='Описание',null=True)
    files = models.CharField(max_length=500,verbose_name='Ссылка на файлы',help_text='Ссылка на облачное хранилище с файлами для вебинара',null=True,blank=True)
    color = ColorField(verbose_name='Фон')
    color_2 = ColorField(verbose_name='Цвет текста')
    photo_preview = models.ImageField(verbose_name='Фото preview', upload_to='webinars_photo_preview')
    recommend = models.BooleanField(verbose_name='Рекомендовано?', default=False)
    published = models.BooleanField(verbose_name='Доступно пользователям?', default=False)

    kol_prosm = models.BigIntegerField(verbose_name='Количество просмотров', default=0)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Вебинар'
        verbose_name_plural = 'Вебинары'
        ordering = ['-datetime']


# pre delete

# @receiver(pre_delete, sender=Teacher)
# def delete_photo(sender, instance, **kwargs):
#     path_photo = instance.photo.name
#     if path_photo:
#         default_storage.delete(path_photo)
#
#
# @receiver(pre_delete, sender=Webinar)
# def delete_photo(sender, instance, **kwargs):
#     path_photo = instance.photo_preview.name
#     if path_photo:
#         default_storage.delete(path_photo)
#
# #
# # @receiver(pre_delete, sender=Review)
# # def delete_photo(sender, instance, **kwargs):
# #     path_photo = instance.photo_preview.name
# #     if path_photo:
# #         default_storage.delete(path_photo)
# #
# #
# # @receiver(pre_delete, sender=Course)
# # def delete_photo(sender, instance, **kwargs):
# #     path_photo = instance.image_course.name
# #     if path_photo:
# #         default_storage.delete(path_photo)
