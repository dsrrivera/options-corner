import './OptionsPage.css'
import { useState } from 'react';
import OptionsForm from '../components/OptionsForm'
import GreeksPlots from '../components/GreeksPlots'

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

  const [submittedForm, setSubmittedForm] = useState(null);

  return(
    <main className='options-page'>

      <section className='sidebar'>
        {/* we lift the state up from OptionsForm since GreeksPlots require the user inputted information*/}
        <OptionsForm form = {form} handleChange={handleChange} setSubmittedForm={setSubmittedForm}/>
      </section>

      <section className='greeks-charts'>
        <GreeksPlots submittedForm={submittedForm}/>
      </section>
    </main>
  )
}