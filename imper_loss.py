priceChange1 = float(input('Price Change of Asset 1: ')) / 100

priceChange2 = float(input('Price Change of Asset 2: ')) / 100

calc = (1.0 + priceChange1) / (1.0 + priceChange2)

iL = 1 - (calc ** 0.5) / (0.5 * calc + 0.5)

print('Impermanent Loss: {}%'.format(iL * 100))
