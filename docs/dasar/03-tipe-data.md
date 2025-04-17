## 03 TIPE DATA

```markdown
# 📦 Tipe Data di JavaScript

> "Tipe data itu kayak karakter game. Ada yang kuat, ada yang fleksibel, dan ada juga yang misterius kayak `undefined`." — Dev RPG 🎮

---

## 🎯 Tujuan Pembelajaran

Setelah mempelajari materi ini, kamu akan:
- Mengenal berbagai jenis tipe data di JavaScript
- Bisa membedakan antara `number`, `string`, `boolean`, dan lainnya
- Tahu cara mengecek tipe data

---

## 📋 Daftar Tipe Data Utama

| Tipe Data    | Contoh                        |
|--------------|-------------------------------|
| String       | `"halo"`, `'javascript'`      |
| Number       | `123`, `3.14`                 |
| Boolean      | `true`, `false`               |
| Undefined    | variabel yang belum diisi     |
| Null         | nilai kosong (sengaja dikosongin) |
| Object       | `{nama: "Marno", umur: 21}`   |
| Array        | `["apel", "jeruk", "durian"]` |

---

## 🔍 Penjelasan Sederhana

### 🔤 String
Teks yang dibungkus pakai tanda kutip:
```javascript
let nama = "Marno";
```

### 🔢 Number
Angka, bisa bulat atau desimal:
```javascript
let umur = 21;
let berat = 65.5;
```

### 🔘 Boolean
Cuma ada 2 nilai: `true` atau `false`
```javascript
let sedangBelajar = true;
```

### 🌫 Undefined
Kalau kamu bikin variabel tapi belum isi nilainya:
```javascript
let mood;
console.log(mood); // undefined
```

### 🕳 Null
Nilai kosong tapi dengan sengaja dikosongin:
```javascript
let pacar = null;
```

### 🧱 Object
Kumpulan data dalam format kunci-nilai:
```javascript
let orang = {
  nama: "Marno",
  umur: 21,
  asal: "Malaysia"
};
```

### 📚 Array
Kumpulan data yang berurutan:
```javascript
let buah = ["apel", "mangga", "durian"];
```

---

## 🧪 Mengecek Tipe Data

Gunakan `typeof`:

```javascript
let umur = 20;
console.log(typeof umur); // "number"

let nama = "Marno";
console.log(typeof nama); // "string"
```

---

## 🧠 Quiz Mini

Apa hasil dari kode berikut?

```javascript
let x;
console.log(typeof x);
```

- A. `null`
- B. `undefined`
- C. `object`
- D. `error`

✅ **Jawaban:** B. `undefined` karena `x` belum punya nilai.

---

## 💪 Tantangan Coding

1. Buat variabel untuk menyimpan:
   - Nama (string)
   - Umur (number)
   - Apakah kamu suka ngoding? (boolean)
   - Tanggal lahir (string atau object Date)
   - List hobi kamu (array)
   - Data profil lengkap kamu (object)

2. Tampilkan semuanya pakai `console.log()`

---

## 🧠 Tips Tambahan

- Tipe data penting banget buat logika program
- JavaScript itu **dinamis** — tipe datanya bisa berubah tergantung nilai:
```javascript
let data = 123;      // number
data = "seratus";    // sekarang jadi string
```

---

## 🔁 Kembali ke [Daftar Materi](../../index.md)
```

---

Gas lagi? Kalau kamu bilang: **"Lanjut ke logika!"**  
Gue siapin `04-logika.md` lengkap sama operator dan humor seger 🤓✨