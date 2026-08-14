import math
import numpy as np
import plotly.express as px

from scipy.stats import norm
from models.black_scholes import BlackScholes

def generateDeltaPlot(black_scholes: BlackScholes):
    stock_price = black_scholes.stock_price

    # the underlying prices range from plus minus 20%, this can change to be user defined later
    underlying_prices = np.linspace(stock_price*0.8, stock_price*1.2, 100)

    # the values for delta are computed across the underlying_prices where a new d1 is computed per price
    delta_values = [black_scholes.computeDelta(black_scholes.computeD1(stock_price=price)) for price in underlying_prices]

    fig = px.line(x=list(underlying_prices), y=delta_values, title="Delta vs Underlying Stock Price")

    fig.add_vline(
        x=black_scholes.stock_price, 
        line_width=3, 
        line_dash="dash", 
        line_color="black",
        annotation_text="Current Stock Price",
        annotation_position="top right"
    )

    fig.add_vline(
        x=black_scholes.strike_price, 
        line_width=3, 
        line_dash="dash", 
        line_color="red",
        annotation_text="Current Strike Price",
        annotation_position="top right"
    )

    fig.show()