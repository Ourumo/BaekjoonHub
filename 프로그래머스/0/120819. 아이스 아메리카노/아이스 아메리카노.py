def solution(money):
    ICE_AMERICANO = 5500
    return [money // ICE_AMERICANO, money % ICE_AMERICANO]