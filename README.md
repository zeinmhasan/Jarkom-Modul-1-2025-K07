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

## Untuk SOAL 14-20 Langkah Setup-nya Sama
- Setup decoder: Buka terminal, jalankan nc 10.15.43.32 <port_sesuai_soal>.
- Setup wireshark: Download file soal, unzip, lalu buka file dengan wireshark.

## SOAL 14
Setelah gagal mengakses FTP, Melkor melancarkan serangan brute force terhadap  Manwe. Analisis file capture yang disediakan dan identifikasi upaya brute force Melkor. 
(link file) nc 10.15.43.32 3401

### **How many packets are recorded in the pcapng file?**
  <br>Jawaban: **500358**
  <br>How: Dapat dilihat di bagian bawah kanan window wireshark, tertera -> Packets:xxx (jumlah packet).
 <br><img width="1070" height="524" alt="image" src="https://github.com/user-attachments/assets/3a7eaec1-0fca-47e2-9e76-e07bf1dbc2c5" />

 
- **What are the user that successfully logged in?**
  <br>Jawaban: **n1enna:y4v4nn4_k3m3nt4r1**
  <br>How: Dengan menggunakan filter, saring packet dengan:
  ```
  frame contains "successful"
  ```
  <br>Filter akan menampilkan packet dengan isi kata "successful" yang merujuk pada packet dengan data user yang berhasil login. Cara melihat datanya ialah dengan klik kanan packet, lalu pilih follow->tcp stream.
  <br><img width="1008" height="618" alt="image" src="https://github.com/user-attachments/assets/ced754f4-3f43-49b2-abce-6835e7bf1612" />

  
- **In which stream were the credentials found?**
  <br>Jawaban: **41824**
  <br>Setelah follow tcp stream di packet tadi, filter akan otomatis berubah menjadi:
  ```
  tcp.stream eq 41824
  ```
  <br>Menandakan lokasi stream dimana kredensial ditemukan: 41824
  <br><img width="1008" height="618" alt="image" src="https://github.com/user-attachments/assets/ced754f4-3f43-49b2-abce-6835e7bf1612" />

- What tools are used for brute force?
  <br>Jawaban: **Fuzz Faster U Fool v2.1.0-dev**
  <br>Tools biasanya tertera pada User-Agent di kredensial tadi, kebetulan User-Agent juga sesuai dengan format jawaban yang diminta soal.
  <br><img width="1008" height="618" alt="image" src="https://github.com/user-attachments/assets/ced754f4-3f43-49b2-abce-6835e7bf1612" />

<img width="1019" height="530" alt="image" src="https://github.com/user-attachments/assets/30017ed1-5389-48e7-aaa0-6ec556c818f9" />


