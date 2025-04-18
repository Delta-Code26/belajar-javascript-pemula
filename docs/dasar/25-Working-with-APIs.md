## WORKING WITH APIs

---

```markdown
# 🧩 Working with APIs in JavaScript

> "API (Application Programming Interface) adalah cara aplikasi berbicara dengan aplikasi lain. Dalam JavaScript, kita dapat menggunakan API untuk berinteraksi dengan server atau aplikasi lain untuk mengambil atau mengirimkan data."

---

## 🎯 Tujuan Pembelajaran

Setelah mempelajari materi ini, kamu akan:
- Memahami apa itu API dan bagaimana cara kerjanya.
- Bisa mengakses dan menggunakan API eksternal di JavaScript.
- Memahami cara menggunakan **fetch API** untuk mendapatkan data dari server.
- Mempelajari cara menangani respons API dalam format **JSON**.
- Memahami penggunaan **async/await** untuk membuat kode lebih bersih dan mudah dibaca saat bekerja dengan API.

---

## 📚 Apa Itu API?

**API** adalah sekumpulan definisi dan protokol yang digunakan untuk membangun dan mengintegrasikan aplikasi perangkat lunak. API memungkinkan aplikasi untuk berkomunikasi satu sama lain.

Contoh penggunaan API yang paling umum adalah mengakses data dari server, seperti mendapatkan informasi cuaca, data produk, atau hasil pencarian.

---

## 🛠️ Mengakses API dengan `fetch()`

JavaScript menyediakan metode **`fetch()`** untuk mengambil data dari API. Fungsi `fetch()` mengirimkan request ke server dan mengembalikan **promise** yang berisi respons dari server.

### Sintaks `fetch()`

```javascript
fetch(url)
  .then(response => response.json()) // Mengonversi respons ke format JSON
  .then(data => console.log(data))    // Menampilkan data API
  .catch(error => console.error('Error:', error)); // Menangani error
```

#### Contoh Penggunaan `fetch()`:

```javascript
fetch('https://api.example.com/data')
  .then(response => response.json())  // Mengonversi respons ke JSON
  .then(data => {
    console.log(data); // Menampilkan data
  })
  .catch(error => console.log('Error:', error));
```

Di sini, kita menggunakan `fetch()` untuk mengakses data dari URL yang diberikan. Jika data berhasil didapatkan, kita mengonversinya menjadi format JSON dan menampilkannya.

---

## 🧠 1. Mengambil Data dari API

Untuk mengambil data dari API, kamu biasanya mengirimkan request HTTP **GET**. Berikut adalah contoh menggunakan **`fetch()`** untuk mengambil data dari API.

#### Contoh: Mengambil Data Pengguna dari API

```javascript
fetch('https://jsonplaceholder.typicode.com/users')
  .then(response => response.json())
  .then(users => {
    users.forEach(user => {
      console.log(`Nama: ${user.name}, Email: ${user.email}`);
    });
  })
  .catch(error => console.log('Error:', error));
```

Di sini, kita mengambil data pengguna dari API `jsonplaceholder.typicode.com` dan menampilkan nama dan email setiap pengguna.

---

## 🔄 2. Mengirim Data ke API (POST Request)

Selain mengambil data, kamu juga bisa mengirimkan data ke API menggunakan **POST** request. Untuk ini, kamu perlu menambahkan beberapa opsi ke `fetch()`, seperti method, headers, dan body.

### Sintaks POST Request:

```javascript
fetch(url, {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json'
  },
  body: JSON.stringify(data)
})
  .then(response => response.json())  // Mengonversi respons ke JSON
  .then(data => console.log(data))    // Menampilkan data
  .catch(error => console.error('Error:', error));  // Menangani error
```

#### Contoh: Mengirim Data Pengguna Baru ke API

```javascript
const newUser = {
  name: 'John Doe',
  email: 'john.doe@example.com'
};

fetch('https://jsonplaceholder.typicode.com/users', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json'
  },
  body: JSON.stringify(newUser)
})
  .then(response => response.json())
  .then(data => {
    console.log('User created:', data);
  })
  .catch(error => console.error('Error:', error));
