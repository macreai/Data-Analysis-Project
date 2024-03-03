import streamlit as st
from matplotlib.patches import Patch
import matplotlib.pyplot as plt
import seaborn as sns
import pickle
import os

st.set_page_config(layout="wide")

# Dapatkan path dari direktori saat ini (direktori tempat file Python berada)
current_directory = os.path.dirname(__file__)

# Gabungkan path relatif dengan nama file pickle
file_path_corr_matrix = os.path.join(current_directory, "correlation_matrix.pkl")

# Buka file pickle menggunakan path relatif
with open(file_path_corr_matrix, "rb") as f:
    correlation_matrix = pickle.load(f)

# Suppress deprecation warning
st.set_option('deprecation.showPyplotGlobalUse', False)

# Set up Streamlit page title dan description
st.title('Visualisasi Data Polusi Udara')
st.write("""
    Berikut adalah visualisasi data polusi berdasarkan data PM2.5, PM10, SO2, NO2, CO, TEMP, PRES, DEWP, RAIN, wd, WSPM yang berada di 12 stasiun yang berbeda, yaitu Aotizhongxin, Changping, Dinlin, Dongsi, Guanyuan, Gucheng, Huairou, Nongzhanguan, Shunyi, Tianta, Wanliu, dan Wanshouxigong.
""")
with st.expander("Informasi mengenai masing-masing data:"):
    """
    - **PM2.5:** Partikulat Matter 2.5 adalah ukuran partikulat matter berukuran 2.5 mikrometer atau lebih kecil, yang dapat mencakup debu, asap, dan partikel kecil lainnya. PM2.5 dapat mencapai saluran pernapasan terdalam dalam paru-paru dan berpotensi menyebabkan masalah kesehatan.
    
    - **PM10:** Partikulat Matter 10 adalah ukuran partikulat matter berukuran 10 mikrometer atau lebih kecil. PM10 dapat mencakup debu, asap, serbuk sari, dan partikel besar lainnya. Paparan PM10 juga dapat memiliki efek negatif pada kesehatan manusia, terutama pada saluran pernapasan.
    
    - **SO2:** Dioksida belerang adalah gas beracun yang berasal dari pembakaran bahan bakar fosil seperti batu bara dan minyak. Paparan jangka pendek terhadap SO2 dapat menyebabkan iritasi pada mata dan saluran pernapasan, sedangkan paparan jangka panjang dapat menyebabkan masalah pernapasan dan masalah kesehatan lainnya.
    
    - **NO2:** Dioksida nitrogen adalah gas beracun yang berasal dari aktivitas pembakaran, seperti kendaraan bermotor dan pembangkit listrik. Paparan NO2 dapat menyebabkan iritasi pada saluran pernapasan, memperburuk kondisi seperti asma, dan berkontribusi pada pembentukan kabut asap.
    
    - **CO:** Karbon monoksida adalah gas beracun yang dihasilkan dari pembakaran bahan bakar fosil. Paparan CO dapat menyebabkan keracunan, dengan gejala mulai dari sakit kepala dan pusing hingga kematian.
    
    - **TEMP:** Suhu adalah pengukuran panas atau dinginnya udara. Fluktuasi suhu dapat mempengaruhi kenyamanan manusia, pertumbuhan tanaman, dan pola cuaca.
    
    - **PRES:** Tekanan atmosfer adalah gaya yang diberikan oleh udara pada permukaan atau objek. Perubahan tekanan atmosfer dapat mengindikasikan perubahan cuaca dan iklim.
    
    - **DEWP:** Titik embun adalah suhu di mana udara jenuh dengan uap air, yang menyebabkan embun atau kondensasi terbentuk pada permukaan yang lebih dingin.
    
    - **RAIN:** Hujan adalah curah hujan yang diukur dalam milimeter atau inci. Curah hujan dapat mempengaruhi pola tanam, pasokan air, dan risiko banjir.
    
    - **wd:** Arah angin adalah arah dari mana angin bertiup. Arah angin dapat mempengaruhi kondisi cuaca dan pola aliran udara.
    
    - **WSPM:** Kecepatan angin adalah kecepatan dari arah angin. Angin yang lebih kencang dapat mempengaruhi suhu, cuaca, dan transportasi debu atau polutan lainnya.
    """
st.write("""
    Dari data ini timbul pertanyaan yaitu:
""")


# Split page 2 columns
col1, col2 = st.columns(2)

