from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('https://sia.unal.edu.co/Catalogo/facespublico/public/servicioPublico.jsf?taskflowId=task-flow-AC_CatalogoAsignaturas')

selectNivelEstudio = driver.find_element(by=By.ID, value='pt1:r1:0:soc1::content')
selectNivelEstudio.send_keys('0')
