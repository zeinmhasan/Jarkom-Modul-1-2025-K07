# Jarkom-Modul-1-2025-K07

## ANGGOTA 
<table>
  <thead>
    <tr>
      <th>No</th>
      <th>Nama</th>
      <th>NRP</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>1</td>
      <td>Zein muhammad hasan</td>
      <td>5027241035</td>
    </tr>
    <tr>
      <td>2</td>
      <td>Ananda Fitri Wibowo</td>
      <td>5027241057</td>
    </tr>
  </tbody>
</table>

# Topologi Jaringan

| Nama Kota    | Interface | IP Address  | Gateway   |
|--------------|-----------|-------------|-----------|
| Eru    | eth1      | 10.67.1.1   | -         |
|              | eth2      | 10.67.2.1   | -         |
| Melkor    | eth0      | 10.67.1.2   | 10.67.1.1 |
| Manwe | eth0      | 10.67.1.3   | 10.67.1.1 |
| Varda     | eth0      | 10.67.2.2   | 10.67.2.1 |
| Ulmo   | eth0      | 10.67.2.3   | 10.67.2.1 |



## SOAL 1
Untuk mempersiapkan peperangan World War MMXXIV (Iya sebanyak itu), Sriwijaya membuat dua kotanya menjadi web server yaitu Tanjungkulai, dan Bedahulu, serta Sriwijaya sendiri akan menjadi DNS Master. Kemudian karena merasa terdesak, Majapahit memberikan bantuan dan menjadikan kerajaannya (Majapahit) menjadi DNS Slave.

###Eru Config
```
auto eth0
iface eth0 inet dhcp

auto eth1
iface eth1 inet static
        address 10.67.1.1
        netmask 255.255.255.0

auto eth2
iface eth2 inet static
         address 10.67.2.1
         netmask 255.255.255.0

iptables -t nat -A POSTROUTING -o eth0 -j MASQUERADE -s 10.67.0.0/16
```

###Melkor Config
```
auto eth0 
iface eth0 inet static
         address 10.67.1.2
         netmask 255.255.255.0
         gateway 10.67.1.1
```

###Manwe Config
```
auto eth0 
iface eth0 inet static
         address 10.67.1.3
         netmask 255.255.255.0
         gateway 10.67.1.1
```

###Varda Config
```
auto eth0 
iface eth0 inet static
         address 10.67.2.2
         netmask 255.255.255.0
         gateway 10.67.2.1
```

###Ulmo Config
```
auto eth0 
iface eth0 inet static
         address 10.67.2.3
         netmask 255.255.255.0
         gateway 10.67.2.1
```

<img width="475" height="348" alt="Image" src="https://github.com/user-attachments/assets/0ae48998-6248-4465-ac6b-1b2acfd23848" />

## SOAL 2
Karena menurut Eru pada saat itu Arda (Bumi) masih terisolasi dengan dunia luar, maka buat agar Eru dapat tersambung ke internet.

Dengan menyambungkan Eru ke NAT maka Eru sudah bisa mengakses internet
<img width="796" height="367" alt="Image" src="https://github.com/user-attachments/assets/4cf75fd4-b88a-4520-841d-42fe8be971c0" />

## SOAL 3
Sekarang pastikan agar setiap Ainur (Client) dapat terhubung satu sama lain.

dengan configurasi yang sudah tertulis di laporan soal 1 sudah menjawab bagaimana cara agar setiap client terhubung satu sama lain.

## SOAL 4
Setelah berhasil terhubung, sekarang Eru ingin agar setiap Ainur (Client) dapat mandiri. Oleh karena itu pastikan agar setiap Client dapat tersambung ke internet

tulis command ini di Eru :
```
iptables -t nat -A POSTROUTING -o eth0 -j MASQUERADE -s 10.67.0.0/16
```
nanti akan mengeluarkan output di /etc/resolv.conf yaitu ip internet untuk disebar ke setiap client

