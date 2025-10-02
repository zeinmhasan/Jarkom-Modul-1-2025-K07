adduser nanda
apt-get update
apt-get install -y openssh-server
/usr/sbin/sshd &

di varda 
ssh nanda@10.67.1.1
