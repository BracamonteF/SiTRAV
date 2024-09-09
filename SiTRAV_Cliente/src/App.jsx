import './App.css'
import MapView from './components/MapView'
import { BrowserRouter, Routes, Route, Navigate } from 'react-router-dom'
import { PaginaConductores } from './pages/PaginaConductores'
import { FormularioConductores } from './pages/FormularioConductores'
import { Navigation } from './components/Navigation'

function App() {
  return (
    <BrowserRouter>
    <Navigation />
    <Routes>
      <Route path="/" element={<Navigate to="/conductores" />} />
      <Route path="/conductores" element={<PaginaConductores />} />
      <Route path="/conductores-crear" element={<FormularioConductores />} />
      <Route path="/conductores/:id" element={<FormularioConductores />} />
    </Routes>
    </BrowserRouter>
  )
}

export default App
