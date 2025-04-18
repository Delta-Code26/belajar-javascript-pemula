Oke bro, saatnya kita bahas fondasi penting dalam alur logika program: **Control Flow**  
Alias... gimana caranya bikin program lo bisa "milih jalan hidupnya sendiri" 🧠🛣️

Berikut isi lengkap file:  
`D:\dokumentasi\javascript\belajar-javascript-pemula\docs\dasar\15-Control-flow.md`

---

```markdown
# 🧭 Control Flow di JavaScript

> "Control flow tuh ibarat rambu lalu lintas buat kode—tanpa itu, semua bakal kacau balau 😵‍💫"

---

## 🎯 Tujuan Pembelajaran

Setelah mempelajari ini, kamu akan:
- Memahami cara program mengambil keputusan
- Menggunakan `if`, `else`, `switch`, dan ternary operator
- Mengontrol alur program berdasarkan kondisi

---

## 🔀 Apa Itu Control Flow?

Control flow adalah **urutan eksekusi perintah** dalam program. Dengan control flow, kita bisa:

- Menentukan kondisi
- Menjalankan kode tertentu saat kondisi terpenuhi
- Mengabaikan bagian lain saat kondisi tidak terpenuhi

---

## 🧱 1. `if` Statement

```javascript
let cuaca = "hujan";

if (cuaca === "hujan") {
  console.log("Bawa payung!");
}
```

---

## 🔄 2. `if...else`

```javascript
let nilai = 70;

if (nilai >= 75) {
  console.log("Lulus!");
} else {
  console.log("Gagal!");
}
```

---

## 🧩 3. `else if`

```javascript
let nilai = 85;

if (nilai >= 90) {
  console.log("A");
} else if (nilai >= 80) {
  console.log("B");
} else if (nilai >= 70) {
  console.log("C");
} else {
  console.log("D");
}
```

---

## 🔘 4. Ternary Operator

Singkatan dari `if...else` yang ringkas.

```javascript
let usia = 18;
let status = (usia >= 17) ? "Dewasa" : "Remaja";
```

---

## 🗂️ 5. `switch` Statement

Cocok untuk banyak kondisi yang berdasarkan 1 variabel.

```javascript
let hari = "Senin";

switch (hari) {
  case "Senin":
    console.log("Awal minggu");
    break;
  case "Jumat":
    console.log("Hampir weekend");
    break;
  default:
    console.log("Hari biasa");
}
```

> Jangan lupa `break`, kalau enggak, dia bakal lanjut ke case selanjutnya!

---

## ❗ Tips Penting

- Pakai `switch` untuk banyak cabang nilai dari satu variabel
- Pakai `if` untuk kondisi kompleks atau pakai operator logika
- Gunakan ternary kalau kondisi dan aksi-nya pendek

---

## 🧠 Quiz Mini

```javascript
let skor = 65;
let hasil = (skor >= 70) ? "Lulus" : "Remedial";
console.log(hasil);
```

Apa output dari kode di atas?

✅ Jawaban: `"Remedial"`

---

## 💪 Tantangan Coding

1. Buat kode yang mengecek apakah suatu angka genap atau ganjil.
2. Gunakan `switch` untuk mencetak nama hari berdasarkan angka (1 = Senin, 7 = Minggu).
3. Pakai `if else` untuk menentukan kategori usia:
   - < 13: Anak-anak
   - < 18: Remaja
   - >= 18: Dewasa

---

## 🔁 Kembali ke [Daftar Materi](../../index.md)
```

---

Gokil! Sekarang kamu udah ngerti cara bikin kode "milih jalan" kayak di game RPG 🎮  
Kalau siap, kita bisa lanjut ke topik yang lebih dalam seperti **fungsi callback**, **async/await**, atau mulai ngulik ke **DOM dan event listener**. Let's go! 🚀

---

<div align='center'>
⬅️ [Kembali](14-Expressions-and-Operators.md) | 🏠 [Beranda](../../index.md) | [Lanjut ➡️](17-Functions.md)
</div>
