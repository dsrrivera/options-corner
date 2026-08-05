import './Footer.css'

export default function footer(){
    return (
        <footer className="footer">
            <p>&copy; {new Date().getFullYear()} OneLab and dssrivera. All rights reserved.</p>
        </footer>
    )
}