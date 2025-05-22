import streamlit as st

st.set_page_config(page_title="Aplikasi Penilaian Keamanan Informasi")

def main():
    st.title("Aplikasi Penilaian Keamanan Informasi Berdasarkan ISO/IEC 27001:2022")
    st.write("Jawablah pertanyaan-pertanyaan di bawah ini dengan benar.")

    st.sidebar.header("Menu")
    selected_page = st.sidebar.radio("Pilih Bagian", ["Informasi Umum", "Konteks Organisasi", "Kepemimpinan", "Perencanaan",
                                                      "Dukungan", "Evaluasi", "Kendali Organisasi", "Kendali Manusia",
                                                      "Kendali Fisik", "Kendali Teknologi", "Kesimpulan"])

    if selected_page == "Informasi Umum":
        informasi_umum()
    elif selected_page == "Konteks Organisasi":
        konteks_organisasi()
    elif selected_page == "Kepemimpinan":
        kepemimpinan()
    elif selected_page == "Perencanaan":
        perencanaan()
    elif selected_page == "Dukungan":
        dukungan()
    elif selected_page == "Evaluasi":
        evaluasi()
    elif selected_page == "Kendali Organisasi":
        kendali_organisasi()
    elif selected_page == "Kendali Manusia":
        kendali_manusia()    
    elif selected_page == "Kendali Fisik":
        kendali_fisik()
    elif selected_page == "Kendali Teknologi":
        kendali_teknologi()
    elif selected_page == "Kesimpulan":
        kesimpulan()

def informasi_umum():
    st.header("Informasi Umum Organisasi")
    nama_organisasi = st.text_input("Nama Organisasi:")
    jumlah_karyawan = st.number_input("Jumlah Karyawan:", min_value=1, step=1)
    industri = st.selectbox("Industri:", ["Teknologi Informasi", "Keuangan", "Kesehatan", "Manufaktur", "Lainnya"])
    st.session_state['nama_organisasi'] = nama_organisasi
    st.session_state['jumlah_karyawan'] = jumlah_karyawan
    st.session_state['industri'] = industri

def konteks_organisasi():
    st.header("Konteks Organisasi")
    pertanyaan1 = [
        "1.1 Apakah organisasi telah menentukan isu eksternal dan internal terkait SMKI?",
        "1.2 Apakah organisasi telah menentukan kebutuhan dan harapan pihak yang terkait SMKI?",
        "1.3 Apakah organisasi telah menentukan ruang lingkup SMKI?"
        ]
    domain1_count = 0
    for i, question in enumerate(pertanyaan1):
        answer = st.radio(
            question,
            ('Iya', 'Tidak'),
            horizontal=True,
            key=f"q_{i}"
            )
        if answer == 'Iya':
            domain1_count += 1
    st.session_state['domain1_count'] = domain1_count
    st.session_state['pertanyaan1'] = len(pertanyaan1)
    
def kepemimpinan():
    st.header("Kepemimpinan")
    pertanyaan2 = [
        "2.1 Apakah manajemen puncak telah menunjukkan komitmen SMKI?",
        "2.2 Apakah manajemen puncak telah menetapkan kebijakan SMKI?",
        "2.3 Apakah manajemen puncak telah menetapkan peran dan tanggung jawab organisasi SMKI?"
    ]
    domain2_count = 0
    for i, question in enumerate(pertanyaan2):
        answer = st.radio(
            question,
            ('Iya', 'Tidak'),
            horizontal=True,
            key=f"q_{i}"
            )
        if answer == 'Iya':
            domain2_count += 1
    st.session_state['domain2_count'] = domain2_count
    st.session_state['pertanyaan2'] = len(pertanyaan2)

def perencanaan():
    st.header("Perencanaan")
    pertanyaan3 = [
        "3.1 Apakah organisasi telah menentukan kriteria risiko SMKI (seperti rendah, sedang, tinggi)?",
        "3.2 Apakah organisasi telah menentukan kriteria penerimaan risiko SMKI (seperti diterima, dimitigasi, ditransfer)?",
        "3.3 Apakah organisasi telah melakukan identifikasi aset dan risikonya terkait SMKI?",
        "3.4 Apakah organisasi telah melakukan analisis risiko SMKI (sesuai dengan kriteria pada 3.1)?",
        "3.5 Apakah organisasi telah melakukan evaluasi risiko SMKI (seperti risiko residual dan prioritas risiko)?",
        "3.6 Apakah organisasi telah menentukan penanganan risiko SMKI (sesuai dengan kriteria pada 3.2)?",
        "3.7 Apakah organisasi telah menentukan perencanaan penerapan kendali-kendali SMKI?",
        "3.8 Apakah organisasi telah menetapkan sasaran SMKI organisasi?"
    ]
    domain3_count = 0
    for i, question in enumerate(pertanyaan3):
        answer = st.radio(
            question,
            ('Iya', 'Tidak'),
            horizontal=True,
            key=f"q_{i}"
            )
        if answer == 'Iya':
            domain3_count += 1
    st.session_state['domain3_count'] = domain3_count
    st.session_state['pertanyaan3'] = len(pertanyaan3)
    
