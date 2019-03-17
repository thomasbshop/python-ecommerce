import random
import os
from django.db import models
from django.db.models import Q
from django.db.models.signals import pre_save, post_save
from django.urls import reverse

from .utils import unique_slug_generator

def get_filename_ext(filepath):
	base_name = os.path.basename(filepath)
	name, ext = os.path.splitext(base_name)
	return name, ext

# change file name to standardize image url path
def upload_image_path(instance, filename):
	print(instance)
	print(filename)
	new_filename = random.randint(1, 2345433456)
	# new_filename_title = 
	name, ext = get_filename_ext(filename)
	final_filename = "{new_filename}{ext}".format(new_filename=new_filename, ext=ext)
	return "products/{new_filename}/{final_filename}".format(new_filename=new_filename, final_filename=final_filename)

 
class ProductQuerySet(models.query.QuerySet):
	def active(self):
		return self.filter(active=True)

	def featured(self):
		return self.filter(featured=True, active=True)

	def search(self, query):
		lookups = Q(title__icontains=query) | Q(description__icontains=query) | Q(price__icontains=query)
		return self.filter(lookups).distinct()
		

class ProductManager(models.Manager):
	def get_queryset(self):  # over-ride get_queryset() method
		return ProductQuerySet(self.model, using=self._db)

	def all(self):
		return self.get_queryset().active()

	def featured(self):
		return self.get_queryset().featured()

	def get_by_id(self, id):
		qs = self.get_queryset().filter(id=id)  # Product.objects == self.get_queryset()
		if qs.count() == 1:
			return qs.first()
		return None

	def search(self, query):
		return self.get_queryset().active().search(query)


class Product(models.Model):
	title       = models.CharField(max_length=128)
	slug		= models.SlugField(blank=True, unique=True)
	description	= models.TextField()
	price 		= models.DecimalField(decimal_places=2, max_digits=20, default=39.99)
	# image 		= models.FileField(upload_to=upload_image_path, null=True, blank=True)
	image 		= models.ImageField(upload_to=upload_image_path, null=True, blank=True)
	featured	= models.BooleanField(default=False) 
	active	= models.BooleanField(default=True) 
	timestamp = models.DateTimeField(auto_now_add=True)
	# for large file uploads https://kirr.co/e1133t

	objects = ProductManager()

	def get_absolute_url(self):  #  django convention
		"""Returns the url to access a particular instance of the model."""
		# return "/products/{slug}/".format(slug=self.slug)
		return reverse("products:detail", kwargs={"slug":self.slug})

	def __str__(self):
		return self.title

	def __unicode__(self):  #similarly
		return self.title


def product_pre_save_reciever(sender, instance, *args, **kwargs):
	if not instance.slug:
		instance.slug = unique_slug_generator(instance)

pre_save.connect(product_pre_save_reciever, sender=Product)