import './HomePage.css'
import { Link } from "react-router";

export default function HomePage() {
  return(
    <section className="hero">
      <div className="hero-content">
        <h1>Calculate and Analyze Options In a Flash</h1>
        
        <p>Quickly compute and visualize European call/put options prices and view dynamically updating options Greeks.</p>
        
        <div className="hero-buttons">
          <Link to="/options" className="button-one"> Get Started </Link>
        </div>
      </div>
    </section>
  )
}