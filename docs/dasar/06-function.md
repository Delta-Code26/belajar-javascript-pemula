Oke Bos Marno, saatnya kita ngulik **fungsi (function)** alias jurus rahasia dalam dunia pemrograman! 🧙‍♂️💻  
Fungsi itu kayak kombo skill di game: bisa dipanggil kapan aja buat nyelesain misi berulang!

Berikut isi lengkap buat file:  
`D:\dokumentasi\javascript\belajar-javascript-pemula\docs\dasar\06-fungsi.md`

---

```markdown
# 🧙‍♂️ Fungsi (Function) di JavaScript

> "Kalau hidup punya tujuan, kode juga harus punya fungsi." — Dev Baper di malam minggu

---

## 🎯 Tujuan Pembelajaran

Di akhir materi ini, kamu akan:
- Mengerti apa itu fungsi dan kenapa penting
- Bisa bikin fungsi sendiri
- Bisa pakai parameter & return value
- Kenal tipe fungsi: deklarasi & ekspresi

---

## 🧠 Apa Itu Fungsi?

Fungsi = blok kode yang bisa dipakai berulang-ulang.  
Bisa diibaratkan kayak mesin otomatis buat tugas tertentu.

```javascript
function sapa() {
  console.log("Halo, Marno!");
}

sapa(); // Output: Halo, Marno!
```

---

## 🧱 Struktur Fungsi

```javascript
function namaFungsi() {
  // isi perintah di sini
}
```

Panggil dengan: `namaFungsi();`

---

## 📥 Fungsi dengan Parameter

```javascript
function sapa(nama) {
  console.log("Halo, " + nama + "!");
}

sapa("Marno"); // Output: Halo, Marno!
sapa("Putri"); // Output: Halo, Putri!
```

---

## 📤 Fungsi dengan Return Value

```javascript
function tambah(a, b) {
  return a + b;
}

let hasil = tambah(3, 5);
console.log(hasil); // 8
```

---

## 🧠 Function Expression

Fungsi bisa disimpan dalam variabel juga:

```javascript
const kali = function(x, y) {
  return x * y;
};

console.log(kali(4, 5)); // 20
```

---

## ⚡ Arrow Function (Versi Singkat)

Arrow function = gaya modern, lebih ringkas:

```javascript
const bagi = (a, b) => {
  return a / b;
};

console.log(bagi(10, 2)); // 5
```

Kalau cuma 1 baris:
```javascript
const halo = nama => `Halo, ${nama}!`;
console.log(halo("Marno")); // Halo, Marno!
```

---

## 🧠 Quiz Mini

Apa hasil dari kode berikut?

```javascript
function cek(nama) {
  return "Halo " + nama;
}
console.log(cek("Asep"));
```

- A. `Halo Asep`  
- B. `cek Asep`  
- C. `undefined`  
- D. Error

✅ **Jawaban:** A. `Halo Asep`

---

## 💪 Tantangan Coding

1. Buat fungsi `luasPersegi(sisi)` → return luas
2. Buat fungsi `luasSegitiga(alas, tinggi)` → return luas
3. Buat fungsi `cekGanjilGenap(angka)` → return `'Ganjil'` atau `'Genap'`

Bonus: Gunakan arrow function buat semuanya ⚡

---

## 🧠 Tips Tambahan

- Fungsi bikin kode lebih rapi, reusable, dan mudah diuji
- Jangan takut pecah-pecah kode ke fungsi kecil
- Kombinasikan fungsi dengan loop atau kondisi buat skill kombo! 🌀

---

## 🔁 Kembali ke [Daftar Materi](../../index.md)
```

---

Next: Kita bisa lanjut ke **Array dan metode-metodenya** — karena data itu asyik kalau diolah rame-rame kayak arisan digital 😆  
Bilang aja: **"Lanjut ke array!"** dan kita buatkan file `07-array.md`!

Atau mau tambahin latihan coding interaktif buat tiap fungsi? Bisa juga!