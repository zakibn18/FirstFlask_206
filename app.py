from flask import Flask, render_template, request

app = Flask(__name__)

# --- ROUTE 1: Menampilkan Form (Halaman Awal) ---
@app.route('/')
def home():
    # Di sini kita cuma menampilkan file HTML form saja
    return render_template('index.html')

# --- ROUTE 2: Memproses Data (Endpoint Baru) ---
@app.route('/halo', methods=['POST'])
def sapa_user():
    # Ambil data yang dikirim dari form sebelumnya
    nama = request.form.get('nama_user')
    
    # Render halaman baru khusus untuk hasil
    return render_template('hasil.html', nama_diterima=nama)

if __name__ == '__main__':
    app.run(debug=True)