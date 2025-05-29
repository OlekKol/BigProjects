import React from "react";
import ReactDOM from "react-dom/client";
import "./scss/main.css";
// ---------------------------------------
import { BrowserRouter, Routes, Route, Link } from "react-router-dom";
// ---------------------------------------


import Header from "./components/Header";
import "./components/Locations";
import Locations from "./components/Locations";
import Characters from "./components/Characters";
import Episodes from "./components/Episodes";
import Glowna from "./components/Glowna";
import Chess from "./components/Chess";
import JC from "./components/JokeComponent";
import STMILB from "./components/SmthThatMakesItLookBetter";


ReactDOM.createRoot(document.getElementById("root")).render(
  <React.StrictMode>
    <Header />
    <BrowserRouter>
      <nav>
        <ul>
          <STMILB />
          <li>
            <Link to="/a1">LOCATIONS - mialem to dożucilem</Link>
          </li>
          <STMILB />
          <li>
            <Link to="/a2">CHARACTERS - mialem to dożucilem</Link>
          </li>
          <STMILB />
          <li>
            <Link to="/a3">EPISODES - mialem to dożucilem</Link>
          </li>
          <STMILB />
          <li>
            <Link to="/a4">str.glowna</Link>
            
          </li>
          <STMILB />
          <li>
            <Link to="/a5">Strona z zartami</Link>
          </li>
          <STMILB />
          <li>
            <Link to="/a6">Chess</Link>
          </li>
          <STMILB />

        </ul>
      </nav>
      <Routes>
        <Route path="/a1" element={<Locations />} />
        <Route path="/a2" element={<Characters />} />
        <Route path="/a3" element={<Episodes />} />
        <Route path="/a4" element={<Glowna />} />
        <Route path="/a5" element={<JC />} />
        <Route path="/a6" element={<Chess />} />
      </Routes>
    </BrowserRouter>
  </React.StrictMode>
);
