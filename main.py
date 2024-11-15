"""Vamos a armar un virus molesto pero no malisioso que solo se cierra si apreto
control mas q (Ctrl + Q) como va a ser  ejecutable vamos a necesitar algunas cosas

Ante de todo crear un entorno virtual para que quede todo encajonado
*Librerias: Pygame, opencv-python y Pyinstaller
*Recursos: icono de chrome, y video a elección
*opencv-python  tengo que instalar tambien
"""
import cv2 #biblioteca para manipular imagenes/videos, etc/
import pygame #Blibloteca para desarroolar video juegos 
import sys #Modulo estandar de python para abrir y cerrar o acceder por linea de comandos
import os  #brinda funciones para interactuar con el sistema de archivos

#Inicializo pygame
pygame.init()

#Configuramos la pantalla a pantalla completa
info = pygame.display.Info()
screen = pygame.display.set_mode((info.current_w,info.current_h), pygame.FULLSCREEN)
pygame.display.set_caption("Video en Pantalla Completa")

# Ruta del Video
video_path = os.path.join(os.path.dirname(__file__),"Video.mp4")

#Cargo el video en OpenCv
cap = cv2.VideoCapture(video_path)

#Compruebo si el video esta abierto correctamente
if not cap.isOpened():
    print("Error en abrir el archivo de video")
    sys.exit()

#Ciclo Principal
while True:
    ret, frame = cap.read()#leo un fotograma del video
    if not ret: #si el video ha terminado, reinicio la reproducción
        cap.set(cv2.CAP_PROP_POS_FRAMES,0)
        continue
    
    #Convertir el fotograma en BGR (opencv) a RGB (pygame)
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    frame = cv2.flip(frame,1 )# aca voy a inverti horizontalemente
    frame = cv2.resize(frame, (info.current_w,info.current_h)) #Ajusto el tamaño 
    
    #Creo una superficie de pygame a parti del fotograma
    frame_surface =  pygame.surfarray.make_surface(frame)
    screen.blit(pygame.transform.rotate(frame_surface, -90),(0,0)) #roto a pantalla completa xq sino lo muestra inverso
    
    pygame.display.update()#actualizo la pantalla
    
    #Manejo el cierre del evento
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LCTRL] and keys[pygame.K_q]: #Apreto Control + Q
                cap.release()
                pygame.quit()
                sys.exit()

#Libero el video y salgo
cap.release()  
pygame.quit()
sys.exit() 