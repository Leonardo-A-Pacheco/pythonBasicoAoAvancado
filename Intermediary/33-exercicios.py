from exercicio33 import produtos
import copy

# copy, sorted, produtos.sort
# Exercícios
# Aumente os preços dos produtos a seguir em 10%
# Gere novos_produtos por deep copy (cópia profunda)
#copiei profundamente da pasta ex33 a lista produtos
produtos_copiados = copy.deepcopy(produtos)
# print(produtos)
# print()
# novos produtos está recebendo uma deepcopy com ajuste de 10% da copia anterior arredondando com round
novos_produtos = [
    {**p, 'preco': round(p['preco'] * 1.1 ,2)}
      for p in copy.deepcopy(produtos_copiados)
]


print(*novos_produtos, sep='\n')
print()
# print(*produtos_copiados, sep='\n')

# Ordene os produtos por nome decrescente (do maior para menor)
p_ordenado_dec = sorted(
    copy.deepcopy(novos_produtos), 
    key=lambda p: p['nome'],
    reverse=True
)


print(*p_ordenado_dec, sep='\n')


# Gere produtos_ordenados_por_nome por deep copy (cópia profunda)


print()
# Ordene os produtos por preco crescente (do menor para maior)
p_ordem_cres = sorted(
    copy.deepcopy(p_ordenado_dec),
    key=lambda p: p['nome'],
    )

print(*p_ordem_cres, sep='\n')

print()
# Gere produtos_ordenados_por_preco por deep copy (cópia profunda)
p_ordem_preco_cres = sorted(
    copy.deepcopy(p_ordem_cres),
    key=lambda p: p['preco'],
    )

print(*p_ordem_preco_cres, sep='\n')