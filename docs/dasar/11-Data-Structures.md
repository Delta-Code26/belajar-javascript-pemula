Let's gooo~ 🚀 Kali ini kita masuk ke topik yang mulai kerasa "berisi banget": **Struktur Data** atau *Data Structures* di JavaScript. Ini penting banget buat ngatur, simpan, dan ngolah data — biar hidup ngoding lo nggak berantakan kayak lemari kontrakan 😆

Berikut isi lengkap file:  
`D:\dokumentasi\javascript\belajar-javascript-pemula\docs\dasar\11-Data-Structures.md`

---

```markdown
# 🧱 Struktur Data di JavaScript

> “Koding tanpa struktur data tuh kayak sawit tanpa kebun—nggak ada tempatnya!” 🌴

---

## 🎯 Tujuan Pembelajaran

Setelah membaca ini, kamu akan:
- Mengenal struktur data dasar di JavaScript
- Mengerti kapan dan bagaimana menggunakannya
- Bisa menyimpan dan mengakses data dengan lebih efisien

---

## 📦 Apa Itu Struktur Data?

Struktur data adalah **cara menyimpan dan mengorganisasi data** agar mudah diakses dan dimodifikasi.

Di JavaScript, struktur data dasarnya meliputi:

- **Array**
- **Object**
- (bonus) **Map** & **Set** — dibahas singkat

---

## 1️⃣ Array: Kumpulan Data Berurutan

Array adalah list (daftar) yang bisa berisi apa aja: string, number, bahkan array lain.

```javascript
let buah = ["apel", "mangga", "durian"];
console.log(buah[1]); // "mangga"
```

### Operasi Umum:
```javascript
buah.push("pisang");    // tambah di akhir
buah.pop();             // hapus dari akhir
buah.shift();           // hapus dari awal
buah.unshift("jeruk");  // tambah di awal
```

### Looping Array:
```javascript
for (let item of buah) {
  console.log(item);
}
```

---

## 2️⃣ Object: Data dengan Label

Object menyimpan data dalam format **key-value**.

```javascript
let pekerja = {
  nama: "Marno",
  umur: 21,
  asal: "Indonesia"
};

console.log(pekerja.nama); // "Marno"
console.log(pekerja["umur"]); // 21
```

### Menambah / Ubah Properti:
```javascript
pekerja.email = "marno@example.com";
pekerja.umur = 22;
```

---

## 3️⃣ Map: Object Tapi Lebih Rapi

`Map` adalah alternatif object, cocok kalau kunci-nya bukan cuma string.

```javascript
let map = new Map();
map.set("nama", "Marno");
map.set("usia", 21);

console.log(map.get("nama")); // "Marno"
```

Keunggulan `Map`:
- Bisa pakai tipe data apa saja sebagai key
- Tetap urutan
- Ukuran bisa dicek dengan `.size`

---

## 4️⃣ Set: Kumpulan Data Unik

`Set` adalah kumpulan data **tanpa duplikat**.

```javascript
let setBuah = new Set();
setBuah.add("apel");
setBuah.add("apel"); // diabaikan karena sudah ada
setBuah.add("mangga");

console.log(setBuah); // Set { "apel", "mangga" }
```

---

## 🔍 Kapan Pakai Apa?

| Kebutuhan                  | Struktur Data |
|---------------------------|----------------|
| Data berurutan            | Array          |
| Data dengan label         | Object         |
| Butuh key yang bukan string| Map           |
| Butuh data tanpa duplikat | Set            |

---

## 🧠 Quiz Mini

Apa output dari kode berikut?

```javascript
let angka = [1, 2, 3];
angka.push(4);
console.log(angka[3]);
```

- A. 3  
- B. 4  
- C. undefined  
- D. Error

✅ **Jawaban:** B. `4`

---

## 💪 Tantangan Coding

1. Buat object `sawit` dengan properti `luas`, `lokasi`, dan `jumlahPohon`.
2. Buat array dari nama-nama pekerja dan tampilkan semuanya pakai `for...of`.
3. Gunakan `Set` untuk menyimpan data blok kebun tanpa duplikat.

---

## ⚠️ Tips Pro

- Array cocok buat daftar yang diakses berdasarkan urutan (index).
- Object cocok buat data yang punya label/nama (key).
- Map lebih fleksibel daripada object, tapi belum selalu dibutuhkan di awal.
- Gunakan Set saat kamu butuh memastikan data **unik**.

---

## 🔁 Kembali ke [Daftar Materi](../../index.md)
```

---

Sip, satu langkah lebih deket jadi **JavaScript Jagoan** 💪  
Mau lanjut ke **null & undefined**, atau langsung ke **function lanjutan** atau mungkin eksplor **Map & Set** lebih dalam? Kasih kode aja, bro 😎