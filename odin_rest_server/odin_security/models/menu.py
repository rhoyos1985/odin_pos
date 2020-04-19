from django.db import models
from django.contrib.auth.models import Group
from .audit import AuditModel

class MenuModel(AuditModel):
	name = models.CharField(max_length=50)
	url = models.CharField(max_length=500)
	parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
	group = models.ManyToManyField(Group, related_name='groups', verbose_name='Lista de Roles')

	def __str__(self):
		return '{}'.format(self.name)


	class Meta:
		verbose_name_plural = 'Menus'
