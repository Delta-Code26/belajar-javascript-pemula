Wuhuu! Let’s go Marno! Sekarang saatnya masuk ke materi yang jadi pondasi dari semua percabangan hidup dan kode: **Logika di JavaScript!** 🧠💥  
Berikut isi lengkap buat file `D:\dokumentasi\javascript\belajar-javascript-pemula\docs\dasar\04-logika.md`

---

```markdown
# 🧠 Logika & Operator di JavaScript

> "Kalau hidup aja butuh logika, apalagi ngoding." — Filosofi koding saat bug menyerang.

---

## 🎯 Tujuan Pembelajaran

Setelah mempelajari materi ini, kamu akan:
- Mengerti konsep percabangan dan pengambilan keputusan
- Mengenal operator logika dan perbandingan
- Bisa membuat kondisi `if`, `else`, dan `else if`

---

## 🧪 Operator Perbandingan

| Operator | Arti                      | Contoh               |
|----------|---------------------------|----------------------|
| `==`     | Sama nilai                 | `5 == '5'` → true    |
| `===`    | Sama nilai & tipe          | `5 === '5'` → false  |
| `!=`     | Tidak sama nilai           | `5 != 4` → true      |
| `!==`    | Tidak sama nilai/tipe      | `5 !== '5'` → true   |
| `>`      | Lebih besar                | `10 > 5` → true      |
| `<`      | Lebih kecil                | `3 < 7` → true       |
| `>=`     | Lebih besar atau sama      | `5 >= 5` → true      |
| `<=`     | Lebih kecil atau sama      | `4 <= 5` → true      |

---

## 🔀 Operator Logika

| Operator | Nama          | Contoh                       | Hasil    |
|----------|---------------|------------------------------|----------|
| `&&`     | AND (dan)     | `true && false`              | false    |
| `||`     | OR (atau)     | `true || false`              | true     |
| `!`      | NOT (kebalikan)| `!true`                      | false    |

---

## 📍 Struktur If-Else

```javascript
let nilai = 80;

if (nilai >= 75) {
  console.log("Lulus 🎉");
} else {
  console.log("Belum lulus 😥");
}
```

---

## 🧱 Struktur Else If

```javascript
let skor = 90;

if (skor >= 90) {
  console.log("Nilai A");
} else if (skor >= 80) {
  console.log("Nilai B");
} else {
  console.log("Nilai C ke bawah");
}
```

---

## 🧠 Kasus Nyata

```javascript
let login = true;
let role = "admin";

if (login && role === "admin") {
  console.log("Selamat datang, Admin!");
} else if (login && role === "user") {
  console.log("Halo, pengguna!");
} else {
  console.log("Silakan login dulu!");
}
```

---

## 🔥 Trik Cepat

Gunakan `===` untuk hasil yang **lebih akurat**, karena dia cek nilai **dan** tipe data!

```javascript
console.log(5 == "5");   // true (cuma nilai)
console.log(5 === "5");  // false (beda tipe)
```

---

## 🧠 Quiz Mini

Apa hasil dari kode ini?

```javascript
let usia = 17;
if (usia >= 18) {
  console.log("Boleh masuk");
} else {
  console.log("Masih bocil");
}
```

- A. Error  
- B. Boleh masuk  
- C. Masih bocil  
- D. Nunggu KTP dulu

✅ **Jawaban:** C. Masih bocil

---

## 💪 Tantangan Coding

1. Buat file `cek-umur.js`
2. Simpan variabel `umur`
3. Jika umur:
   - < 13 → tampilkan "Anak-anak"
   - 13–17 → tampilkan "Remaja"
   - 18+ → tampilkan "Dewasa"

Bonus: Tambahkan logika jika umur negatif → tampilkan "Umur gak valid"

---

## 🧠 Tips Tambahan

- Jangan kebanyakan `else if`, nanti kode kayak sinetron: panjang & dramatis
- Gunakan `switch` kalau kondisinya banyak tapi dari 1 variabel (nanti kita bahas!)

---

## 🔁 Kembali ke [Daftar Materi](../../index.md)
```

---

Kalau kamu udah siap mental, kita bisa lanjut ke `05-function.md` buat ngebahas **fungsi-fungsi** alias jurus pamungkas pemrograman!  
Bilang aja: **"Lanjut ke fungsi!"** dan kita gas lagi! 🧙‍♂️✨

---

<div align='center'>
⬅️ [Kembali](03-Tipe-Data.md) | 🏠 [Beranda](../../index.md) | [Lanjut ➡️](05-Loop.md)
</div>
