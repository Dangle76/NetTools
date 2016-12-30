coproc auth { tail -n1 -f /var/log/auth.log; }
read latestAuth <&"${auth[0]}"
echo "Latest authentication attempt: $latestAuth"
