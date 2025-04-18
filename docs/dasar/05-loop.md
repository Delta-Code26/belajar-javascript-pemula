Gas terus Marno! Sekarang saatnya masuk ke dunia perulangan alias **looping** — skill wajib buat ngoding efisien tanpa ngopi sampai pagi! 🔁☕

Berikut isi lengkap buat file:  
`D:\dokumentasi\javascript\belajar-javascript-pemula\docs\dasar\05-perulangan.md`

---

```markdown
# 🔁 Perulangan (Loop) di JavaScript

> "Kalau hidupmu terasa berulang-ulang, selamat, kamu udah kayak program." — Dev Galau

---

## 🎯 Tujuan Pembelajaran

Di materi ini, kamu akan:
- Mengenal jenis-jenis perulangan di JavaScript
- Mengetahui kapan dan bagaimana menggunakan `for`, `while`, dan `do...while`
- Paham cara break dan continue kerja loop

---

## 🔂 Kenapa Butuh Loop?

Bayangin mau print "Halo" 100 kali. Masa nulis 100 `console.log()`?  
Loop = cara otomatis dan cerdas untuk ngulang suatu aksi berkali-kali 💡

---

## 🔁 Tipe-Tipe Perulangan

### 1. 🔄 `for` loop

Cocok buat loop dengan jumlah pasti.

```javascript
for (let i = 1; i <= 5; i++) {
  console.log("Loop ke-", i);
}
```

Penjelasan:
- `let i = 1` → mulai dari 1
- `i <= 5` → berhenti saat i lebih dari 5
- `i++` → setiap putaran naik 1

---

### 2. 🌀 `while` loop

Dipakai kalau jumlah perulangan **nggak pasti**, asal kondisinya masih `true`.

```javascript
let i = 1;
while (i <= 5) {
  console.log("While loop ke-", i);
  i++;
}
```

---

### 3. 🔁 `do...while` loop

Mirip `while`, tapi dijalankan **minimal sekali**, walau kondisi `false`.

```javascript
let i = 1;
do {
  console.log("Do...While ke-", i);
  i++;
} while (i <= 5);
```

---

## ✂️ `break` dan `continue`

### 🔚 `break` → menghentikan loop

```javascript
for (let i = 1; i <= 10; i++) {
  if (i === 5) break;
  console.log(i);
}
// Output: 1 2 3 4
```

### ⏩ `continue` → skip 1 iterasi

```javascript
for (let i = 1; i <= 5; i++) {
  if (i === 3) continue;
  console.log(i);
}
// Output: 1 2 4 5
```

---

## 🧠 Quiz Mini

Berapa kali kode ini nge-print "Halo"?

```javascript
let i = 1;
while (i < 4) {
  console.log("Halo");
  i++;
}
```

- A. 2 kali  
- B. 3 kali  
- C. 4 kali  
- D. Infinite loop

✅ **Jawaban:** B. 3 kali (i: 1, 2, 3)

---

## 💪 Tantangan Coding

1. Buat program yang menampilkan angka 1 sampai 100
2. Tampilkan hanya angka genap
3. Jika angka kelipatan 10, tampilkan: `"Kelipatan 10: 10"` dst.

Contoh output:
```
2
4
...
10 → Kelipatan 10!
...
100 → Kelipatan 10!
```

---

## 🧠 Tips Tambahan

- Gunakan `for` kalau kamu tahu berapa kali harus ngulang
- Gunakan `while` buat kondisi dinamis (contoh: login sampai benar)
- Jangan lupa update nilai loop biar gak infinite loop (browser kamu bisa ngambek lho)

---

## 🔁 Kembali ke [Daftar Materi](../../index.md)
```

---

Kalau kamu mau lanjut bahas jurus sakti berikutnya: **fungsi!**  
Bilang aja: **"Lanjut ke fungsi!"** dan kita bakal bikin `06-fungsi.md` bareng 🧙‍♂️✨

Mau lanjut atau rehat dulu, Bos Marno? 😎

---

<div align='center'>
⬅️ [Kembali](04-Logika.md) | 🏠 [Beranda](../../index.md) | [Lanjut ➡️](06-Function.md)
</div>