ipnya :
```
192.168.122.1
```
lalu pasang command ini di setiap client :
```
echo nameserver 192.168.122.1 > /etc/resolv.conf
```
setelah itu setiap client dapat mengakses internet
<img width="818" height="510" alt="Image" src="https://github.com/user-attachments/assets/f8450beb-f575-4fe7-8980-271c15ccb74f" />

## SOAL 5
Ainur terkuat Melkor tetap berusaha untuk menanamkan kejahatan ke dalam Arda (Bumi). Sebelum terjadi kerusakan, Eru dan para Ainur lainnya meminta agar semua konfigurasi tidak hilang saat semua node di restart.

pertama buka file /root/.bashrc di Eru
```
nano /root/.bashrc
```
lalu tulis command2 konfigurasi tadi didalam file itu, ini berguna untuk ketika restart dan terminal dibuka maka akan otomatis menjalankan script konfigurasi

script yang bisa dimasukan :
```
iptables -t nat -A POSTROUTING -o eth0 -j MASQUERADE -s 10.67.0.0/16
echo nameserver 192.168.122.1 > /etc/resolv.conf
```
<img width="792" height="441" alt="Image" src="https://github.com/user-attachments/assets/ea4cbc60-6081-4130-9619-66aed70ad5e2" />

## SOAL 6
Setelah semua Ainur terhubung ke internet, Melkor mencoba menyusup ke dalam komunikasi antara Manwe dan Eru. Jalankan file berikut (link file) lalu lakukan packet sniffing menggunakan Wireshark pada koneksi antara Manwe dan Eru, lalu terapkan display filter untuk menampilkan semua paket yang berasal dari atau menuju ke IP Address Manwe. Simpan hasil capture tersebut sebagai bukti.

di melkor download file nya dulu 
```
wget --no-check-certificate 'https://docs.google.com/uc?export=download&id=1bE3kF1Nclw0VyKq4bL2VtOOt53IC7lG5' -O traffic.zip
unzip traffic.zip
chmod +x traffic.exe
./traffic.exe
```
setelah itu kita bisa lihat jalur Eru ke Manwe di wireshark.

<img width="1919" height="1017" alt="Image" src="https://github.com/user-attachments/assets/86cba392-ae0b-4382-a90a-0e7d441fa0c3" />

## SOAL 7
Untuk meningkatkan keamanan, Eru memutuskan untuk membuat sebuah FTP Server di node miliknya. Lakukan konfigurasi FTP Server pada node Eru. Buat dua user baru: ainur dengan hak akses write&read dan melkor tanpa hak akses sama sekali ke direktori shared. Buktikan hasil tersebut dengan membuat file teks sederhana kemudian akses file tersebut menggunakan kedua user.

pertama tama kita harus buat FTP service dulu di Eru 
install klo belum :
```
apt update
apt install inetutils-ftp -y
```
lalu buat folder shared nya :
```
mkdir -p /srv/ftp/shared
chmod 777 /srv/ftp/shared
```
tambahkan user :
```
adduser ainur
adduser melkor
```
atur izin untuk setiap usernya :
```
chown ainur:ainur /srv/ftp/shared
chmod 755 /srv/ftp
chmod 770 /srv/ftp/shared
```
pindah folder shared nya :
```
mv /srv/ftp/shared /home/ainur/shared
chown ainur:ainur /home/ainur/shared
```
atur akses untuk ainur :
```
chmod 770 /home/ainur/shared
```
atur file vsftpd.conf :
```
nano /etc/vsftpd.conf
local_enable=YES
write_enable=YES
chroot_local_user=YES
listen=YES
listen_ipv6=NO
allow_writeable_chroot=YES
```
restart dan mulai FTP :
```
service vsftpd restart
```
tes buat file :
```
echo "Ini file uji coba FTP" > /srv/ftp/shared/test.txt
```
masuk ke ftp :
```
ftp 10.67.1.1
```
taruh file tadi dan coba keluar terus login lagi dengan kedua akun tersebut dan coba tes akses nya:
<img width="800" height="510" alt="Image" src="https://github.com/user-attachments/assets/0948034a-1338-43ee-8cff-117a8edc403b" />

