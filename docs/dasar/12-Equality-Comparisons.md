Siap, boskuu! Sekarang kita masuk ke topik yang sering bikin galau developer:  
**Perbandingan (Equality) di JavaScript** — alias si `==` dan `===` yang kelihatannya mirip tapi kelakuannya beda banget 🤯

Berikut isi lengkap file:  
`D:\dokumentasi\javascript\belajar-javascript-pemula\docs\dasar\12-Equality-Comparisons.md`

---

```markdown
# 🤝 Perbandingan Nilai (Equality) di JavaScript

> “Kelihatannya sama, tapi ternyata beda. Kayak dia pas udah punya yang lain 😔”

---

## 🎯 Tujuan Pembelajaran

Setelah membaca ini, kamu akan:
- Mengerti perbedaan `==` dan `===`
- Tahu cara membandingkan nilai dengan benar
- Terhindar dari jebakan type coercion

---

## 🧠 Apa Itu Equality Comparison?

Perbandingan adalah cara untuk mengecek apakah dua nilai itu **sama** atau **tidak**.

Di JavaScript, ada dua operator utama:

| Operator | Nama                    | Perbandingan |
|----------|-------------------------|--------------|
| `==`     | Loose Equality          | Membandingkan setelah konversi tipe (coercion) |
| `===`    | Strict Equality         | Membandingkan nilai dan tipe secara ketat |

---

## ⚖️ Contoh `==` (Loose Equality)

```javascript
5 == "5";         // true
0 == false;       // true
"" == false;      // true
null == undefined;// true
```

⚠️ Tapi ini bisa jadi **bahaya** karena JavaScript otomatis konversi tipe!

---

## 🧱 Contoh `===` (Strict Equality)

```javascript
5 === "5";        // false
0 === false;      // false
"" === false;     // false
null === undefined; // false
```

✅ Lebih aman karena tidak ada coercion!

---

## 🚨 Jangan Terjebak Coercion!

Contoh jebakan maut:
```javascript
"0" == false   // true
[] == false    // true
[] == 0        // true
"" == 0        // true
```

Tapi:
```javascript
[] === false   // false
[] === 0       // false
```

---

## 🧪 Perbandingan dengan `Object`, `Array`, dan `Function`

Semua referensi objek dibandingkan berdasarkan **referensi** (alamat memori), bukan isi!

```javascript
[] == []            // false
{} == {}            // false

let a = [];
let b = a;
a == b              // true
```

---

## ✅ Best Practice

- Selalu gunakan `===` dan `!==`  
- Gunakan `==` **hanya jika kamu benar-benar tahu yang kamu lakukan**
- Hati-hati membandingkan nilai falsy seperti `0`, `""`, `null`, dan `undefined`

---

## 🧠 Quiz Mini

Apa hasil dari:

```javascript
false == "0"
```

- A. true  
- B. false  
- C. Error  
- D. undefined

✅ **Jawaban:** A. `true`  
Karena keduanya di-coerce ke number 0.

---

## 💪 Tantangan Coding

1. Buat dua variabel `a = 5` dan `b = "5"`, bandingkan dengan `==` dan `===`
2. Bandingkan array kosong `[]` dengan `false` dan cek hasilnya.
3. Buat object `user1` dan `user2` dengan isi yang sama, lalu bandingkan. Kenapa hasilnya `false`?

---

## 🤓 Tips Pro

- Gunakan `Object.is()` jika kamu butuh banding lebih ketat dari `===`
- Pahami nilai **falsy** di JS: `0`, `""`, `null`, `undefined`, `NaN`, `false`

---

## 🧠 Ingat!

| Ekspresi             | Hasil dengan `==` | Hasil dengan `===` |
|----------------------|------------------|--------------------|
| `5 == "5"`           | true             | false              |
| `null == undefined`  | true             | false              |
| `[] == false`        | true             | false              |
| `0 == false`         | true             | false              |

---

## 🔁 Kembali ke [Daftar Materi](../../index.md)
```

---

Gimana? Udah nggak tertipu `==` vs `===` lagi kan? 😎  
Kalau kamu mau lanjut, kita bisa bahas tentang **Truthy & Falsy**, **Operator Logika**, atau masuk ke **Control Flow yang lebih dalam**. Kasih komando aja, komandan 🫡