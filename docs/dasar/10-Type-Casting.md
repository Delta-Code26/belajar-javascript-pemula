Langsung kita gas, bro! Kali ini kita bahas topik yang sering bikin pemula bengong: **Type Casting** di JavaScript — alias cara nyulap satu tipe data jadi tipe lain. ⚡

Berikut isi lengkap untuk file:  
`D:\dokumentasi\javascript\belajar-javascript-pemula\docs\dasar\10-Type-Casting.md`

---

```markdown
# 🔄 Type Casting di JavaScript

> “Kalau hidup bisa berubah, kenapa tipe data nggak? 😎”  
> Yup, di JavaScript, semua bisa berubah… asal kamu paham cara casting-nya!

---

## 🎯 Tujuan Pembelajaran

Setelah membaca materi ini, kamu akan:
- Mengerti perbedaan antara type casting **implisit** dan **eksplisit**
- Bisa mengubah tipe data dari string ke number, boolean, dan sebaliknya
- Tahu trik-trik casting yang sering digunakan di JavaScript

---

## 🧠 Apa Itu Type Casting?

**Type casting** adalah proses mengubah satu tipe data ke tipe lain.

Contoh:
```javascript
let angka = "42";
let hasil = Number(angka); // dari string ke number
```

---

## 1️⃣ Implicit Type Casting (Coercion)

JavaScript kadang otomatis ubah tipe data saat dibutuhkan.

Contoh:
```javascript
let hasil = "5" * 2;    // hasil: 10 → "5" diubah jadi number
let gabung = "5" + 2;   // hasil: "52" → angka diubah jadi string
```

⚠️ **Hati-hati!**  
`+` bisa berarti penjumlahan **atau** penggabungan string.

---

## 2️⃣ Explicit Type Casting

Kamu ubah tipe data secara langsung pakai fungsi:

### ➡️ String → Number

```javascript
Number("42");        // 42
parseInt("42px");    // 42
parseFloat("3.14");  // 3.14
```

### ➡️ Number → String

```javascript
String(42);          // "42"
(42).toString();     // "42"
```

### ➡️ Boolean → String / Number

```javascript
String(true);        // "true"
Number(false);       // 0
```

### ➡️ String / Number → Boolean

```javascript
Boolean("halo");     // true
Boolean("");         // false
Boolean(1);          // true
Boolean(0);          // false
```

---

## 🔥 Trik Cepat Type Casting

### 1. `!!` → ke Boolean

```javascript
!!"halo";     // true
!!0;          // false
```

### 2. `+` → ke Number

```javascript
+"123";       // 123
+"3.14";      // 3.14
```

### 3. Template literal atau `"" +` → ke String

```javascript
"" + 123;     // "123"
`${true}`;    // "true"
```

---

## 🧪 Cek Tipe Data

Pakai `typeof` buat ngecek hasil casting:

```javascript
let hasil = Number("123");
console.log(typeof hasil); // "number"
```

---

## 🧠 Quiz Mini

Apa hasil dari:

```javascript
let x = "5";
let y = 2;
let z = x + y;
```

- A. 7  
- B. "7"  
- C. "52"  
- D. Error

✅ **Jawaban:** C. `"52"`  
Karena `+` digunakan, jadi string "5" + 2 di-coerce jadi string.

---

## 💪 Tantangan Coding

1. Buat fungsi yang menerima input string angka dan mengembalikan hasil perkalian setelah dikonversi ke number.
2. Konversikan array angka `[1, 2, 3]` ke string `"1,2,3"` dan kembali ke array.
3. Cek apakah input user bisa dikonversi ke number dengan aman (`!isNaN(Number(input))`).

---

## ⚠️ Tips Ngebut

- Jangan campur-campur string dan number kalau bisa dihindari.
- Selalu cek hasil `typeof` saat ngoding logic penting.
- Pakai `Number()`, `String()`, dan `Boolean()` biar jelas dan eksplisit.

---

## 🔁 Kembali ke [Daftar Materi](../../index.md)
```

---

Udah makin jago nih kamu, Marno! 🔥  
Abis ini kita bisa lanjut ke **null vs undefined**, **operator perbandingan**, atau **truthy & falsy values**. Mau lanjut ke mana, bosku?

---

<div align='center'>
⬅️ [Kembali](09-JSON.md) | 🏠 [Beranda](../../index.md) | [Lanjut ➡️](11-Data-Structures.md)
</div>
