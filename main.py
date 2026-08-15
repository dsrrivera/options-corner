from models.black_scholes import BlackScholes
from solvers.newton_raphson import NewtonRaphson
from services.greeks_plots import generateDeltaPlot, generateGammaPlot, generateThetaPlot, generateVegaPlot, generateRhoPlot

from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

class BlackScholesInput(BaseModel):
    stock_price: float
    strike_price: float
    time_til_expiration: float
    option_type: str
    interest_rate: float
    volatility: float

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_headers=["*"],
    allow_methods=["*"]
)

@app.post("/api/pricer")
def get_option_price(input: BlackScholesInput):
    b1 = BlackScholes(input.stock_price, input.strike_price, input.time_til_expiration, input.option_type, input.interest_rate, input.volatility)

    return {"option_price": b1.option_price}

@app.post("/api/greeks-plots")
def get_greeks_plots(input: BlackScholesInput):
    b2 = BlackScholes(input.stock_price, input.strike_price, input.time_til_expiration, input.option_type, input.interest_rate, input.volatility)

    delta_plot = generateDeltaPlot(b2)
    gamma_plot = generateGammaPlot(b2)
    theta_plot = generateThetaPlot(b2)
    vega_plot = generateVegaPlot(b2)
    rho_plot = generateRhoPlot(b2)

    return {"delta_plot": delta_plot, "gamma_plot": gamma_plot, "theta_plot": theta_plot, "vega_plot": vega_plot, "rho_plot": rho_plot}