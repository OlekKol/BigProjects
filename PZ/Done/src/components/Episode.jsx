import React from "react";

function Episode(props) {
  return (
    <div>
      <p>id: {props.id}</p>
      <p>name: {props.name}</p>
      <p>air_date {props.air_date}</p>
      <p>episode {props.episode}</p>
    </div>
  );
}

export default Episode;
