# ===== SERVIDOR (password + whitelist) =====
import os, socket

PASSWORD = "clave123"                    # <-- cámbiala
WHITELIST = ["sleep", "gedit", "python"] # <-- comandos permitidos


def recvline(conn):
    data = b""
    while not data.endswith(b"\n"):
        chunk = conn.recv(1)
        if not chunk:
            break
        data += chunk
    return data.decode().strip()


def listar():
    os.system("ps -eo pid,comm | tail -n 30")

def iniciar(conn):
    cmd = recvline(conn)              
    ok = False
    for w in WHITELIST:
        if cmd == w or cmd.startswith(w + " "):
            ok = True
            break
    if ok:
        os.system(cmd + " &")
    else:
        print("Bloqueado por whitelist:", cmd)

def detener(conn):
    pid = recvline(conn) 
    os.system("kill " + pid)

server = socket.socket()
server.bind(("127.0.0.1", 5000))  # para una sola PC usa ("127.0.0.1", 5000)
server.listen(5)
print("Servidor listo...")

while True:
    conn, addr = server.accept()
    print("Conexión de:", addr) 
    # 1) Autenticación simple
    pwd = recvline(conn)
    print("Password recibida (len):", len(pwd))
    print("Password esperada (len):", len(PASSWORD))
    print("Password recibida (repr):", repr(pwd))        # <-- agrega esta línea
    print("Password esperada (repr):", repr(PASSWORD)) 

    if pwd != PASSWORD:
        print("Password incorrecta. Cerrando.")
        conn.close()
        continue

    # 2) Operación
    op = recvline(conn)
    print("Operación:", op)
    if op == "1": listar()
    elif op == "2": iniciar(conn)
    elif op == "3": detener(conn)


    conn.close()









