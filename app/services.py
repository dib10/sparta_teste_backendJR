from . import schemas
from typing import List
from .exceptions import InconsistentDataError 

# ------- Função principal ----------------
def calcular_taxa_administracao(data: schemas.InputData) -> List[float]:

    taxa_anual = data.taxa #acessando a taxa anual
    dados_diarios = data.cotas
    num_cotistas = _obter_num_cotistas(dados_diarios) 

    if num_cotistas == 0:
        return [] 
    resultado = _executar_soma_taxas(dados_diarios, taxa_anual, num_cotistas)
    
    return resultado

# ---- Funções aux------

## o numero de cotistas é o tamanho da lista de quantidades do primeiro dia
def _obter_num_cotistas(dados_diarios: List[schemas.ItemCota]) -> int: 
    if not dados_diarios:
        return 0 # se o tamanho da lista for 0, assumo que não tem cotistas
    return len(dados_diarios[0].quantidades) #retorno o tamanho da lista, que é = cotistas


def _executar_soma_taxas(dados_diarios: List[schemas.ItemCota], taxa_anual: float, num_cotistas: int) -> List[float]:
    taxa_por_cotista = [0.0] * num_cotistas 
    for dia in dados_diarios: ## loop externo 

        if len(dia.quantidades) != num_cotistas: # o numero de cotistas deve ser o mesmo para todos os dias 
            raise InconsistentDataError(
                "O número de cotistas na lista 'quantidades' é inconsistente entre os dias."
            )

        valor_cota = dia.valor
        quantidade_cotistas_dia = dia.quantidades

        for j in range(num_cotistas): ## loop interno
            quantidade_do_cotista_dia = quantidade_cotistas_dia[j] 
            taxa_diaria = (quantidade_do_cotista_dia * valor_cota * taxa_anual) / 252
            taxa_por_cotista[j] += taxa_diaria 
            
    return taxa_por_cotista


# Minha linha de pensamento:
#
# 1. Criei uma function _obter_num_cotistas para determinar a quantidade
#    de cotistas (M) para o calculo. Uma lista de resultados é inicializada com zeros.
#
# 2.  A função _executar_soma_taxas inicia um loop externo para percorrer
#    cada dia do período (no caso o i da fórmula).
#
# 3. Dentro de cada dia, um loop interno percorre cada cotista
#    (no caso o j da fórmula)
#
# 4.  Para cada combinação de (dia, cotista), a taxa diária é calculada
#    aplicando a fração da fórmula: (c * v * t) / 252
#
# 5. O valor da taxa diária é somado ao total já acumulado para
#    o respectivo cotista. O  += seria o somatório (Σ)
#
# 6. Após todos os loops, a lista de resultados contém a taxa final para cada
#    cotista aJ que é então retornada, ai chamo essa função na principal