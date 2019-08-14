from django.db import models

# Create your models here.



class BookInfoManager(models.Manager):
    def get_queryset(self):
        return super(BookInfoManager,self).get_queryset().filter(isDelete=False)
    def create(self,btitle,bpub_date):
        b=BookInfo()
        b.btitle=btitle
        b.bpub_date=bpub_date
        b.bread=0
        b.bcommet=0
        b.isDelete=False
        return b

class BookInfo(models.Model):
    btitle=models.CharField(max_length=20)
    bpub_date=models.DateTimeField(db_column='pub_date')
    bread=models.IntegerField(default=0)
    bcommet=models.IntegerField(default=False)
    isDelete=models.BooleanField(default=False)
    class Meta:
        db_table='bookinfo'
    books1=models.Manager()
    books2=BookInfoManager()
    def __str__(self):
        return self.btitle



class HeroInfo(models.Model):
    hname=models.CharField(max_length=10)
    hgender=models.BooleanField(default=True)
    hcontent=models.CharField(max_length=1000)
    isDelete=models.BooleanField(default=False)
    book=models.ForeignKey(BookInfo,on_delete=models.CASCADE)
    class Meta:
        db_table='heroinfo'
    def __str__(self):
        return self.hname
    m = models.Manager()

'''
class BookInfo(models.Model):
    btitle=models.CharField(max_length=20)
    bpub_date=models.DateTimeField()
    def __str__(self):
        return self.btitle

class HeroInfo(models.Model):
    hname=models.CharField(max_length=10)
    hgender=models.BooleanField()
    hcontent=models.CharField(max_length=1000)
    hbook=models.ForeignKey(BookInfo,on_delete=models.CASCADE)

    def __str__(self):
        return self.hname
 '''

class ContactInfo(models.Model):
    cname=models.CharField(max_length=10)
    ctype=models.CharField(max_length=10)
    cmail=models.CharField(max_length=30)
    cextinfo = models.CharField(max_length=30)
    class Meta:
        db_table='contactinfo'
    def __str__(self):
        return self.cname