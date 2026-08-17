import { useState } from 'react';
import './OptionsForm.css'

function OptionsForm({ form, handleChange, setSubmittedForm }) {  
  const [result, setResult] = useState(null);
  const [error, setError] = useState(null);

  //sends POST request to api/pricer to compute options_price in black_scholes.py from api in main.py
  const handleSubmit = async (e) => {
    e.preventDefault();
    setError(null);
    try {
      const optionsPrice = await fetch("http://localhost:8000/api/pricer", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(form),
      });
      if (!optionsPrice.ok) throw new Error(`Request failed: ${optionsPrice.status}`);
      const data = await optionsPrice.json(); //currently receives just option_price: price
      setResult(data); //remains null if error is caught

      // we update the submittedForm state only after the POST request is OK
      setSubmittedForm(form)

    } catch (err) {
      setError(err.message);
    }
  };

  return (
    <section className='options-form-result'>
      {/* handles the user input and modifies form state */}
      <form className='options-form' onSubmit={handleSubmit}>
        {/* label-input containers help organize space between different inputs and the labels and their respective inputs */}
        <div className='form-label-input'>
          <label for='option_type' className='form-label'>Option Type</label>
          <input name="option_type" value={form.option_type} onChange={handleChange} placeholder="Call or Put" id='option_type' />
        </div>

        <div className='form-label-input'>
          <label for='stock_price' className='form-label'>Stock Price</label>
          <input name="stock_price" value={form.stock_price} onChange={handleChange} placeholder="0.00" id='stock_price' />
        </div>

        <div className='form-label-input'>
          <label for='strike_price' className='form-label'>Strike Price</label>
          <input name="strike_price" value={form.strike_price} onChange={handleChange} placeholder="0.00" id='strike_price' />
        </div>

        <div className='form-label-input'>
          <label for='time_til_expiration' className='form-label'>Time to Expiration</label>
          <input name="time_til_expiration" value={form.time_til_expiration} onChange={handleChange} placeholder="Days" id='time_til_expiration' />
        </div>

        <div className='form-label-input'>
          <label for='interest_rate' className='form-label'>Interest Rate</label>
          <input name="interest_rate" value={form.interest_rate} onChange={handleChange} placeholder="0.00" id='interest_rate' />
        </div>

        <div className='form-label-input'>
          <label for='volatility' className='form-label'>Volatility</label>
          <input name="volatility" value={form.volatility} onChange={handleChange} placeholder="0.00" id='volatility' />
        </div>

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