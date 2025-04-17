Oke, bro! Kita udah masuk ke dunia nyata JavaScript, tempat di mana kode kamu mulai **interaktif** dan **ngomong langsung sama browser**:  
**DOM API** – alias jurus ninja buat ngubah isi halaman secara dinamis 😎🔥

Berikut isi lengkap file:  
`D:\dokumentasi\javascript\belajar-javascript-pemula\docs\dasar\18-DOM-APIs.md`

---

```markdown
# 🌐 DOM API (Document Object Model)

> "DOM itu kayak jembatan antara JavaScript dan dunia nyata (halaman web). Tanpa DOM, JavaScript cuma ngomong sendiri."

---

## 🎯 Tujuan Pembelajaran

Setelah belajar ini, kamu akan:
- Tahu apa itu DOM
- Bisa ambil elemen HTML lewat JavaScript
- Bisa manipulasi teks, atribut, dan style elemen
- Bisa bikin interaksi user (event)

---

## 🧱 Apa Itu DOM?

DOM (Document Object Model) adalah representasi struktur dokumen HTML dalam bentuk objek.  
Setiap tag HTML jadi **node** yang bisa diakses dan dimodifikasi lewat JavaScript.

---

## 🔍 Mengakses Elemen HTML

```html
<p id="pesan">Halo Dunia!</p>
```

```javascript
const el = document.getElementById("pesan");
console.log(el.textContent); // "Halo Dunia!"
```

Metode lainnya:

| Metode                        | Keterangan                        |
|------------------------------|-----------------------------------|
| `getElementById()`           | Berdasarkan id                    |
| `getElementsByClassName()`   | Berdasarkan class (HTMLCollection) |
| `getElementsByTagName()`     | Berdasarkan tag                   |
| `querySelector()`            | Selector tunggal (CSS style)      |
| `querySelectorAll()`         | Semua yang cocok selector (NodeList) |

---

## ✏️ Mengubah Konten

```javascript
el.textContent = "Hai dari JavaScript!";
el.innerHTML = "<strong>Bold</strong>";
```

---

## 🎨 Mengubah Style

```javascript
el.style.color = "red";
el.style.fontSize = "20px";
```

---

## 🧪 Mengubah Atribut

```html
<img id="gambar" src="awal.jpg" />
```

```javascript
const img = document.getElementById("gambar");
img.setAttribute("src", "baru.jpg");
img.getAttribute("src"); // "baru.jpg"
```

---

## ➕ Menambah & Menghapus Elemen

```javascript
const container = document.getElementById("kontainer");

let p = document.createElement("p");
p.textContent = "Paragraf baru";

container.appendChild(p);
```

Untuk hapus:

```javascript
container.removeChild(p);
```

---

## 🔁 Event Listener

```html
<button id="klik">Klik Aku</button>
```

```javascript
document.getElementById("klik").addEventListener("click", function() {
  alert("Tombol diklik!");
});
```

---

## 🔥 Contoh Real

```html
<input id="nama" placeholder="Masukkan nama" />
<button id="halo">Say Hello</button>
<p id="output"></p>
```

```javascript
document.getElementById("halo").addEventListener("click", function() {
  let nama = document.getElementById("nama").value;
  document.getElementById("output").textContent = `Halo, ${nama}!`;
});
```

---

## 🧠 Quiz Mini

**Pertanyaan:**  
Gimana cara ganti warna teks elemen dengan ID `judul` jadi biru?

**Jawaban:**
```javascript
document.getElementById("judul").style.color = "blue";
```

---

## 💪 Tantangan Coding

1. Buat tombol yang saat diklik, menambahkan elemen `<li>` ke dalam `<ul>`.
2. Buat input dan tombol untuk mengganti gambar `<img>` berdasarkan URL yang dimasukkan user.
3. Tampilkan jumlah huruf yang diketik user secara realtime saat isi input berubah (`input` event).

---

## 🚀 Tips DOM Ninja

- Gunakan `querySelector()` untuk fleksibilitas selector seperti CSS.
- Event listener bisa dipisah ke function sendiri untuk rapiin kode.
- DOM hanya bekerja setelah seluruh elemen halaman dimuat!

---

## 🔁 Kembali ke [Daftar Materi](../../index.md)
```

---

Sekarang JavaScript kamu udah bisa **hidup di browser**, bro!  
Next bisa lanjut ke topik **event bubbling**, **form validation**, atau mulai masuk ke **DOM traversal dan manipulasi kelas**!  
Kalo udah panas, tinggal gas ke **project mini** biar makin skill up 💪🔥