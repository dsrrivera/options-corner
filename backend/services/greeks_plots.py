import math
import numpy as np
import plotly.io as pio
import plotly.express as px
import plotly.graph_objects as go

from models.black_scholes import BlackScholes

def generateDeltaPlot(black_scholes: BlackScholes):
    stock_price = black_scholes.stock_price

    # the underlying prices range from plus minus 20%, this can change to be user defined later
    underlying_prices = np.linspace(stock_price*0.8, stock_price*1.2, 100)

    # the values for delta are computed across the underlying_prices where a new d1 is computed per price
    delta_values = [black_scholes.computeDelta(black_scholes.computeD1(stock_price=price)) for price in underlying_prices]

    fig = px.line(x=list(underlying_prices), y=delta_values, title="Delta vs Underlying Stock Price")

    fig.update_traces(line=dict(width=5))

    fig.update_layout(
        xaxis_title="Stock Price",
        yaxis_title="Delta",

        # center the main plot title
        title={
            'x': 0.5,               # exactly half of the containers width
            'xanchor': 'center'
        }
    )

    # make X-axis labels and ticks larger
    fig.update_xaxes(
        title_font_size=18,    
        tickfont_size=14
    )

    # make Y-axis labels and ticks larger
    fig.update_yaxes(
        title_font_size=18,    
        tickfont_size=14
    )

    fig.add_vline(
        x=black_scholes.stock_price, 
        line_width=3, 
        line_dash="dash", 
        line_color="black"
    )

    fig.add_vline(
        x=black_scholes.strike_price, 
        line_width=3, 
        line_dash="dash", 
        line_color="red"
    )

    # fig.show()
    return pio.to_json(fig)

def generateGammaPlot(black_scholes: BlackScholes):
    stock_price = black_scholes.stock_price

    # the underlying prices range from plus minus 20%, this can change to be user defined later
    underlying_prices = np.linspace(stock_price*0.8, stock_price*1.2, 100)

    # the values for gamma are computed across the underlying_prices where a new d1 is computed per price
    gamma_values = [black_scholes.computeGamma(stock_price = price, d1=black_scholes.computeD1(stock_price=price)) for price in underlying_prices]

    fig = px.line(x=list(underlying_prices), y=gamma_values, title="Gamma vs Underlying Stock Price")

    fig.update_traces(line_color="#2f9d50", line=dict(width=5))

    fig.update_layout(
        xaxis_title="Stock Price",
        yaxis_title="Gamma",

        # center the main plot title
        title={
            'x': 0.5,               # exactly half of the containers width
            'xanchor': 'center'
        }
    )

    # make X-axis labels and ticks larger
    fig.update_xaxes(
        title_font_size=18,    
        tickfont_size=14
    )

    # make Y-axis labels and ticks larger
    fig.update_yaxes(
        title_font_size=18,    
        tickfont_size=14
    )

    fig.add_vline(
        x=black_scholes.stock_price, 
        line_width=3, 
        line_dash="dash", 
        line_color="black"
    )

    fig.add_vline(
        x=black_scholes.strike_price, 
        line_width=3, 
        line_dash="dash", 
        line_color="red"
    )

    # fig.show()
    return pio.to_json(fig)

def generateThetaPlot(black_scholes: BlackScholes):
    stock_price = black_scholes.stock_price

    # the underlying prices range from plus minus 20%, this can change to be user defined later
    underlying_prices = np.linspace(stock_price*0.8, stock_price*1.2, 100)

    # the values for theta are computed across the underlying_prices where a new d1 and d2 are computed per price
    theta_values = []
    for price in underlying_prices:
        d1=black_scholes.computeD1(stock_price=price)
        d2=black_scholes.computeD2(d1=d1)
        cur_theta = black_scholes.computeTheta(stock_price = price, d1=d1, d2=d2)
        theta_values.append(cur_theta)

    fig = px.line(x=list(underlying_prices), y=theta_values, title="Theta vs Underlying Stock Price")

    fig.update_traces(line_color="#dd1c1a", line=dict(width=5))

    fig.update_layout(
        xaxis_title="Stock Price",
        yaxis_title="Theta",

        # center the main plot title
        title={
            'x': 0.5,               # exactly half of the containers width
            'xanchor': 'center'
        }
    )

    # make X-axis labels and ticks larger
    fig.update_xaxes(
        title_font_size=18,    
        tickfont_size=14
    )

    # make Y-axis labels and ticks larger
    fig.update_yaxes(
        title_font_size=18,    
        tickfont_size=14
    )

    fig.add_vline(
        x=black_scholes.stock_price, 
        line_width=3, 
        line_dash="dash", 
        line_color="black"
    )

    fig.add_vline(
        x=black_scholes.strike_price, 
        line_width=3, 
        line_dash="dash", 
        line_color="red"
    )

    # fig.show()
    return pio.to_json(fig)

