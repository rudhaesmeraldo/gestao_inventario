from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class Categoria(models.Model):
    nome = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.nome

class Produto(models.Model):
    nome = models.CharField(max_length=250)
    descricao = models.TextField(blank=True, null=True)
    quantidade = models.PositiveIntegerField(default=0)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    fornecedor = models.CharField(max_length=250, blank=True, null=True)
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.nome} ({self.quantidade} em estoque)"
    
    def estoque_baixo(self):
        return self.quantidade < 10

class MovimentacaoEstoque(models.Model):
    TIPO_CHOICES = [
        ('entrada', 'Entrada'),
        ('saida', 'Saída')
    ]

    produto = models.ForeignKey(Produto, on_delete=models.SET_NULL, null=True, blank=True)
    nome_produto = models.CharField(max_length=255, blank=True, null=True) # save para movimentações
    tipo = models.CharField(max_length=7, choices=TIPO_CHOICES)
    quantidade = models.PositiveIntegerField()
    motivo = models.TextField(blank=True, null=True)
    responsavel = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.tipo.capitalize()} de {self.quantidade}x {self.nome_produto or 'Produto Removido'} em {self.data.strftime('%d/%m/%Y')}"

    def save(self, *args, **kwargs):
        if self.produto and not self.nome_produto:
            self.nome_produto = self.produto.nome

        if self.produto and self.tipo == 'saida':
            if self.produto.quantidade < self.quantidade:
                raise ValidationError('Quantidade insuficiente no estoque!')

            self.produto.quantidade -= self.quantidade
            self.produto.save()

        super().save(*args, **kwargs)

        if self.produto and self.produto.quantidade == 0:
            self.produto.delete()
