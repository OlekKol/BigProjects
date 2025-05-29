import React, { useEffect, useState } from "react";

const JokeComponent = () => {
  const [joke, setJoke] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  
  useEffect(() => {
    const fetchJoke = async () => {
      try {
        const response = await fetch("https://v2.jokeapi.dev/joke/Programming?type=any");
        const data = await response.json();

        if (data.error) {
          throw new Error("JokeAPI returned an error");
        }

        setJoke(data);
      } catch (err) {
        setError(err.message);
      } finally {
        setLoading(false);
      }
    };

    fetchJoke();
  }, []);

  if (loading) return <p>Loading joke...</p>;
  if (error) return <p>Error: {error}</p>;

  return (
    <div className="joke">
      {joke.type === "single" ? (
        <p>{joke.joke}</p>
      ) : (
        <div>
          <p className="setup">{joke.setup}</p>
          <p className="delivery">{joke.delivery}</p>
        </div>
      )}
    </div>
  );
};

export default JokeComponent;