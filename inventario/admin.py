from django.contrib import admin
from .models import Produtom MovimentacaoEstoque

@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'quantidade', 'preco', 'fornecedor', 'atualizado_em')
    search_fields = ('nome', 'fornecedor')

@admin.register(MovimentacaoEstoque)
class MovimentacaoEstoque(admin.ModelAdmin):
    list_display = ('produto', 'tipo', 'quantidade', 'data')
    search_fields = ('produto__nome',)
    list_filter = ('tipo', 'data')
