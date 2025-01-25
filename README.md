# Discord Auto Chat

Bot Discord untuk auto-leveling dengan fitur pengiriman pesan otomatis yang mendukung multiple akun.

## Fitur

- Support multiple akun (token)
- Auto delete pesan setelah dikirim
- Pendeteksian timeout channel
- Penanganan rate limit dan slowmode
- Error handling yang lengkap
- Customizable delay antar pesan
- 54 variasi pesan random

## Persyaratan

- Python 3.7+
- discord.py 1.7.3
- asyncio
- colorama

## Instalasi

1. Clone repository ini
```bash
git clone https://github.com/Aethereal-Collective/discord-auto-chat.git
cd discord-auto-chat
```

2. Setup Virtual Environment
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/Mac
python3 -m venv venv
source venv/bin/activate
```

3. Install dependencies
```bash
pip install -r requirements.txt
```

## Penggunaan

1. Buat file `token.txt` dan masukkan token Discord (satu token per baris)
```
TOKEN1
TOKEN2
TOKEN3
```

2. Jalankan script
```bash
python jawa.py
```

3. Masukkan informasi yang diminta:
- Channel ID
- Jumlah pesan yang akan dikirim
- Delay antara setiap pesan (dalam detik)

## Cara Mendapatkan Token Discord

1. Buka Discord di browser
2. Tekan F12 untuk membuka Developer Tools
3. Pergi ke tab Network
4. Ketik "api" di filter
5. Cari request yang memiliki header "authorization"
6. Copy nilai token dari sana

## Cara Mendapatkan Channel ID

1. Aktifkan Developer Mode di Discord (User Settings > App Settings > Advanced > Developer Mode)
2. Klik kanan pada channel
3. Pilih "Copy ID"

## Peringatan

⚠️ **PENTING**:
- Penggunaan self-bot melanggar Terms of Service Discord
- Gunakan dengan risiko sendiri
- Disarankan menggunakan delay minimal 10 detik antar pesan
- Pastikan token yang digunakan valid dan fresh

## Error Handling

Script akan menangani berbagai jenis error:
- Token tidak valid/expired
- Channel tidak ditemukan
- Timeout channel
- Rate limit
- Slowmode
- Tidak ada izin mengirim/menghapus pesan
- Voice channel detection

## Tips Penggunaan

1. Gunakan delay yang aman:
   - Minimal 10 detik antara pesan
   - Jangan spam terlalu banyak pesan

2. Jika terjadi error:
   - Token tidak valid: Perbarui token di token.txt
   - Rate limit: Script akan otomatis menunggu
   - Timeout: Tunggu sampai timeout selesai
