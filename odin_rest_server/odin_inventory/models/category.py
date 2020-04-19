from django.db import models
from django.utils.translation import ugettext_lazy as _

from .auditory import Auditory

class Category(Auditory):
	code = models.CharField(max_length=10, verbose_name=_("Código"), blank=True, null=True)
	description = models.CharField(max_length=100, verbose_name=_("Descripción"), blank=True, null=True)

	def __str__(self):
		return "{}".format(
			self.description,
		)

	class Meta:
		verbose_name_plural = 'Categorias'
