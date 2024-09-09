import { Link } from "react-router-dom";

export function Navigation() {
  return (
    <div>
        <Link to="/conductores">Condcutores</Link>
        <Link to="/conductores-crear">Crear Conductores</Link>
    </div>   
  )
}
