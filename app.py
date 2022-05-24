import streamlit.components.v1 as components
import streamlit as st 
import ee as ee
import geemap as gee
import ipyleaflet as leaflet
import folium as folium
import numpy as np
import pandas as pd
import json



st.title("Active Fires Map")
    
Map = geemap.Map(center=(49, -120), zoom=6.5)
Map.add_basemap('CartoDB.Positron')
dataset_inz = ee.ImageCollection('FIRMS')
image2 = dataset_inz.first()
Map.addLayer(image2, {}, 'Active Fires:FIRMS')
Map