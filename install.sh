echo "net.ipv6.conf.all.disable_ipv6 =1" >/etc/sysctl.conf
sysctl -p
sysctl -w net.ipv6.conf.all.disable_ipv6=1
echo "precedence ::ffff:0:0/96 100" >>/etc/gai.conf

curl -L -s https://install.direct/go.sh -o go.sh
bash go.sh

systemctl  enable v2ray