# Visualisasi correlation matrix 
with col1:
    st.markdown('Bagaimana pengaruh lingkungan terhadap polusi?')
    plt.figure(figsize=(8, 6))
    sns.heatmap(correlation_matrix[['PM10', 'PM2.5']], annot=True, cmap='coolwarm', fmt=".2f", linewidths=0.5)
    plt.title('Korelasi antara PM10 dan PM2.5 dengan Fitur Lainnya')       
    st.pyplot()
    with st.expander("Kesimpulan"):
        """
        1. Terdapat korelasi yang sangat tinggi antara PM2.5 dan PM10, seperti yang ditunjukkan oleh nilai 0.87. Ini menunjukkan bahwa ketika tingkat PM10 berubah, tingkat PM2.5 cenderung berubah dengan cara yang serupa.

        2. Baik PM10 maupun PM2.5 menunjukkan korelasi positif sedang hingga kuat dengan CO (Karbon Monoksida), NO2 (Nitrogen Dioksida), dan SO2 (Sulfur Dioksida), dengan nilai berkisar antara 0.44 dan 0.74. Ini mengindikasikan bahwa konsentrasi yang lebih tinggi dari PM10 dan PM2.5 sering kali terkait dengan konsentrasi yang lebih tinggi dari gas-gas tersebut.

        3. Ozon (O3) memiliki korelasi negatif yang sedikit dengan baik PM10 maupun PM2.5, yang menyiratkan bahwa tingkat ozon yang lebih tinggi mungkin terkait dengan konsentrasi materi partikulat yang lebih rendah.

        4. Suhu (TEMP), tekanan (PRES), dan arah angin (wd) memiliki korelasi negatif yang sangat rendah dengan PM10 dan PM2.5, menunjukkan hampir tidak ada hubungan linear.

        5. Kecepatan angin (WSPM) menunjukkan korelasi negatif yang sedikit hingga sedang dengan PM10 dan PM2.5, yang bisa berarti bahwa kecepatan angin yang lebih tinggi mungkin terkait dengan tingkat materi partikulat yang lebih rendah karena dispersi.

        6. Hujan (RAIN) dan titik embun (DEWP) memiliki korelasi yang sangat rendah hingga sedikit positif dengan PM10 dan PM2.5, tetapi korelasi ini sangat lemah sehingga menunjukkan sedikit atau tidak ada hubungan linear."""

    
# Gabungkan path relatif dengan nama file pickle
file_path_statition_means = os.path.join(current_directory, "station_means_renamed_dict.pkl")

# Buka file pickle menggunakan path relatif
with open(file_path_statition_means, "rb") as f:
    station_means = pickle.load(f)

# Extract data untuk visualization
labels = list(station_means.keys())
values1 = [val[0] for val in station_means.values()]  
values2 = [val[1] for val in station_means.values()]

# Plotting
fig, ax = plt.subplots(figsize=(8, 6))

bar_width = 0.35
opacity = 0.8

bars1 = plt.bar(range(len(station_means)), values1, bar_width, alpha=opacity, color='brown', label='PM2.5')
bars2 = plt.bar([p + bar_width for p in range(len(station_means))], values2, bar_width, alpha=opacity, color='yellow', label='PM10')

# Highlight most polluted dan least polluted stations
most_polluted_station = "Gucheng"
least_polluted_station = "Dingling"
for i, label in enumerate(labels):
    if label == most_polluted_station:
        ax.get_xticklabels()[i].set_color('red')
    elif label == least_polluted_station:
        ax.get_xticklabels()[i].set_color('blue')

plt.xlabel('Station')
plt.ylabel('PM')
plt.title('PM by Station')
plt.xticks([p + 0.5 * bar_width for p in range(len(station_means))], labels, rotation=45)
legend_elements = [Patch(facecolor='red', edgecolor='red', label='Most Polluted'),
                   Patch(facecolor='blue', edgecolor='blue', label='Least Polluted'),
                   Patch(facecolor='brown', edgecolor='blue', label='PM2.5'),
                   Patch(facecolor='yellow', edgecolor='blue', label='PM10'),
                   ]
plt.legend(handles=legend_elements)

plt.tight_layout()

# Display plot
with col2:
    st.markdown('Stasiun mana yang paling sedikit polusi dan paling banyak polusi?')
    st.pyplot(fig)
    with st.expander("Kesimpulan"):
        """
        1. Stasiun yang bernama sebagai "Gucheng" memiliki tingkat PM2.5 dan PM10 yang tertinggi yang tercatat, menjadikannya stasiun "Paling Terpolusi".

        2. Stasiun yang bernama sebagai "Dingling" memiliki tingkat PM2.5 dan PM10 yang terendah yang tercatat, sehingga stasiun ini ditetapkan sebagai "Paling Sedikit Terpolusi."

        3. Untuk sebagian besar stasiun, tingkat PM10 secara konsisten lebih tinggi daripada tingkat PM2.5.

        4. Tingkat materi polusi bervariasi secara signifikan di berbagai stasiun. Misalnya, sementara "Gucheng" menunjukkan tingkat polusi yang sangat tinggi, "Dingling" menunjukkan tingkat yang jauh lebih rendah.

        5. Grafik menunjukkan tren umum di mana beberapa stasiun memiliki tingkat PM2.5 dan PM10 yang relatif serupa, sementara yang lain memiliki perbedaan yang lebih jelas antara kedua ukuran materi polusi ini."""
