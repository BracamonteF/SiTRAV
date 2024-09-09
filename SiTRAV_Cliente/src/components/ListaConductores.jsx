import React from 'react'
import { useEffect, useState } from 'react'
import { getAllConductores } from '../api/conductores.api'
import { CardConductor } from './CardConductor';

export function ListaConductores() {

  const [conductores, setConductores] = useState([]);
  useEffect(() => {
    async function cargarConductores() {
      const res = await getAllConductores()
      console.log(res)
      setConductores(res.data)
    }
    cargarConductores()
  }, [])
  return (
    <div>{conductores.map(conductor => (
      <CardConductor key={conductor.id} conductor={conductor}/>
    ))}</div>
  )
}