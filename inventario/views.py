from django.shortcuts import render, get_object_or_404, redirect
from .models import Produto, MovimentacaoEstoque
from .forms import ProdutoForm


def estoque_view(request):
    produtos = Produto.objects.all()
    return render(request, 'index.html', {'produtos': produtos})

def movimentacoes_view(request):
    movimentacoes = MovimentacaoEstoque.objects.all().order_by('-data')
    return render(request, 'movimentacoes.html', {'movimentacoes':movimentacoes})

def adicionar_produto(request):
    if request.method == 'POST':
        form = ProdutoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('estoque')
    
    else:
        form = ProdutoForm()
    
    return render(request, 'produto_form.html', {'form': form, 'titulo':'Adicionar Produto'})

def registrar_saida(request, produto_id):
    produto = get_object_or_404(Produto, id=produto_id)

    if request.method == 'POST':
        quantidade = int(request.POST.get('quantidade', 0))
        if quantidade > 0:
            MovimentacaoEstoque.objects.create(
                produto=produto,
                nome_produto=produto.nome,
                tipo='saida',
                quantidade=quantidade,
                responsavel=request.user
            )
            return redirect('estoque')

    return render(request, 'saida_form.html', {'produto': produto, 'titulo': 'Registrar Saída'}) 




        
