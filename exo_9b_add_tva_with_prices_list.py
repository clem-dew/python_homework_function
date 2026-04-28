def add_tva(n):
    return n + n * 0.21


def sum_prices(prices_list = [2, 5.50, 100, 42]):
    return sum(prices_list)


print(add_tva(sum_prices()))
