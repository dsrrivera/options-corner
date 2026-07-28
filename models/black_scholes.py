import math
from scipy.stats import norm

class BlackScholes:
    def __init__(self, stock_price, strike_price,  time_til_expiration, option_type, interest_rate=0.04, volatility = .20):
        self.stock_price = stock_price
        self.strike_price = strike_price
        self.time_til_expiration = time_til_expiration  #in years
        self.interest_rate = interest_rate
        self.volatility = volatility
        self.d1 = self.computeD1()
        self.d2 = self.computeD2()

        if option_type == 'call':
            self.option_price = self.computeCallOptionPrice()
        elif option_type == 'put':
            self.option_price = self.computePutOptionPrice()
        else:
            self.option_price = 0.0
    
    # 
    def computeD1(self):
        numerator = math.log(self.strike_price/self.stock_price) + (self.interest_rate + (self.volatility**2)/2) * self.time_til_expiration
        denominator = self.volatility*(math.sqrt(self.time_til_expiration))
        d1 = numerator/denominator
        return d1

    def computeD2(self):
        d2 = self.d1 - (self.volatility * math.sqrt(self.time_til_expiration))
        return d2

    def computeCallOptionPrice(self):
        d1_norm = norm.cdf(self.d1)
        d2_norm = norm.cdf(self.d2)
        theoretical_price = (self.stock_price * d1_norm) - ((math.e**(-self.interest_rate * self.time_til_expiration)) * self.strike_price * d2_norm)
        return theoretical_price

    def computePutOptionPrice(self):
        d1_norm = norm.cdf(-self.d1)
        d2_norm = norm.cdf(-self.d2)
        theoretical_price = ((math.e**(-self.interest_rate * self.time_til_expiration)) * self.strike_price * d2_norm) - (self.stock_price * d1_norm)
        return theoretical_price
