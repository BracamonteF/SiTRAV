import { useNavigate } from "react-router-dom"

export function CardConductor({conductor}) {
    const navigate = useNavigate();

    return (
        <div 
        style={{background: "grey"}}
        onClick={() => {
            navigate(`/conductores/${conductor.id}`)
        }}>
            <h1>{conductor.nombre_completo}</h1>
            <p>{conductor.legajo_vial}</p>
            <p>{conductor.tipo_documento}: {conductor.documento}</p>
        </div>
        )
}