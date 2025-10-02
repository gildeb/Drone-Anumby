## Developpement micropython pour le contrôleur de vol esp-drone

# Pour flasher micropython sur l'ESP32S3 de la carte

Connecter la carte en USB _en maintenant enfoncé l'interrupteur BOOT_ (celui qui est du côté de la LED blanche), puis dans Thonny :

<img width="301" height="327" alt="Thonny 1" src="https://github.com/user-attachments/assets/04f9d17b-6c33-43f6-8f18-0869f58750e4" />

Sélectionner ESP32, puis install :

<img width="373" height="361" alt="Thonny 2" src="https://github.com/user-attachments/assets/02d0e6e0-54ba-42e4-a7ac-74f021b8c9c2" />

Sélectionner les options d'installation ci-dessous, puis lancer l'installation:

<img width="370" height="276" alt="Thonny 3" src="https://github.com/user-attachments/assets/ac6bc1c6-21ca-4b07-a9cb-80d48a1936df" />

Fermer la fenêtre. L'interpréteur est lancé automatiquement:

<img width="372" height="276" alt="Thonny 4" src="https://github.com/user-attachments/assets/d8ddf8cc-18cd-4fb7-8c8b-fd39225df367" />

Charger les scripts de ce répertoire sur la carte.

# Les scripts

- _test_ADC_bat.py_ : affiche en continu (toutes les secondes), le voltage de la batterie (penser à connecter la batterie, CTRL-c pour interrompre))
- _test_motors.py_  : fait tourner les moteurs les uns à la suite des autres pendant un seconde (penser à connecter la batterie et vérifier le sens de rotation des 4 hélices)
- _test_MPU6050.py_ : initialise l'IMU et affiche en continu (3 fois par seconde) le pitch (tangage) et le roll (roulis) en degrés (CTRL-c pour interrompre)

# Commande ESPnow

Pour tester l'ESPnow, on utilise la télécommande du Robot Service Jeunesse 2025. Commencer par déterminer l'adresse mac du drone avec le script _display_mac.py_, puis copier cette adresse dans le script _telecommande_drone.py_.
