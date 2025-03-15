from django import forms
from .models import Produto, MovimentacaoEstoque

class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ['nome', 'descricao', 'quantidade', 'preco', 'fornecedor', 'categoria']
        labels = {
            'nome': 'Nome do Produto',
            'descricao': 'Descrição',
            'quantidade': 'Quantidade em Estoque',
            'preco': 'Preço (R$)',
            'fornecedor': 'fornecedor',
            'categoria': 'Categoria',
        }
        widgets = {
            'descricao': forms.Textarea(attrs={'rows': 3}),
            'preco': forms.NumberInput(attrs={'step': '0.01'}),
        }

class RegistrarSaidaForm(forms.Form):
    quantidade = forms.IntegerField(min_value=1, label='Quantidade para retirada')