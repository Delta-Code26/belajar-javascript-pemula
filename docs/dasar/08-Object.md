Mantap Marno! Sekarang kita masuk ke **Object** — struktur data yang lebih keren dan fleksibel buat simpan data yang lebih kompleks. Ibarat kotak perhiasan yang bisa simpan berbagai jenis barang di dalamnya ✨💍

Berikut adalah isi lengkap untuk file:  
`D:\dokumentasi\javascript\belajar-javascript-pemula\docs\dasar\08-object.md`

---

```markdown
# 🗂️ Object di JavaScript

> "Kalau array itu warung makan, object itu lemari penyimpanan penuh barang." — Dev Serius

---

## 🎯 Tujuan Pembelajaran

Di akhir materi ini, kamu akan:
- Memahami apa itu object
- Bisa membuat object dengan properti dan method
- Mengakses dan mengubah data dalam object
- Kenal dengan konsep `this` dalam object

---

## 📦 Apa Itu Object?

Object = kumpulan data yang lebih kompleks, terdiri dari **key (nama)** dan **value (nilai)**. Bisa berbagai tipe data, bahkan array atau fungsi!  

Object ini penting banget karena sering dipakai untuk representasi data nyata, seperti `person`, `mobil`, atau `produk` dalam aplikasi.

```javascript
let person = {
  nama: "Marno",
  umur: 22,
  profesi: "Mahasiswa",
  alamat: "Malaysia",
};
console.log(person);
```

---

## 🧭 Mengakses dan Mengubah Properti

Untuk mengakses properti di object, kamu bisa pakai **dot notation** atau **bracket notation**.

### 1. Dot Notation

```javascript
console.log(person.nama);  // Output: Marno
console.log(person.umur);  // Output: 22
```

### 2. Bracket Notation

```javascript
console.log(person["profesi"]);  // Output: Mahasiswa
console.log(person["alamat"]);   // Output: Malaysia
```

---

## ✏️ Menambah dan Mengubah Properti

Kamu bisa menambah atau ubah properti dengan cara yang sama:

```javascript
person.alamat = "Kuala Lumpur";   // Mengubah nilai alamat
person.email = "marno@example.com"; // Menambah properti email

console.log(person.email);   // Output: marno@example.com
```

---

## 🔧 Method dalam Object

Object bisa punya **method**, yaitu fungsi yang bekerja di dalam object. Biasanya buat ngelola data dalam object tersebut.

```javascript
let mobil = {
  merk: "Toyota",
  tahun: 2020,
  sapa: function() {
    console.log("Halo, saya mobil " + this.merk);
  }
};

mobil.sapa(); // Output: Halo, saya mobil Toyota
```

Penjelasan:  
- `this` mengacu pada object tempat method itu dipanggil.

---

## 🧠 `this` dalam Object

`this` di dalam object merujuk pada object itu sendiri.

```javascript
let person = {
  nama: "Marno",
  sapa: function() {
    console.log("Halo, " + this.nama);
  }
};

person.sapa();  // Output: Halo, Marno
```

---

## 🧠 Quiz Mini

Apa output dari kode ini?

```javascript
let laptop = {
  brand: "Lenovo",
  harga: 8000,
  tampilkan: function() {
    console.log("Laptop " + this.brand + " seharga " + this.harga);
  }
};
laptop.tampilkan();
```

- A. Laptop Lenovo seharga 8000
- B. Laptop Lenovo seharga undefined
- C. Error
- D. 8000

✅ **Jawaban:** A. Laptop Lenovo seharga 8000

---

## 💪 Tantangan Coding

1. Buat object `mobil` dengan properti `merk`, `tahun`, `warna`, dan `jenis`
2. Tambahkan method `deskripsi()` yang menampilkan info tentang mobil
3. Panggil method `deskripsi()` dan pastikan tampil dengan benar

---

## 🧠 Tips Tambahan

- Gunakan object kalau data yang kamu simpan melibatkan banyak **atribut** yang berhubungan
- Jangan lupa `this` saat membuat method di dalam object
- Object literal adalah cara tercepat bikin object: `{ key: value }`

---

## 🔁 Kembali ke [Daftar Materi](../../index.md)
```

---

Berikutnya kita bisa lanjut ke **JSON** (JavaScript Object Notation), yang sering banget dipakai buat kirim data antar aplikasi via API.  
Mau lanjut ke **JSON** atau ada materi lain yang ingin diperdalam? 😎

---

<div align='center'>
⬅️ [Kembali](07-Array.md) | 🏠 [Beranda](../../index.md) | [Lanjut ➡️](09-JSON.md)
</div>
