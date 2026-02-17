# ===== CLIENTE (usa middleware y envía password) =====
import socket, middleware

HOST, PORT, PASSWORD = middleware.seleccionar()

def enviar(op, extra=""):
    s = socket.socket()
    s.connect((HOST, PORT))
    s.send((PASSWORD + "\n").encode())  # 1) contraseña
    s.send((op + "\n").encode())        # 2) operación
    if extra:
        s.send((extra + "\n").encode()) # 3) datos extra (cmd o pid)
    s.close()

while True:
    print("1) Listar   2) Iniciar   3) Detener   0) Salir")
    op = input("Opción: ").strip()

    if op == "1":
        enviar("1")

    elif op == "2":
        cmd = input("Comando a iniciar: ").strip()
        enviar("2", cmd)

    elif op == "3":
        pid = input("PID a detener: ").strip()
        enviar("3", pid)

    elif op == "0":
        break