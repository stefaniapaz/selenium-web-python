from selenium import webdriver
from faker import Faker
from datetime import datetime

fake = Faker()

# Configura el navegador y abre la página del formulario
url_formulario = "https://demoqa.com/text-box"
# Ruta de chromedriver
ruta_chromedriver = "/home/stefania/Documentos/Cursos/chromedriver_linux64/chromedriver"
# Puedes cambiar 'Chrome()' por 'Firefox()' u otro navegador compatible
driver = webdriver.Chrome(executable_path=ruta_chromedriver)

driver.get(url_formulario)

# Genera datos aleatorios con Faker
full_name = fake.name()
email = fake.email()
current_address = fake.address()
permanent_address = fake.address()

# Localiza los campos del formulario e ingresa la información
campo_full_name = driver.find_element_by_id("userName")
campo_email = driver.find_element_by_id("userEmail")
campo_current_address = driver.find_element_by_id("currentAddress")
campo_permanent_address = driver.find_element_by_id("permanentAddress")

campo_full_name.send_keys(full_name)
campo_email.send_keys(email)
campo_current_address.send_keys(current_address)
campo_permanent_address.send_keys(permanent_address)

# Obtiene la fecha y hora actual
marca_tiempo = datetime.now().strftime("%Y%m%d_%H%M%S")
# Guarda los datos en un archivo de texto
nombre_archivo = f'Datos_formulario_{marca_tiempo}.txt'
with open(nombre_archivo, 'w') as archivo:
    archivo.write(f"Nombre Completo: {full_name}\n")
    archivo.write(f"Email: {email}\n")
    archivo.write(f"Dirección Actual: {current_address}\n")
    archivo.write(f"Dirección Permanente: {permanent_address}\n")

# Envía el formulario
boton_submit = driver.find_element_by_id("submit")
boton_submit.click()

# Puedes agregar una pausa (sleep) para asegurar que la página se cargue completamente
# from time import sleep
# sleep(2)

# Cierra el navegador al finalizar
driver.quit()


