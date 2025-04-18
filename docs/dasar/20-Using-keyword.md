Yess, kali ini kita bakal ngulik tentang keyword di JavaScript yang sering banget dipake, yaitu:  
**`this`, `new`, `super`, `class`, dan lainnya** — benda-benda penting yang bikin kode kamu lebih powerful 🔑🚀

Berikut isi lengkap file:  
`D:\dokumentasi\javascript\belajar-javascript-pemula\docs\dasar\20-Using-keyword.md`

---

```markdown
# 🔑 Menggunakan Keyword di JavaScript

> "Keyword di JavaScript tuh bukan cuma kata-kata kunci, tapi kayak senjata rahasia yang punya kekuatan besar buat program kamu!"

---

## 🎯 Tujuan Pembelajaran

Setelah mempelajari ini, kamu akan:
- Mengerti cara kerja keyword penting di JavaScript
- Bisa menggunakan keyword seperti `this`, `new`, `super`, dan lainnya dalam konteks yang tepat

---

## 🧱 1. `this` Keyword

`this` adalah referensi ke objek yang sedang berinteraksi dengan fungsi. Tapi, konteksnya bisa beda-beda, tergantung di mana dan bagaimana `this` dipanggil.

### Contoh:

```javascript
function halo() {
  console.log(this);
}

let obj = {
  nama: "Marno",
  halo: halo
};

obj.halo();  // `this` mengacu pada objek `obj`
```

**Kapan `this` Mengacu ke Apa?**
- Dalam function biasa, `this` mengacu ke **global object** (di browser: `window`)
- Dalam method objek, `this` mengacu ke **objek itu sendiri**
- Dalam constructor atau class, `this` mengacu ke **instansi objek**

---

## 🔧 2. `new` Keyword

Digunakan untuk membuat **object instance** baru dari **constructor function** atau **class**.

### Contoh:

```javascript
function Orang(nama, umur) {
  this.nama = nama;
  this.umur = umur;
}

let orang1 = new Orang("Marno", 22);
console.log(orang1.nama);  // "Marno"
```

Atau dengan class:

```javascript
class Mobil {
  constructor(merek) {
    this.merek = merek;
  }
}

let mobil1 = new Mobil("Toyota");
console.log(mobil1.merek);  // "Toyota"
```

---

## 🚀 3. `super` Keyword

`super` digunakan untuk memanggil **constructor** atau method dari **parent class** di dalam **class child**.

### Contoh:

```javascript
class Hewan {
  constructor(nama) {
    this.nama = nama;
  }

  suara() {
    console.log("Suara hewan!");
  }
}

class Anjing extends Hewan {
  constructor(nama) {
    super(nama);  // Memanggil constructor parent class
  }

  suara() {
    super.suara();  // Memanggil method parent class
    console.log("Guk guk!");
  }
}

let anjing = new Anjing("Buddy");
anjing.suara();
// Output:
// "Suara hewan!"
// "Guk guk!"
```

---

## 🛠️ 4. `class` Keyword

`class` adalah cara modern untuk mendefinisikan constructor dan method di JavaScript.

### Contoh:

```javascript
class Manusia {
  constructor(nama, umur) {
    this.nama = nama;
    this.umur = umur;
  }

  kenalan() {
    console.log(`Halo, nama saya ${this.nama} dan saya berumur ${this.umur} tahun.`);
  }
}

let manusia1 = new Manusia("Marno", 22);
manusia1.kenalan();  // "Halo, nama saya Marno dan saya berumur 22 tahun."
```

---

## 🧳 5. `let`, `const`, dan `var` Keyword

- `let` dan `const` lebih disarankan untuk deklarasi variabel karena lebih aman dalam konteks **block-scoping**.
- `var` digunakan di JavaScript lama, dan lebih rentan terhadap kesalahan (terutama karena **hoisting**).

```javascript
let a = 10;
const b = 20;
var c = 30;

{
  let a = 5;  // Scoped hanya dalam blok ini
  console.log(a);  // 5
}
console.log(a);  // 10 (a yang luar block)

{
  var c = 50;  // `var` nggak scoping ke blok, jadi c diubah di luar
}
console.log(c);  // 50
```

---

## ⚠️ 6. `delete` Keyword

Dipakai untuk menghapus properti dari objek.

### Contoh:

```javascript
let orang = {
  nama: "Marno",
  umur: 22
};

delete orang.umur;  // Menghapus properti umur
console.log(orang);  // { nama: "Marno" }
```

---

## 🧠 Tips Penting

- Gunakan `this` dengan hati-hati, terutama di function yang tidak berhubungan dengan objek (misalnya dalam event handler).
- Selalu pakai `new` saat membuat instance dari class atau constructor.
- `super` sangat berguna saat bekerja dengan inheritance, jadi manfaatkan kalau kamu bikin class turunan.
- Hindari `var`, lebih baik pakai `let` atau `const` untuk scoping yang lebih jelas.

---

## 💪 Tantangan Coding

1. Buat class `Sepeda` yang memiliki properti `merek` dan method `berjalan()`.  
   Kemudian buat class turunan `SepedaGunung` yang memanggil method `berjalan()` dari class parent dan menambah fitur `rem()`.
2. Buat program yang menggunakan `this` untuk menghitung jumlah total nilai dalam objek `siswa`.

---

## 🔁 Kembali ke [Daftar Materi](../../index.md)
```

---

Itulah pembahasan mengenai **keyword** yang sering dipake di JavaScript!  
Kalo udah ngerti ini, lo siap buat ngoding dengan konsep yang lebih kuat dan fleksibel. Mau lanjut ke **modul ES6**, **async/await**, atau eksplorasi **JavaScript design patterns**? Lanjut terus aja, bro! 🚀

---

<div align='center'>
⬅️ [Kembali](19-Strict-Mode.md) | 🏠 [Beranda](../../index.md) | [Lanjut ➡️](21-Asynchronous-Javascript.md)
</div>
