# Exception para a regra de negocio onde o nuemrop de cotista deve ser igual durante o periodo
class InconsistentDataError(ValueError):
    """Exceção para quando os dados de cotas são inconsistentes entre os dias."""
    pass
