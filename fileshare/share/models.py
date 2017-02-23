from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User

# Create your models here.

class File(models.Model):
	user = models.ForeignKey(User, verbose_name='Usuário', related_name='users', on_delete=models.CASCADE)
	description = models.CharField('Descrição', max_length=200, null=True, blank=True)
	publication_date = models.DateField('Data de Publicação')
	created_at = models.DateTimeField('Criado em', auto_now_add=True)
	update_at = models.DateTimeField('Atualizado em', auto_now_add=True)
	published = models.BooleanField()
	file = models.FileField('Arquivo', upload_to='upload/file')

	def __str__(self):
		return self.description

	def get_absolute_url(self):
		return reverse('share:file_list')