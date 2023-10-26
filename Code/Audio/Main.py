import pygame
from pygame import mixer
import serial
import struct

#*-----------------------------------------------------------------------------*#
# Initialize PyGame Library
pygame.init()
mixer.init()

# Set Preferred Volume
mixer.music.set_volume(0.2)

# Audio Settings
settings = 0
if settings == 0:
    C_low = pygame.mixer.Sound('Audio/Piano/c4.mp3')
    D = pygame.mixer.Sound('Audio/Piano/d4.mp3')
    E = pygame.mixer.Sound('Audio/Piano/e4.mp3')
    F = pygame.mixer.Sound('Audio/Piano/f4.mp3')
    G = pygame.mixer.Sound('Audio/Piano/g4.mp3')
    A = pygame.mixer.Sound('Audio/Piano/a5.mp3')
    B = pygame.mixer.Sound('Audio/Piano/b5.mp3')
    C_high = pygame.mixer.Sound('Audio/Piano/c5.mp3')
elif settings == 1:
    C_low = pygame.mixer.Sound('Audio/Harmonica/LowC.mp3')
    D = pygame.mixer.Sound('Audio/Harmonica/D.wav')
    E = pygame.mixer.Sound('Audio/Harmonica/E.mp3')
    F = pygame.mixer.Sound('Audio/Harmonica/F.mp3')
    G = pygame.mixer.Sound('Audio/Harmonica/G.mp3')
    A = pygame.mixer.Sound('Audio/Harmonica/A.mp3')
    B = pygame.mixer.Sound('Audio/Harmonica/B.mp3')
    C_high = pygame.mixer.Sound('Audio/Harmonica/HighC.wav')
elif settings == 2:
    C_low = pygame.mixer.Sound('Audio/Horns/Horn1.mp3')
    D = pygame.mixer.Sound('Audio/Horns/Horn2.mp3')
    E = pygame.mixer.Sound('Audio/Horns/Horn3.mp3')
    F = pygame.mixer.Sound('Audio/Horns/Horn4.mp3')
    G = pygame.mixer.Sound('Audio/Horns/Horn5.mp3')
    A = pygame.mixer.Sound('Audio/Horns/Horn6.mp3')
    B = pygame.mixer.Sound('Audio/Horns/Horn7.mp3')
    C_high = pygame.mixer.Sound('Audio/Horns/Horn8.mp3')
elif settings == 3:
    C_low = pygame.mixer.Sound('Audio/Cat/LowC.mp3')
    D = pygame.mixer.Sound('Audio/Cat/D.mp3')
    E = pygame.mixer.Sound('Audio/Cat/E.mp3')
    F = pygame.mixer.Sound('Audio/Cat/F.mp3')
    G = pygame.mixer.Sound('Audio/Cat/G.mp3')
    A = pygame.mixer.Sound('Audio/Cat/A.mp3')
    B = pygame.mixer.Sound('Audio/Cat/B.mp3')
    C_high = pygame.mixer.Sound('Audio/Cat/HighC.mp3')
#*-----------------------------------------------------------------------------*#
# Run "ls /dev/tty.*" for serial code (Mac)
# Mac: /dev/tty.usbmodemSDA412CDE561
# Windows: COM7
with serial.Serial('/dev/tty.usbmodemSDA412CDE561', 115200) as ser:

    print(ser.readline())  # Read to the first '\n' character

    while True:
        some_bytes = ser.read()  # Read one character

        # Returns a list (of length 1) of decoded python types
        decoded_bytes = struct.unpack('B', some_bytes)

        # Locate Corresponding Notes Given Input From FRDM-KL46Z
        if (chr(some_bytes[0]) == 'c'):
            pygame.mixer.stop()
            C_low.play(1)
            print("Low C")

        elif (chr(some_bytes[0]) == 'D'):
            pygame.mixer.stop()
            D.play(1)
            print("D")

        elif (chr(some_bytes[0]) == 'E'):
            pygame.mixer.stop()
            E.play(1)
            print("E")

        elif (chr(some_bytes[0]) == 'F'):
            pygame.mixer.stop()
            F.play(1)
            print("F")

        elif (chr(some_bytes[0]) == 'G'):
            pygame.mixer.stop()
            G.play(1)
            print("G")

        elif (chr(some_bytes[0]) == 'A'):
            pygame.mixer.stop()
            A.play(1)
            print("A")

        elif (chr(some_bytes[0]) == 'B'):
            pygame.mixer.stop()
            B.play(1)
            print("B")

        elif (chr(some_bytes[0]) == 'C'):
            pygame.mixer.stop()
            C_high.play(1)
            print("High C")
