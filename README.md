# Gestion de l'alimentation avec Tkinter

Ce script en Python utilise Tkinter pour créer une interface graphique permettant de gérer les modes d'alimentation d'un système Windows. Il propose deux modes : Normal et Film.

## Prérequis

Avant d'exécuter ce script, assurez-vous d'avoir Python installé sur votre système. De plus, ce script utilise la bibliothèque `tkinter`, qui est généralement incluse dans les installations Python standard. Si ce n'est pas le cas, vous pouvez l'installer via pip :
pip install tk

Assurez-vous également d'avoir les privilèges nécessaires pour exécuter les commandes système via `os.system`.

Ce script utilise également la bibliothèque `watchdog` pour détecter les modifications du script et effectuer un rechargement à chaud.

## Fonctionnalités

- Activation du mode Normal : Réduit les délais de mise en veille de l'écran et du système à 3 minutes en mode secteur et 5 minutes en mode batterie.
- Activation du mode Film : Augmente les délais de mise en veille de l'écran et du système à 120 minutes en mode secteur et batterie.
- Surveillance des modifications du script pour le rechargement à chaud : Les modifications apportées au script Python sont automatiquement détectées, et le programme est redémarré pour prendre en compte les changements.

## Utilisation

1. Exécutez le script en utilisant Python :
python gestion_alimentation.py

Ou en cliquant directement sur le fichier.

2. Sélectionnez le mode d'alimentation souhaité en cliquant sur les boutons correspondants.

3. Pour quitter le programme, cliquez sur le bouton "Quitter".

## Avertissement

Ce script utilise des commandes système pour modifier les paramètres d'alimentation de votre système Windows. Assurez-vous de comprendre les effets de ces modifications avant de les utiliser.

