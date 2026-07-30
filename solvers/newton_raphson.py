import math
from scipy.stats import norm

class NewtonRaphson:
    def __init__(self, blk_scholes): 
        self.black_scholes = blk_scholes

    def computeIV(self, observed_price=0, max_iterations=0, threshold = 0.000001):
        black_scholes = self.black_scholes

        stock_price = black_scholes.stock_price
        time_til_expiration = black_scholes.time_til_expiration #in years

        volatility = black_scholes.volatility     
        volatilites = []
        volatilites.append(volatility)

        for i in range(1,max_iterations):
            # d1 and d2 computed from black_scholes since they need to update every iteration for every new volatility
            d1 = black_scholes.computeD1(volatility)
            d2 = black_scholes.computeD2(volatility, d1)
            
            # similarly, a new theoretical price is computed using the updated d1 and d2 to compare against the observed price
            if black_scholes.option_type == 'call': 
                option_price = black_scholes.computeCallOptionPrice(d1,d2)
            elif black_scholes.option_type == 'put': 
                option_price = black_scholes.computePutOptionPrice(d1,d2)
            else:
                print("Option type not specified or unavailable.")
                break

            vega = stock_price * norm.pdf(d1) * math.sqrt(time_til_expiration)

            #update volatility, difference between last two volatilies is measured against the threshold
            volatility = volatility - ((option_price-observed_price)/vega)
            volatilites.append(volatility)
            print(black_scholes.option_price, option_price, observed_price, volatility)
            if abs(volatilites[-1]-volatilites[-2]) < threshold or abs(option_price-observed_price) < threshold:
                break

        return volatilites