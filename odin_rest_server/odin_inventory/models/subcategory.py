from django.db import models
from django.utils.translation import ugettext_lazy as _

from .auditory import Auditory
from .category import Category

class SubCategory(Auditory):
	code = models.CharField(max_length=10, verbose_name=_("Código"), blank=True, null=True)
	description = models.CharField(max_length=100, verbose_name=_("Descripción"), blank=True, null=True)
	category = models.ForeignKey(Category, verbose_name=_("Categorias"), on_delete=models.CASCADE, null=True, blank=True, related_name='subcategories')

	def __str__(self):
		return "{} {}".format(
			self.code,
			self.description,
		)

	class Meta:
		verbose_name_plural = 'SubCategorias'
