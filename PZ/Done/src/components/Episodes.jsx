import React, { useState, useEffect } from "react";
import Episode from "./Episode";

function Episodes() {
  function addEpisode({ id, name, air_date, episode }) {
    return (
      <Episode key={id} id={id} name={name} status={episode} type={air_date} />
    );
  }

  const [episodes, setEpisodes] = useState([]);

  useEffect(() => {
    fetch("https://rickandmortyapi.com/api/episode")
      .then((response) => {
        if (!response.ok) {
          throw new Error(`HTTP status: ${response.status}`);
        }
        return response.json();
      })
      .then((data) => {
        console.log(data.results);
        setEpisodes(data.results); // <---------
      })
      .catch((error) => {
        console.error("Error fetching Episodes:", error);
      });
  }, []); // Pusty array dependency powoduje, że fetch zostanie wykonany tylko raz po zamontowaniu komponentu

  return <div>{episodes.map((episode) => addEpisode(episode))}</div>;
}

export default Episodes;
