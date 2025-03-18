from django.urls import path
from .views import estoque_view, movimentacoes_view, adicionar_produto, registrar_saida

urlpatterns = [
    path('', estoque_view, name='estoque'),
    path('movimentacoes/', movimentacoes_view, name='movimentacoes'),
    path('adicionar_produto/', adicionar_produto, name='adicionar_produto'),
    path('registrar_saida/<int:produto_id>/', registrar_saida, name='registrar_saida'),

]
