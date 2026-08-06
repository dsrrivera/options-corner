import './HomePage.css'

export default function HomePage() {
  return(
    <section className="hero">
      <div className="hero-content">
        <h1>Calculate and Analyze Options In a Flash</h1>
        
        <p>Quickly compute and visualize European call/put options and view a dynamically updating implied volatility surface.</p>
        
        <div className="hero-buttons">
          <button className="button-one">Get Started</button>
          <button className="button-two">GitHub</button>
        </div>
      </div>
    </section>
  )
}