def dukungan():
    st.header("Dukungan")
    pertanyaan4 = [
        "4.1 Apakah organisasi telah menyediakan sumber daya yang dibutuhkan terkait SMKI?",
        "4.2 Apakah organisasi telah menentukan dan meningkatkan kompetensi pegawai terkait SMKI?",
        "4.3 Apakah organisasi telah melakukan peningkatan kesadaran SMKI?",
        "4.4 Apakah organisasi telah menentukan prosedur komunikasi terkait SMKI?",
        "4.5 Apakah organisasi telah menentukan prosedur pengelolaan informasi terdokumentasi?"
    ]
    domain4_count = 0
    for i, question in enumerate(pertanyaan4):
        answer = st.radio(
            question,
            ('Iya', 'Tidak'),
            horizontal=True,
            key=f"q_{i}"
            )
        if answer == 'Iya':
            domain4_count += 1
    st.session_state['domain4_count'] = domain4_count
    st.session_state['pertanyaan4'] = len(pertanyaan4)

def evaluasi():
    st.header("Evaluasi")
    pertanyaan5 = [
        "5.1 Apakah organisasi telah melakukan pemantauan dan pengukuran SMKI?",
        "5.2 Apakah organisasi telah melakukan audit internal SMKI?",
        "5.3 Apakah organisasi telah melakukan tinjauan manajemen SMKI?",
        "5.4 Apakah organisasi telah melakukan perencanaan dan tindakan perbaikan SMKI?"
    ]
    domain5_count = 0
    for i, question in enumerate(pertanyaan5):
        answer = st.radio(
            question,
            ('Iya', 'Tidak'),
            horizontal=True,
            key=f"q_{i}"
            )
        if answer == 'Iya':
            domain5_count += 1
    st.session_state['domain5_count'] = domain5_count
    st.session_state['pertanyaan5'] = len(pertanyaan5)

def kendali_organisasi():
    st.header("Kendali Organisasi")
    pertanyaan6 = [
        "6.1 Apakah organisasi telah melakukan pemisahan kewenangan terkait SMKI?",
        "6.2 Apakah organisasi telah melakukan hubungan dengan otoritas terkait SMKI (seperti BSSN, kepolisian, pemadam kebakaran)?",
        "6.3 Apakah organisasi telah memiliki threat intelligence atau pengetahuan tentang ancaman-ancaman terkait SMKI?",
        "6.4 Apakah organisasi telah melakukan integrasi SMKI ke dalam manajemen proyek?",
        "6.5 Apakah organisasi telah menetapkan prosedur penggunaan aset dan informasi terkait SMKI?",
        "6.6 Apakah organisasi telah menetapkan prosedur pengembalian aset terkait SMKI?",
        "6.7 Apakah organisasi telah menentukan klasifikasi informasi organisasi?",
        "6.8 Apakah organisasi telah melakukan pelabelan aset dan informasi sesuai dengan 6.7?",
        "6.9 Apakah organisasi telah menetapkan prosedur transfer informasi?",
        "6.10 Apakah organisasi telah menetapkan prosedur akses fisik dan non-fisik?",
        "6.11 Apakah organisasi telah menetapkan prosedur manajemen identitas?",
        "6.12 Apakah organisasi telah menetapkan prosedur autentikasi?",
        "6.13 Apakah organisasi telah melakukan peninjauan hak akses secara berkala?",
        "6.14 Apakah organisasi telah melakukan integrasi SMKI ke dalam hubungan dengan penyedia layanan eksternal?",
        "6.15 Apakah organisasi telah menetapkan prosedur manajemen rantai pasok aset dan informasi terkait SMKI?",
        "6.16 Apakah organisasi telah melakukan peninjauan aktivitas rantai pasok aset dan informasi terkait SMKI?",
        "6.17 Apakah organisasi telah melakukan integrasi SMKI ke dalam penggunaan layanan cloud?",
        "6.18 Apakah organisasi telah menetapkan prosedur manajemen insiden SMKI?",
        "6.19 Apakah organisasi telah melakukan penilaian insiden SMKI?",
        "6.20 Apakah organisasi telah melakukan tanggap insiden SMKI?",
        "6.21 Apakah organisasi telah mengumpulkan bukti-bukti insiden SMKI?",
        "6.22 Apakah organisasi telah melakukan pembelajaran dari insiden SMKI?",
        "6.23 Apakah organisasi telah merencanakan penerapan SMKI ketika terjadi gangguan?",
        "6.24 Apakah organisasi telah merencanakan kesiapan untuk keberlanjutan bisnis ketika terjadi gangguan?",
        "6.25 Apakah organisasi telah melakukan identifikasi kepatuhan terkait SMKI?",
        "6.26 Apakah organisasi telah menetapkan perlindungan hak kekayaan intelektual?",
        "6.27 Apakah organisasi telah menetapkan perlindungan rekaman?",
        "6.28 Apakah organisasi telah menetapkan perlindungan data pribadi?"
    ]
    domain6_count = 0
    for i, question in enumerate(pertanyaan6):
        answer = st.radio(
            question,
            ('Iya', 'Tidak'),
            horizontal=True,
            key=f"q_{i}"
            )
        if answer == 'Iya':
            domain6_count += 1
    st.session_state['domain6_count'] = domain6_count
    st.session_state['pertanyaan6'] = len(pertanyaan6)

