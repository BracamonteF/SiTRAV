import axios from "axios"

const conductoresApi = axios.create({
    baseURL: "http://localhost:8000/api/conductores/conductores/"
});

export const getAllConductores = () => conductoresApi.get('/');

export const getConductor = (id) => conductoresApi.get(`/${id}/`);

export const crearConductor = (conductor) => conductoresApi.post('/', conductor);

export const eliminarConductor = (id) => conductoresApi.delete(`/${id}/`);

export const actualizarConductor = (id, conductor) => conductoresApi.put(`/${id}/`,
    conductor)