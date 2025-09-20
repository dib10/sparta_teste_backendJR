import pytest
from app import services, schemas, exceptions

def test_calcular_taxa_administracao_deve_retornar_valores_corretos_quando_dados_validos():
   
    # Arrange
    dados_de_teste = schemas.InputData(
        taxa=0.01,
        cotas=[
            schemas.ItemCota(valor=10.50, quantidades=[100, 200]),
            schemas.ItemCota(valor=11.00, quantidades=[100, 250])
        ]
    )
    
    resultado_esperado = [
        0.08531746031746032,
        0.19246031746031744
    ]

    # Act
    resultado_calculado = services.calcular_taxa_administracao(dados_de_teste)

    # Assert
    assert resultado_calculado == pytest.approx(resultado_esperado)

def test_calcular_taxa_administracao_deve_retornar_lista_vazia_quando_cotas_vazias():
    
    # Arrange
    dados_de_teste = schemas.InputData(taxa=0.01, cotas=[])
    
    # Act
    resultado = services.calcular_taxa_administracao(dados_de_teste)
    
    # Assert
    assert resultado == []

def test_calcular_taxa_administracao_deve_retornar_zero_quando_cotistas_tem_zero_cotas():
    
    # Arrange
    dados_de_teste = schemas.InputData(
        taxa=0.01,
        cotas=[
            schemas.ItemCota(valor=10.0, quantidades=[0, 0]),
            schemas.ItemCota(valor=12.0, quantidades=[0, 0])
        ]
    )
    
    # Act
    resultado = services.calcular_taxa_administracao(dados_de_teste)
    
    # Assert
    assert resultado == pytest.approx([0.0, 0.0])

def test_calcular_taxa_administracao_deve_lancar_excecao_quando_dados_cotistas_inconsistentes():
    
    # Arrange
    dados_de_teste = schemas.InputData(
        taxa=0.01,
        cotas=[
            schemas.ItemCota(valor=10.0, quantidades=[100, 200]),
            schemas.ItemCota(valor=11.0, quantidades=[100, 250, 300])
        ]
    )
    
    # Act & Assert
    with pytest.raises(exceptions.InconsistentDataError) as excinfo:
        services.calcular_taxa_administracao(dados_de_teste)
    
    assert "O número de cotistas na lista 'quantidades' é inconsistente entre os dias." in str(excinfo.value)