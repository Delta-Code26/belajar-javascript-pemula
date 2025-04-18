Siap, bro! Kali ini kita gaskeun ke materi yang sering dipakai buat ngulang-ngulang proses secara otomatis — alias **Loops and Iterations** 🔁

Berikut isi lengkap file:  
`D:\dokumentasi\javascript\belajar-javascript-pemula\docs\dasar\13-Loops-and-Iterations.md`

---

```markdown
# 🔁 Loops & Iterasi di JavaScript

> “Ngoding tanpa loop itu kayak panen sawit manual—capek, lambat, dan bikin nangis 😭”

---

## 🎯 Tujuan Pembelajaran

Setelah belajar ini, kamu akan:
- Memahami konsep pengulangan (loop)
- Menggunakan berbagai macam loop di JavaScript
- Menentukan loop yang tepat untuk tiap kasus

---

## 🧠 Apa Itu Loop?

Loop adalah cara untuk menjalankan perintah **berulang kali** tanpa harus menulis kode yang sama berkali-kali.

---

## 🔄 1. `for` Loop

Loop klasik. Punya tiga bagian: inisialisasi, kondisi, dan increment.

```javascript
for (let i = 0; i < 5; i++) {
  console.log("Iterasi ke-" + i);
}
```

---

## 🔁 2. `while` Loop

Loop yang akan terus berjalan selama kondisinya **true**.

```javascript
let i = 0;
while (i < 5) {
  console.log("While ke-" + i);
  i++;
}
```

---

## 🔂 3. `do...while` Loop

Mirip `while`, tapi **dijamin berjalan minimal 1 kali**.

```javascript
let i = 0;
do {
  console.log("Do While ke-" + i);
  i++;
} while (i < 5);
```

---

## 🧭 4. `for...of` Loop

Loop untuk **array atau iterable object**.

```javascript
let buah = ["apel", "pisang", "mangga"];
for (let item of buah) {
  console.log(item);
}
```

---

## 🗂️ 5. `for...in` Loop

Loop untuk **object properties (key)**.

```javascript
let pekerja = { nama: "Marno", umur: 21, asal: "Malaysia" };
for (let key in pekerja) {
  console.log(key + ": " + pekerja[key]);
}
```

---

## 🚨 Break & Continue

- `break` → keluar dari loop
- `continue` → skip iterasi saat ini, lanjut ke berikutnya

```javascript
for (let i = 1; i <= 5; i++) {
  if (i === 3) continue;
  console.log(i);
}
// Output: 1, 2, 4, 5
```

---

## ✅ Kapan Gunakan Yang Mana?

| Kebutuhan                        | Gunakan       |
|----------------------------------|---------------|
| Loop berdasarkan jumlah pasti    | `for`         |
| Loop sampai kondisi berhenti     | `while`       |
| Loop minimal sekali jalan        | `do...while`  |
| Loop isi array/list              | `for...of`    |
| Loop property dalam object       | `for...in`    |

---

## 🧠 Quiz Mini

Berapa kali loop ini jalan?

```javascript
let i = 5;
do {
  console.log(i);
  i++;
} while (i < 5);
```

- A. 0  
- B. 1  
- C. 5  
- D. Infinite Loop

✅ **Jawaban:** B. 1  
Karena `do...while` akan jalan dulu baru cek kondisi.

---

## 💪 Tantangan Coding

1. Print angka ganjil dari 1 sampai 20 pakai `for`.
2. Loop array pekerja dan print semua nama.
3. Loop object data panen dan tampilkan semua key dan value.

---

## 🧠 Tips Pro

- Hindari infinite loop (loop yang nggak pernah berhenti) — bisa hang browser!
- Gunakan `forEach`, `map`, dan method array modern saat sudah paham dasar loop

---

## 🔁 Kembali ke [Daftar Materi](../../index.md)
```

---

Siip~ dengan ini kamu udah paham looping dasar di JavaScript.  
Kalau mau lanjut, kita bisa bahas **`Array.prototype.map`, `filter`, `reduce`**, atau langsung ke **asynchronous loop** kayak `for await...of`. Tinggal bilang aja yaa 🚀

---

<div align='center'>
⬅️ [Kembali](12-Equality-Comparisons.md) | 🏠 [Beranda](../../index.md) | [Lanjut ➡️](14-Expressions-and-Operators.md)
</div>
