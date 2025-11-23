import streamlit as st
import pickle
import numpy as np
from PIL import Image

pickle_in = open("model.pkl", "rb")
model = pickle.load(pickle_in)

def predict(house_age, distance_to_nearest_metro, no_of_nearby_stores):
    List = [house_age, distance_to_nearest_metro, no_of_nearby_stores]
    array = np.array(List, np.float64)
    prediction = model.predict([array])
    return prediction

def main():
    st.title("HOUSE_PRICE-PREDICTION")

    template = """
    <div style="background-color: black; padding: 10px; font-size:23px;">
        <h1 style="color:white; text-align:center;"> HOUSE PRICE PREDICTION </h1>
    </div>
    """
    st.markdown(template, unsafe_allow_html=True)

    img = Image.open("beautiful-exterior-home-pictures-new-home-design-images-modern-best-house-design-images-best-house-images-images-latest-168696855.webp")
    st.image(img, width=300, caption="House-worth")

    house_age = st.text_input("Houseage", "enter your house age")
    distance_to_nearest_metro = st.text_input("Distance to nearest metro", "enter your nearest metro distance")
    no_of_nearby_stores = st.text_input("No of nearby stores", "enter no.of nearby stores")

    result = ""

    if st.button("predict"):
        result = predict(house_age, distance_to_nearest_metro, no_of_nearby_stores)
        st.success("the house predicted value is {}".format(result))

if __name__ == "__main__":
    main()
