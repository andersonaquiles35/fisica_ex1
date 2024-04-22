from scipy.stats import rankdata
import numpy as np

def xi_correlation(x, y, ties="auto"):
    """
    Calcula o coeficiente de correlação de Chatterjee entre duas arrays x e y.

    Parâmetros:
        x (array-like): Array contendo os valores de x.
        y (array-like): Array contendo os valores de y.
        ties (str or bool, opcional): Determina como os empates (ties) devem ser tratados.
            - "auto": O programa determina automaticamente se há empates em y.
            - True: Empates são considerados.
            - False: Empates não são considerados.

    Retorna:
        float: Coeficiente de correlação de Chatterjee entre x e y.

    Raises:
        IndexError: Se o comprimento de x for diferente do comprimento de y.
        ValueError: Se o argumento ties não for "auto" ou um valor booleano.
    """

    # Converte x e y para arrays NumPy e os achatam para garantir que sejam unidimensionais
    x = np.asarray(x).flatten()
    y = np.asarray(y).flatten()
    n = len(y)

    # Verifica se os comprimentos de x e y são iguais
    if len(x) != n:
        raise IndexError(
            f"Divergência de comprimento entre x e y: {len(x)}, {len(y)}"
        )

    # Determina a existência de valores repetidos em y automaticamente
    if ties == "auto":
        ties = len(np.unique(y)) < n
    # Verifica se o argumento ties é válido
    elif not isinstance(ties, bool):
        raise ValueError(
            f"O argumento ties deve ser \"auto\" ou um valor booleano, "
            f"obtido {ties} ({type(ties)}) em vez disso"
        )
    
    # Ordena os valores de y com base nos valores de x ordenados
    y = y[np.argsort(x)]
    # Calcula os ranks de y usando o método "ordinal" para tratar empates
    r = rankdata(y, method="ordinal")
    # Calcula o numerador do coeficiente de correlação
    numerator = np.sum(np.abs(np.diff(r)))

    # Se os empates estiverem presentes
    if ties:
        # Calcula os ranks de y usando o método "max" para tratar empates
        l = rankdata(y, method="max")
        # Calcula o denominador modificado para levar em conta os empates
        denominator = 2 * np.sum(l * (n - l))
        # Multiplica o numerador por n para levar em conta a correção de empates
        numerator *= n
    # Se os empates não estiverem presentes
    else:
        # Calcula o denominador padrão
        denominator = np.power(n, 2) - 1
        # Multiplica o numerador por 3 para ajustar o cálculo
        numerator *= 3

    # Calcula o coeficiente de correlação xi
    statistic = 1 - float(numerator)/float(denominator)

    return statistic

c = xi_correlation([1,2,3,4,5],[6.54,7.4,9,11,15])
print(c)

















