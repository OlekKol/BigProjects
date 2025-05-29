import React from "react";

function Character(props) {
  return (
    
    <div>
      <div className="redLine"> redLine------------------------------------</div>
    <div>
      <p>id: {props.id}</p>
      <p>name: {props.name}</p>
      <p>status {props.status}</p>
      <img src={props.image} alt="" />
    </div>
      {/* <div className="redLine">redLine</div> */}
    </div>
  );
}

export default Character;
