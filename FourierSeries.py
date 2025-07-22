from scipy.integrate import quad
import math

class FourierSeries:
    def __init__(self):
        self.n = 0 

    def _a_n(self, f, l1, l2):
        l = (l1 - l2) / 2 
        if l == 0: 
            raise ValueError("L_arg_denom cannot be zero for Fourier Series argument. Check interval (l1, l2).")

        def integrand(x):
            return f(x) * math.cos((self.n * math.pi * x) / l)

        integral_result, _ = quad(integrand, l1, l2)
        return integral_result

    def _b_n(self, f, l1, l2):
        l = (l1 - l2) / 2 
        if l == 0:
            raise ValueError("L_arg_denom cannot be zero for Fourier Series argument. Check interval (l1, l2).")

        def integrand(x):
            return f(x) * math.sin((self.n * math.pi * x) / l)

        integral_result, _ = quad(integrand, l1, l2)
        return integral_result

    def _a_0(self, f, l1, l2):
        def integrand_a0(x):
            return f(x)

        integral_result, _ = quad(integrand_a0, l1, l2)
        return integral_result

    def FourierSeries(self, f, l1, l2, num_terms=50):
        l = (l1 - l2) / 2
        if l == 0:
            raise ValueError("L_arg_denom cannot be zero for Fourier Series argument. Check interval (l1, l2).")
        
        L_coeff_factor = (l2 - l1) / 2 
        if L_coeff_factor == 0:
            raise ValueError("Coefficient factor L cannot be zero. Check interval (l1, l2).")

        a_0_integral_part = self._a_0(f, l1, l2)
        a_0 = a_0_integral_part / L_coeff_factor 

        a_n_coeffs = []
        b_n_coeffs = []

        for n_val in range(1, num_terms + 1):
            self.n = n_val 
            a_n_integral_part = self._a_n(f, l1, l2)
            b_n_integral_part = self._b_n(f, l1, l2)
            
            a_n_coeffs.append(a_n_integral_part / L_coeff_factor)
            b_n_coeffs.append(b_n_integral_part / L_coeff_factor)

        
        def series_evaluator(x_val):
            
            current_sum = a_0 / 2.0 

            for i in range(num_terms):
                n = i + 1 
                current_sum += a_n_coeffs[i] * math.cos((n * math.pi * x_val) / l) + \
                               b_n_coeffs[i] * math.sin((n * math.pi * x_val) / l)
            return current_sum
        
        return series_evaluator