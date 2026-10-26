import React from "react";

const Map = ({ locations }) => {
  return (
    <div className="map">
      {locations.length > 0 ? (
        <ul>
          {locations.map((loc, index) => (
            <li key={index}>
              {loc.name}: {loc.lat}, {loc.lng}
            </li>
          ))}
        </ul>
      ) : (
        <p>No locations to display.</p>
      )}
    </div>
  );
};

export default Map;
