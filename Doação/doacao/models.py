from django.db import models
class Produto(models.Model):
    descricao = models.CharField(max_length=200)
    unidade_medida = models.CharField(max_length=200)
    quantidade = models.IntegerField(default=0)
    def __str__(self):
        return self.descricao
    objects = models.Manager()

    def incrementar_quantidade(self, quantidade):
        self.quantidade += quantidade
        self.save()

class Doacao(models.Model):
    data = models.CharField(max_length=200)
    def __str__(self):
        return self.data
    objects = models.Manager()


class DoacaoItem(models.Model):
    doacao = models.ForeignKey(Doacao, on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    unidade_medida = models.CharField(max_length=200)
    quantidade = models.IntegerField(default=0)

class Entrega(models.Model):
    data = models.CharField(max_length=200)
    local = models.CharField(max_length=200)

class Entrega_Item(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    unidade_medida = models.CharField(max_length=200)
    quantidade = models.IntegerField(default=0)