def generateVegaPlot(black_scholes: BlackScholes):
    stock_price = black_scholes.stock_price

    # the underlying prices range from plus minus 20%, this can change to be user defined later
    underlying_prices = np.linspace(stock_price*0.8, stock_price*1.2, 100)

    # the values for vega are computed across the underlying_prices where a new d1 is computed per price
    vega_values = [black_scholes.computeVega(stock_price=price, d1=black_scholes.computeD1(stock_price=price)) for price in underlying_prices]

    fig = px.line(x=list(underlying_prices), y=vega_values, title="Vega vs Underlying Stock Price")

    fig.update_traces(line_color="#eca009", line=dict(width=5))

    fig.update_layout(
        xaxis_title="Stock Price",
        yaxis_title="Vega",

        # center the main plot title
        title={
            'x': 0.5,               # exactly half of the containers width
            'xanchor': 'center'
        }
    )

    # make X-axis labels and ticks larger
    fig.update_xaxes(
        title_font_size=18,    
        tickfont_size=14
    )

    # make Y-axis labels and ticks larger
    fig.update_yaxes(
        title_font_size=18,    
        tickfont_size=14
    )

    fig.add_vline(
        x=black_scholes.stock_price, 
        line_width=3, 
        line_dash="dash", 
        line_color="black"
    )

    fig.add_vline(
        x=black_scholes.strike_price, 
        line_width=3, 
        line_dash="dash", 
        line_color="red"
    )

    # fig.show()
    return pio.to_json(fig)

def generateRhoPlot(black_scholes: BlackScholes):
    stock_price = black_scholes.stock_price

    # the underlying prices range from plus minus 20%, this can change to be user defined later
    underlying_prices = np.linspace(stock_price*0.8, stock_price*1.2, 100)

    # the values for delta are computed across the underlying_prices where a new d2 and therefore d1 is computed per price
    rho_values = []
    for price in underlying_prices:
        d1=black_scholes.computeD1(stock_price=price)
        d2=black_scholes.computeD2(d1=d1)
        cur_rho = black_scholes.computeRho(d2=d2)
        rho_values.append(cur_rho)

    fig = px.line(x=list(underlying_prices), y=rho_values, title="Rho vs Underlying Stock Price")

    fig.update_traces(line_color="#47304b", line=dict(width=5))

    fig.update_layout(
        xaxis_title="Stock Price",
        yaxis_title="Rho",

        # center the main plot title
        title={
            'x': 0.5,               # exactly half of the containers width
            'xanchor': 'center'
        }
    )

    # make X-axis labels and ticks larger
    fig.update_xaxes(
        title_font_size=18,    
        tickfont_size=14
    )

    # make Y-axis labels and ticks larger
    fig.update_yaxes(
        title_font_size=18,    
        tickfont_size=14
    )

    fig.add_vline(
        x=black_scholes.stock_price, 
        line_width=3, 
        line_dash="dash", 
        line_color="black"
    )

    fig.add_vline(
        x=black_scholes.strike_price, 
        line_width=3, 
        line_dash="dash", 
        line_color="red"
    )

    # fig.show()
    return pio.to_json(fig)

def generateThetaSurface(black_scholes: BlackScholes):
    stock_price = black_scholes.stock_price

    underlying_prices = np.linspace(stock_price*0.8, stock_price*1.2, 100)

    if black_scholes.time_til_expiration > 90:
        max_expiration = black_scholes.time_til_expiration
    else:
        max_expiration = 90

    times_til_expiration = np.linspace(0.1, max_expiration, 100)

    # creates the 2D coordinate grids
    X, Y = np.meshgrid(underlying_prices, times_til_expiration)

    Z = np.zeros_like(X)  # same shape as X and Y

    # we compute Z from X and Y by iterating over their values in the meshgrid to fill in Z
    rows, cols = X.shape
    for i in range(rows):
        for j in range(cols):
            cur_underlying_price = X[i, j]
            cur_time_til_expiry = Y[i, j]

            d1=black_scholes.computeD1(stock_price=cur_underlying_price, time_til_expiration=cur_time_til_expiry)
            d2=black_scholes.computeD2(d1=d1, time_til_expiration=cur_time_til_expiry)
            cur_theta = black_scholes.computeTheta(time_til_expiration=cur_time_til_expiry, stock_price = cur_underlying_price, d1=d1, d2=d2)
            Z[i, j] = cur_theta

    fig = go.Figure(
        go.Surface(
            x=X,
            y=Y,
            z=Z,
            colorscale="ice"
        )
    )

    camera = dict(eye=dict(x=1.0, y=-2.0, z=1)) # positions the camera low and directly along the X-axis

    fig.update_layout(
        title={
            'text': 'Theta Surface',

            # center and lower the main plot title
            'x': 0.5,  # exactly half of the containers width
            'xanchor': 'center',
            'y': 0.90, # nudged down slightly
            'yanchor': 'top'
        },
        scene_camera=camera,
        scene={
            'xaxis_title': "Stock Price",
            'yaxis_title': "TTE",
            'zaxis_title': "Theta",
            'domain': {'x':[0, 1], 'y':[0, 1]}  # makes the plot fill the entire domain, different than container
        },

        margin=dict(l=20, r=40, t=80, b=20)     # adjusts plotly's automatic margin for the plot
    )

    # fig.show()
    return pio.to_json(fig)