<img width="372" height="240" alt="Image" src="https://github.com/user-attachments/assets/88c75b84-f099-4bef-adef-f9d33df83f04" />

## SOAL 8 
Ulmo, sebagai penjaga perairan, perlu mengirimkan data ramalan cuaca ke node Eru. Lakukan koneksi sebagai client dari node Ulmo ke FTP Server Eru menggunakan user ainur. Upload sebuah file berikut (link file). Analisis proses ini menggunakan Wireshark dan identifikasi perintah FTP yang digunakan untuk proses upload.

pergi ke client Ulmo
lalu download file nya :
```
apt update && apt install wget -y
wget --no-check-certificate 'https://docs.google.com/uc?export=download&id=11ra_yTV_adsPIXeIPMSt0vrxCBZu0r33' -O cuaca.zip
```
setelah itu masuk ftp :
```
ftp 10.67.1.1
```
login sebagai ainur dan taroh file nya 
```
put cuaca.zip
```
<img width="1368" height="680" alt="Image" src="https://github.com/user-attachments/assets/5c687a2e-711f-451a-84ab-cf52002286cd" />

## SOAL 9
Eru ingin membagikan "Kitab Penciptaan" di (link file) kepada Manwe. Dari FTP Server Eru, download file tersebut ke node Manwe. Karena Eru merasa Kitab tersebut sangat penting maka ia mengubah akses user ainur menjadi read-only. Gunakan Wireshark untuk memonitor koneksi, identifikasi perintah FTP yang digunakan, dan uji akses user ainur.

di Eru masuk dulu sebagai ke FTP sebagai ainur lalu masukin file yang di download
```
wget --no-check-certificate 'https://docs.google.com/uc?export=download&id=11ua2KgBu3MnHEIjhBnzqqv2RMEiJsILY' -O kitab.zip
ftp 10.67.1.1
cd shared
put kitab.zip
```
lalu kita ubah akses ainur menjadi read only 
Edit /etc/vsftpd.conf :
```
nano /etc/vsftpd.conf
```
tambahin kode ini :
```
user_config_dir=/etc/vsftpd_user_conf
```
buat folder untuk konfigurasi user :
```
mkdir -p /etc/vsftpd_user_conf
nano /etc/vsftpd_user_conf/ainur
```
isi :
```
write_enable=NO
```

reset dan uji coba :
```
service vsftpd restart
ftp 10.67.1.1
```

hasilnya akan seperti ini :

<img width="797" height="324" alt="Image" src="https://github.com/user-attachments/assets/fa92c648-2930-4bfa-b15e-95f2b11614da" />

## SOAL 10
Melkor yang marah karena tidak diberi akses, mencoba melakukan serangan dengan mengirimkan banyak sekali request ke server Eru. Gunakan command ping dari node Melkor ke node Eru dengan jumlah paket yang tidak biasa (spam ping misalnya 100 paket). Amati hasilnya, apakah ada packet loss? Catat average round trip time untuk melihat apakah serangan tersebut mempengaruhi kinerja Eru.

di Melkor cukup jalankan :
```
ping -c 100 -i 0.1 10.67.1.1
```
trus pantau dari wireshark 
<img width="1919" height="1018" alt="Image" src="https://github.com/user-attachments/assets/cbb13160-d933-4edd-bbee-4434d3d12494" />

## SOAL 12
Eru mencurigai Melkor menjalankan beberapa layanan terlarang di node-nya. Lakukan pemindaian port sederhana dari node Eru ke node Melkor menggunakan Netcat (nc) untuk memeriksa port 21, 80, dalam keadaan terbuka dan port rahasia 666 dalam keadaan tertutup.

pergi ke meklor lalu buat port : 

download dulu klo belum : 
```
apt update
apt install -y ncat
```

lalu buat port 21 :
```
ncat -l -p 21 --keep-open &
NCAT21_PID=$!
echo "ncat21 pid = $NCAT21_PID"
```

