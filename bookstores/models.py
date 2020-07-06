from django.db import models

class Bookstores(models.Model):
    bookstoreID = models.AutoField(verbose_name='서점 ID', primary_key=True)
    bookstoreName = models.CharField(verbose_name='서점 이름', max_length=20)
    bookstoreExp = models.TextField(verbose_name='서점 정보')
    bookstoreAddress = models.CharField(verbose_name='서점 주소', max_length=200)
    bookstoreTel = models.PhoneNumberField(verbose_name='서점 연락처', blank=True)
    bookstorePic = models.ImageField(verbose_name='서점 이미지', blank=True)

    def __str__(self):
        return self.bookstoreName
    