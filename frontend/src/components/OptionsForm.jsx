import { useState } from 'react';
import './OptionsForm.css'

function OptionsForm({ form, handleChange}) {  
  const [result, setResult] = useState(null);
  const [error, setError] = useState(null);

  //sends POST request to api/pricer to compute options_price in black_scholes.py from api in main.py
  const handleSubmit = async (e) => {
    e.preventDefault();
    setError(null);
    try {
      const res = await fetch("http://localhost:8000/api/pricer", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          stock_price: form.stock_price,
          strike_price: form.strike_price,
          time_til_expiration: form.time_til_expiration,
          interest_rate: form.interest_rate,
          option_type: form.option_type,
          volatility: form.volatility,
        }),
      });
      if (!res.ok) throw new Error(`Request failed: ${res.status}`);
      const data = await res.json(); //currently receives just option_price: price
      setResult(data); //remains null if error is caught
      
    } catch (err) {
      setError(err.message);
    }
  };

  return (
    <section className='options-form-result'>
      {/* handles the user input and modifies form state */}
      <form className='options-form' onSubmit={handleSubmit}>
        <input name="option_type" value={form.option_type} onChange={handleChange} placeholder="Option Type" />
        <input name="stock_price" value={form.stock_price} onChange={handleChange} placeholder="Stock/Index Price" />
        <input name="strike_price" value={form.strike_price} onChange={handleChange} placeholder="Strike Price" />
        <input name="time_til_expiration" value={form.time_til_expiration} onChange={handleChange} placeholder="DTE (In Days)" />
        <input name="interest_rate" value={form.interest_rate} onChange={handleChange} placeholder="Interest Rate" />
        <input name="volatility" value={form.volatility} onChange={handleChange} placeholder="Volatility" />

        <button className='price-submit-btn' type="submit">Calculate Theoretical Price </button>
      </form>

      {/* if result is not null we display the price */}
      {result && (
        <div className='result'>
          <p>Price: {result.option_price}</p>
        </div>
      )}
      {error && <p style={{ color: "red" }}>{error}</p>}
    </section>
  );
}

export default OptionsForm;