def kendali_manusia():
    st.header("Kendali Manusia")
    pertanyaan7 = [
        "7.1 Apakah organisasi telah melakukan verifikasi persyaratan terkait SMKI terhadap calon pegawai?",
        "7.2 Apakah organisasi telah melakukan integrasi SMKI ke dalam perjanjian kerja pegawai?",
        "7.3 Apakah organisasi telah menetapkan proses kedisiplinan terhadap pelanggaran terkait SMKI oleh pegawai?",
        "7.4 Apakah organisasi telah melakukan perjanjian kerahasiaan dengan pihak eksternal yang bekerja di organisasi?",
        "7.5 Apakah organisasi telah menetapkan prosedur bekerja jarak jauh?"
    ]
    domain7_count = 0
    for i, question in enumerate(pertanyaan7):
        answer = st.radio(
            question,
            ('Iya', 'Tidak'),
            horizontal=True,
            key=f"q_{i}"
            )
        if answer == 'Iya':
            domain7_count += 1
    st.session_state['domain7_count'] = domain7_count
    st.session_state['pertanyaan7'] = len(pertanyaan7)

def kendali_fisik():
    st.header("Kendali Fisik")
    pertanyaan8 = [
        "8.1 Apakah organisasi telah menetapkan perimeter keamanan fisik?",
        "8.2 Apakah organisasi telah melakukan keamanan akses fisik?",
        "8.3 Apakah organisasi telah melakukan keamanan ruangan dan fasilitas dalam organisasi?",
        "8.4 Apakah organisasi telah melakukan keamanan terhadap ancaman dari lingkungan?",
        "8.5 Apakah organisasi telah menetapkan prosedur bekerja yang aman?",
        "8.6 Apakah organisasi telah melakukan pembersihan meja dan layar dari informasi sensitif?",
        "8.7 Apakah organisasi telah melakukan keamanan pada peralatan?",
        "8.8 Apakah organisasi telah melakukan keamanan aset yang berada di luar lokasi?",
        "8.9 Apakah organisasi telah melakukan keamanan pada media penyimpanan?",
        "8.10 Apakah organisasi telah menyediakan sumber daya pendukung kelistrikan?",
        "8.11 Apakah organisasi telah melakukan keamanan perkabelan?",
        "8.12 Apakah organisasi telah melakukan pemeliharaan peralatan secara berkala?",
        "8.13 Apakah organisasi telah menetapkan prosedur pemusnahan aset?"
    ]
    domain8_count = 0
    for i, question in enumerate(pertanyaan8):
        answer = st.radio(
            question,
            ('Iya', 'Tidak'),
            horizontal=True,
            key=f"q_{i}"
            )
        if answer == 'Iya':
            domain8_count += 1
    st.session_state['domain8_count'] = domain8_count
    st.session_state['pertanyaan8'] = len(pertanyaan8)

