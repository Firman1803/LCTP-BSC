import streamlit as st

# Data soal: pertanyaan, pilihan, dan jawaban benar
soal_list = [
    {
        "pertanyaan": "Ibu kota Indonesia adalah...",
        "pilihan": ["Bandung", "Surabaya", "Jakarta", "Medan"],
        "jawaban": "Jakarta"
    },
    {
        "pertanyaan": "2 + 2 = ...",
        "pilihan": ["3", "4", "5", "6"],
        "jawaban": "4"
    },
    {
        "pertanyaan": "Planet terdekat dengan Matahari adalah...",
        "pilihan": ["Mars", "Venus", "Merkurius", "Bumi"],
        "jawaban": "Merkurius"
    }
]

st.title("Lembar Soal Cerdas Cermat")

# Simpan jawaban pengguna di session
if "jawaban_pengguna" not in st.session_state:
    st.session_state.jawaban_pengguna = {}

# Form pengerjaan soal
with st.form("form_soal"):
    for i, soal in enumerate(soal_list):
        jawaban = st.radio(
            soal["pertanyaan"],
            soal["pilihan"],
            key=f"soal_{i}"
        )
        st.session_state.jawaban_pengguna[i] = jawaban

    submitted = st.form_submit_button("Kumpulkan Jawaban")

# Tampilkan hasil setelah submit
if submitted:
    benar = 0
    st.subheader("Hasil:")
    for i, soal in enumerate(soal_list):
        jawaban_benar = soal["jawaban"]
        jawaban_user = st.session_state.jawaban_pengguna.get(i, "")
        if jawaban_user == jawaban_benar:
            st.write(f"✅ {soal['pertanyaan']} Jawaban Anda: **{jawaban_user}** (Benar)")
            benar += 1
        else:
            st.write(f"❌ {soal['pertanyaan']} Jawaban Anda: **{jawaban_user}**, seharusnya: **{jawaban_benar}**")

    st.success(f"Skor Anda: {benar} dari {len(soal_list)}")
