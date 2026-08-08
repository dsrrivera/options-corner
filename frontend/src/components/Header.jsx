import { Link } from 'react-router';
import { FaGithubAlt } from "react-icons/fa";
import './Header.css'

export default function Header() {
  return (
    <header>
      <nav className="navbar">
          <div className="nav-logo">OptionsCorner</div>

          <ul className="nav-links">
            <li><Link to="/options">Options</Link></li>
            <li><Link to="/contact">Contact</Link></li>
          </ul>

          <a
            href="https://github.com/dsrrivera/one-lab"
            target="_blank"
            rel="noopener noreferrer"
            className="nav-github-button"
          >
            <FaGithubAlt size={30} />
            <span>GitHub</span>
          </a>

        </nav>
    </header>
  )
}