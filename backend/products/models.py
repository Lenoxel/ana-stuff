from django.db import models

class Product(models.Model):

    name = models.CharField('Nome', max_length=60)
    description = models.TextField('Descrição', max_length=150, blank=True, null=True)
    price = models.DecimalField('Preço', decimal_places=2, max_digits=5)
    evaluation = models.DecimalField('Avaliação', decimal_places=2, max_digits=3)
    quantity = models.PositiveSmallIntegerField()
    checked = models.BooleanField(default=False)
    picture = models.ImageField('Foto', upload_to='img/products/', default='img/products/default')
    creationDate = models.DateTimeField('Criado em', auto_now_add=True)
    lastUpdatedDate = models.DateTimeField('Última modificação', auto_now=True)

    class Meta:
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'
        ordering = ['name']

    def __str__(self):
        return self.name

