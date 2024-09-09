import React, { useEffect, useState } from 'react';
import axios from 'axios';

const MiComponente = () => {
  const [data, setData] = useState([]);

  useEffect(() => {
    axios.get('http://localhost/api/endpoint/')
      .then(response => {
        setData(response.data);
      })
      .catch(error => {
        console.error('Error:', error);
      });
  }, []); // [] asegura que la petición se realice solo una vez al montar el componente

  return (
    <div>
      {data.map(item => (
        <div key={item.id}>{item.nombre}</div>
      ))}
    </div>
  );
};

export default MiComponente;