# PE-5-Fresh-Mango-vs-Rotten-Mango

# Contibutors REG NO.:
## 23/EG/PE/004
## 22/EG/PE/1544
## 22/EG/PE/1514
## 23/EG/PE/024
## 22/EG/PE/1474
## 22/EG/PE/1524
#  Fresh vs Rotten Mango Classification

A deep learning project that classifies mangoes as **Fresh** or **Rotten** using a Convolutional Neural Network (CNN) built with TensorFlow/Keras. The notebook includes dataset preparation, data cleaning, duplicate image detection, data augmentation, model training, and evaluation.

---

##  Project Overview

This project develops an image classification model capable of distinguishing between fresh and rotten mangoes.

The workflow includes:

- Downloading the dataset from Kaggle
- Exploring the dataset structure
- Detecting filename collisions
- Identifying duplicate images
- Cleaning and organizing the dataset
- Loading images into TensorFlow datasets
- Optimizing the data pipeline
- Applying data augmentation
- Building a custom CNN model
- Training the model
- Evaluating model performance

---

##  Project Structure

```
.
├── Fresh_Mango_vs_rotten_mango.ipynb
├── mango_clean_split/
│   ├── train/
│   │   ├── fresh/
│   │   └── rotten/
│   ├── validation/
│   │   ├── fresh/
│   │   └── rotten/
│   └── test/
│       ├── fresh/
│       └── rotten/
└── README.md
```

---

## 🗂 Dataset

The notebook downloads the **fruitquality1** dataset from Kaggle using `kagglehub`.

The project focuses only on the **mango** subset.

Images are organized into two classes:

- Fresh
- Rotten

---

##  Features

- Automatic dataset download
- Dataset inspection
- Duplicate image detection
- Filename collision detection
- Dataset cleaning
- TensorFlow data pipelines
- Data augmentation
- Custom CNN architecture
- Model evaluation

---

## 🛠 Technologies Used

- Python 3.x
- TensorFlow / Keras
- NumPy
- Matplotlib
- KaggleHub
- OS utilities
- Hashlib

---

# Installation

## 1. Clone the repository

```bash
git clone https://github.com/yourusername/fresh-vs-rotten-mango.git

cd fresh-vs-rotten-mango
```

---

## 2. Create a virtual environment (Recommended)

### Windows

```bash
python -m venv venv

venv\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv venv

source venv/bin/activate
```

---

## 3. Install dependencies

```bash
pip install tensorflow
pip install matplotlib
pip install numpy
pip install kagglehub
pip install notebook
```

Or install everything at once:

```bash
pip install tensorflow matplotlib numpy kagglehub notebook
```

---

## 4. Configure Kaggle Credentials

Create a Kaggle account if you don't already have one.

Download your `kaggle.json` API credentials from your Kaggle account and place them in:

**Linux/macOS**

```
~/.kaggle/kaggle.json
```

**Windows**

```
C:\Users\<username>\.kaggle\kaggle.json
```

---

# Running the Project

Start Jupyter Notebook:

```bash
jupyter notebook
```

Open:

```
Fresh_Mango_vs_rotten_mango.ipynb
```

streamlit deployment:

```
pip install streamlit
```
```
streamlit run app.py
```

Run every cell sequentially.

The notebook will:

1. Download the dataset
2. Inspect the dataset
3. Detect duplicate images
4. Clean the dataset
5. Create training, validation, and test datasets
6. Apply data augmentation
7. Build the CNN model
8. Train the model
9. Evaluate model performance

---

## Model Pipeline

```
Dataset Download
        │
        ▼
Dataset Inspection
        │
        ▼
Duplicate Detection
        │
        ▼
Dataset Cleaning
        │
        ▼
Train / Validation / Test Split
        │
        ▼
Image Preprocessing
        │
        ▼
Data Augmentation
        │
        ▼
Custom CNN
        │
        ▼
Training
        │
        ▼
Evaluation
```

---

## Hyperparameters

The notebook defines image preprocessing parameters including:

- Image height
- Image width
- Batch size
- Data augmentation layers

These values can be modified directly in the notebook to experiment with different configurations.

---

## Data Augmentation

The project improves model generalization using augmentation techniques such as:

- Random horizontal flipping
- Random rotation
- Random translation

---

## Model Architecture

A custom Convolutional Neural Network (CNN) is implemented using TensorFlow/Keras.

The network consists of:

- Convolutional layers
- Pooling layers
- Dense layers
- Dropout (if configured)
- Softmax/Sigmoid output layer for binary classification

---

## Evaluation

After training, the notebook evaluates the model on the validation dataset and reports metrics such as:

- Validation Accuracy
- Validation Loss

Additional evaluation or visualization can be added if desired.

---

## Future Improvements

- Transfer Learning (EfficientNet, MobileNetV2, ResNet50)
- Early stopping
- Learning rate scheduling
- Model checkpointing
- TensorBoard logging

---

## License

This project is intended for educational and research purposes.

---

## Author

Developed as a deep learning image classification project for identifying fresh and rotten mangoes using TensorFlow and Keras.