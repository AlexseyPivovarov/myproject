from django.db import models


# Create your models here.
class Category(models.Model):
    category_name = models.CharField(max_length = 20, blank=False, verbose_name=u'category name')
    # category_image = models.ImageField(upload_to='categor/', max_length=100, default='images/No-image.jpg')

    def __str__(self):
        return self.category_name


# def user_directory_path(instance, filename):
#     # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
#     return 'user_{0}/{1}'.format(instance.user.id, filename)


class Product(models.Model):
    DELETED = 0
    TO_MODERETION = 1
    ACTIVE = 2
    MODERATING = (
        (DELETED, 'Deleted'),
        (TO_MODERETION, 'To moderation'),
        (ACTIVE, 'Active')
    )

    STANDART = 0
    VIP = 1
    TO_VIP = (
        (STANDART, 'Standart'),
        (VIP, 'VIP')
    )

    VIP_MODER = (
        (STANDART, 'OK'),
        (VIP, 'Want VIP')
    )

    product_category = models.ForeignKey('Category', on_delete=models.DO_NOTHING, verbose_name=u'category')
    product_name = models.CharField(max_length=20, blank=False, verbose_name=u'name')
    product_image = models.ImageField(verbose_name=u'foto', default='images/No-image.jpg')
    product_info = models.TextField(verbose_name=u'info')
    product_price = models.PositiveIntegerField(verbose_name=u'price')
    product_status = models.IntegerField(choices=MODERATING, default=TO_MODERETION, verbose_name=u'status')
    product_vip = models.IntegerField(choices=TO_VIP, default=STANDART, verbose_name=u'VIP status')
    product_vip_moderation = models.IntegerField(choices=VIP_MODER, default=STANDART, verbose_name=u'VIP moderation')
    product_datatime_creation = models.DateTimeField(verbose_name=u'Created', auto_now_add=True)

    def __str__(self):
        return self.product_name