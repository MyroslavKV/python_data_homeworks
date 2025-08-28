import numpy as np

coefficients = [2, -8, 6, -4, 2]

p = np.poly1d(coefficients)
print("Поліном:", p)

roots = np.roots(coefficients)
print("Корені полінома:", roots)

p_deriv = p.deriv()
print("Перша похідна полінома:", p_deriv)

p_second_deriv = p.deriv(2)
print("Друга похідна полінома:", p_second_deriv)

n_value = 50
p_at_n = p(n_value)
print(f"Значення ({n_value}) =", p_at_n)