import './OptionsPage.css'
import { useState } from 'react';
import OptionsForm from '../components/OptionsForm'

export default function OptionsPage(){
  // form holds the values from the user needed for black_scholes.py
  const [form, setForm] = useState({
    stock_price: "",
    strike_price: "",
    time_til_expiration: "",
    interest_rate: "",
    option_type: "",
    volatility: ""
  });

  //used to update form state every time user inputs a value
  const handleChange = (e) => {
    setForm({ 
      ...form,  //carry over everything already in the form
      [e.target.name]: e.target.value });
  };

  return(
    <main className='options-page'>

      <section className='sidebar'>
        {/* we lift the state up from OptionsForm since GreeksPlots require the user inputted information*/}
        <OptionsForm form = {form} handleChange={handleChange}/>
      </section>

      <section className='greeks-charts'>
        <div className='test-box'></div>
        <div className='test-box'></div>
        <div className='test-box'></div>
        <div className='test-box'></div>
        <div className='test-box'></div>
        <div className='test-box'></div>
      </section>
    </main>
  )
}