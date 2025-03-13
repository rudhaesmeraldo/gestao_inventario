from django.contrib import admin
from .models import Produto, MovimentacaoEstoque, Categoria

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    search_fields = ('nome',)

@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'quantidade', 'preco', 'fornecedor', 'atualizado_em')
    search_fields = ('nome', 'fornecedor')
    list_filter = ('fornecedor', 'atualizado_em')

@admin.register(MovimentacaoEstoque)
class MovimentacaoEstoqueAdmin(admin.ModelAdmin):
    list_display = ('produto', 'tipo', 'quantidade', 'data')
    search_fields = ('produto__nome', 'tipo', 'motivo')
    list_filter = ('tipo', 'data')

