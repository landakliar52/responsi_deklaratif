import streamlit as st

# Judul dan deskripsi aplikasi
st.title("Formulir Deteksi Virus Corona")
st.write("Isilah formulir berikut untuk mendeteksi kemungkinan terinfeksi COVID-19.")

# Informasi pribadi
st.header("Informasi Pribadi")
name = st.text_input("Nama")
age = st.number_input("Usia", min_value=0)
gender = st.selectbox("Jenis Kelamin", ["Laki-laki", "Perempuan", "Lainnya"])

# Gejala
st.header("Gejala")
fever = st.checkbox("Demam")
cough = st.checkbox("Batuk kering")
shortness_of_breath = st.checkbox("Sesak napas atau kesulitan bernapas")
fatigue = st.checkbox("Kelelahan")
sore_throat = st.checkbox("Sakit tenggorokan")
muscle_pain = st.checkbox("Nyeri otot atau badan terasa sakit")
loss_of_smell_taste = st.checkbox("Kehilangan indera penciuman atau perasa")
headache = st.checkbox("Sakit kepala")
diarrhea = st.checkbox("Diare")
nausea_vomiting = st.checkbox("Mual atau muntah")
nasal_congestion = st.checkbox("Hidung tersumbat atau pilek")

# Kontak dengan Orang yang Terinfeksi
st.header("Kontak dengan Orang yang Terinfeksi")
contact_with_infected = st.radio(
    "Apakah Anda pernah kontak dengan seseorang yang terinfeksi COVID-19?",
    ("Tidak", "Ya", "Tidak yakin")
)
if contact_with_infected == "Ya":
    contact_duration = st.slider(
        "Berapa lama durasi kontak tersebut? (dalam menit)", 
        min_value=0, max_value=120, step=5, value=0
    )
    contact_location = st.radio(
        "Apakah kontak terjadi di dalam ruangan tertutup?",
        ("Tidak", "Ya")
    )

# Riwayat Perjalanan
st.header("Riwayat Perjalanan")
travel_history = st.radio(
    "Apakah Anda baru saja melakukan perjalanan ke daerah berisiko tinggi?",
    ("Tidak", "Ya")
)
if travel_history == "Ya":
    transportation_mode = st.selectbox(
        "Moda transportasi apa yang Anda gunakan?",
        ["Pesawat", "Kereta Api", "Bus", "Mobil Pribadi", "Lainnya"]
    )
    stayed_in_high_risk_area = st.radio(
        "Apakah Anda tinggal di daerah dengan tingkat penyebaran tinggi?",
        ("Tidak", "Ya")
    )

# Kondisi Kesehatan yang Ada
st.header("Kondisi Kesehatan yang Ada")
chronic_conditions = st.multiselect(
    "Apakah Anda memiliki kondisi kesehatan kronis?",
    ["Diabetes", "Penyakit Jantung", "Penyakit Paru-paru", "Sistem Kekebalan yang Lemah", "Lainnya"]
)
pregnancy = st.radio("Apakah Anda memiliki riwayat penyakit atau sedang mengonsumsi obat yang dapat mempengaruhi sistem kekebalan tubuh Anda?", ("Tidak", "Ya"))
immune_weakness = st.radio("Apakah Anda sedang mengonsumsi obat yang dapat mempengaruhi sistem kekebalan tubuh?", ("Tidak", "Ya"))

# Tombol Submit
if st.button("Submit"):
    # Logika deteksi sederhana
    risk_score = 0
    
    # Penilaian berdasarkan gejala
    if fever:
        risk_score += 1
    if cough:
        risk_score += 1
    if shortness_of_breath:
        risk_score += 2
    if fatigue:
        risk_score += 1
    if sore_throat:
        risk_score += 1
    if muscle_pain:
        risk_score += 1
    if loss_of_smell_taste:
        risk_score += 2
    if headache:
        risk_score += 1
    if diarrhea:
        risk_score += 1
    if nausea_vomiting:
        risk_score += 1
    if nasal_congestion:
        risk_score += 1
    
    # Penilaian berdasarkan kontak
    if contact_with_infected == "Ya":
        risk_score += 2
        if contact_duration > 15:
            risk_score += 1  # Tambah risiko jika durasi kontak > 15 menit
        if contact_location == "Ya":
            risk_score += 1  # Tambah risiko jika terjadi di ruangan tertutup
    elif contact_with_infected == "Tidak yakin":
        risk_score += 1

    # Penilaian berdasarkan riwayat perjalanan
    if travel_history == "Ya":
        risk_score += 2
        if transportation_mode in ["Pesawat", "Kereta Api", "Bus"]:
            risk_score += 1  # Tambah risiko jika menggunakan transportasi umum
        if stayed_in_high_risk_area == "Ya":
            risk_score += 1  # Tambah risiko jika tinggal di daerah berisiko tinggi

    # Penilaian berdasarkan kondisi kesehatan yang ada
    if "Diabetes" in chronic_conditions:
        risk_score += 1
    if "Penyakit Jantung" in chronic_conditions:
        risk_score += 1
    if "Penyakit Paru-paru" in chronic_conditions:
        risk_score += 1
    if "Sistem Kekebalan yang Lemah" in chronic_conditions:
        risk_score += 1
    if pregnancy == "Ya":
        risk_score += 1
    if immune_weakness == "Ya":
        risk_score += 1

    # Menentukan hasil
    if risk_score >= 5:
        st.error("Hasil: Positif - Risiko tinggi infeksi COVID-19. Silakan konsultasi dengan tenaga medis.")
    else:
        st.success("Hasil: Negatif - Risiko rendah infeksi COVID-19. Tetap jaga kesehatan dan ikuti protokol kesehatan.")

# Simpan file ini sebagai `corona_detection.py` atau nama lain sesuai keinginan Anda.
