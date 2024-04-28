import tkinter as tk
import os
import sys
import subprocess
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class HotReloadHandler(FileSystemEventHandler):
    def on_any_event(self, event):
        if event.src_path.endswith(".py"):
            restart_program()

def set_power_mode(mode):
    if mode == "Normal":
        os.system("powercfg /change monitor-timeout-ac 3")
        os.system("powercfg /change standby-timeout-ac 5")
        os.system("powercfg /change monitor-timeout-dc 3")
        os.system("powercfg /change standby-timeout-dc 5")
    elif mode == "Film":
        os.system("powercfg /change monitor-timeout-ac 120")
        os.system("powercfg /change standby-timeout-ac 120")
        os.system("powercfg /change monitor-timeout-dc 120")
        os.system("powercfg /change standby-timeout-dc 120")

def quit_program():
    set_power_mode("Normal")
    root.destroy()

def update_mode_label(mode):
    mode_label.config(text=f"Mode actuel : {mode}")

def normal_mode():
    set_power_mode("Normal")
    update_mode_label("Normal")

def film_mode():
    set_power_mode("Film")
    update_mode_label("Film")

def restart_program():
    python = sys.executable
    subprocess.Popen([python] + sys.argv)
    root.destroy()

# Création de la fenêtre principale
root = tk.Tk()
root.title("Gestion de l'alimentation")
root.geometry("800x400")  # Définition de la taille de la fenêtre
root.configure(bg="#E7F1FA")  # Couleur de fond

# Style pour les boutons
button_style = {
    "font": ("Helvetica", 12),
    "width": 15,
    "height": 2,
    "bg": "#ffffff",
    "bd": 3,
    "relief": "raised",
    "activebackground": "#dddddd"
}

# Style pour le label
label_style = {
    "font": ("Helvetica", 14),
    "bg": "#E7F1FA",
    "fg": "#31456A"  # Couleur du texte
}

# Label pour afficher le mode actuel
mode_label = tk.Label(root, text="Mode actuel : Normal", **label_style)
mode_label.pack(pady=10)

# Cadre pour contenir les boutons
button_frame = tk.Frame(root, bg="#E7F1FA")
button_frame.pack(pady=20)

# Bouton pour activer le mode Normal
normal_button = tk.Button(button_frame, text="Mode Normal", command=normal_mode, **button_style)
normal_button.grid(row=0, column=0, padx=10)

# Bouton pour activer le mode Film
film_button = tk.Button(button_frame, text="Mode Film", command=film_mode, **button_style)
film_button.grid(row=0, column=1, padx=10)

# Bouton pour quitter le programme
quit_button = tk.Button(root, text="Quitter", command=quit_program, **button_style)
quit_button.pack(pady=10)

# Surveillance des modifications du script pour le rechargement à chaud
event_handler = HotReloadHandler()
observer = Observer()
observer.schedule(event_handler, ".", recursive=True)
observer.start()

root.mainloop()
