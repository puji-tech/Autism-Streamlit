import pickle
import streamlit as st


# Membaca model-model
gnb_model = pickle.load(open('gnb_model.sav', 'rb'))
svm_model = pickle.load(open('svm_model.sav', 'rb'))


# Judul web
st.title('Klasifikasi Penyakit Autisme')


st.markdown('#### Pertanyaan Ciri-Ciri Perilaku')
st.info("Jawab 0 jika 'Tidak' dan 1 jika 'Iya'")
A1_Score_input = st.selectbox('Apakah Anda sering mendengarkan suara-suara kecil yang orang lain tidak bisa mendengarnya?', ['Iya', 'Tidak'])
A1_Score = 1 if A1_Score_input == 'Iya' else 0

A2_Score_input = st.selectbox('Apakah Anda cenderung fokus pada gambaran keseluruhan suatu hal daripada detail-detail kecil di dalamnya?', ['Iya', 'Tidak'], key='A2')
A2_Score = 1 if A2_Score_input == 'Iya' else 0

A3_Score_input = st.selectbox('Apakah Anda merasa mudah melakukan lebih dari satu tugas atau aktivitas secara bersamaan?', ['Iya', 'Tidak'], key='A3')
A3_Score = 1 if A3_Score_input == 'Iya' else 0

A4_Score_input = st.selectbox('Apakah Anda dapat dengan cepat beralih kembali ke keadaan semula jika mengalami gangguan?', ['Iya', 'Tidak'], key='A4')
A4_Score = 1 if A4_Score_input == 'Iya' else 0

A5_Score_input = st.selectbox('Apakah Anda merasa mudah untuk membaca pesan yang tersirat ketika berbicara dengan seseorang?', ['Iya', 'Tidak'], key='A5')
A5_Score = 1 if A5_Score_input == 'Iya' else 0

A6_Score_input = st.selectbox('Apakah anda mengetahui ketika seseorang mulai bosan dengan pembicaraan yang anda lakukan?', ['Iya', 'Tidak'], key='A6')
A6_Score = 1 if A6_Score_input == 'Iya' else 0

A7_Score_input = st.selectbox('Apakah Anda merasa sulit untuk memahami karakter ketika membaca sebuah cerita?', ['Iya', 'Tidak'], key='A7')
A7_Score = 1 if A7_Score_input == 'Iya' else 0

A8_Score_input = st.selectbox('Apakah Anda tertarik untuk mengumpulkan informasi tentang kategori benda?', ['Iya', 'Tidak'], key='A8')
A8_Score = 1 if A8_Score_input == 'Iya' else 0

A9_Score_input = st.selectbox('Apakah Anda bisa mengetahui apa yang dipikirkan atau dirasakan seseorang hanya dengan melihat wajah mereka?', ['Iya', 'Tidak'], key='A9')
A9_Score = 1 if A9_Score_input == 'Iya' else 0

A10_Score_input = st.selectbox('Apakah anda mengalami kesulitan dalam membantu persoalan seseorang?', ['Iya', 'Tidak'], key='A10')
A10_Score = 1 if A10_Score_input == 'Iya' else 0

st.markdown('#### Pertanyaan Ciri-Ciri Individu')
col1, col2 = st.columns(2)
with col1:
    age_input = st.text_input('Berapakah usia anda saat ini?') 
    if not age_input.isdigit():
        st.error('Input tidak valid. Harap masukkan angka.')
    else:
        age = int(age_input)
with col2:
    gender_input = st.selectbox('Apa jenis kelamin Anda?', ['Laki-Laki', 'Perempuan'])
    gender = 1 if gender_input == 'Laki-Laki' else 0
with col1:
    jundice_input = st.selectbox('Apakah anda mempunyai riwayat penyakit kuning?', ['Iya', 'Tidak'])
    jundice = 1 if jundice_input == 'Iya' else 0
with col2:
    austim_input = st.selectbox('Apakah dari pihak keluarga memiliki riwayat autisme?', ['Iya', 'Tidak'])
    austim = 1 if austim_input == 'Iya' else 0
with col1:
    used_app_before_input = st.selectbox('Apakah anda pernah mengikuti tes survey sebelumnya?', ['Iya', 'Tidak'],key='used')
    used_app_before = 1 if used_app_before_input == 'Iya' else 0
    st.markdown('---')
with col2:
    result_input = st.text_input('Berapa hasil total dari pertanyaan ciri-ciri perilaku?') 
    result = int(result_input) if result_input else 0
    st.markdown('---')

# Kode untuk prediksi
gnb_diagnosis = ''
svm_diagnosis = ''


# Tombol untuk prediksi
with col1:
        if st.button('Test Prediksi Autisme GNB'):
            gnb_prediction = gnb_model.predict([[A1_Score, A2_Score, A3_Score, A4_Score, A5_Score, A6_Score, A7_Score, A8_Score, A9_Score, A10_Score, age, gender, jundice, austim, used_app_before, result]])

            if gnb_prediction[0] == 1:
                gnb_diagnosis = 'Pasien terindikasi menderita autisme'
            else:
                gnb_diagnosis = 'Pasien terindikasi tidak menderita autisme'

    
            st.success('Hasil prediksi menggunakan model GNB: {}'.format(gnb_diagnosis))

with col2:
        if st.button('Test Prediksi Autisme SVM'):
            svm_prediction = svm_model.predict([[A1_Score, A2_Score, A3_Score, A4_Score, A5_Score, A6_Score, A7_Score, A8_Score, A9_Score, A10_Score, age, gender, jundice, austim, used_app_before, result]])
  
            if svm_prediction[0] == 1:
                svm_diagnosis = 'Pasien terindikasi menderita autisme'
            else:
                svm_diagnosis = 'Pasien terindikasi tidak menderita autisme'

            st.success('Hasil prediksi menggunakan model SVM: {}'.format(svm_diagnosis))

st.markdown('---')