lalu buat port 80 :
```
ncat -l -p 80 --keep-open &
NCAT80_PID=$!
echo "ncat80 pid = $NCAT80_PID"
```

terkahir cek listener Pastikan port 666 tidak listen (harus kosong):
```
ss -tulnp | grep -E ':(21|80)\b'
ss -tulnp | grep -E ':(666)\b' || echo "port 666 closed (no listener)"
```
pergi ke Eru dan lakukan scan :
```
for p in 21 80 666; do
  echo "=== port $p ==="
  nc -zv -w 2 10.67.1.2 $p
done
```
nanti hasilnya akan seperti ini :
<img width="832" height="231" alt="Image" src="https://github.com/user-attachments/assets/d6a8d422-fbb9-4d52-bb79-bb8a8a41b95e" />

# Untuk SOAL 14-20 Langkah Setup-nya Sama
- Setup decoder: Buka terminal, jalankan nc 10.15.43.32 <port_sesuai_soal>.
- Setup wireshark: Download file soal, unzip, lalu buka file dengan wireshark.

## SOAL 14
Setelah gagal mengakses FTP, Melkor melancarkan serangan brute force terhadap  Manwe. Analisis file capture yang disediakan dan identifikasi upaya brute force Melkor. (link file) nc 10.15.43.32 3401

#### A. How many packets are recorded in the pcapng file?
  Jawaban: **500358**
  <br>How: Dapat dilihat di bagian bawah kanan window wireshark, tertera -> Packets:xxx (jumlah packet).
<br><img width="486" height="204" alt="image" src="https://github.com/user-attachments/assets/62aa579c-5819-4fb3-b732-992e1f7d88d3" />
 
### B. What are the user that successfully logged in?
  Jawaban: **n1enna:y4v4nn4_k3m3nt4r1**
  <br>How: Dengan menggunakan filter, saring packet dengan:
  ```
  frame contains "successful"
  ```
  <br>Filter akan menampilkan packet dengan isi kata "successful" yang merujuk pada packet dengan data user yang berhasil login. Cara melihat datanya ialah dengan klik kanan packet, lalu pilih Follow->TCP Stream.
 <br><img width="535" height="262" alt="image" src="https://github.com/user-attachments/assets/3a7eaec1-0fca-47e2-9e76-e07bf1dbc2c5" />
<img width="470" height="285" alt="image" src="https://github.com/user-attachments/assets/ced754f4-3f43-49b2-abce-6835e7bf1612" />
  
### C. In which stream were the credentials found?
  Jawaban: **41824**
  <br>Setelah Follow TCP Stream di packet tadi, filter akan otomatis berubah menjadi:
  ```
  tcp.stream eq 41824
  ```
  <br>Menandakan lokasi stream dimana kredensial ditemukan: 41824


### D. What tools are used for brute force?
  Jawaban: **Fuzz Faster U Fool v2.1.0-dev**
  <br>Tools biasanya tertera pada User-Agent di kredensial tadi, kebetulan User-Agent juga sesuai dengan format jawaban yang diminta soal.
  <br><img width="504" height="309" alt="image" src="https://github.com/user-attachments/assets/ced754f4-3f43-49b2-abce-6835e7bf1612" />

### Screenshot Pengerjaan
<img width="508" height="265" alt="image" src="https://github.com/user-attachments/assets/30017ed1-5389-48e7-aaa0-6ec556c818f9" />


## Soal 15
Melkor menyusup ke ruang server dan memasang keyboard USB berbahaya pada node Manwe. Buka file capture dan identifikasi pesan atau ketikan (keystrokes) yang berhasil dicuri oleh Melkor untuk menemukan password rahasia. (link file) nc 10.15.43.32 3402

#### A. What device does Melkor use?
  Jawaban: **Keyboard**
  <br>Setelah mengecek beberapa isi packet, saya menemukan string dengan nama "U" dan "USB Keyboard". Ketika saya input keduanya sebagai jawaban, ternyata salah. Lalu saya coba "Keyboard" saja dan ternyata berhasil.
  <br><img width="765" height="306" alt="image" src="https://github.com/user-attachments/assets/e87ba9c9-90a6-4b44-bc71-3d61730ab195" />

