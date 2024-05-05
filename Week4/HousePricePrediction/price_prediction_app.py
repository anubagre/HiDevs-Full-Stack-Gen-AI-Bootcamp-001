import pickle
import streamlit as st

st.title("House Price Prediction")

with open('model_rfr.pkl', 'rb') as file:
    model=pickle.load(file)

area=float(st.text_input("Enter Area of House in Square-Feet:"))
bhk=int(st.text_input("Enter BHK Value:"))
bath=int(st.text_input("Enter number of Bathrooms:"))
prk=int(st.text_input("Enter number of Parkings:"))
sta=int((st.text_input("Enter 1 if house is 'Ready to Move'\nEnter 0 if house is 'Almost Ready':")))
if sta!=0 or sta!=1:
    st.write("Invalid Input")
trn=int((st.text_input("Enter 1 if house is 'New Property'\nEnter 0 if house is for 'Resale':")))
if trn!=0 or trn!=1:
    st.write("Invalid Input")
typ=int((st.text_input("Enter 1 if house is 'Apartment'\nEnter 0 if house is 'Builder Floor':")))
if typ!=0 or typ!=1:
    st.write("Invalid Input")
input=[area,bhk,bath,prk,sta,trn,typ]
bt=st.button("Predict Price")
if bt:
    st.write("Predicted Price of House(in Lakhs):",model.predict(input))