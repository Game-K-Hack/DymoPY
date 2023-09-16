from tkinter import Tk, StringVar, Canvas, Label, Entry
from pystray import MenuItem as item
from threading import Thread
from yaml import safe_load
from PIL import Image
import pystray
import pickle
import signal
import time
import os

from win32com.client import Dispatch
import pathlib

config = safe_load(open(os.path.join(os.path.dirname(__file__), "config.yml"), "r"))
app_started = True
size_entry = config["gui"]["sizeEntry"]

root = Tk()
root.title("DymoPY by Game K")
root.resizable(False, False)
root.iconbitmap(os.path.join(os.path.dirname(__file__), "images", "icon.ico"))

config_file = os.path.join(os.path.dirname(__file__), "profile.pkl") if config["config"]["profilePath"] is None else config["config"]["profilePath"]
if os.path.exists(config_file):
    a, b, c = pickle.load(open(config_file, "rb"))
else:
    dflt = config["default"]
    a, b, c = dflt["printer"], dflt["labelFile"], dflt["scanDossier"]

printer = StringVar(value=a)
label_file = StringVar(value=b)
scan_dossier = StringVar(value=c)

def to_print() -> bool:
    if os.path.exists(label_file.get() + ".tmp"):
        barcode_path = pathlib.Path(label_file.get() + ".tmp")
        printer_com = Dispatch("Dymo.DymoAddIn")
        printer_com.SelectPrinter(printer.get())
        printer_com.Open(barcode_path)
        printer_com.StartPrintJob()
        printer_com.Print(1, False)
        printer_com.EndPrintJob()
        return True
    else:
        return False

def create_label_temp(code:str):
    tmp_file = open(label_file.get(), "r", encoding="latin-1").read()
    s = tmp_file.index(config["config"]["startTextBalise"])
    e = tmp_file.index(config["config"]["endTextBalise"], s) + len(config["config"]["endTextBalise"])
    tmp_file = tmp_file.replace(tmp_file[s:e], config["config"]["startTextBalise"] + code + config["config"]["endTextBalise"])
    open(label_file.get() + ".tmp", "w", encoding="latin-1").write(tmp_file)

def check_dir():
    while app_started:
        while app_started:
            if os.path.exists(scan_dossier.get()):
                break 
            time.sleep(0.5)

        for file in os.listdir(scan_dossier.get()):
            file = os.path.join(scan_dossier.get(), file)
            if os.path.isfile(file) and file.lower().endswith(config["config"]["searchExtention"]):
                code = os.path.basename(file).split('/')[-1].split("_")[0]
                create_label_temp(code)
                printed = to_print()
                if printed:
                    os.remove(file)
                    os.remove(label_file.get() + ".tmp")
        time.sleep(0.5)

def close(icon, item):
    global app_started
    app_started = False
    os.kill(os.getppid(), signal.SIGTERM)
    os.kill(os.getpid(), signal.SIGTERM)
    root.destroy()
    icon.stop()
    exit()

def show_window(icon, item):
   icon.stop()
   root.deiconify()
   root.attributes("-topmost", True)
   root.attributes("-topmost", False)

def save():
    root.iconify()
    v = [printer.get(), label_file.get(), scan_dossier.get()]
    pickle.dump(v, open(config_file, "wb"))
    root.withdraw()
    image = Image.open(os.path.join(os.path.dirname(__file__), "images", "icon.png"))
    menu = (item('Paramètre', show_window), item('Quit', close))
    tray_icon = pystray.Icon("DymoPY", image, "DymoPY", menu)
    Thread(target=lambda: tray_icon.run()).start()

Canvas(root, width=10, height=10).grid(row=0, column=0)
Canvas(root, width=10, height=10).grid(row=6, column=6)
Label(root, text="Scan Dossier : ").grid(row=1, column=1, sticky="w")
Entry(root, textvariable=scan_dossier, width=config["gui"]["sizeEntryPath"]).grid(row=1, column=2, columnspan=1, sticky="w", pady=10)
Label(root, text="Fichier Label : ").grid(row=2, column=1, sticky="w")
Entry(root, textvariable=label_file, width=config["gui"]["sizeEntryPath"]).grid(row=2, column=2, columnspan=1, sticky="w", pady=10)
Label(root, text="Étiqueteuse : ").grid(row=3, column=1, sticky="w")
Entry(root, textvariable=printer, width=config["gui"]["sizeEntryPath"]).grid(row=3, column=2, columnspan=1, sticky="w", pady=10)

Thread(target=check_dir).start()
root.protocol("WM_DELETE_WINDOW", save)
save()
root.mainloop()
