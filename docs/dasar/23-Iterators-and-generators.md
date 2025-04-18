Berikut isi lengkap untuk file:  
`D:\dokumentasi\javascript\belajar-javascript-pemula\docs\dasar\23-Iterators-and-generators.md`

---

```markdown
# 🔄 Iterators and Generators in JavaScript

> "Iterators dan Generators adalah alat untuk mengontrol bagaimana kita mengakses elemen dalam sebuah koleksi secara lebih fleksibel dan efisien."

---

## 🎯 Tujuan Pembelajaran

Setelah mempelajari ini, kamu akan:
- Memahami apa itu **iterators** dan **generators** di JavaScript
- Bisa membuat koleksi data yang bisa diiterasi menggunakan **iterator**
- Bisa membuat **generators** untuk menghasilkan data secara bertahap tanpa memuat semuanya sekaligus

---

## 🧩 Apa Itu Iterators?

**Iterator** adalah objek yang memungkinkan kita untuk mengakses elemen-elemen dari koleksi (seperti array atau objek) satu per satu tanpa mengakses koleksi tersebut secara langsung. Iterator menggunakan dua metode utama:  
- **`next()`**: Mengambil elemen berikutnya dalam koleksi.
- **`done`**: Menandakan apakah koleksi sudah habis atau belum.

Iterator biasanya digunakan dengan objek seperti array, string, atau map yang dapat diiterasi.

### Contoh:

```javascript
const numbers = [1, 2, 3];
const iterator = numbers[Symbol.iterator](); // Mendapatkan iterator untuk array

console.log(iterator.next()); // { value: 1, done: false }
console.log(iterator.next()); // { value: 2, done: false }
console.log(iterator.next()); // { value: 3, done: false }
console.log(iterator.next()); // { value: undefined, done: true }
```

**Catatan:** Pada contoh di atas, kita menggunakan `Symbol.iterator` untuk mendapatkan iterator untuk array. Setiap panggilan ke `next()` akan memberikan objek dengan dua properti:
- **value**: Nilai elemen berikutnya.
- **done**: Boolean yang menandakan apakah kita sudah selesai mengiterasi semua elemen.

---

## 🛠️ 1. Custom Iterator

Kamu bisa membuat iterator sendiri untuk objek atau struktur data kustom dengan mendefinisikan fungsi `next()` dan menggunakan `Symbol.iterator`.

#### Contoh:

```javascript
const myCollection = {
  items: ['apple', 'banana', 'cherry'],
  [Symbol.iterator]: function() {
    let index = 0;
    let items = this.items;

    return {
      next: function() {
        if (index < items.length) {
          return { value: items[index++], done: false };
        } else {
          return { value: undefined, done: true };
        }
      }
    };
  }
};

const iterator = myCollection[Symbol.iterator]();
console.log(iterator.next()); // { value: 'apple', done: false }
console.log(iterator.next()); // { value: 'banana', done: false }
console.log(iterator.next()); // { value: 'cherry', done: false }
console.log(iterator.next()); // { value: undefined, done: true }
```

---

## 🔄 Apa Itu Generators?

**Generators** adalah fungsi khusus yang memungkinkan kita untuk menunda eksekusi fungsi dan melanjutkannya di lain waktu menggunakan keyword `yield`. Generator memungkinkan kita untuk menghasilkan nilai satu per satu, yang sangat berguna ketika bekerja dengan data besar atau alur yang harus menghemat memori.

Generator dapat diidentifikasi dengan menggunakan `function*` (perhatikan tanda bintang setelah kata kunci `function`).

### Contoh Generator:

```javascript
function* generateNumbers() {
  yield 1;
  yield 2;
  yield 3;
}

const generator = generateNumbers();
console.log(generator.next()); // { value: 1, done: false }
console.log(generator.next()); // { value: 2, done: false }
console.log(generator.next()); // { value: 3, done: false }
console.log(generator.next()); // { value: undefined, done: true }
```

Di sini, setiap kali `next()` dipanggil, eksekusi fungsi generator dihentikan pada pernyataan `yield` dan akan dilanjutkan dari titik tersebut saat `next()` dipanggil lagi.

---

## 📝 2. Generator dengan Parameter

Kamu juga bisa memberikan nilai ke generator dengan menggunakan parameter `yield` dan mengembalikan nilai ke generator dengan `next()`.

#### Contoh:

```javascript
function* generatorWithParams() {
  let result = yield 'Masukkan angka:';
  console.log(`Angka yang dimasukkan: ${result}`);
  yield 'Selesai!';
}

const gen = generatorWithParams();
console.log(gen.next().value); // 'Masukkan angka:'
console.log(gen.next(5).value); // 'Selesai!'
```

**Catatan:** Ketika kita memanggil `gen.next(5)`, angka 5 dikirimkan ke dalam generator dan diproses pada bagian `yield`.

---

## 🔄 3. Menggunakan Generator untuk Asynchronous Programming

Generator juga sangat berguna untuk mengelola proses asynchronous dengan cara yang lebih sederhana, sebelum adanya `async/await`.

#### Contoh:

```javascript
function* fetchData() {
  const data = yield fetch('https://jsonplaceholder.typicode.com/posts');
  const posts = yield data.json();
  console.log(posts);
}

const gen = fetchData();
const dataPromise = gen.next().value;
dataPromise
  .then((data) => gen.next(data))
  .then((posts) => gen.next(posts));
```

Di sini, kita menggunakan generator untuk menangani proses asynchronous dengan cara yang lebih mirip dengan kode synchronous.

---

## ⚡ 4. Perbedaan Iterators dan Generators

- **Iterator**: Merupakan objek yang memiliki metode `next()` untuk mengiterasi elemen satu per satu. Biasanya digunakan dalam struktur data seperti array, string, dan set.
- **Generator**: Merupakan fungsi khusus yang dapat menghentikan eksekusi dengan `yield` dan melanjutkannya di kemudian waktu. Generator memudahkan pembuatan koleksi yang besar secara lebih efisien.

---

## 💡 Tips

- **Gunakan Iterator** jika kamu ingin mengakses elemen-elemen koleksi secara bertahap atau sekuensial.
- **Gunakan Generator** ketika kamu ingin menghasilkan data secara bertahap dan mengatur eksekusi fungsi dengan cara yang lebih fleksibel.
- Generator sangat berguna untuk menangani **asynchronous programming**, sebelum adanya `async/await`.

---

## 💪 Tantangan Coding

1. Buat iterator untuk objek `Books` yang memiliki beberapa properti dan bisa diiterasi menggunakan `next()`.
2. Coba buat generator untuk menghasilkan bilangan Fibonacci satu per satu.
3. Implementasikan generator untuk mengambil data secara bertahap menggunakan `fetch` dan `yield` untuk menangani data dari API secara lebih efisien.

---

## 🔁 Kembali ke [Daftar Materi](../../index.md)
```

---

Dengan topik **Iterators** dan **Generators** di JavaScript, kamu bisa menangani koleksi data dan proses yang membutuhkan alur bertahap dengan cara yang lebih efisien.  
Jangan lupa untuk eksplor lebih lanjut tentang **async generators** atau **streaming data** untuk kebutuhan aplikasi yang lebih kompleks! 🚀

---

<div align='center'>
⬅️ [Kembali](22-Modules-in-Javascript.md) | 🏠 [Beranda](../../index.md) | [Lanjut ➡️](24-Classes.md)
</div>
