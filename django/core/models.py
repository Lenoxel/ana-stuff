from django.db import models

class Category(models.Model):
    objects = models.Manager()

    name = models.CharField('Nome', max_length=60)
    creationDate = models.DateTimeField('Criado em', auto_now_add=True)
    lastUpdatedDate = models.DateTimeField('Última modificação', auto_now=True)

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        ordering = ['name']

    def __str__(self):
        return self.name


class Product(models.Model):
    objects = models.Manager()

    category = models.ForeignKey('core.Category', verbose_name='Categoria', null=True, on_delete=models.SET_NULL)
    name = models.CharField('Nome', max_length=60)
    description = models.TextField('Descrição', max_length=150, blank=True, null=True)
    picture_url = models.CharField('Url da imagem', max_length=300, default="https://i.imgur.com/9lEWQF2.jpg")
    price = models.DecimalField('Preço', decimal_places=2, max_digits=5, blank=True, null=True)
    discount = models.DecimalField("Desconto", decimal_places=2, max_digits=5, blank=True, null=True)
    onSale = models.BooleanField("Em promoção", default=False)
    quantity = models.PositiveSmallIntegerField("Quantidade", default=0)
    creationDate = models.DateTimeField('Criado em', auto_now_add=True)
    lastUpdatedDate = models.DateTimeField('Última modificação', auto_now=True)

    class Meta:
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'
        ordering = ['name']

    def __str__(self):
        return self.name

class Evaluation(models.Model):
    objects = models.Manager()

    product_id = models.ForeignKey('core.Product', verbose_name='Produto', on_delete=models.CASCADE)
    evaluator_name = models.CharField('Avaliador', max_length=60)
    evaluator_email = models.EmailField('Email')
    evaluation = models.PositiveSmallIntegerField('Avaliação')
    comment = models.TextField('Comentário', max_length=200)
    creationDate = models.DateTimeField('Criado em', auto_now_add=True)

    def intialize_object(self, evaluation_object):
        self.product_id = Product.objects.get(id=evaluation_object.get('product_id'))
        self.evaluator_name = evaluation_object.get('evaluator_name')
        self.evaluator_email = evaluation_object.get('evaluator_email')
        self.evaluation = evaluation_object.get('evaluator_evaluation')
        self.comment = evaluation_object.get('evaluator_comment')

    class Meta:
        verbose_name = 'Avaliação'
        verbose_name_plural = 'Avaliações'
        ordering = ['creationDate']

    def __str__(self):
        if self.evaluation > 1:
            return '{} - {} estrelas'.format(self.evaluator_name, self.evaluation)
        else:
            return '{} - {} estrela'.format(self.evaluator_name, self.evaluation)