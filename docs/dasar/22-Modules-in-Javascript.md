Berikut isi lengkap untuk file:  
`D:\dokumentasi\javascript\belajar-javascript-pemula\docs\dasar\22-Modules-in-Javascript.md`

---

```markdown
# 📦 Modules in JavaScript

> "Modules di JavaScript itu kayak lemari di rumah lo. Semua barang dikelompokkan dan disimpan rapi, jadi lo bisa ambil dengan mudah dan terorganisir."

---

## 🎯 Tujuan Pembelajaran

Setelah mempelajari ini, kamu akan:
- Mengerti apa itu **modules** dalam JavaScript
- Bisa memisahkan kode menjadi beberapa file menggunakan **export** dan **import**
- Mengetahui perbedaan antara **CommonJS** dan **ES6 Modules**

---

## 🧩 Apa Itu Modules?

Modules di JavaScript adalah cara untuk membagi kode kamu ke dalam file yang lebih kecil dan terpisah. Ini membantu dalam mengorganisir kode agar lebih rapi dan memudahkan pengelolaan proyek besar.

### Kenapa Modules Penting?
- Membantu dalam **scoping**, sehingga variabel dan fungsi tidak berserakan ke seluruh proyek.
- Memudahkan dalam **reuse code** antara berbagai bagian aplikasi.
- Meningkatkan **maintainability**, karena setiap modul hanya menangani satu tugas tertentu.

---

## 🛠️ 1. **Exporting** dan **Importing**

Di JavaScript, kamu bisa menggunakan dua cara untuk **export** dan **import** modul:  
- **Named Exports**
- **Default Export**

### 📤 Named Exports

Menggunakan `export` untuk mengekspor beberapa variabel atau fungsi dari modul.

#### Contoh:

**math.js** (file module)
```javascript
export const add = (a, b) => a + b;
export const subtract = (a, b) => a - b;
```

**main.js** (file utama)
```javascript
import { add, subtract } from './math.js';

console.log(add(2, 3));        // 5
console.log(subtract(5, 3));   // 2
```

---

### 📤 Default Export

Menggunakan `export default` untuk mengekspor satu nilai atau objek sebagai default.

#### Contoh:

**calculator.js** (file module)
```javascript
export default function multiply(a, b) {
  return a * b;
}
```

**main.js** (file utama)
```javascript
import multiply from './calculator.js';

console.log(multiply(2, 3));   // 6
```

---

## 🌍 2. **Menggunakan Modules di Browser**

Untuk menggunakan modules di browser, kamu perlu menambahkan atribut `type="module"` di tag `<script>`.

#### Contoh:

**index.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Modular JavaScript</title>
</head>
<body>
  <script type="module">
    import { add } from './math.js';
    console.log(add(2, 3));  // 5
  </script>
</body>
</html>
```

**math.js**
```javascript
export const add = (a, b) => a + b;
```

**Catatan**: Pada penggunaan **modules di browser**, file JavaScript harus diakses melalui server (local server atau web server), dan bukan file system langsung (file:///).

---

## 🔧 3. **CommonJS vs ES6 Modules**

JavaScript memiliki dua sistem modul yang populer:
- **CommonJS**: Digunakan di **Node.js** dan mengekspor menggunakan `module.exports` dan `require()`.
- **ES6 Modules**: Merupakan standar modul di JavaScript modern yang menggunakan `export` dan `import`.

### Contoh CommonJS:
**math.js**
```javascript
module.exports = {
  add: (a, b) => a + b,
  subtract: (a, b) => a - b
};
```

**main.js**
```javascript
const math = require('./math.js');
console.log(math.add(2, 3));  // 5
console.log(math.subtract(5, 3)); // 2
```

### Kapan Menggunakan Mana?
- **CommonJS** digunakan di server-side JavaScript (Node.js).
- **ES6 Modules** digunakan di browser dan proyek JavaScript modern yang menggunakan bundler seperti Webpack atau Rollup.

---

## ⚡ 4. **Dynamic Import**

ES6 Modules memungkinkan kita untuk mengimpor modul secara dinamis, yang bisa membantu mengoptimalkan performa dengan hanya memuat modul ketika dibutuhkan.

#### Contoh:

```javascript
if (someCondition) {
  import('./math.js')
    .then((math) => {
      console.log(math.add(2, 3));
    })
    .catch((error) => {
      console.error('Error loading module:', error);
    });
}
```

Dengan dynamic import, modul hanya akan dimuat saat dibutuhkan, meningkatkan efisiensi aplikasi.

---

## 💡 Tips

- Gunakan **default export** ketika modul hanya memiliki satu ekspor utama, seperti fungsi atau kelas.
- Gunakan **named exports** untuk mengekspor beberapa variabel atau fungsi dari modul.
- Manfaatkan **dynamic imports** untuk hanya memuat modul saat dibutuhkan, misalnya untuk modul yang jarang digunakan atau berbasis fitur.
- Di proyek Node.js, lebih sering menggunakan **CommonJS**, sementara di proyek frontend modern, gunakan **ES6 Modules**.

---

## 💪 Tantangan Coding

1. Buat dua modul: satu untuk fungsi matematika (`add`, `subtract`, `multiply`, dll.) dan satu untuk mengelola data pengguna (misalnya, `createUser`, `getUser`). Ekspor dan impor fungsi-fungsi tersebut di file utama.
2. Implementasikan **dynamic import** untuk memuat modul tertentu hanya ketika suatu event terjadi (misalnya, klik tombol).
3. Pisahkan kode proyek yang lebih besar menjadi beberapa modul menggunakan **ES6 Modules**.

---

## 🔁 Kembali ke [Daftar Materi](../../index.md)
```

---

Sekarang kamu sudah paham betul soal **modules di JavaScript**! Dengan memanfaatkan **export** dan **import**, kamu bisa membagi aplikasi JavaScript menjadi bagian-bagian kecil yang rapi dan mudah dikelola.  
Lanjut terus, dan kita bisa bahas lebih lanjut tentang **bundling tools** atau **JavaScript libraries** lainnya! 🚀

---

<div align='center'>
⬅️ [Kembali](21-Asynchronous-Javascript.md) | 🏠 [Beranda](../../index.md) | [Lanjut ➡️](23-Iterators-and-generators.md)
</div>
