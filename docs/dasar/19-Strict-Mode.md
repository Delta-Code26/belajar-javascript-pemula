Siap, bro! Kali ini kita bahas topik yang keliatannya kalem tapi diam-diam penting banget buat ngehindarin bug:  
**Strict Mode** — kayak "mode serius" di JavaScript. Tanpa basa-basi, dia galak tapi bikin kode kita lebih aman dan rapi 😤👮‍♂️

Berikut isi lengkap untuk file:  
`D:\dokumentasi\javascript\belajar-javascript-pemula\docs\dasar\19-Strict-Mode.md`

---

```markdown
# 🔒 Strict Mode di JavaScript

> "Strict mode itu kayak pelatih yang galak, tapi bikin kamu nggak jadi programmer barbar."

---

## 🎯 Tujuan Pembelajaran

Setelah mempelajari ini, kamu akan:
- Tahu apa itu `strict mode`
- Mengaktifkan strict mode
- Paham kenapa strict mode penting untuk mencegah bug dan kesalahan

---

## ❓ Apa Itu Strict Mode?

`Strict mode` adalah fitur di JavaScript yang:
- Membuat aturan jadi lebih ketat
- Mencegah kesalahan umum yang sulit dideteksi
- Mempercepat performa JavaScript di beberapa engine

Aktifkan dengan:

```javascript
"use strict";
```

Letakkan di atas file atau fungsi:

```javascript
"use strict";

let angka = 10;
```

---

## 📛 Contoh Kesalahan yang Dicegah

### 1. Variabel Tanpa Deklarasi

Tanpa strict:

```javascript
nama = "Marno";
console.log(nama); // Masih jalan, tapi ini sebenarnya bug!
```

Dengan strict:

```javascript
"use strict";
nama = "Marno"; // ❌ Error: nama is not defined
```

---

### 2. Duplikat Parameter

```javascript
"use strict";
function contoh(a, a) {
  return a + a;
}
// ❌ Error: Duplicate parameter name not allowed
```

---

### 3. Akses ke Properti yang Dilindungi

```javascript
"use strict";
delete Object.prototype; // ❌ Tidak diizinkan
```

---

## 🧠 Kenapa Harus Pakai?

- Bikin kode **lebih aman**
- Mencegah typo dan kesalahan fatal
- Kompatibel dengan JavaScript modern
- Direkomendasikan di semua file JavaScript

---

## ⚠️ Catatan

- Pastikan kamu memang butuh strict mode (kalau belajar, **YES**)
- Bisa juga pakai strict mode hanya di fungsi tertentu:

```javascript
function jalanSerius() {
  "use strict";
  // kode aman & ketat
}
```

---

## 🧪 Mini Quiz

Apa output dari kode ini?

```javascript
"use strict";
x = 100;
console.log(x);
```

**Jawaban:**
❌ Error: `x` is not defined — harus dideklarasikan dulu!

---

## 💪 Tantangan Coding

1. Buat kode tanpa strict mode, lalu coba tambahkan `use strict` dan perbaiki error yang muncul.
2. Coba buat fungsi dengan parameter yang sama (`function tes(a, a)`) dan lihat perbedaan dengan dan tanpa strict mode.
3. Cari tahu apakah strict mode aktif di file eksternal atau inline script di HTML.

---

## 🚀 Tips Ninja

- Selalu pakai `"use strict"` di awal file JS kamu
- Ini bikin kamu kebal terhadap banyak "jebakan Batman" di JavaScript
- Lebih gampang untuk debugging dan kerja tim

---

## 🔁 Kembali ke [Daftar Materi](../../index.md)
```

---

Udah siap jadi programmer disiplin? 😎  
Dengan `strict mode`, JavaScript lo makin rapih, bug makin minim, dan mental kode makin kuat!  
Next kita bisa lanjut bahas **ES6 modules**, **error handling**, atau **debugging 101**. Gas terus, bro! 🏁🔥

---

<div align='center'>
⬅️ [Kembali](18-DOM-APIs.md) | 🏠 [Beranda](../../index.md) | [Lanjut ➡️](20-Using-keyword.md)
</div>
