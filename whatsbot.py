from ast import Break
from time import sleep
from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver as RemoteWebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
import threading

driver = webdriver.Chrome(executable_path=r"C:\DriveChrome\chromedriver.exe")
dicContactos ={}
condicion = threading.Condition()
hiloEnUso = False

def abrirWhatsApp():
    driver.get("https://web.whatsapp.com/")
    sleep(5)

def validarQR():
    try:
        driver.find_element_by_tag_name("canvas")
    except:
        return False
    return True    
    
def autenticacionWhatsApp():
    esperar = True
    while(esperar):
        print("Valide pues admin")
        esperar = validarQR()
        sleep(2)
        if(esperar==False):
            print("Gracias admin por validar")

def buscarContacto(contacto):
    buscando = True
    while (buscando):
        elementos = driver.find_elements_by_tag_name("span")
        for elemento in elementos:
            if(elemento.get_attribute("title") == contacto):
                elemento.click()
                buscando = False
                break


def regulacionChat(contacto, condicion):
    while(True):
        with condicion:
            #Esperar que otros hilos se ejecuten
            # if(hiloEnUso==True):
            #     condicion.wait()
            #Pedir mi turno de ejecucion (hilo)
            # hiloEnUso =True
            buscarContacto(contacto)
            # hiloEnUso = False
            #condicion.notifyAll()







def main():
    #Abrimos WhatsApp
    abrirWhatsApp()

    #Autenticamos nuestro chat
    autenticacionWhatsApp()

    #Esperando Contactos
    while(True):
        print("Hola señor admin, ingrese los usuarios a los que quiere implementarle la automatización por WhatsApp")
        name = input()
        if(name=="F"):
            break
        hilo = threading.Thread(name="hilo%s" %name, target=regulacionChat, args=(name, condicion))
        dicContactos.setdefault(name, hilo.start())

if __name__ == '__main__':
    main()