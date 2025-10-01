apt update
apt install -y ncat
ncat -l -p 21 --keep-open &
NCAT21_PID=$!
echo "ncat21 pid = $NCAT21_PID"

ncat -l -p 80 --keep-open &
NCAT80_PID=$!
echo "ncat80 pid = $NCAT80_PID"

ss -tulnp | grep -E ':(21|80)\b'
ss -tulnp | grep -E ':(666)\b' || echo "port 666 closed (no listener)"

for p in 21 80 666; do
  echo "=== port $p ==="
  nc -zv -w 2 10.67.1.2 $p
done
