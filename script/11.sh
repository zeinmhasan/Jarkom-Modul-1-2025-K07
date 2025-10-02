adduser zein
apt-get update
apt-get install -y inetutils-inetd inetutils-telnetd
echo "telnet  stream  tcp     nowait  root    /usr/sbin/in.telnetd  in.telnetd" >> /etc/inetd.conf

di eru 
telnet 10.67.1.2
