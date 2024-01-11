from django.db import models
from datetime import datetime

class Review(models.Model):
    author = models.CharField(max_length=100)
    content = models.TextField()
    rating = models.IntegerField(choices=[(i,i) for i in range(1,6)])
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.author





class Zaved(models.Model):
    name = models.CharField("Название", max_length=100)

    kitchen = models.TextField("Кухня")
    avr_cost = models.TextField("Средний счет")
    count_people = models.TextField("Количество мест")
    have = models.TextField("Есть в зале")
    desc_zal = models.TextField('Описание зала')
    music = models.TextField('Музыка')
    children = models.TextField('Что есть для Детей')
    parking = models.TextField('Парковка')
    time_work = models.TextField("Время работы")
    adress = models.TextField('Адрес')

    #contact info
    telephone = models.TextField('номер телефона (если нет -)')
    whatsapp = models.TextField('Ватцап номер (если нет -)')
    sotial = models.TextField('Социальная сеть (если нет -)')
    site_adress = models.TextField('Веб сайт ресторана (если нет -)')

    more_desc = models.TextField('Полное описание заведения')


    # description = models.TextField("Описание")
    type = models.TextField("Тип заведения")
    #image = models.ImageField("Изображение", upload_to="ZavIMG/", default=0)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Заведение"
        verbose_name_plural = "Заведения"


class rating(models.Model):
    zaved = models.ForeignKey(Zaved, related_name='reting', on_delete=models.CASCADE)

    author = models.CharField(max_length=100)
    bis = models.TextField()

    content = models.TextField()
    is_good = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)


class MenuPhotos(models.Model):
    zaved = models.ForeignKey(Zaved, related_name ='menu_photos', on_delete=models.CASCADE)

    photos = models.ImageField("Меню",upload_to = "ZavIMG/Menu/")





class bookingTableZaved(models.Model):
    zaved = models.ForeignKey(Zaved,related_name='booking',on_delete=models.CASCADE)
    number_tabel = models.IntegerField("Номер столика")
    deposit_table = models.IntegerField("Депозит стола")
    date = models.DateField('Дата брони стола')
    time = models.TimeField("Время брони стола")




class ZavedSchema(models.Model):
    zaved = models.ForeignKey(Zaved,related_name='schema', on_delete=models.CASCADE)
    schemaPhoto = models.ImageField("Схема зала",upload_to = "ZavIMG/Schema/")

    class Meta:
        verbose_name = "Схема зала"
        verbose_name_plural = "Схемы зала"



class Auth(models.Model):

    login = models.TextField('Логин')
    password = models.TextField('Пароль')
    name = models.TextField("Имя", default='noname')
    # book = models.ForeignKey(bookingTable, related_name='book', on_delete=models.CASCADE, null=True)

class bookingTable(models.Model):

    zaved = models.ForeignKey(Zaved, related_name='booking_table', on_delete=models.CASCADE)
    date_t = models.DateField("Выбор даты")
    time_t = models.TextField("Время")
    count_g = models.IntegerField("Количество гостей")
    disc = models.TextField("Пожелания к брони")

    auth = models.ForeignKey(Auth, related_name='auth', on_delete=models.CASCADE, null=True)

    class Meta:
        verbose_name = "Бронь столов"
        verbose_name_plural = "бронирование стола"


class Zaved_menu(models.Model):
    zaved = models.ForeignKey(Zaved, related_name='menu', on_delete= models.CASCADE)
    text_menu = models.TextField ("Меню")

class ZavedImage(models.Model):
    zaved = models.ForeignKey(Zaved, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField("Изображение", upload_to="ZavIMG/")

    def __str__(self):
        return f"Изображение для {self.zaved.name}"

    class Meta:
        verbose_name = "Изображение Заведения"
        verbose_name_plural = "Изображения Заведения"



class Menu(models.Model):
    name = models.CharField('Название Блюда', max_length=150)
    description = models.TextField("Описание блюда")
    price = models.PositiveSmallIntegerField("Цена блюда", default=0)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Меню и блюдо"
        verbose_name_plural = "Меню и блюда"


