from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Person(models.Model):
	user = models.CharField(max_length=20, unique=True)
	pwd = models.CharField(max_length=20)
	first_name = models.CharField(max_length=20, unique=True)
	last_name = models.CharField(max_length=20, unique=True)
	age = models.IntegerField()
	email_id = models.EmailField(unique=True)
	dob = models.DateField()
	date_created = models.DateTimeField(auto_now=True)
	# last_used = models.DateTimeField(auto_now=True)
	phone = models.CharField(max_length=10, unique=True)
	address = models.CharField(max_length=200)

	def __unicode__(self):
		return unicode(self.first_name + self.last_name)


class DealersInfo(models.Model):
	person_info = models.ForeignKey(Person) 
	company_name = models.CharField(max_length=50)
	dl1 = models.CharField(max_length=15, unique=True)
	dl2 = models.CharField(max_length=15, unique=True)
	tin = models.CharField(max_length=15, unique=True)

	def __unicode__(self):
		return unicode(self.person_info.first_name + self.person_info.last_name)


class ComplteStockDetails(models.Model):
    batch_num = models.IntegerField(unique=True)
    item_name = models.CharField(max_length=50, unique=True)
    company = models.CharField(max_length=30)
    price_per_unit = models.FloatField()
    manf_date = models.CharField(max_length=10)
    exp_date = models.CharField(max_length=10)
    quantity = models.IntegerField()
    dealer = models.ForeignKey(DealersInfo)
    comments = models.CharField(max_length=100)

    def __unicode__(self):
	# changed return statement.
        return unicode(self.company)
