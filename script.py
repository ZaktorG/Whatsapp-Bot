import pywhatkit

def run():
    mensaje = input("Ingrese mensaje: ")
    while True:
        try:  
            hora = int(input("Ingrese hora: "))
            minuto = int(input("Ingrese minuto: "))
            break
        except ValueError:
             print("Ingrese un numero")   
    pywhatkit.playonyt("Minero version orquesta")
    pywhatkit.sendwhatmsg("+5212761013577", mensaje, hora, minuto)
 
if __name__ == "__main__":
    run()
