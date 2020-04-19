from django.db import models
from django.conf import settings
from django.utils.translation import ugettext_lazy as _


class Auditory(models.Model):
	user_created = models.CharField(max_length=30,
									editable=False,
									verbose_name=_("Usuario Creación")
									)
	user_updated = models.CharField(max_length=30,
									verbose_name=_("Usuario Actualización"),
									editable=False)
	created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True, verbose_name=_("Fecha Creación"))
	updated_at = models.DateTimeField(auto_now=True, null=True, blank=True, verbose_name=_("Fecha Actualización"))

	class Meta:
		abstract = True
