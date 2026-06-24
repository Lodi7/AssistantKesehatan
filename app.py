import streamlit as st
from inference import chat_inference

st.set_page_config(page_title="Asisten Kesehatan Digital")
st.title("Asisten Kesehatan Lodi Health's")

st.markdown("""
## Selamat datang di Asisten Kesehatan Lodi Health's!

Kamu bisa:

- **Tanya gejala atau keluhan kesehatan**  
- **Cari dokter** (sebutkan spesialis)
- **Temukan rumah sakit** (sebutkan kota/provinsi)  
- **Baca berita kesehatan terbaru**

---

*Berikan pertanyaan yang jelas dan spesifik*  
Contoh: `rumah sakit di Surabaya`

*Catatan: Sistem ini masih dalam tahap pengembangan dan belum sepenuhnya otomatis. Mohon maaf jika terdapat kekeliruan atau keterbatasan.*

> Asisten ini memberi info awal berbasis AI  
> Bukan pengganti diagnosis atau konsultasi dokter
""")

with st.sidebar:
    st.header("Pengaturan")
    if st.button("Reset Percakapan"):
        st.session_state.messages = []
        st.rerun()

# Inisialisasi state percakapan
if "messages" not in st.session_state:
    st.session_state.messages = []

# Tampilkan riwayat chat sebelumnya
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Input user
prompt = st.chat_input("Ketik keluhan atau pertanyaan lainnya di sini...")

if prompt:
    # Tampilkan input user
    with st.chat_message("user"):
        st.markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    try:
        with st.spinner("Sedang menganalisis..."):
            response = chat_inference(prompt)

        # Tampilkan respon asisten
        with st.chat_message("assistant"):
            if isinstance(response, dict) and response.get("type") == "doctors":
                st.markdown("Berikut beberapa rekomendasi dokter:")

                for doc in response["content"]:
                    col1, col2 = st.columns([1, 3])
                    with col1:
                        if doc.get("image"):
                            st.image(doc["image"], width=100)
                    with col2:
                        st.markdown(f"""
**{doc['name']}**  
*{doc['specialization']}*  
{doc['hospital']}  
""")
                    st.markdown("---")

                # Tambahkan ke session
                doctor_summary = "\n\n".join(
                    f"**{doc['name']}** - {doc['specialization']} ({doc['hospital']})"
                    for doc in response["content"]
                )
                st.session_state.messages.append({
                    "role": "assistant",
                    "content": doctor_summary
                })

            else:
                st.markdown(response)
                st.session_state.messages.append({"role": "assistant", "content": response})

    except Exception as e:
        st.error("Maaf, terjadi kesalahan saat memproses permintaan Anda.")
        print(f"Error pada inference: {e}")


#app.py 