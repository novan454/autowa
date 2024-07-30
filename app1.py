import streamlit as st
import pandas as pd
import pywhatkit as kit
import time

# Fungsi untuk mengirim pesan WhatsApp
def send_whatsapp_message(nomor_wa, pesan):
    try:
        # Mengirim pesan secara instan
        kit.sendwhatmsg_instantly(f"+{nomor_wa}", pesan)
        return f"Pesan terkirim ke {nomor_wa}"
    except Exception as e:
        return f"Gagal mengirim pesan ke {nomor_wa}: {e}"

# Streamlit UI
st.title("WhatsApp Automation")

uploaded_file = st.file_uploader("Pilih file Excel", type=["xlsx"])

if uploaded_file is not None:
    # Membaca file Excel yang diunggah
    data = pd.read_excel(uploaded_file)

    if st.button('Start Automation'):
        with st.spinner('Sending messages...'):
            results = []
            for index, row in data.iterrows():
                nama_kontak = row['Nama']
                nomor_wa = row['Nomor WA']
                nama_cs = row['Nama CS']
                pesan = f"Halo kak {nama_kontak}, saya {nama_cs} dari Nenavin. Apakah ingin order lagi?"

                # Memanggil fungsi untuk mengirim pesan
                result = send_whatsapp_message(nomor_wa, pesan)
                results.append(result)

                # Penundaan 15 detik sebelum mengirim pesan berikutnya
                time.sleep(15)
            
            st.success('Automation completed!')
            st.write('\n'.join(results))