def kendali_teknologi():
    st.header("Kendali Teknologi")
    pertanyaan9 = [
        "9.1 Apakah organisasi telah melakukan keamanan perangkat titik akhir pengguna (end user)?",
        "9.2 Apakah organisasi telah melakukan keamanan akses ke kode sumber (source code)?",
        "9.3 Apakah organisasi telah melakukan manajemen kapasitas (seperti pemantauan dan perencanaan penggunaan sumber daya)?",
        "9.4 Apakah organisasi telah melakukan manajemen kerentanan?",
        "9.5 Apakah organisasi telah melakukan manajemen konfigurasi?",
        "9.6 Apakah organisasi telah menetapkan prosedur penghapusan informasi?",
        "9.7 Apakah organisasi telah melakukan penyamaran informasi?",
        "9.8 Apakah organisasi telah melakukan pencegahan kebocoran data?",
        "9.9 Apakah organisasi telah melakukan pencadangan informasi?",
        "9.10 Apakah organisasi telah menyediakan sumber daya redundansi?",
        "9.11 Apakah organisasi telah melakukan pencatatan atau perekaman aktivitas terkait SMKI?",
        "9.12 Apakah organisasi telah melakukan sinkronisasi waktu?",
        "9.13 Apakah organisasi telah menetapkan prosedur instalasi perangkat lunak?",
        "9.14 Apakah organisasi telah melakukan keamanan jaringan?",
        "9.15 Apakah organisasi telah melakukan pemisahan jaringan?",
        "9.16 Apakah organisasi telah melakukan keamanan akses ke website eksternal?",
        "9.17 Apakah organisasi telah menggunakan kriptografi?",
        "9.18 Apakah organisasi telah melakukan keamanan pada pengembangan perangkat lunak?",
        "9.19 Apakah organisasi telah menetapkan persyaratan keamanan perangkat lunak?",
        "9.20 Apakah organisasi telah melakukan pengujian keamanan perangkat lunak?",
        "9.21 Apakah organisasi telah menetapkan persyaratan pada pengembangan perangkat lunak oleh pihak eksternal?",
        "9.22 Apakah organisasi telah melakukan pemisahan lingkungan pengembangan, pengujian, dan produksi?",
        "9.23 Apakah organisasi telah menetapkan prosedur manajemen perubahan?"
    ]
    domain9_count = 0
    for i, question in enumerate(pertanyaan9):
        answer = st.radio(
            question,
            ('Iya', 'Tidak'),
            horizontal=True,
            key=f"q_{i}"
            )
        if answer == 'Iya':
            domain9_count += 1
    st.session_state['domain9_count'] = domain9_count
    st.session_state['pertanyaan9'] = len(pertanyaan9)

def kesimpulan():
    st.header("Kesimpulan")
    st.success(f"Organisasi telah memenuhi **{st.session_state['domain1_count']}** dari {st.session_state['pertanyaan1']} persyaratan Konteks Organisasi.")
    st.success(f"Organisasi telah memenuhi **{st.session_state['domain2_count']}** dari {st.session_state['pertanyaan2']} persyaratan Kepemimpinan.")
    st.success(f"Organisasi telah memenuhi **{st.session_state['domain3_count']}** dari {st.session_state['pertanyaan3']} persyaratan Perencanaan.")
    st.success(f"Organisasi telah memenuhi **{st.session_state['domain4_count']}** dari {st.session_state['pertanyaan4']} persyaratan Dukungan.")
    st.success(f"Organisasi telah memenuhi **{st.session_state['domain5_count']}** dari {st.session_state['pertanyaan5']} persyaratan Evaluasi.")
    st.success(f"Organisasi telah memenuhi **{st.session_state['domain6_count']}** dari {st.session_state['pertanyaan6']} persyaratan Kendali Organisasi.")
    st.success(f"Organisasi telah memenuhi **{st.session_state['domain7_count']}** dari {st.session_state['pertanyaan7']} persyaratan Kendali Manusia.")
    st.success(f"Organisasi telah memenuhi **{st.session_state['domain8_count']}** dari {st.session_state['pertanyaan8']} persyaratan Kendali Fisik.")
    st.success(f"Organisasi telah memenuhi **{st.session_state['domain9_count']}** dari {st.session_state['pertanyaan9']} persyaratan Kendali Teknologi.")
    
if __name__ == "__main__":
    main()
