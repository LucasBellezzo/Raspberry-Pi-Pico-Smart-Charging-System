import time
from machine import Pin

ledvd = Pin(3, Pin.OUT)
ledam = Pin(2, Pin.OUT)
ledvm = Pin(1, Pin.OUT)


def controlar_recarga(ger, consumo):

    energia = ger - consumo

    if energia > 1000:
        ledvd.on()
        time.sleep(2)
        ledvd.off()
        status = "RECARGA AUTORIZADA"

    elif energia > 0:
        ledam.on()
        time.sleep(2)
        ledam.off()
        status = "RECARGA REDUZIDA"

    else:
        ledvm.on()
        time.sleep(2)
        ledvm.off()
        status = "RECARGA BLOQUEADA"

    print("=" * 30)
    print("      CONTROLADOR DE RECARGA")
    print("=" * 30)

    print(f"Gerador  : {ger} W")
    print(f"Consumo  : {consumo} W")
    print(f"Energia  : {energia} W")
    print(f"Status   : {status}")

    print("=" * 30)

    return energia, status


controlar_recarga(4500, 2500)
time.sleep(2)
controlar_recarga(1800, 1500)
time.sleep(2)
controlar_recarga(1000, 1800)