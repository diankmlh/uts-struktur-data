import pandas as pd

df = pd.read_excel("Struktur_Data_Dataset_Kelas_A_B_C.xlsx") 

def linear_search(df, kolom, target):
    hasil = df[df[kolom].astype(str).str.lower().str.contains(str(target).lower())]
    return hasil

def binary_search(df, kolom, target):
    if kolom == 'Tahun Terbit':
        df[kolom] = pd.to_numeric(df[kolom], errors='coerce')  
        target = pd.to_numeric(target, errors='coerce')  
    else:
        df[kolom] = df[kolom].astype(str).str.strip().str.lower().fillna("") 
        target = target.strip().lower() 
   
    df_sorted = df.sort_values(by=kolom).reset_index(drop=True)
    data = df_sorted[kolom].tolist() 

    kiri, kanan = 0, len(data) - 1
    hasil_index = []

    while kiri <= kanan:
        tengah = (kiri + kanan) // 2
        if data[tengah] == target:  
            i = tengah
            while i >= 0 and data[i] == target:
                hasil_index.append(i)
                i -= 1
            i = tengah + 1
            while i < len(data) and data[i] == target:
                hasil_index.append(i)
                i += 1
            break
        elif data[tengah] < target:
            kiri = tengah + 1
        else:
            kanan = tengah - 1

    if hasil_index:
        return df_sorted.iloc[sorted(hasil_index)]  
    else:
        return None

def tampilkan_hasil(hasil):
    for index, row in hasil.iterrows():
        print("\n📄 Judul Paper:", row.get("Judul Paper", "N/A"))
        print("📆 Tahun Terbit:", row.get("Tahun Terbit", "N/A"))
        print("👨‍🔬 Nama Penulis:", row.get("Nama Penulis", "N/A"))
        print("🔗 Link Paper:", row.get("Link Paper", "N/A"))
        print("📄 Abstrak:", str(row.get("Abstrak (langusung copas dari paper)", ""))[:200], "...")
        print("🧾 Kesimpulan:", str(row.get("Kesimpulan (Langusung copas dari paper)", ""))[:200], "...")
        print("-" * 70)

while True:
    print("\nPilih metode pencarian:")
    print("1. Linear Search")
    print("2. Binary Search")
    print("3. Keluar")

    pilihan = input("Masukkan pilihan : ")

    if pilihan == '3':
        print("👋 Terima kasih! Program selesai.")
        break

    if pilihan not in ['1', '2']:
        print("❌ Pilihan nggak valid!")
        continue

    print("\nCari berdasarkan:")
    print("1. Judul Paper")
    print("2. Tahun Terbit")
    print("3. Nama Penulis")

    kolom_pilihan = input("Pilih kolom : ")
    kolom_map = {
        '1': 'Judul Paper',
        '2': 'Tahun Terbit',
        '3': 'Nama Penulis'
    }

    if kolom_pilihan not in kolom_map:
        print("❌ Kolom nggak valid!")
        continue

    kolom = kolom_map[kolom_pilihan]
    keyword = input(f"🔎 Masukkan keyword untuk {kolom}: ")

    if pilihan == '1':
        print(f"\n=== Hasil Linear Search untuk '{keyword}' ===")
        hasil = linear_search(df, kolom, keyword)
        if not hasil.empty:
            tampilkan_hasil(hasil)
        else:
            print("🚫 Tidak ditemukan.")
    elif pilihan == '2':
        print(f"\n=== Hasil Binary Search untuk '{keyword}' ===")
        hasil = binary_search(df, kolom, keyword)
        if hasil is not None and not hasil.empty:
            tampilkan_hasil(hasil)
        else:
            print("🚫 Tidak ditemukan.")