#### B. What did Melkor write?
  Jawaban: **UGx6X3ByMHYxZGVfeTB1cl91czNybjRtZV80bmRfcDRzc3cwcmQ=**
  <br>Karena di packet-packet mengandung string dengan format HID, maka bisa kita lakukan Export Packet Dissections As Plain Text.
  <br><img width="390" height="280" alt="image" src="https://github.com/user-attachments/assets/fca5cb46-f7a5-4579-be27-f0e6eff63236" />
  <br>Kemudian dapat kita decode menggunakan script decoder:
  ```
import sys

# Kamus pemetaan HID ke ASCII
HID_TO_ASCII = {
    0x04: 'a', 0x05: 'b', 0x06: 'c', 0x07: 'd', 0x08: 'e', 0x09: 'f', 0x0A: 'g',
    0x0B: 'h', 0x0C: 'i', 0x0D: 'j', 0x0E: 'k', 0x0F: 'l', 0x10: 'm', 0x11: 'n',
    0x12: 'o', 0x13: 'p', 0x14: 'q', 0x15: 'r', 0x16: 's', 0x17: 't', 0x18: 'u',
    0x19: 'v', 0x1A: 'w', 0x1B: 'x', 0x1C: 'y', 0x1D: 'z',
    0x1E: '1', 0x1F: '2', 0x20: '3', 0x21: '4', 0x22: '5', 0x23: '6', 0x24: '7',
    0x25: '8', 0x26: '9', 0x27: '0',
    0x28: '\n', 0x29: '[ESC]', 0x2A: '[BACKSPACE]', 0x2B: '\t', 0x2C: ' ',
    0x2D: '-', 0x2E: '=', 0x2F: '[', 0x30: ']', 0x31: '\\', 0x33: ';', 0x34: '\'',
    0x35: '`', 0x36: ',', 0x37: '.', 0x38: '/',
    0x59: '1', 0x5A: '2', 0x5B: '3', 0x5C: '4', 0x5D: '5', 0x5E: '6', 0x5F: '7',
    0x60: '8', 0x61: '9', 0x62: '0',
}

SHIFT_HID_TO_ASCII = {
    0x04: 'A', 0x05: 'B', 0x06: 'C', 0x07: 'D', 0x08: 'E', 0x09: 'F', 0x0A: 'G',
    0x0B: 'H', 0x0C: 'I', 0x0D: 'J', 0x0E: 'K', 0x0F: 'L', 0x10: 'M', 0x11: 'N',
    0x12: 'O', 0x13: 'P', 0x14: 'Q', 0x15: 'R', 0x16: 'S', 0x17: 'T', 0x18: 'U',
    0x19: 'V', 0x1A: 'W', 0x1B: 'X', 0x1C: 'Y', 0x1D: 'Z',
    0x1E: '!', 0x1F: '@', 0x20: '#', 0x21: '$', 0x22: '%', 0x23: '^', 0x24: '&',
    0x25: '*', 0x26: '(', 0x27: ')',
    0x2D: '_', 0x2E: '+', 0x2F: '{', 0x30: '}', 0x31: '|', 0x33: ':', 0x34: '"',
    0x35: '~', 0x36: '<', 0x37: '>', 0x38: '?',
}

def decrypt_hid_data(hid_codes):
    result = ""
    for report in hid_codes:
        if len(report) < 3:
            continue
        modifier_byte = report[0]
        keycode = report[2]
        is_shift_pressed = (modifier_byte & 2) or (modifier_byte & 32)
        char = ''
        if keycode == 0:  # Abaikan jika tidak ada tombol yang ditekan (key release)
            continue
        if is_shift_pressed:
            char = SHIFT_HID_TO_ASCII.get(keycode, HID_TO_ASCII.get(keycode, ''))
        else:
            char = HID_TO_ASCII.get(keycode, '')
        result += char
    return result

