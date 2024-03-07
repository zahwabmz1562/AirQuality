import streamlit as st 
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import plotly.colors as PC


url = 'Data/merged_data.csv'
data = pd.read_csv(url)
data['month'] = pd.to_datetime(data['month'])

st.title('Air Quality Dashboard 2024')
with st.sidebar:
    col1, col2, col3 = st.columns(3)
    with col1:
        st.write(' ')
    with col2:
        st.image("https://cdn1.iconfinder.com/data/icons/air-pollution-21/62/Air-quality-mask-pollution-protection-256.png"
                 , width=100)
    with col3:
        st.write(' ')
    st.header('Filters')


import matplotlib.pyplot as plt
import seaborn as sns



# Memilih kolom yang ingin ditampilkan dalam heatmap
selected_columns = ['PM2.5', 'PM10', 'SO2', 'NO2', 'CO', 'O3']

# Fungsi untuk membuat heatmap
def create_heatmap():
    plt.figure(figsize=(12, 6))
    sns.heatmap(data[selected_columns].corr(), annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5)
    plt.title('Heatmap Korelasi Parameter Udara')
    st.pyplot()

# Fungsi untuk membuat plot lainnya
def create_other_plot():
    # Implementasi plot lainnya di sini
    st.write("")

# Membuat tombol untuk beralih antara heatmap dan plot lainnya
if st.button("Tampilkan Heatmap"):
    create_heatmap()
else:
    create_other_plot()

import warnings
warnings.filterwarnings('ignore')
st.set_option('deprecation.showPyplotGlobalUse', False)

# Memilih kolom yang ingin ditampilkan dalam boxplot
selected_columns = ['PM2.5', 'PM10', 'SO2', 'NO2', 'CO', 'O3']

# Memilih kolom yang ingin ditampilkan dalam boxplot
selected_columns = ['PM2.5', 'PM10', 'SO2', 'NO2', 'CO', 'O3']

# Fungsi untuk membuat boxplot
def create_boxplot():
    plt.figure(figsize=(12, 6))
    sns.boxplot(data=data[selected_columns], palette='Set3')
    plt.title('Boxplot Parameter Udara')
    st.pyplot()

# Fungsi untuk membuat visualisasi lainnya
def create_other_visualization():
    # Implementasi visualisasi lainnya di sini
    st.write("")

# Membuat tombol untuk beralih antara boxplot dan visualisasi lainnya
if st.button("Tampilkan Boxplot"):
    create_boxplot()
else:
    create_other_visualization()



