# 🧠 Variabel di JavaScript 👑

> "Variabel itu seperti Tupperware—buat nyimpan isi. Bedanya, kalau hilang, nggak dimarahin emak." — Dev waras.

---

## 🎯 Tujuan Pembelajaran

Di materi ini, kamu akan:
- Memahami apa itu variabel
- Mengenal `var`, `let`, dan `const`
- Tahu cara menyimpan dan mengakses data di dalam variabel

---

## 🔍 Apa itu Variabel?

Variabel adalah **wadah penyimpanan data** di dalam program.  
Contoh simpel:

```javascript
let nama = "Marno";
const umur = 21;
var status = "Belajar JavaScript";
```

---

## 🔧 Jenis-Jenis Variabel

### 1. `var`
- Versi lama
- Bisa di-*redeclarate*
- **Kurang aman**, jangan sering dipakai

```javascript
var nama = "Marno";
var nama = "Mahasiswa"; // ini valid tapi nggak direkomendasikan
```

### 2. `let`
- Bisa diganti nilainya
- Tidak bisa dideklarasi ulang dalam scope yang sama

```javascript
let mood = "semangat";
mood = "lelah"; // bisa!
```

### 3. `const`
- Nilainya TIDAK bisa diubah
- Harus langsung diisi saat dibuat

```javascript
const planet = "Bumi";
planet = "Mars"; // ❌ error
```

---

## 💻 Contoh Program

```javascript
let nama = "Marno";
const umur = 21;

console.log("Nama saya:", nama);
console.log("Umur saya:", umur);

nama = "Marno Mahasiswa";
console.log("Nama baru saya:", nama);
```

---

## 📦 Peraturan Main
<table align="left">
<th>Keyword</th>
<th>Bisa Diubah</th>
<th>Bisa Dideklarasi Ulang</th>
<th>Keterangan</th>
<tr align="center">
<td>var</td>
<td>✅</td>
<td>✅</td>
<td>Jangan sering digunakan</td>
</tr>
<tr align="center">
<td>let</td>
<td>✅</td>
<td>❌</td>
<td>Rekomendasi Utama</td>
</tr>
<tr align="center">
<td>const</td>
<td>❌</td>
<td>❌</td>
<td>Bisa nilai tetap</td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
</table>

-----
---

## 🧠 Quiz Mini

Kode ini akan menghasilkan apa?

```javascript
const nama = "Raka";
nama = "Budi";
console.log(nama);
```

- A. Raka  
- B. Budi  
- C. Error  
- D. Nama bukan urusan saya

✅ **Jawaban:** C. Error! Karena `const` tidak boleh diubah setelah dideklarasikan.

---

## 💪 Tantangan Coding

1. Buat file `biodata.js`
2. Simpan:
   - Nama kamu (let)
   - Umur kamu (const)
   - Hobi kamu (let)
3. Tampilkan semuanya di console

Contoh output:
```
Nama saya Marno
Umur saya 21
Hobi saya ngoding di kebun sawit 🌴💻
```

---

## 💬 Tips Tambahan

- Gunakan `let` untuk nilai yang bisa berubah
- Gunakan `const` untuk nilai tetap (seperti API key, config, dsb)
- Hindari `var` kecuali lagi nostalgia

---

<div align="center">

## ⬅️ [Kembali](../dasar/01-hello-world.md) &nbsp;&nbsp;|&nbsp;&nbsp; 🏠 [Beranda](../index.md) &nbsp;&nbsp;|&nbsp;&nbsp; [Lanjut ➡️](../dasar/03-Tipe-Data.md)

</div>

---

<div align='center'>
⬅️ [Kembali](01-hello-world.md) | 🏠 [Beranda](../../index.md) | [Lanjut ➡️](03-Tipe-Data.md)
</div>
