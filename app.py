import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="Fresh vs Rotten Mango Classifier",
    page_icon="🥭",
    layout="centered"
)

st.title("Fresh vs Rotten Mango Classifier")
st.write(
    "Upload a mango image and the model will predict whether it is **Fresh** or **Rotten**."
)

# -----------------------------
# Load Model
# -----------------------------
@st.cache_resource
def load_model():
    return tf.keras.models.load_model("model/custom_cnn_best.keras")

model = load_model()

# -----------------------------
# Parameters
# -----------------------------
IMG_HEIGHT = 160
IMG_WIDTH = 160

CLASS_NAMES = [
    "Fresh",
    "Rotten"
]

# -----------------------------
# Image Preprocessing
# -----------------------------
def preprocess_image(image):
    image = image.convert("RGB")
    image = image.resize((IMG_WIDTH, IMG_HEIGHT))
    img_array = np.array(image).astype("float32")   # no /255.0
    img_array = np.expand_dims(img_array, axis=0)
    return img_array


# -----------------------------
# Upload Image
# -----------------------------
uploaded_file = st.file_uploader(
    "Choose a mango image",
    type=["jpg", "jpeg", "png","webp"]
)

if uploaded_file is not None:

    image = Image.open(uploaded_file)

    st.image(image, caption="Uploaded Image", use_container_width=True)

    img = preprocess_image(image)

    prediction = model.predict(img)

    # Binary Classification
    if prediction.shape[-1] == 1:

        probability = float(prediction[0][0])

        if probability >= 0.5:
            predicted_class = "Rotten"
            confidence = probability
        else:
            predicted_class = "Fresh"
            confidence = 1 - probability

    # Two-node Softmax Output
    else:

        index = np.argmax(prediction)

        predicted_class = CLASS_NAMES[index]
        confidence = prediction[0][index]

    st.subheader("Prediction")

    if predicted_class == "Fresh":
        st.success(f"{predicted_class}")
    else:
        st.error(f"{predicted_class}")

    st.write(f"**Confidence:** {confidence*100:.2f}%")
