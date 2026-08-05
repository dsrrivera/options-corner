import { Link } from 'react-router';
import './Header.css'

export default function Header() {
  return (
    <header>
      <nav className="navbar">
          <div className="nav-logo">OneLab</div>
          <ul className="nav-links">
            <li><Link to="/pricer">Pricing Visualizer</Link></li>
            <li><Link to="/contact">Contact</Link></li>
          </ul>
          <button className="nav-button">GitHub</button>
        </nav>
    </header>
  )
}