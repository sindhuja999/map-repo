import React from "react";
import { ReactDOM } from "react";
import { render } from 'react-dom'

export class CurrentLocation extends React.Component {
    recenterMap() {
        const map = this.map;
        const current = this.state.currentLocation;
        const google = this.props.google;
        const maps = google.maps;
    
        if (map) {
          let center = new maps.LatLng(current.lat, current.lng);
          map.panTo(center);
        }
      }
    componentDidMount() {
    if (this.props.centerAroundCurrentLocation) {
      if (navigator && navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(pos => {
          const coords = pos.coords;
          this.setState({
            currentLocation: {
              lat: coords.latitude,
              lng: coords.longitude
            }
          });
        });
      }
    }
    this.loadMap();
  }
    loadMap() {
      if (this.props && this.props.google) {
        // checks if google is available
        const { google } = this.props;
        const maps = google.maps;
  
        const mapRef = this.refs.map;
  
        // reference to the actual DOM element
        const node = ReactDOM.findDOMNode(mapRef);
  
        let { zoom } = this.props;
        const { lat, lng } = this.state.currentLocation;
        const center = new maps.LatLng(lat, lng);
  
        const mapConfig = Object.assign(
          {},
          {
            center: center,
            zoom: zoom
          }
        );
        this.map = new maps.Map(node, mapConfig);
      }
    }
  }