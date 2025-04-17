Mantap, sekarang kita masuk ke inti dapurnya JavaScript: **Ekspresi dan Operator**!  
Ibaratnya ini senjata utama buat ngolah data dan bikin program bisa mikir 💥🧠

Berikut isi lengkap file:  
`D:\dokumentasi\javascript\belajar-javascript-pemula\docs\dasar\14-Expressions-and-Operators.md`

---

```markdown
# 🧮 Expressions dan Operators di JavaScript

> “JavaScript tanpa operator ibarat sawit tanpa dodos — nggak bisa panen cuy!”

---

## 🎯 Tujuan Pembelajaran

Setelah mempelajari ini, kamu akan:
- Paham apa itu ekspresi
- Tahu berbagai jenis operator di JavaScript
- Bisa ngoperasikan nilai dan logika dalam kode

---

## 🧠 Apa Itu Ekspresi?

Ekspresi adalah **kombinasi nilai, variabel, dan operator** yang menghasilkan sebuah nilai.

Contoh:

```javascript
5 + 3       // ekspresi dengan hasil 8
a * 10      // hasil tergantung nilai a
true && false // ekspresi boolean
```

---

## 🔧 Jenis-Jenis Operator

### 1. 🧮 Operator Aritmatika

Digunakan untuk operasi matematika dasar.

| Operator | Nama         | Contoh       |
|----------|--------------|--------------|
| `+`      | Penjumlahan  | `5 + 2` = 7  |
| `-`      | Pengurangan  | `5 - 2` = 3  |
| `*`      | Perkalian    | `5 * 2` = 10 |
| `/`      | Pembagian    | `5 / 2` = 2.5|
| `%`      | Modulus      | `5 % 2` = 1  |
| `**`     | Eksponen     | `2 ** 3` = 8 |

---

### 2. 🟰 Operator Penugasan

Untuk mengisi atau mengubah nilai variabel.

```javascript
let x = 10;
x += 5;  // x = x + 5 → 15
x *= 2;  // x = x * 2 → 30
```

---

### 3. 🔍 Operator Perbandingan

Digunakan untuk membandingkan dua nilai.

| Operator | Arti                        |
|----------|-----------------------------|
| `==`     | Sama nilai (longgar)        |
| `===`    | Sama nilai dan tipe (ketat) |
| `!=`     | Tidak sama nilai            |
| `!==`    | Tidak sama nilai atau tipe  |
| `>`      | Lebih besar                 |
| `<`      | Lebih kecil                 |
| `>=`     | Lebih besar atau sama       |
| `<=`     | Lebih kecil atau sama       |

---

### 4. ⚙️ Operator Logika

Digunakan untuk logika boolean.

| Operator | Nama           | Contoh         |
|----------|----------------|----------------|
| `&&`     | AND            | `true && true` |
| `||`     | OR             | `true || false`|
| `!`      | NOT            | `!true` = false|

---

### 5. 📦 Operator String

```javascript
"halo" + " dunia" // "halo dunia"
```

Kalau kamu `+` antara string dan angka, angka akan diubah jadi string:

```javascript
"hasil: " + 10 // "hasil: 10"
```

---

### 6. 👥 Operator Tipe

```javascript
typeof 123      // "number"
typeof "hello"  // "string"
typeof true     // "boolean"
typeof {}       // "object"
```

---

### 7. ❓ Ternary Operator

Operator kondisional singkat.

```javascript
let hasil = (nilai >= 75) ? "Lulus" : "Gagal";
```

---

## 🧠 Ekspresi vs Pernyataan

- **Ekspresi**: Menghasilkan nilai  
- **Pernyataan (Statement)**: Melakukan aksi

Contoh ekspresi:

```javascript
5 + 3
nama === "Marno"
```

Contoh pernyataan:

```javascript
if (nilai > 80) {
  console.log("Bagus!");
}
```

---

## 💪 Tantangan Coding

1. Buat ekspresi untuk menghitung luas persegi panjang.
2. Coba gunakan `typeof` pada string, boolean, dan array.
3. Gunakan ternary operator untuk menentukan hasil lulus/gagal.

---

## 🔁 Kembali ke [Daftar Materi](../../index.md)
```

---

Kalau udah paham ini, kamu udah bisa "ngoding mikir" 💡  
Next kita bisa lanjut ke topik seru kayak **Error Handling**, **Asynchronous JavaScript (Promise & async/await)**, atau **DOM Manipulation**. Tinggal bilang, bro! 🧠⚡