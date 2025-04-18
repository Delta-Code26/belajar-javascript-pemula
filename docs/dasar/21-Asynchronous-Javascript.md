Oke, kita siap buat bahas topik yang cukup powerful dan penting di JavaScript:  
**Asynchronous JavaScript** — yaitu bagaimana cara kita menangani proses yang nggak langsung selesai dan membutuhkan waktu, kayak permintaan ke server, pengolahan file, atau event user.

Berikut isi lengkap untuk file:  
`D:\dokumentasi\javascript\belajar-javascript-pemula\docs\dasar\21-Asynchronous-Javascript.md`

---

```markdown
# ⏳ Asynchronous JavaScript

> "Asynchronous JavaScript itu kayak ninja di dunia programming: diam-diam menjalankan tugas sambil nunggu proses lain selesai tanpa mengganggu yang lainnya."

---

## 🎯 Tujuan Pembelajaran

Setelah mempelajari ini, kamu akan:
- Paham apa itu **Asynchronous JavaScript** dan kenapa penting
- Bisa menggunakan **callbacks**, **Promises**, dan **async/await** dalam kode JavaScript kamu
- Mengetahui cara menangani operasi yang memerlukan waktu, seperti API request atau pengolahan data besar

---

## 🚶‍♂️ Apa Itu Asynchronous JavaScript?

Asynchronous JavaScript memungkinkan kita untuk melakukan beberapa tugas sekaligus tanpa harus menunggu satu tugas selesai dulu. Dalam operasi **synchronous**, semua tugas dijalankan berurutan, artinya kode berikutnya baru dieksekusi setelah tugas pertama selesai. Sebaliknya, **asynchronous** membebaskan proses untuk berjalan sembari menunggu tugas lainnya selesai.

### Contoh:

Misalnya, kamu sedang memesan pizza. Di dunia synchronous, kamu akan menunggu pizza datang dulu, baru bisa makan. Di asynchronous, kamu bisa mulai makan sebelum pizza datang, dan begitu pizza datang, kamu langsung lanjutkan makan pizza!

---

## 📝 1. Callbacks

Callback adalah fungsi yang dijalankan setelah tugas lain selesai. Pada JavaScript, kita sering menggunakan callback untuk menangani operasi asynchronous.

### Contoh:

```javascript
console.log("Mulai");

setTimeout(function() {
  console.log("Tugas selesai setelah 2 detik!");
}, 2000);

console.log("Selesai");
```

Output:
```
Mulai
Selesai
Tugas selesai setelah 2 detik!
```

**Catatan:** `setTimeout` adalah fungsi asynchronous, jadi setelah memanggilnya, eksekusi kode terus berlanjut dan baru kembali ke callback setelah waktu yang ditentukan.

---

## 📦 2. Promises

Promises adalah cara yang lebih modern dan terstruktur untuk menangani asynchronous code, menggantikan callback. Promise bisa dalam 3 status:
- **Pending**: Ketika operasi belum selesai
- **Resolved**: Ketika operasi berhasil
- **Rejected**: Ketika operasi gagal

### Contoh:

```javascript
let janji = new Promise(function(resolve, reject) {
  let sukses = true; // ubah jadi false untuk melihat hasil reject

  if (sukses) {
    resolve("Operasi berhasil!");
  } else {
    reject("Terjadi kesalahan.");
  }
});

janji.then(function(result) {
  console.log(result);  // "Operasi berhasil!"
}).catch(function(error) {
  console.log(error);  // "Terjadi kesalahan."
});
```

---

## ⚡ 3. Async/Await

`async/await` adalah sintaks baru yang lebih mudah dipahami untuk menangani operasi asynchronous. `async` digunakan untuk mendeklarasikan fungsi asynchronous, dan `await` digunakan untuk menunggu hasil dari Promise.

### Contoh:

```javascript
async function ambilData() {
  let response = await fetch('https://jsonplaceholder.typicode.com/posts');
  let data = await response.json();
  console.log(data);
}

ambilData();
```

Dengan `async/await`, kode menjadi lebih seperti kode synchronous, tetapi tetap bersifat asynchronous.

---

## 🛠️ 4. Error Handling dalam Asynchronous JavaScript

Menangani error dalam kode asynchronous itu penting banget. Kalau pakai callback, error biasanya dikelola dengan parameter kedua dalam callback. Untuk Promise, kita bisa pakai `.catch()`, dan dengan `async/await`, kita bisa gunakan `try/catch`.

### Contoh Callback Error:

```javascript
function ambilData(callback) {
  let error = false;  // coba ganti ke true untuk lihat error handling

  if (error) {
    callback("Terjadi kesalahan!", null);
  } else {
    callback(null, "Data berhasil diambil");
  }
}

ambilData(function(err, data) {
  if (err) {
    console.log(err);  // "Terjadi kesalahan!"
  } else {
    console.log(data);  // "Data berhasil diambil"
  }
});
```

### Contoh Promise Error:

```javascript
let janji = new Promise(function(resolve, reject) {
  let error = false;  // coba ganti ke true untuk lihat error handling

  if (error) {
    reject("Terjadi kesalahan");
  } else {
    resolve("Data berhasil diambil");
  }
});

janji.then(function(result) {
  console.log(result);  // "Data berhasil diambil"
}).catch(function(error) {
  console.log(error);  // "Terjadi kesalahan"
});
```

### Contoh Async/Await Error:

```javascript
async function ambilData() {
  try {
    let response = await fetch('https://jsonplaceholder.typicode.com/posts');
    let data = await response.json();
    console.log(data);
  } catch (error) {
    console.log("Terjadi kesalahan:", error);
  }
}

ambilData();
```

---

## 💡 Tips

- **Gunakan `async/await` jika memungkinkan**: Kode menjadi lebih mudah dibaca dan dikelola.
- **Hati-hati dengan callback hell**: Jika terlalu banyak callback bertingkat, pertimbangkan untuk menggunakan Promise atau async/await.
- **Error handling itu penting**: Jangan lupa untuk menangani error di setiap langkah asynchronous untuk mencegah aplikasi crash.

---

## 💪 Tantangan Coding

1. Buat aplikasi yang mengambil data dari API dan menampilkan hasilnya setelah 2 detik menggunakan `setTimeout` dan callback.
2. Gunakan `fetch` API untuk mengambil data dari API JSONPlaceholder dan tampilkan data dalam bentuk list menggunakan `async/await`.
3. Coba buat error handling yang lebih canggih: tangani kesalahan baik dalam callback, Promise, dan async/await dengan `try/catch`.

---

## 🔁 Kembali ke [Daftar Materi](../../index.md)
```

---

Sekarang, lo udah paham cara kerja **asynchronous JavaScript** yang keren ini.  
Dengan `callbacks`, **Promises**, dan **async/await**, lo bisa menghandle proses-proses berat tanpa ngacauin alur eksekusi program lo!  
Mau lanjut ke topik **Event Loop** atau **Web APIs**? Kita gas terus aja! 💪🚀

---

<div align='center'>
⬅️ [Kembali](20-Using-keyword.md) | 🏠 [Beranda](../../index.md) | [Lanjut ➡️](22-Modules-in-Javascript.md)
</div>