```

Di sini, kita mengirimkan data pengguna baru ke API menggunakan **POST** request. Data dikirim dalam format JSON, dan kita menunggu respons dari server untuk mengonfirmasi bahwa data telah berhasil ditambahkan.

---

## ⏳ 3. Menggunakan `async/await`

**`async/await`** adalah cara yang lebih modern dan lebih bersih untuk menangani operasi asynchronous, seperti mengambil data dari API. `async` memungkinkan kamu untuk menggunakan `await` di dalamnya, yang membuat kode kamu terlihat lebih mirip dengan kode sinkron.

### Sintaks `async/await`:

```javascript
async function fetchData() {
  try {
    const response = await fetch(url);  // Tunggu hingga data diterima
    const data = await response.json();  // Mengonversi respons ke JSON
    console.log(data);
  } catch (error) {
    console.error('Error:', error);
  }
}
```

#### Contoh: Menggunakan `async/await` untuk Mengambil Data

```javascript
async function getUserData() {
  try {
    const response = await fetch('https://jsonplaceholder.typicode.com/users');
    const users = await response.json();
    users.forEach(user => {
      console.log(`Nama: ${user.name}, Email: ${user.email}`);
    });
  } catch (error) {
    console.log('Error:', error);
  }
}

getUserData();
```

Dengan menggunakan `async/await`, kita bisa menangani API secara lebih rapi dan mudah dibaca, menghindari **callback hell** yang terjadi saat menggunakan `.then()`.

---

## 🛑 4. Menangani Error dengan `try/catch`

Saat bekerja dengan API, penting untuk menangani error yang mungkin terjadi, misalnya jika server tidak dapat dijangkau atau ada kesalahan dalam data yang dikirimkan.

### Menangani Error dengan `catch()`:

```javascript
fetch('https://api.example.com/data')
  .then(response => {
    if (!response.ok) {
      throw new Error('Network response was not ok');
    }
    return response.json();
  })
  .then(data => console.log(data))
  .catch(error => console.log('Error:', error));
```

### Menangani Error dengan `try/catch` (menggunakan async/await):

```javascript
async function fetchData() {
  try {
    const response = await fetch('https://api.example.com/data');
    if (!response.ok) {
      throw new Error('Network response was not ok');
    }
    const data = await response.json();
    console.log(data);
  } catch (error) {
    console.log('Error:', error);
  }
}

fetchData();
```

Dengan **`try/catch`** atau **`.catch()`**, kita bisa menangani error dengan lebih baik dan memberikan informasi yang berguna jika terjadi masalah.

---

## 💡 Tips

- Gunakan **`async/await`** untuk menulis kode asynchronous dengan lebih bersih dan mudah dibaca.
- Selalu menangani error ketika bekerja dengan API, terutama jika ada kemungkinan server tidak merespons atau data yang diterima tidak sesuai.
- Periksa status respons dengan `.ok` untuk memastikan bahwa request ke API berhasil sebelum memproses data.
- Jangan lupa untuk selalu menangani **CORS (Cross-Origin Resource Sharing)** ketika bekerja dengan API yang berasal dari domain berbeda.

---

## 💪 Tantangan Coding

1. Buat aplikasi yang menampilkan daftar pengguna dari API **`https://jsonplaceholder.typicode.com/users`** menggunakan **`fetch()`** dan tampilkan nama dan emailnya di halaman HTML.
2. Kirim data pengguna baru (seperti nama dan email) ke API dan tampilkan respons yang diterima.
3. Coba gunakan **`async/await`** untuk mengambil data dari API dan tampilkan hasilnya di halaman web.
4. Implementasikan penanganan error untuk API yang gagal dimuat, seperti menampilkan pesan kesalahan kepada pengguna.

---

## 🔁 Kembali ke [Daftar Materi](../index.md)
```

---

Sekarang kamu telah mempelajari cara bekerja dengan **API** menggunakan JavaScript, baik untuk mengambil maupun mengirimkan data ke server. Ini adalah keterampilan yang sangat penting dalam pengembangan aplikasi web modern. Jangan ragu untuk menguji pengetahuanmu dengan tantangan coding yang telah disediakan! 🚀
```
---
## [BACK](./24-Classes.md)    ---    [HOME](../index.md) --- [NEXT](./26-Memory-Management.md)

---

<div align='center'>
⬅️ [Kembali](24-Classes.md) | 🏠 [Beranda](../../index.md) | [Lanjut ➡️](26-Memory-Management.md)
</div>
