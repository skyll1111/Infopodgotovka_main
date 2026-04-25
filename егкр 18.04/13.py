import ipaddress

ip = "191.89.109.206"
mask = "255.255.224.0"

network = ipaddress.IPv4Network(f"{ip}/{mask}", strict=False)

max_host = list(network.hosts())[-1]

print(network.network_address)
print(network.broadcast_address)
print(max_host)
print(sum(max_host.packed))