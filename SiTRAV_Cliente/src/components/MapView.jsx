import React from 'react';
import { MapContainer, TileLayer, Marker, Popup, Polyline } from 'react-leaflet';
import 'leaflet/dist/leaflet.css';

// Si tienes problemas con los iconos de marcador, añade estas líneas
import L from 'leaflet';
import icon from 'leaflet/dist/images/marker-icon.png';
import iconShadow from 'leaflet/dist/images/marker-shadow.png';

let DefaultIcon = L.icon({
  iconUrl: icon,
  shadowUrl: iconShadow
});

L.Marker.prototype.options.icon = DefaultIcon;

const MapView = () => {
  const position = [-51.6230, -69.2168]; // Latitud y longitud iniciales

  const routeCoordinates = [
    [-51.623, -69.216],
    [-51.6218, -69.2166],
    [-51.6206, -69.2171],
    [-51.6195, -69.2177],
    [-51.6183, -69.2182],
    [-51.6171, -69.2188],
    [-51.6159, -69.2193],
    [-51.6148, -69.2199],
    [-51.6136, -69.2205],
    [-51.6124, -69.2210]
  ];

  return (
    <MapContainer center={position} zoom={13} style={{ height: "100vh", width: "100vw" }}>
      <TileLayer
        url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
        attribution='&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
      />
      <Marker position={position}>
        <Popup>
          A pretty CSS3 popup. <br /> Easily customizable.
        </Popup>
      </Marker>
      <Polyline
        positions={routeCoordinates}
        color="red"
        weight={5}
      />
    </MapContainer>
  );
};

export default MapView;