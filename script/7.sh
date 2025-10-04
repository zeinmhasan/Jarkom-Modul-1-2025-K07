apt update
apt install vsftpd -y
mkdir -p /srv/ftp/shared
chmod 777 /srv/ftp/shared
adduser ainur
adduser melkor
chown ainur:ainur /srv/ftp/shared
chmod 755 /srv/ftp
chmod 770 /srv/ftp/shared
mv /srv/ftp/shared /home/ainur/shared
chown ainur:ainur /home/ainur/shared
chmod 770 /home/ainur/shared

nano /etc/vsftpd.conf
local_enable=YES
write_enable=YES
chroot_local_user=YES
listen=YES
listen_ipv6=NO
allow_writeable_chroot=YES

service vsftpd restart

echo "Ini file uji coba FTP" > /srv/ftp/shared/test.txt

ftp 10.67.1.1
