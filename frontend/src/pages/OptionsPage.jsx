import './OptionsPage.css'
import OptionsForm from '../components/OptionsForm'

export default function OptionsPage(){
  return(
    <main className='options-page'>
      <section className='sidebar'>
        <OptionsForm />
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