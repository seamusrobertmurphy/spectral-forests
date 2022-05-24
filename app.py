import ee 
import streamlit as st 
import geemap.foliumap as geemap

WIDTH = 1060
HEIGHT = 600

def app():
    st.title("Active Fires Map")
    
    Map = geemap.Map(center=(49, -120), zoom=6.5)
    Map.add_basemap('CartoDB.Positron')
    dataset_inz = ee.ImageCollection('FIRMS')
    image2 = dataset_inz.first()
    Map.addLayer(image2, {}, 'Active Fires:FIRMS')
    Map