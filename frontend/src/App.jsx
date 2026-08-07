import { useState } from 'react'
import {BrowserRouter, Route, Routes} from 'react-router'
import Header from './components/Header'
import Footer from './components/Footer'
import HomePage from './pages/HomePage'
import OptionsPage from './pages/OptionsPage'

import './App.css'

export default function App() {

    return (
    <BrowserRouter>
      <Header />
      
      <Routes>
        <Route path="/" element={<HomePage />} />
        <Route path="/options" element={<OptionsPage />} />
      </Routes>

      <Footer />
    </BrowserRouter>
  );
}