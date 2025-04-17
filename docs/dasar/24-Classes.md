Berikut isi lengkap untuk file:  
`D:\dokumentasi\javascript\belajar-javascript-pemula\docs\dasar\24-Classes.md`

---

```markdown
# 🏷️ Classes in JavaScript

> "Classes di JavaScript adalah cara untuk membuat template objek yang lebih terstruktur, mirip seperti blueprint yang bisa digunakan untuk membuat banyak objek."

---

## 🎯 Tujuan Pembelajaran

Setelah mempelajari ini, kamu akan:
- Memahami konsep **classes** di JavaScript
- Bisa membuat **class** untuk mendefinisikan objek dengan properti dan metode
- Mengetahui cara kerja **constructor**, **inheritance**, dan **static methods** di dalam class

---

## 🧩 Apa Itu Class?

**Class** adalah template atau cetak biru untuk membuat objek. Di dalam class, kamu bisa mendefinisikan **properties** (atribut) dan **methods** (fungsi) yang dimiliki oleh objek yang dibuat dari class tersebut.

Dengan menggunakan **class**, kamu bisa membuat banyak objek yang memiliki pola yang sama, tetapi dengan nilai yang berbeda.

### Sintaks Dasar Class

```javascript
class ClassName {
  constructor(param1, param2) {
    // Properti yang dimiliki oleh setiap objek
    this.property1 = param1;
    this.property2 = param2;
  }

  // Method yang dimiliki oleh setiap objek
  method1() {
    console.log('Hello, world!');
  }
}
```

- **constructor**: Fungsi khusus yang dijalankan ketika objek dibuat.
- **this**: Merujuk pada objek yang sedang dibuat.

---

## 🛠️ 1. Membuat dan Menggunakan Class

Untuk membuat objek dari class, kamu cukup menggunakan keyword `new` diikuti dengan nama class.

#### Contoh:

```javascript
class Person {
  constructor(name, age) {
    this.name = name;
    this.age = age;
  }

  greet() {
    console.log(`Hello, my name is ${this.name} and I am ${this.age} years old.`);
  }
}

const person1 = new Person('Alice', 25);
const person2 = new Person('Bob', 30);

person1.greet();  // Hello, my name is Alice and I am 25 years old.
person2.greet();  // Hello, my name is Bob and I am 30 years old.
```

Di sini, kita membuat class **Person** yang memiliki properti `name` dan `age`, serta metode `greet()` yang mencetak salam.

---

## 🔄 2. Inheritance (Pewarisan)

JavaScript juga mendukung **inheritance** (pewarisan), yang memungkinkan kita untuk membuat class baru berdasarkan class yang sudah ada. Dengan inheritance, class baru bisa mewarisi properti dan metode dari class lama.

### Sintaks Inheritance

```javascript
class SubClass extends SuperClass {
  constructor() {
    super(); // Memanggil constructor dari SuperClass
  }
}
```

#### Contoh:

```javascript
class Animal {
  constructor(name) {
    this.name = name;
  }

  speak() {
    console.log(`${this.name} makes a sound.`);
  }
}

class Dog extends Animal {
  constructor(name, breed) {
    super(name);  // Memanggil constructor dari class Animal
    this.breed = breed;
  }

  speak() {
    console.log(`${this.name} barks.`);
  }
}

const dog1 = new Dog('Rex', 'Labrador');
dog1.speak();  // Rex barks.
```

Di sini, **Dog** mewarisi properti `name` dan metode `speak()` dari class **Animal**, namun kita dapat mengganti metode `speak()` di class **Dog** untuk berperilaku berbeda.

---

## 🔑 3. Constructor Method

Constructor adalah metode khusus yang dijalankan saat objek dibuat. Fungsi constructor ini digunakan untuk menginisialisasi properti objek.

#### Contoh:

```javascript
class Car {
  constructor(make, model) {
    this.make = make;
    this.model = model;
  }

  getCarInfo() {
    return `${this.make} ${this.model}`;
  }
}

const car1 = new Car('Toyota', 'Corolla');
console.log(car1.getCarInfo());  // Toyota Corolla
```

Di sini, kita menggunakan constructor untuk menginisialisasi properti `make` dan `model` untuk setiap objek **Car** yang dibuat.

---

## ⚡ 4. Static Methods

**Static methods** adalah metode yang didefinisikan di dalam class tetapi tidak dapat diakses oleh objek yang dibuat dari class tersebut. Static methods hanya dapat dipanggil langsung pada class itu sendiri.

### Sintaks Static Methods

```javascript
class MyClass {
  static staticMethod() {
    console.log('This is a static method.');
  }
}
```

#### Contoh:

```javascript
class Calculator {
  static add(a, b) {
    return a + b;
  }

  static subtract(a, b) {
    return a - b;
  }
}

console.log(Calculator.add(5, 3));       // 8
console.log(Calculator.subtract(5, 3));  // 2
```

Di sini, kita mendefinisikan dua static methods **add** dan **subtract** yang bisa dipanggil langsung melalui class **Calculator**, tanpa perlu membuat objek terlebih dahulu.

---

## 🔧 5. Getter dan Setter

**Getter** dan **Setter** digunakan untuk mengakses atau memperbarui nilai properti objek secara terkontrol.

### Sintaks Getter dan Setter

```javascript
class MyClass {
  constructor(value) {
    this._value = value;
  }

  get value() {
    return this._value;
  }

  set value(val) {
    this._value = val;
  }
}
```

#### Contoh:

```javascript
class Person {
  constructor(name) {
    this._name = name;
  }

  get name() {
    return this._name;
  }

  set name(newName) {
    this._name = newName;
  }
}

const person = new Person('Alice');
console.log(person.name);  // Alice

person.name = 'Bob';
console.log(person.name);  // Bob
```

Dengan **getter** dan **setter**, kita bisa mengontrol akses terhadap properti objek dan menyertakan logika tambahan saat membaca atau menulis nilai.

---

## 💡 Tips

- Gunakan **class** untuk mendefinisikan objek dengan pola yang sama, tetapi dengan nilai yang berbeda. Ini akan membuat kode lebih terstruktur dan lebih mudah untuk dikelola.
- Manfaatkan **inheritance** untuk memperluas class yang sudah ada dan menghindari duplikasi kode.
- **Static methods** sangat berguna untuk fungsi yang tidak bergantung pada objek tertentu dan lebih terkait dengan class itu sendiri.
- Gunakan **getter dan setter** untuk mengontrol bagaimana properti objek diakses atau dimodifikasi.

---

## 💪 Tantangan Coding

1. Buat class **Rectangle** dengan properti **width** dan **height**, dan tambahkan metode untuk menghitung **area** dan **perimeter**.
2. Implementasikan pewarisan dengan membuat class **Car** yang mewarisi dari class **Vehicle** dan menambahkan properti serta metode tambahan untuk fitur mobil.
3. Coba buat **static method** untuk menghitung nilai rata-rata dari daftar angka dalam class **Statistics**.
4. Gunakan **getter dan setter** untuk mengatur dan mengakses nilai properti **age** di dalam class **Person**.

---

## 🔁 Kembali ke [Daftar Materi](../../index.md)
```

---

Sekarang kamu sudah paham konsep dasar **classes** di JavaScript, dan bagaimana cara menggunakannya untuk mendefinisikan objek serta memanfaatkan fitur seperti **inheritance**, **static methods**, dan **getter/setter**.  
Lanjutkan eksplorasi ke topik lainnya dan gunakan konsep ini dalam pembuatan aplikasi yang lebih kompleks! 🚀