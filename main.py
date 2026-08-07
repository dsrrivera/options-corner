import os
import time
import numpy as np
from models.black_scholes import BlackScholes
from solvers.newton_raphson import NewtonRaphson

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
    result = BlackScholes(input.stock_price, input.strike_price, input.time_til_expiration, input.option_type, input.interest_rate, input.volatility)

    return {"option_price": result.option_price}

start_time = time.perf_counter_ns()

b1 = BlackScholes(stock_price=336.91, strike_price=337.50,  time_til_expiration=25/365, option_type='call', interest_rate=0.0414, volatility = .2984)
print(b1.option_price)

b2 = BlackScholes(stock_price=336.91, strike_price=337.50,  time_til_expiration=25/365, option_type='put', interest_rate=0.0414, volatility = .3025)
print(b2.option_price)

end_time = time.perf_counter_ns()
print(end_time/1e-9)

print(NewtonRaphson(b1).computeIV(10.75,1000,0.00000001))