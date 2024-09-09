import { useEffect } from 'react';
import { useForm } from 'react-hook-form'
import { crearConductor, eliminarConductor, actualizarConductor, getConductor } from '../api/conductores.api'
import { useNavigate, useParams } from 'react-router-dom'

export function FormularioConductores() {
    const navigate = useNavigate();
    const params = useParams();

    const {
        register,
        handleSubmit,
        formState: { errors },
        setValue
    } = useForm();

    const onSubmit = handleSubmit(async data => {
        if (params.id) {
            await actualizarConductor(params.id, data)
        } else {
            await crearConductor(data)
        }
        navigate("/conductores")
    });

    useEffect(() => {
        async function loadConductor() {
            if (params.id) {
                const res = await getConductor(params.id);
                console.log(res)
                setValue('documento', res.data.documento)
                setValue('tipo_documento', res.data.tipo_documento)
                setValue('nombre_completo', res.data.nombre_completo)
                setValue('legajo_vial', res.data.legajo_vial)
            }
        }
        loadConductor();
    }, [])

    return (
        <div>
            <form onSubmit={onSubmit}>
                <div>
                    <label>Documento:</label>
                    <input
                        type="number"
                        name="documento"
                        {...register("documento", { required: true })}
                        required
                    />
                </div>
                <div>
                    <label>Tipo de Documento:</label>
                    <input
                        type="text"
                        name="tipo_documento"
                        {...register("tipo_documento", { required: true })}
                        required
                    />
                </div>
                <div>
                    <label>Nombre Completo:</label>
                    <input
                        type="text"
                        name="nombre_completo"
                        {...register("nombre_completo", { required: true })}
                        required
                    />
                </div>
                <div>
                    <label>Legajo Vial:</label>
                    <input
                        type="text"
                        name="legajo_vial"
                        {...register("legajo_vial", { required: true })}
                        required
                    />
                </div>
                <button type="submit">Crear Conductor</button>
            </form>
            {params.id && <button onClick={async () => {
                const accepted = window.confirm("Estas seguro?");
                if (accepted) {
                    await eliminarConductor(params.id);
                    navigate("/conductores");
                }
            }}>Eliminar</button>}
        </div>
    )
}
