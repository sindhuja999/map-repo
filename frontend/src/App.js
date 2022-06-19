import logo from './logo.svg';
import React from "react";
import { Route, Routes } from "react-router-dom";
import { endPoints } from './constants';
import { MapsComponent } from './mapsComponent'
import { HomeComponent } from './homeComponent';
import './App.css';
  const RouterComponent = () => {
    return (
      <div>
      <header className="App-header">
        <Routes>
            <Route path="/" element={<HomeComponent />} />
            <Route path={endPoints.maps_url} element={<MapsComponent/>} />
        </Routes>
        </header>
        </div>
    );
}
export default RouterComponent;