def parse_hid_data_from_log(file_content):
    """
    Mengekstrak data HID dari log Wireshark dan mengubahnya ke format yang benar.
    """
    hid_codes = []
    for line in file_content.splitlines():
        # Cari baris yang mengandung 'HID Data:'
        if 'HID Data:' in line:
            # Ambil string hex setelah 'HID Data: '
            hex_str = line.split(':')[-1].strip()
            
            try:
                # Ubah string hex (misal: "020018...") menjadi list of integers
                # Contoh: [int('02', 16), int('00', 16), int('18', 16), ...]
                # Menjadi: [2, 0, 24, 0, 0, 0, 0, 0]
                byte_list = [int(hex_str[i:i+2], 16) for i in range(0, len(hex_str), 2)]
                hid_codes.append(byte_list)
            except (ValueError, IndexError):
                # Lewati jika ada baris yang formatnya tidak valid
                continue
    return hid_codes

def main():
    if len(sys.argv) < 2:
        print("Error: Mohon sertakan nama file input.")
        print("Contoh: python3 hid_decoder.py namafile.txt")
        return

    input_filename = sys.argv[1]
    
    try:
        with open(input_filename, 'r') as f:
            log_content = f.read()
    except FileNotFoundError:
        print(f"Error: File '{input_filename}' tidak ditemukan.")
        return

    # Ekstrak data HID dari log
    hid_data_list = parse_hid_data_from_log(log_content)
    
    # Lakukan dekripsi dan cetak hasilnya
    decoded_text = decrypt_hid_data(hid_data_list)
    print(decoded_text, end='')

