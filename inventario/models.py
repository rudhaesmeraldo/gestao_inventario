from django.db import models

class Produto(models.Model):
    nome = models.CharField(max_length=250)
    descricao = models.TextField(blank=True, null=True)
    quantidade = models.PositiveIntegerField(default=0)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    fornecedor = models.CharField(max_length=250, blank=True, null=True)
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.name}({self.quantidade} em estoque)'

class MovimentacaoEstoque(models.Model):
    TIPO_CHOICES = [
        ('entrada', 'Entrada'),
        ('saida', 'Saída')
    ]

    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    tipo = models.CharField(max_length=7, choices=TIPO_CHOICES)
    quantidade = models.PositiveIntegerField()
    motivo = models.TextField(blank=True, null=True)
    data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.tipo.capitalize()} de {self.quantidade}x {self.produto.nome} em {self.data.strftime('%d/%m/%Y')}'
    
