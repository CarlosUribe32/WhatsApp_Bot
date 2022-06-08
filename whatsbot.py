from ast import Break
from time import sleep
from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver as RemoteWebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path=r"C:\DriveChrome\chromedriver.exe")
dicContactos ={}

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
        dicContactos.setdefault(name, 'Hola')
        print(dicContactos)

if __name__ == '__main__':
    main()