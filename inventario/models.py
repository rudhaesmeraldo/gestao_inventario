from django.db import models

class Produto(models.Model):
    nome = models.CharField(max_length=250)
    descricao = models.TextField(blank=True, null=True)
    quantidade = models.PositiveIntegerField(default=0)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    fornecedor = models.CharField(max_length=250, blank=True, null=True)
    criado_em = models.DateField(auto_now_add=True)
    atualizado_em = models.DateField(auto_now=True)

    def __str__(self):
        return f'{self.name}({self.quantidade} em estoque)'

class MovimentacaoEstoque(models.Model):
    TIPO_CHOICE = [
        ('entrada', 'Entrada'),
        ('saida', 'Saida')
    ]

    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    tipo = models.CharField(max_length=7, choices=TIPO_CHOICE)
    quantidade =  
    motivo =
    data = 
    