if __name__ == "__main__":
    main()
  ```
  <br>Script dapat dijalankan dan menghasilkan: UGx6X3ByMHYxZGVfeTB1cl91czNybjRtZV80bmRfcDRzc3cwcmQ=

#### C. What is Melkor's secret message?
  Jawaban: **Plz_pr0v1de_y0ur_us3rn4me_4nd_p4ssw0rd**
  <br>String "UGx6X3ByMHYxZGVfeTB1cl91czNybjRtZV80bmRfcDRzc3cwcmQ=" dapat didecode menggunakan cyberchef, menghasilkan: Plz_pr0v1de_y0ur_us3rn4me_4nd_p4ssw0rd
  <br><img width="511" height="199" alt="image" src="https://github.com/user-attachments/assets/91640210-c375-4600-a207-de2a5b642d4a" />



#### Screenshot Pengerjaan
<img width="548" height="221" alt="image" src="https://github.com/user-attachments/assets/5276d755-a6a8-4bd0-8a45-77576cbef6dc" />

## Soal 16
Melkor semakin murka ia meletakkan file berbahaya di server milik Manwe. Dari file capture yang ada, identifikasi file apa yang diletakkan oleh Melkor. (link file) nc 10.15.43.32 3403

#### A. What credential did the attacker use to log in?
  Jawaban: **ind@psg420.com:{6r_6e#TfT1p**
  <br>Seperti mencari kredensial di nomor 14, saya coba cari packet dengan protokol TCP. Saya menemukan 1 packet dengan warna merah yang ternyata memiliki kredensial tersebut. Saya menemukan 2 packet warna merah lain namun isinya tidak menjawab permintaan soal. Cara ceknya dengan Follow TCP Stream.
  <img width="532" height="229" alt="image" src="https://github.com/user-attachments/assets/8a21fb5d-0069-4d58-a82c-bfccd56af786" />

#### B. How many files are suspected of containing malware?
  Jawaban: **5**
  <br>Karena malware erat hubungannya dengan aplikasi, maka saya coba menghitung jumlah string dengan ekstensi ".exe". Total ada 5 dengan detail: q, w, e, r, t.exe.
  <br><img width="570" height="539" alt="image" src="https://github.com/user-attachments/assets/8742821b-6ae9-4abb-823c-0fe669d4b4b6" />

### Format C-H Kurang Lebih Sama
- Langkah yang dapat dilakukan ialah mencari packet dengan info "huruf.exe".
- Cari packet dengan data lenght terbesar, lalu Follow TCP Stream.
- Ubah format data dari ASCII menjadi **Raw**.
- Save file as "all files" (tanpa ekstensi).
- Lalu decode file menggunakan **sha256**, seperti:
  ```
  sha256sum nama_file
  ```
- File sudah terdecrypt yeyy.
  <img width="800" height="500" alt="image" src="https://github.com/user-attachments/assets/2c6a825f-b910-43d4-8cca-9324dd2f0da2" />
<img width="500" height="27" alt="image" src="https://github.com/user-attachments/assets/58c46155-2fd1-4fde-8a22-6dfd4972604b" />

#### C. What is the hash of the first file (q.exe)?
  Jawaban: **ca34b0926cdc3242bbfad1c4a0b42cc2750d90db9a272d92cfb6cb7034d2a3bd**
  <br>Menggunakan langkah tadi.

#### D. What is the hash of the second file (w.exe)?
  Jawaban: **08eb941447078ef2c6ad8d91bb2f52256c09657ecd3d5344023edccf7291e9fc**

#### E. What is the hash of the third file (e.exe)?
  Jawaban: **32e1b3732cd779af1bf7730d0ec8a7a87a084319f6a0870dc7362a15ddbd3199**
  <br>Menggunakan langkah tadi.

#### F. What is the hash of the fourth file (r.exe)?
  Jawaban: **4ebd58007ee933a0a8348aee2922904a7110b7fb6a316b1c7fb2c6677e613884**
  <br>Menggunakan langkah tadi.

#### G. What is the hash of the fifth file (t.exe)?
  Jawaban: **10ce4b79180a2ddd924fdc95951d968191af2ee3b7dfc96dd6a5714dbeae613a**
  <br>Menggunakan langkah tadi.

#### Screenshot Pengerjaan
<img width="550" height="404" alt="image" src="https://github.com/user-attachments/assets/4aa90764-cab8-48b0-8981-8e4ab976578a" />

## Soal 17
Manwe membuat halaman web di node-nya yang menampilkan gambar cincin agung. Melkor yang melihat web tersebut merasa iri sehingga ia meletakkan file berbahaya agar web tersebut dapat dianggap menyebarkan malware oleh Eru. Analisis file capture untuk menggagalkan rencana Melkor dan menyelamatkan web Manwe. (link file) nc 10.15.43.32 3404

#### A. What is the name of the first suspicious file?
  Jawaban: **Invoice&MSO-Request.doc**
  <br> Karena malware ditaruh di web, maka dicari packet dengan protokol HTTP. Terdapat 3 file dengan ekstensi, akhirnya saya coba satu-satu.
  <br><img width="690" height="210" alt="image" src="https://github.com/user-attachments/assets/74fabf44-2420-48a9-83cf-15cb6728e42c" />

#### B. What is the name of the second suspicious file?
  Jawaban: **knr.exe**
  <br>Masih coba-coba kaya tadi.
  <br><img width="640" height="210" alt="image" src="https://github.com/user-attachments/assets/74fabf44-2420-48a9-83cf-15cb6728e42c" />

#### C. What is the hash of the second suspicious file (knr.exe)?
  Jawaban: **749e161661290e8a2d190b1a66469744127bc25bf46e5d0c6f2e835f4b92db18**
  <br>Awalnya saya coba menggunakan cara nomor 16 tadi, dengan [Klik kanan packet -> Follow TCP & HTTP -> Save as -> sha256sum]
  <br><img width="550" height="190" alt="image" src="https://github.com/user-attachments/assets/0cd91e3f-b90e-4707-90cc-c96506efdb2a" />
  <br>Namun tidak tahu mengapa decodenya salah terus. Akhirnya saya coba cari fitur lain, dan menemukan fitur [File->Export Object->HTTP...]
  <br>Setelahnya dilakukan cara sha256 tadi.
  <br><img width="650" height="400" alt="image" src="https://github.com/user-attachments/assets/78c79ebd-7017-4e39-9539-c38ef18b98aa" />

#### Screenshot Pengerjaan
<img width="225" height="215" alt="image" src="https://github.com/user-attachments/assets/e99e3bad-202b-4589-a22a-c4a1ecce2d7a" />

## Soal 18
Karena rencana Melkor yang terus gagal, ia akhirnya berhenti sejenak untuk berpikir. Pada saat berpikir ia akhirnya memutuskan untuk membuat rencana jahat lainnya dengan meletakkan file berbahaya lagi tetapi dengan metode yang berbeda. Gagalkan lagi rencana Melkor dengan mengidentifikasi file capture yang disediakan agar dunia tetap aman. (link file) nc 10.15.43.32 3405

#### A. How many files are suspected of containing malware?
  Jawaban: **2**
  <br>Ditemukan 2 nama file yang kemungkinan adalah malware dengan menggunakan filter:
  ```
