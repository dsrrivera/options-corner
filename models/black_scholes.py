import math
from scipy.stats import norm

class BlackScholes:
    def __init__(self, stock_price, strike_price,  time_til_expiration, option_type, interest_rate=0.04, volatility = .20):
        self.stock_price = stock_price
        self.strike_price = strike_price
        self.time_til_expiration = time_til_expiration  #in years
        self.interest_rate = interest_rate
        self.option_type = option_type
        self.volatility = volatility
        self.d1 = self.computeD1()
        self.d2 = self.computeD2()

        if self.option_type == 'call':
            self.option_price = self.computeCallOptionPrice()
        elif self.option_type == 'put':
            self.option_price = self.computePutOptionPrice()
        else:
            self.option_price = 0.0

    # d1 and d2 can be computed using object instance variables or with passed volatility or strike_price as needed in newton_raphson and Greeks
    def computeD1(self, volatility=None, stock_price=None):
        volatility = self.volatility if volatility is None else volatility
        stock_price = self.stock_price if stock_price is None else stock_price

        numerator = math.log(stock_price/self.strike_price) + (self.interest_rate + (volatility**2)/2) * self.time_til_expiration
        denominator = volatility*(math.sqrt(self.time_til_expiration))
        d1 = numerator/denominator
        return d1

    # d1 may change in newton_raphson or for Greeks charts so d1 may be set manually to correctly compute d2
    def computeD2(self, volatility=None, d1=None):
        volatility = self.volatility if volatility is None else volatility
        d1 = self.d1 if d1 is None else d1

        d2 = d1 - (volatility * math.sqrt(self.time_til_expiration))
        return d2

    # call/put option prices can be computed using object instance variables or with updated d1 and d2 values needed in newton_raphson
    def computeCallOptionPrice(self, d1=None, d2=None):
        d1 = self.d1 if d1 is None else d1
        d2 = self.d2 if d2 is None else d2

        d1_norm = norm.cdf(d1)
        d2_norm = norm.cdf(d2)
        theoretical_price = (self.stock_price * d1_norm) - ((math.e**(-self.interest_rate * self.time_til_expiration)) * self.strike_price * d2_norm)
        return theoretical_price

    def computePutOptionPrice(self, d1=None, d2=None):
        d1 = self.d1 if d1 is None else d1
        d2 = self.d2 if d2 is None else d2

        d1_norm = norm.cdf(-d1)
        d2_norm = norm.cdf(-d2)
        theoretical_price = ((math.e**(-self.interest_rate * self.time_til_expiration)) * self.strike_price * d2_norm) - (self.stock_price * d1_norm)
        return theoretical_price

    def computeDelta(self):
        if self.option_type == 'call':
            delta = norm.cdf(self.d1)
            return delta
        
        elif self.option_type == 'put':
            norm.cdf(self.d1) - 1
            return delta

        return 0

    def computeTheta(self):
        if self.option_type == 'call':
            first_term = -(self.stock_price * norm.cdf(self.d1) * self.volatility) / (2 * math.sqrt(self.time_til_expiration))
            second_term = self.interest_rate * self.strike_price * math.e**(-self.interest_rate * self.time_til_expiration) * norm.cdf(self.d2)
            theta = first_term - second_term
            return theta
        
        elif self.option_type == 'put':
            first_term = -(self.stock_price * norm.cdf(self.d1) * self.volatility) / (2 * math.sqrt(self.time_til_expiration)) 
            second_term = self.interest_rate * self.strike_price * math.e**(-self.interest_rate * self.time_til_expiration) * norm.cdf(-self.d2)
            return theta

        return 0

    def computeRho(self):
        if self.option_type == 'call':
            rho = self.strike_price * self.time_til_expiration * math.e**(-self.interest_rate * self.time_til_expiration) * norm.cdf(self.d2)
            return rho
        
        elif self.option_type == 'put':
            rho = -self.strike_price * self.time_til_expiration * math.e**(-self.interest_rate * self.time_til_expiration) * norm.cdf(-self.d2)
            return rho

        return 0

    def computeGamma(self):
        gamma = norm.pdf(self.d1) / (self.stock_price * self.volatility * math.sqrt(self.time_til_expiration))

        return gamma

    def computeVega(self):
        vega = self.stock_price * norm.pdf(self.d1) * math.sqrt(self.time_til_expiration)

        return vega