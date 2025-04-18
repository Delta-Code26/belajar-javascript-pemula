import os

base_dir = "../docs"

file_paths = [
    "index.md",
    "dasar/01-hello-world.md",
    "dasar/02-Variabel.md",
    "dasar/03-Tipe-Data.md",
    "dasar/04-Logika.md",
    "dasar/05-Loop.md",
    "dasar/06-Function.md",
    "dasar/07-Array.md",
    "dasar/08-Object.md",
    "dasar/09-JSON.md",
    "dasar/10-Type-Casting.md",
    "dasar/11-Data-Structures.md",
    "dasar/12-Equality-Comparisons.md",
    "dasar/13-Loops-and-Iterations.md",
    "dasar/14-Expressions-and-Operators.md",
    "dasar/15-Control-flow.md",
    "dasar/17-Functions.md",
    "dasar/18-DOM-APIs.md",
    "dasar/19-Strict-Mode.md",
    "dasar/20-Using-keyword.md",
    "dasar/21-Asynchronous-Javascript.md",
    "dasar/22-Modules-in-Javascript.md",
    "dasar/23-Iterators-and-generators.md",
    "dasar/24-Classes.md",
    "dasar/25-Working-with-APIs.md",
    "dasar/26-Memory-Management.md",
    "dasar/27-Using-Browser-DevTools.md",
]

def get_filename(path):
    return os.path.basename(path)

def build_nav(index):
    nav = []
    if index > 0:
        nav.append(f"⬅️ [Kembali]({get_filename(file_paths[index - 1])})")
    nav.append("🏠 [Beranda](../../index.md)" if "index.md" not in file_paths[index] else "")
    if index < len(file_paths) - 1:
        nav.append(f"[Lanjut ➡️]({get_filename(file_paths[index + 1])})")
    
    # Join dengan separator tengah dan bungkus HTML div agar rapi di tengah
    return "\n\n---\n\n<div align='center'>\n" + " | ".join(filter(None, nav)) + "\n</div>\n"

for i, rel_path in enumerate(file_paths):
    full_path = os.path.join(base_dir, rel_path)

    if not os.path.exists(full_path):
        print(f"⚠️ File tidak ditemukan: {rel_path}")
        continue

    with open(full_path, "r", encoding="utf-8") as file:
        content = file.read().strip()

    # Hapus navigasi lama jika ada (deteksi berdasarkan tag navigasi khas)
    split_point = content.find("<div align='center'>")
    if split_point != -1:
        content = content[:split_point].strip()

    # Tambahkan navigasi baru
    new_content = content + build_nav(i)

    with open(full_path, "w", encoding="utf-8") as file:
        file.write(new_content)

    print(f"✅ Navigasi ditambahkan ke: {rel_path}")

print("\n🔥 Semua file sudah diupdate dengan navigasi!")