frame contain ".exe"
```
  <br><img width="920" height="120" alt="image" src="https://github.com/user-attachments/assets/d27301f7-a8f2-4323-abd3-81fa437563ff" />
  <br>(di packet TCP juga tertera file "d0p2nc6ka3f_fixhohlycj4ovqfcy_smchzo_ub83urjpphrwahjwhv_o5c0fvf6.exe")

#### B. What is the name of the first malicious file?
  Jawaban: **d0p2nc6ka3f_fixhohlycj4ovqfcy_smchzo_ub83urjpphrwahjwhv_o5c0fvf6.exe**
  <br>Dengan menyelami packet, didapati nama filenya
  <br><img width="505" height="355" alt="image" src="https://github.com/user-attachments/assets/6dec71fe-3f44-4b5a-88b0-ec31d259cdd0" />

#### C. Apa nama file berbahaya yang kedua?
  Jawaban: **oiku9bu68cxqenfmcsos2aek6t07_guuisgxhllixv8dx2eemqddnhyh46l8n_di.exe**
  <br>Dengan menyelami packet, didapati nama filenya
  <br><img width="505" height="350" alt="image" src="https://github.com/user-attachments/assets/5487605c-196f-4b07-b3de-590350685fed" />

#### D. What is the hash of the first malicious file?
  Jawaban: **59896ae5f3edcb999243c7bfdc0b17eb7fe28f3a66259d797386ea470c010040**
  <br>Setelah mencoba menyimpan packet dengan format raw text dan salah (bukan jawaban benar), saya coba menggunakan cara Export Object seperti sebelumnya. Karena protocol yang digunakan packet ialah SMB, maka saya lakukan [File->Export Object->SMB->Save]
  <br><img width="480" height="365" alt="image" src="https://github.com/user-attachments/assets/2cc300c1-ea6d-4908-a7b2-233881f94308" />
  <br>Kemudian decrypt dengan sha256.
  <br><img width="504" height="90" alt="image" src="https://github.com/user-attachments/assets/9496b151-2ae7-45b0-ab81-73d10b309c67" />

#### E. What is the hash of the second malicious file?
  Jawaban: **cf99990bee6c378cbf56239b3cc88276eec348d82740f84e9d5c343751f82560**
  <br>Seperti poin D. Setelah mencoba menyimpan packet dengan format raw text dan salah (bukan jawaban benar), saya coba menggunakan cara Export Object seperti sebelumnya. Karena protocol yang digunakan packet ialah SMB, maka saya lakukan [File->Export Object->SMB->Save]
  <br><img width="480" height="365" alt="image" src="https://github.com/user-attachments/assets/2cc300c1-ea6d-4908-a7b2-233881f94308" />
  <br>Kemudian decrypt dengan sha256.
  <br><img width="504" height="90" alt="image" src="https://github.com/user-attachments/assets/9496b151-2ae7-45b0-ab81-73d10b309c67" />

#### Bukti Screenshot
<img width="560" height="365" alt="image" src="https://github.com/user-attachments/assets/633d068e-c414-4293-a8c6-8b1257ec1f3b" />

## Soal 19

  
