import os

base_dir = "./docs"
file_paths = []

# Scan semua file .md secara rekursif
for root, dirs, files in os.walk(base_dir):
    for file in sorted(files):
        if file.endswith(".md"):
            # Simpan path relatif terhadap base_dir
            full_path = os.path.join(root, file)
            rel_path = os.path.relpath(full_path, base_dir).replace("\\", "/")
            file_paths.append(rel_path)

# Tampilkan hasilnya
print("file_paths = [")
for path in file_paths:
    print(f'    "{path}",')
print("]")
