import React, { useState, useEffect } from "react";
import A1 from "./Location";
import Character from "./Character";

function Characters() {
  function addCharacter({ id, name, status, type, image }) {
    return (
      <Character key={id} id={id} name={name} status={status} type={type} image={image} />
    );
  }

  const [characters, setCharacters] = useState([]);

  useEffect(() => {
    fetch("https://rickandmortyapi.com/api/character")
      .then((response) => {
        if (!response.ok) {
          throw new Error(`HTTP status: ${response.status}`);
        }
        return response.json();
      })
      .then((data) => {
        console.log(data.results);
        setCharacters(data.results); // <---------
      })
      .catch((error) => {
        console.error("Error fetching characters:", error);
      });
  }, []); // Pusty array dependency powoduje, że fetch zostanie wykonany tylko raz po zamontowaniu komponentu

  return <div>{characters.map((character) => addCharacter(character))}</div>;
}

export default Characters;
