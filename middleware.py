# ===== MIDDLEWARE (selección de servidor) =====
# Agrega aquí los servidores disponibles en tu laboratorio
SERVERS = [
    ("127.0.0.1", 5000, "clave123"),       # servidor local
    # ("192.168.1.10", 5000, "claveA"),    # ejemplo otro servidor
    # ("192.168.1.11", 5000, "claveB"),
]

def seleccionar():
    print("Servidores disponibles:")
    for i, s in enumerate(SERVERS):
        print(i, s[0], "puerto", s[1])
    sel = int(input("Elige servidor (número): "))
    host, port, pwd = SERVERS[sel]
    return host, port, pwd