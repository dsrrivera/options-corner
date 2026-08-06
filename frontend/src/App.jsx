import { useState } from 'react'
import {BrowserRouter, Route, Routes} from 'react-router'
import Header from './components/Header'
import Footer from './components/Footer'
import HomePage from './pages/HomePage'
import './App.css'

export default function App() {

    return (
    <BrowserRouter>
      <Header />
      
      <Routes>
        <Route path="/" element={<HomePage />} />
      </Routes>

      <Footer />
    </BrowserRouter>
  );
}