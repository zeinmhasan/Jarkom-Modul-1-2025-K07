wget --no-check-certificate 'https://docs.google.com/uc?export=download&id=11ua2KgBu3MnHEIjhBnzqqv2RMEiJsILY' -O kitab.zip
ftp 10.67.1.1
cd shared
put kitab.zip
nano /etc/vsftpd.conf
user_config_dir=/etc/vsftpd_user_conf
mkdir -p /etc/vsftpd_user_conf
nano /etc/vsftpd_user_conf/ainur
write_enable=NO
service vsftpd restart
ftp 10.67.1.1
