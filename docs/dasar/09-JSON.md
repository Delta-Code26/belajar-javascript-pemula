Oke, siap! Sekarang kita bahas **JSON** (JavaScript Object Notation) — format data yang sering banget dipakai untuk pertukaran data antar server dan aplikasi, terutama di web dan API 🌐💻

Berikut isi lengkap untuk file:  
`D:\dokumentasi\javascript\belajar-javascript-pemula\docs\dasar\09-json.md`

---

```markdown
# 🌐 JSON (JavaScript Object Notation)

> "JSON itu kayak surat cinta buat aplikasi. Dibaca semua, dipahami, dikirim ke penerima." — Dev Pecinta Data

---

## 🎯 Tujuan Pembelajaran

Di akhir materi ini, kamu akan:
- Mengerti apa itu JSON dan kenapa penting
- Bisa mengubah JavaScript object ke JSON dan sebaliknya
- Memahami penggunaan JSON dalam aplikasi web

---

## 📦 Apa Itu JSON?

JSON adalah format teks yang digunakan untuk menyimpan dan mentransfer data. Data dalam JSON disusun dalam pasangan **key** dan **value**, mirip seperti object di JavaScript. Tapi JSON lebih sederhana dan sering digunakan untuk komunikasi antar server dan client.

Contoh JSON:

```json
{
  "nama": "Marno",
  "umur": 22,
  "profesi": "Mahasiswa",
  "alamat": "Malaysia"
}
```

---

## 🔧 Mengubah Object ke JSON (Stringify)

Untuk mengubah object JavaScript menjadi string JSON, kita bisa pakai `JSON.stringify()`.

```javascript
let person = {
  nama: "Marno",
  umur: 22,
  profesi: "Mahasiswa"
};

let jsonPerson = JSON.stringify(person);
console.log(jsonPerson);
```

Output:

```json
{"nama":"Marno","umur":22,"profesi":"Mahasiswa"}
```

---

## 🔄 Mengubah JSON ke Object (Parse)

Sebaliknya, untuk mengubah string JSON kembali ke object JavaScript, kita gunakan `JSON.parse()`.

```javascript
let jsonPerson = '{"nama":"Marno","umur":22,"profesi":"Mahasiswa"}';
let person = JSON.parse(jsonPerson);

console.log(person.nama);   // Output: Marno
console.log(person.umur);   // Output: 22
```

---

## 🧰 Keuntungan Menggunakan JSON

- **Ringan**: JSON menggunakan format yang sangat efisien untuk mentransfer data
- **Kompatibilitas Tinggi**: JSON didukung oleh banyak bahasa pemrograman
- **Mudah Dibaca**: Format JSON sangat mudah dipahami dan di-debug

---

## 🧠 Quiz Mini

Apa hasil dari kode ini?

```javascript
let jsonStr = '{"nama":"Putri","usia":25}';
let obj = JSON.parse(jsonStr);
console.log(obj.usia);
```

- A. Putri  
- B. 25  
- C. Error  
- D. undefined

✅ **Jawaban:** B. 25

---

## 💪 Tantangan Coding

1. Buat object `produk` dengan properti `nama`, `harga`, dan `stok`
2. Ubah object `produk` jadi string JSON
3. Ubah string JSON kembali jadi object dan tampilkan harga produk

---

## 🧠 Tips Tambahan

- JSON hanya mendukung tipe data dasar seperti string, number, object, array, dan boolean. 
- JSON **tidak mendukung function**! Jadi, fungsi di dalam object tidak akan dipertahankan saat di-convert ke JSON.
- JSON juga tidak mendukung simbol dan `undefined`.

---

## 🔁 Kembali ke [Daftar Materi](../../index.md)
```

---

Sekarang kita sudah masuk ke dunia **JSON**! Dengan ini, kamu bisa mulai menghubungkan aplikasi JavaScript dengan server atau API menggunakan format data ini.  
Selanjutnya, kita bisa masuk ke **Asynchronous JavaScript**, yaitu cara untuk menangani operasi yang butuh waktu lama, kayak fetching data dari API 🕑🚀

Mau lanjut ke materi **Asynchronous JavaScript** atau ada topik lainnya yang ingin dikejar? 😎