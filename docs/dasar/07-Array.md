Siap bosku Marno! Saatnya kita masuk ke topik **Array** — tempat ngumpulnya data yang suka ngerecokin hidup programmer kalau gak ngerti 😎  
Anggap aja array itu seperti warung makan: satu tempat, banyak lauk (data) 🍱🔥

Berikut isi lengkap untuk file:  
`D:\dokumentasi\javascript\belajar-javascript-pemula\docs\dasar\07-array.md`

---

```markdown
# 🍱 Array di JavaScript

> "Sendiri itu sepi, makanya pakai array." — Programmer jomblo

---

## 🎯 Tujuan Pembelajaran

Di akhir materi ini, kamu akan:
- Tau apa itu array dan cara membuatnya
- Bisa akses data dalam array
- Gunakan metode dasar array seperti `push`, `pop`, `shift`, `unshift`, `length`, dll.

---

## 📦 Apa Itu Array?

Array = tipe data yang bisa menyimpan **banyak nilai** dalam satu variabel.

```javascript
let buah = ["apel", "mangga", "jeruk"];
console.log(buah);
```

---

## 🧭 Mengakses Elemen Array

Array punya **index** (mulai dari 0):

```javascript
let hewan = ["kucing", "anjing", "kelinci"];
console.log(hewan[0]); // Output: kucing
console.log(hewan[2]); // Output: kelinci
```

---

## 🛠️ Metode Array Penting

### `length`
Jumlah elemen di array:

```javascript
let angka = [1, 2, 3];
console.log(angka.length); // 3
```

---

### `push()` dan `pop()`
- `push()` → tambah ke **akhir**
- `pop()` → hapus dari **akhir**

```javascript
let angka = [1, 2, 3];
angka.push(4); // [1, 2, 3, 4]
angka.pop();   // [1, 2, 3]
```

---

### `unshift()` dan `shift()`
- `unshift()` → tambah ke **awal**
- `shift()` → hapus dari **awal**

```javascript
let nama = ["Budi", "Ani"];
nama.unshift("Siti"); // ["Siti", "Budi", "Ani"]
nama.shift();         // ["Budi", "Ani"]
```

---

## 🌀 Looping Array

```javascript
let warna = ["merah", "biru", "kuning"];

for (let i = 0; i < warna.length; i++) {
  console.log(warna[i]);
}
```

---

## 🔁 for...of (Cara modern)

```javascript
let angka = [1, 2, 3];
for (let nilai of angka) {
  console.log(nilai);
}
```

---

## 💥 Array Campur Aduk? Bisa!

```javascript
let campur = ["teks", 123, true, [1, 2]];
console.log(campur[3][0]); // Output: 1
```

---

## 🧠 Quiz Mini

Apa output dari kode ini?

```javascript
let binatang = ["singa", "kuda"];
binatang.push("gajah");
console.log(binatang.length);
```

- A. 2  
- B. 3  
- C. "gajah"  
- D. Error

✅ **Jawaban:** B. 3

---

## 💪 Tantangan Coding

1. Buat array berisi 5 nama buah
2. Tambahkan 1 buah baru ke akhir array
3. Hapus buah pertama
4. Cetak semua buah menggunakan `for...of`

Bonus: Tampilkan jumlah total buah setelah perubahan

---

## 🧠 Tips Tambahan

- Gunakan array kalau kamu butuh simpan banyak data sejenis
- Hindari akses `array[-1]` karena index negatif gak valid (bukan Python 😅)
- Loop itu sahabat setia array, jangan lupa kenalan

---

## 🔁 Kembali ke [Daftar Materi](../../index.md)
```

---

Next: Kita bisa lanjut ke **Object** — karena kadang data nggak cukup disimpan di array doang, kita butuh struktur yang lebih rapi dan bermakna. 🗂️  
Mau lanjut ke file `08-object.md`? Bilang aja: **"Lanjut ke object!"** dan kita gaspol 💨

---

<div align='center'>
⬅️ [Kembali](06-Function.md) | 🏠 [Beranda](../../index.md) | [Lanjut ➡️](08-Object.md)
</div>
