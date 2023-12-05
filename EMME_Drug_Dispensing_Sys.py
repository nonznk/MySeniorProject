# EMME Drug Dispensing System
# for final project conbine GUI & Serial Communication

import tkinter as tk
from tkinter import *
from tkinter import ttk
import PIL, time, serial
from PIL import ImageTk, Image

root = tk.Tk()
root.title("EMME Drug Dispensing System")  # title app
root.iconbitmap(r"D:/Final Project/Main System/eMME_logo.ico")


# FullScreen
class FullScreenApp(object):
    def __init__(self, master, **kwargs):
        self.master = master
        pad = 3
        self._geom = "200x200+0+0"
        master.geometry(
            "{0}x{1}+0+0".format(
                master.winfo_screenwidth() - pad, master.winfo_screenheight() - pad
            )
        )
        master.bind("<Escape>", self.toggle_geom)

    def toggle_geom(self, event):
        geom = self.master.winfo_geometry()
        print(geom, self._geom)
        self.master.geometry(self._geom)
        self._geom = geom


app = FullScreenApp(root)

ser = serial.Serial(
    port="COM4",
    baudrate=9600,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS,
    timeout=1,
)

### List of Dropdown menus
machine_options = ["Machine 01"]  # Show on Machine Number
quality_options = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]  # Show on Quality

### Parameter for Change State
yd_m = "Please Select Machine"
drug = "N/A"
yd_q = "Please Select Quality"

# parameter for num of each drug
num_para325 = 10
num_para500 = 10
num_chl = 10
num_ca = 10

num_am = 10
num_tf = 10
num_ax = 10
num_so = 10

num_po = 10
num_do = 10
num_al = 10
num_no = 10

num_se = 10
num_bd = 10
num_na = 10
num_go = 10


########## Additional each drug ##########
def check_Drug():
    global num_D
    if drug == "Paracetamol 325mg":
        num_D = "01"
        ch.config(text="Paracetamol 325mg", fg="blue")
        print("Drug Serial: " + num_D)
        print("WANTED Paracetamol 325mg")
    elif drug == "Paracetamol 500mg":
        num_D = "02"
        ch.config(text="Paracetamol 500mg", fg="blue")
        print("Drug Serial: " + num_D)
        print("WANTED Paracetamol 500mg")
    elif drug == "Chlorpheniramine":
        num_D = "03"
        ch.config(text="Chlorpheniramine", fg="blue")
        print("Drug Serial: " + num_D)
        print("WANTED Chlorpheniramine")
    elif drug == "CA-R-BON":
        num_D = "04"
        ch.config(text="CA-R-BON", fg="blue")
        print("Drug Serial: " + num_D)
        print("WANTED CA-R-BON")
    elif drug == "Amoxicillin":
        num_D = "05"
        ch.config(text="Amoxicillin", fg="blue")
        print("Drug Serial: " + num_D)
        print("WANTED Amoxicillin")
    elif drug == "TIFFY DEY":
        num_D = "06"
        ch.config(text="TIFFY DEY", fg="blue")
        print("Drug Serial: " + num_D)
        print("WANTED TIFFY DEY")
    elif drug == "Air-X":
        num_D = "07"
        ch.config(text="Air-X", fg="blue")
        print("Drug Serial: " + num_D)
        print("WANTED Air-X")
    elif drug == "Solmax":
        num_D = "08"
        ch.config(text="Solmax", fg="blue")
        print("Drug Serial: " + num_D)
        print("WANTED Solmax")
    elif drug == "Ponstan 500":
        num_D = "09"
        ch.config(text="Ponstan 500", fg="blue")
        print("Drug Serial: " + num_D)
        print("WANTED Ponstan 500")
    elif drug == "Domperidone":
        num_D = "10"
        ch.config(text="Domperidone", fg="blue")
        print("Drug Serial: " + num_D)
        print("WANTED Domperidone")
    elif drug == "Allernix":
        num_D = "11"
        ch.config(text="Allernix", fg="blue")
        print("Drug Serial: " + num_D)
        print("WANTED Allernix")
    elif drug == "Norgesic":
        num_D = "12"
        ch.config(text="Norgesic", fg="blue")
        print("Drug Serial: " + num_D)
        print("WANTED Norgesic")
    elif drug == "Senokot":
        num_D = "13"
        ch.config(text="Senokot", fg="blue")
        print("Drug Serial: " + num_D)
        print("WANTED Senokot")
    elif drug == "Benda 500":
        num_D = "14"
        ch.config(text="Benda 500 ", fg="blue")
        print("Drug Serial: " + num_D)
        print("WANTED Benda 500")
    elif drug == "NAVAMED":
        num_D = "15"
        ch.config(text="NAVAMED", fg="blue")
        print("Drug Serial: " + num_D)
        print("WANTED NAVAMED")
    elif drug == "GOFEN 400":
        num_D = "16"
        ch.config(text="GOFEN 400", fg="blue")
        print("Drug Serial: " + num_D)
        print("WANTED GOFEN 400")


########## Function of buttons ##########
def button_Paracetamol325mg():
    global drug
    drug = "Paracetamol 325mg"
    check_Drug()


def button_Paracetamol500mg():
    global drug
    drug = "Paracetamol 500mg"
    check_Drug()


def button_Chlorpheniramine():
    global drug
    drug = "Chlorpheniramine"
    check_Drug()


def button_CARBON():
    global drug
    drug = "CA-R-BON"
    check_Drug()


def button_Amoxicillin():
    global drug
    drug = "Amoxicillin"
    check_Drug()


def button_TIFFY_DEY():
    global drug
    drug = "TIFFY DEY"
    check_Drug()


def button_Air_X():
    global drug
    drug = "Air-X"
    check_Drug()


def button_Solmax():
    global drug
    drug = "Solmax"
    check_Drug()


def button_Ponstan500():
    global drug
    drug = "Ponstan 500"
    check_Drug()


def button_Domperidone():
    global drug
    drug = "Domperidone"
    check_Drug()


def button_Allernix():
    global drug
    drug = "Allernix"
    check_Drug()


def button_Norgesic():
    global drug
    drug = "Norgesic"
    check_Drug()


def button_Senokot():
    global drug
    drug = "Senokot"
    check_Drug()


def button_Benda500():
    global drug
    drug = "Benda 500"
    check_Drug()


def button_NAVAMED():
    global drug
    drug = "NAVAMED"
    check_Drug()


def button_GOFEN400():
    global drug
    drug = "GOFEN 400"
    check_Drug()


def click_machine(event):
    global yd_m
    machine.config(text=machine_op.get(), fg="blue")
    yd_m = machine_op.get()
    yd_m = str(yd_m)
    print(yd_m)


def click_qty(event):
    global yd_q
    qty.config(text=qty_op.get(), fg="blue")
    yd_q = qty_op.get()
    yd_q = str(yd_q)
    print("Qty: " + str(yd_q))
    if (
        yd_m != "Please Select Machine"
        and drug != "N/A"
        and yd_q != "Please Select Quality"
    ):
        load_button["state"] = NORMAL
    else:
        load_button["state"] = DISABLED


def loadButton():
    cyd_m.config(text=machine_op.get(), fg="blue")
    cyd_drug.config(text=drug, fg="blue")
    cyd_qty.config(text=qty_op.get(), fg="blue")
    check_button["state"] = NORMAL


def ok_button():
    print("OK")
    start_button["state"] = NORMAL

    # part update quality
    if drug == "Paracetamol 325mg":
        global num_para325
        if num_para325 > 0:
            num_para325 = int(num_para325) - int(yd_q)
            para325.config(text=num_para325, fg="blue")
            # print(num_para325)
        else:
            para325.config(text="N/A", fg="blue")
            # print("N/A")
    elif drug == "Paracetamol 500mg":
        global num_para500
        if num_para500 > 0:
            num_para500 = int(num_para500) - int(yd_q)
            para500.config(text=num_para500, fg="blue")
            # print(num_para500)
        else:
            para500.config(text="N/A", fg="blue")
            # print("N/A")
    elif drug == "Chlorpheniramine":
        global num_chl
        if num_chl > 0:
            num_chl = int(num_chl) - int(yd_q)
            chl.config(text=num_chl, fg="blue")
            # print(chl)
        else:
            chl.config(text="N/A", fg="blue")
            # print("N/A")
    elif drug == "CA-R-BON":
        global num_ca
        if num_ca > 0:
            num_ca = int(num_ca) - int(yd_q)
            ca.config(text=num_ca, fg="blue")
            # print(ca)
        else:
            ca.config(text="N/A", fg="blue")
            # print("N/A")
    elif drug == "Amoxicillin":
        global num_am
        if num_am > 0:
            num_am = int(num_am) - int(yd_q)
            am.config(text=num_am, fg="blue")
            # print(am)
        else:
            am.config(text="N/A", fg="blue")
            # print("N/A")
    elif drug == "TIFFY DEY":
        global num_tf
        if num_tf > 0:
            num_tf = int(num_tf) - int(yd_q)
            tf.config(text=num_tf, fg="blue")
            # print(tf)
        else:
            tf.config(text="N/A", fg="blue")
            # print("N/A")
    elif drug == "Air-X":
        global num_ax
        if num_ax > 0:
            num_ax = int(num_ax) - int(yd_q)
            ax.config(text=num_ax, fg="blue")
            # print(ax)
        else:
            ax.config(text="N/A", fg="blue")
            # print("N/A")
    elif drug == "Solmax":
        global num_so
        if num_so > 0:
            num_so = int(num_so) - int(yd_q)
            so.config(text=num_so, fg="blue")
            # print(so)
        else:
            so.config(text="N/A", fg="blue")
            # print("N/A")
    elif drug == "Ponstan 500":
        global num_po
        if num_po > 0:
            num_po = int(num_po) - int(yd_q)
            po.config(text=num_po, fg="blue")
            # print(po)
        else:
            po.config(text="N/A", fg="blue")
            # print("N/A")
    elif drug == "Domperidone":
        global num_do
        if num_do > 0:
            num_do = int(num_do) - int(yd_q)
            do.config(text=num_do, fg="blue")
            # print(do)
        else:
            do.config(text="N/A", fg="blue")
            # print("N/A")
    elif drug == "Allernix":
        global num_al
        if num_al > 0:
            num_al = int(num_al) - int(yd_q)
            al.config(text=num_al, fg="blue")
            # print(al)
        else:
            al.config(text="N/A", fg="blue")
            # print("N/A")
    elif drug == "Norgesic":
        global num_no
        if num_no > 0:
            num_no = int(num_no) - int(yd_q)
            no.config(text=num_no, fg="blue")
            # print(no)
        else:
            no.config(text="N/A", fg="blue")
            # print("N/A")
    elif drug == "Senokot":
        global num_se
        if num_se > 0:
            num_se = int(num_se) - int(yd_q)
            se.config(text=num_se, fg="blue")
            # print(se)
        else:
            se.config(text="N/A", fg="blue")
            # print("N/A")
    elif drug == "Benda 500":
        global num_bd
        if num_bd > 0:
            num_bd = int(num_bd) - int(yd_q)
            bd.config(text=num_bd, fg="blue")
            # print(bd)
        else:
            bd.config(text="N/A", fg="blue")
            # print("N/A")
    elif drug == "NAVAMED":
        global num_na
        if num_na > 0:
            num_na = int(num_na) - int(yd_q)
            na.config(text=num_na, fg="blue")
            # print(na)
        else:
            na.config(text="N/A", fg="blue")
            # print("N/A")
    elif drug == "GOFEN 400":
        global num_go
        if num_go > 0:
            num_go = int(num_go) - int(yd_q)
            go.config(text=num_go, fg="blue")
            # print(go)
        else:
            go.config(text="N/A", fg="blue")
            # print("N/A")


def sendSerial():
    # myCode = input("Please input your code: ")
    # myCode = int(Serial_code)
    myCode = Serial_code
    print(myCode, type(myCode))
    ser.write(myCode.encode())
    start_button["state"] = DISABLED


def start_button():
    """
    My Code to real use:
    Ctl M/C: 001 (3-Bits) Dec
    CH: 01-16 (2-Bit) Dec
    QTY: 00-10 (2-Bits) Dec
    Ender: 1 (Stop bit)

    Ctl M/C | CH | QTY | Ender
    M/C = num_M
    CH = num_D
    QTY = num_Q
    Ender = 1
    """
    print("Start")  # For check button is work

    # Machine
    if yd_m == "Machine 01":
        num_M = "001"
    print("Checking Machine: " + num_M)

    # Drug
    print("Checking Drug: " + num_D)

    # QTY
    if yd_q == "1":
        num_Q = "01"
    elif yd_q == "2":
        num_Q = "02"
    elif yd_q == "3":
        num_Q = "03"
    elif yd_q == "4":
        num_Q = "04"
    elif yd_q == "5":
        num_Q = "05"
    elif yd_q == "6":
        num_Q = "06"
    elif yd_q == "7":
        num_Q = "07"
    elif yd_q == "8":
        num_Q = "08"
    elif yd_q == "9":
        num_Q = "09"
    elif yd_q == "10":
        num_Q = "10"
    print("Checking QTY: " + num_Q)

    Ender = "1"

    global Serial_code
    Serial_code = num_M + num_D + num_Q + Ender
    print("Serial Code: " + Serial_code, type(Serial_code))
    number = len(Serial_code)
    print("Number of Serial code: " + str(number))

    ## Reset in frame_status and frame_show_qty
    # frame_status
    machine.config(text="Please Select Machine", fg="red")
    ch.config(text="N/A", fg="red")
    qty.config(text="Please Select Quality", fg="red")
    qty_op.set(quality_options[0])
    load_button["state"] = DISABLED
    # frame_show_qty
    cyd_m.config(text="N/A", fg="red")
    cyd_drug.config(text="N/A", fg="red")
    cyd_qty.config(text="N/A", fg="red")
    check_button["state"] = DISABLED

    # Send Serial
    sendSerial()


### Main Frame
main_frame = tk.LabelFrame(root, padx=5, pady=5)
main_frame.pack()  # .grid() default value is zero (row=0, column=0)

### Frame Drug order
frame_drug = tk.LabelFrame(main_frame, text="Drug Order", padx=10, pady=10)
frame_drug.grid(row=0, column=0, rowspan=4, columnspan=4)  #  rowspan=4, columnspan=4

########## Drug List ##########
""" Paracetamol 325mg
Paracetamol 500mg
Chlorpheniramine
CARBON
Amoxicillin
TIFFY DEY
AirX, Air-x (Simethicone)
Solmax
Ponstan500
Domperidone
Allernix
Norgesic
Senokot
Benda500
NAVAMED
GOFEN400 """

### Paracetamol_325mg
# Import Image on a botton
paracetamol325mg = Image.open(r"D:/Final Project/Main System/paracetamol325mg.png")
# Resize pictures
paracetamol325mg = paracetamol325mg.resize((100, 100), Image.ANTIALIAS)
reset_paracetamol325mg = ImageTk.PhotoImage(paracetamol325mg)
# Define Buttons
button_Paracetamol_325mg = tk.Button(
    frame_drug,
    text="Paracetamol 325mg",
    image=reset_paracetamol325mg,
    padx=19,
    pady=5,
    compound=BOTTOM,
    command=button_Paracetamol325mg,
)

### Paracetamol_500mg
# Import Image on a botton
paracetamol500mg = Image.open(r"D:/Final Project/Main System/paracetamol500mg.png")
# Resize pictures
paracetamol500mg = paracetamol500mg.resize((100, 100), Image.ANTIALIAS)
reset_paracetamol500mg = ImageTk.PhotoImage(paracetamol500mg)
# Define Buttons
button_Paracetamol_500mg = tk.Button(
    frame_drug,
    text="Paracetamol 500mg",
    image=reset_paracetamol500mg,
    padx=20,
    pady=5,
    compound=BOTTOM,
    command=button_Paracetamol500mg,
)

### Chlorpheniramine
chlorpheniramine = Image.open(r"D:/Final Project/Main System/chlorpheniramine.png")
# Resize pictures
chlorpheniramine = chlorpheniramine.resize((100, 100), Image.ANTIALIAS)
reset_chlorpheniramine = ImageTk.PhotoImage(chlorpheniramine)
# Define Buttons
button_Chlorpheniramine = tk.Button(
    frame_drug,
    text="Chlorpheniramine",
    image=reset_chlorpheniramine,
    padx=20,
    pady=5,
    compound=BOTTOM,
    command=button_Chlorpheniramine,
)

### CARBON
CARBON = Image.open(r"D:/Final Project/Main System/CARBON.png")
# Resize pictures
CARBON = CARBON.resize((100, 100), Image.ANTIALIAS)
reset_CARBON = ImageTk.PhotoImage(CARBON)
# Define Buttons
button_CARBON = tk.Button(
    frame_drug,
    text="CA-R-BON",
    image=reset_CARBON,
    padx=20,
    pady=5,
    compound=BOTTOM,
    command=button_CARBON,
)

### Amoxicillin
amoxicillin = Image.open(r"D:/Final Project/Main System/amoxicillin.png")
# Resize pictures
amoxicillin = amoxicillin.resize((100, 100), Image.ANTIALIAS)
reset_amoxicillin = ImageTk.PhotoImage(amoxicillin)
# Define Buttons
button_Amoxicillin = tk.Button(
    frame_drug,
    text="Amoxicillin",
    image=reset_amoxicillin,
    padx=22,
    pady=5,
    compound=BOTTOM,
    command=button_Amoxicillin,
)

### TIFFY DEY
TIFFY_DEY = Image.open(r"D:/Final Project/Main System/TIFFY DEY.png")
# Resize pictures
TIFFY_DEY = TIFFY_DEY.resize((100, 100), Image.ANTIALIAS)
reset_TIFFY_DEY = ImageTk.PhotoImage(TIFFY_DEY)
# Define Buttons
button_TIFFY_DEY = tk.Button(
    frame_drug,
    text="TIFFY DEY",
    image=reset_TIFFY_DEY,
    padx=22,
    pady=5,
    compound=BOTTOM,
    command=button_TIFFY_DEY,
)

### Air-x
airX = Image.open(r"D:/Final Project/Main System/Air-x.png")
# Resize pictures
airX = airX.resize((100, 100), Image.ANTIALIAS)
reset_airX = ImageTk.PhotoImage(airX)
# Define Buttons
button_Air_X = tk.Button(
    frame_drug,
    text="Air-X",
    image=reset_airX,
    padx=20,
    pady=5,
    compound=BOTTOM,
    command=button_Air_X,
)

### Solmax
Solmax = Image.open(r"D:/Final Project/Main System/Solmax.png")
# Resize pictures
Solmax = Solmax.resize((100, 100), Image.ANTIALIAS)
reset_Solmax = ImageTk.PhotoImage(Solmax)
# Define Buttons
button_Solmax = tk.Button(
    frame_drug,
    text="Solmax",
    image=reset_Solmax,
    padx=20,
    pady=5,
    compound=BOTTOM,
    command=button_Solmax,
)

### Ponstan500
Ponstan500 = Image.open(r"D:/Final Project/Main System/Ponstan500.png")
# Resize pictures
Ponstan500 = Ponstan500.resize((100, 100), Image.ANTIALIAS)
reset_Ponstan500 = ImageTk.PhotoImage(Ponstan500)
# Define Buttons
button_Ponstan500 = tk.Button(
    frame_drug,
    text="Ponstan 500",
    image=reset_Ponstan500,
    padx=22,
    pady=5,
    compound=BOTTOM,
    command=button_Ponstan500,
)

### Domperidone
Domperidone = Image.open(r"D:/Final Project/Main System/Domperidone.png")
# Resize pictures
Domperidone = Domperidone.resize((100, 100), Image.ANTIALIAS)
reset_Domperidone = ImageTk.PhotoImage(Domperidone)
# Define Buttons
button_Domperidone = tk.Button(
    frame_drug,
    text="Domperidone",
    image=reset_Domperidone,
    padx=22,
    pady=5,
    compound=BOTTOM,
    command=button_Domperidone,
)

### Allernix
Allernix = Image.open(r"D:/Final Project/Main System/Allernix.png")
# Resize pictures
Allernix = Allernix.resize((100, 100), Image.ANTIALIAS)
reset_Allernix = ImageTk.PhotoImage(Allernix)
# Define Buttons
button_Allernix = tk.Button(
    frame_drug,
    text="Allernix",
    image=reset_Allernix,
    padx=20,
    pady=5,
    compound=BOTTOM,
    command=button_Allernix,
)

### Norgesic
Norgesic = Image.open(r"D:/Final Project/Main System/Norgesic.png")
# Resize pictures
Norgesic = Norgesic.resize((100, 100), Image.ANTIALIAS)
reset_Norgesic = ImageTk.PhotoImage(Norgesic)
# Define Buttons
button_Norgesic = tk.Button(
    frame_drug,
    text="Norgesic",
    image=reset_Norgesic,
    padx=20,
    pady=5,
    compound=BOTTOM,
    command=button_Norgesic,
)

### Senokot
Senokot = Image.open(r"D:/Final Project/Main System/Senokot.png")
# Resize pictures
Senokot = Senokot.resize((55, 100), Image.ANTIALIAS)
reset_Senokot = ImageTk.PhotoImage(Senokot)
# Define Buttons
button_Senokot = tk.Button(
    frame_drug,
    text="Senokot",
    image=reset_Senokot,
    padx=45,
    pady=5,
    compound=BOTTOM,
    command=button_Senokot,
)

### Benda500
Benda500 = Image.open(r"D:/Final Project/Main System/Benda500.png")
# Resize pictures
Benda500 = Benda500.resize((100, 100), Image.ANTIALIAS)
reset_Benda500 = ImageTk.PhotoImage(Benda500)
# Define Buttons
button_Benda500 = tk.Button(
    frame_drug,
    text="Benda 500",
    image=reset_Benda500,
    padx=22,
    pady=5,
    compound=BOTTOM,
    command=button_Benda500,
)

### NAVAMED
NAVAMED = Image.open(r"D:/Final Project/Main System/NAVAMED.png")
# Resize pictures
NAVAMED = NAVAMED.resize((100, 100), Image.ANTIALIAS)
reset_NAVAMED = ImageTk.PhotoImage(NAVAMED)
# Define Buttons
button_NAVAMED = tk.Button(
    frame_drug,
    text="NAVAMED",
    image=reset_NAVAMED,
    padx=20,
    pady=5,
    compound=BOTTOM,
    command=button_NAVAMED,
)

### GOFEN400
GOFEN400 = Image.open(r"D:/Final Project/Main System/GOFEN400.png")
# Resize pictures
GOFEN400 = GOFEN400.resize((100, 100), Image.ANTIALIAS)
reset_GOFEN400 = ImageTk.PhotoImage(GOFEN400)
# Define Buttons
button_GOFEN400 = tk.Button(
    frame_drug,
    text="GOFEN 400",
    image=reset_GOFEN400,
    padx=20,
    pady=5,
    compound=BOTTOM,
    command=button_GOFEN400,
)

# Put the buttons on the screen
button_Paracetamol_325mg.grid(row=0, column=0)
button_Paracetamol_500mg.grid(row=0, column=1)
button_Chlorpheniramine.grid(row=0, column=2)
button_CARBON.grid(row=0, column=3)

button_Amoxicillin.grid(row=1, column=0)
button_TIFFY_DEY.grid(row=1, column=1)
button_Air_X.grid(row=1, column=2)
button_Solmax.grid(row=1, column=3)

button_Ponstan500.grid(row=2, column=0)
button_Domperidone.grid(row=2, column=1)
button_Allernix.grid(row=2, column=2)
button_Norgesic.grid(row=2, column=3)

button_Senokot.grid(row=3, column=0)
button_Benda500.grid(row=3, column=1)
button_NAVAMED.grid(row=3, column=2)
button_GOFEN400.grid(row=3, column=3)

########## Drug remaining ##########
frame_remain = tk.LabelFrame(main_frame, text="Drug Remaining", padx=10, pady=10)

### show pic each drug
# paracetamol325mg
frame_paracetamol325mg = tk.LabelFrame(frame_remain, padx=5)
paracetamol325mg_remain = paracetamol325mg.resize((70, 70), Image.ANTIALIAS)
reset_paracetamol325mg_remain = ImageTk.PhotoImage(paracetamol325mg_remain)
pic_reset_paracetamol325mg_remain = tk.Label(
    frame_paracetamol325mg,
    image=reset_paracetamol325mg_remain,
    text="Paracetamol 325mg remain",
    compound=BOTTOM,
    pady=5,
)
para325 = tk.Label(
    frame_paracetamol325mg, text=num_para325, font=("Helvetica", 10), fg="blue"
)

# paracetamol500mg
frame_paracetamol500mg = tk.LabelFrame(frame_remain, padx=5)
paracetamol500mg_remain = paracetamol500mg.resize((70, 70), Image.ANTIALIAS)
reset_paracetamol500mg_remain = ImageTk.PhotoImage(paracetamol500mg_remain)
pic_reset_paracetamol500mg_remain = tk.Label(
    frame_paracetamol500mg,
    image=reset_paracetamol500mg_remain,
    text="Paracetamol 500mg remain",
    compound=BOTTOM,
    pady=5,
)
para500 = tk.Label(
    frame_paracetamol500mg, text=num_para500, font=("Helvetica", 10), fg="blue"
)

# Chlorpheniramine
frame_chlorpheniramine = tk.LabelFrame(frame_remain, padx=10)
chlorpheniramine_remain = chlorpheniramine.resize((70, 70), Image.ANTIALIAS)
reset_chlorpheniramine_remain = ImageTk.PhotoImage(chlorpheniramine_remain)
pic_reset_chlorpheniramine_remain = tk.Label(
    frame_chlorpheniramine,
    image=reset_chlorpheniramine_remain,
    text="Chlorpheniramine remain",
    compound=BOTTOM,
    pady=5,
)
chl = tk.Label(frame_chlorpheniramine, text=num_chl, font=("Helvetica", 10), fg="blue")

# CARBON
frame_CARBON = tk.LabelFrame(frame_remain, padx=29)
CARBON_remain = CARBON.resize((70, 70), Image.ANTIALIAS)
reset_CARBON_remain = ImageTk.PhotoImage(CARBON_remain)
pic_reset_CARBON_remain = tk.Label(
    frame_CARBON,
    image=reset_CARBON_remain,
    text="CA-R-BON remain",
    compound=BOTTOM,
    pady=5,
)
ca = tk.Label(frame_CARBON, text=num_ca, font=("Helvetica", 10), fg="blue")

# Amoxicillin
frame_amoxicillin = tk.LabelFrame(frame_remain, padx=28)
amoxicillin_remain = amoxicillin.resize((70, 70), Image.ANTIALIAS)
reset_amoxicillin_remain = ImageTk.PhotoImage(amoxicillin_remain)
pic_reset_amoxicillin_remain = tk.Label(
    frame_amoxicillin,
    image=reset_amoxicillin_remain,
    text="Amoxicillin remain",
    compound=BOTTOM,
    pady=5,
)
am = tk.Label(frame_amoxicillin, text=num_am, font=("Helvetica", 10), fg="blue")

# TIFFY DEY
frame_TIFFY_DEY = tk.LabelFrame(frame_remain, padx=31)
TIFFY_DEY_remain = TIFFY_DEY.resize((70, 70), Image.ANTIALIAS)
reset_TIFFY_DEY_remain = ImageTk.PhotoImage(TIFFY_DEY_remain)
pic_reset_TIFFY_DEY_remain = tk.Label(
    frame_TIFFY_DEY,
    image=reset_TIFFY_DEY_remain,
    text="TIFFY DEY remain",
    compound=BOTTOM,
    pady=5,
)
tf = tk.Label(frame_TIFFY_DEY, text=num_tf, font=("Helvetica", 10), fg="blue")

# Air-X
frame_airX = tk.LabelFrame(frame_remain, padx=43)
airX_remain = airX.resize((70, 70), Image.ANTIALIAS)
reset_airX_remain = ImageTk.PhotoImage(airX_remain)
pic_reset_airX_remain = tk.Label(
    frame_airX, image=reset_airX_remain, text="Air-X remain", compound=BOTTOM, pady=5
)
ax = tk.Label(frame_airX, text=num_ax, font=("Helvetica", 10), fg="blue")

# Solmax
frame_Solmax = tk.LabelFrame(frame_remain, padx=38)
Solmax_remain = Solmax.resize((70, 70), Image.ANTIALIAS)
reset_Solmax_remain = ImageTk.PhotoImage(Solmax_remain)
pic_reset_Solmax_remain = tk.Label(
    frame_Solmax,
    image=reset_Solmax_remain,
    text="Solmax remain",
    compound=BOTTOM,
    pady=5,
)
so = tk.Label(frame_Solmax, text=num_so, font=("Helvetica", 10), fg="blue")

# Ponstan500
frame_Ponstan500 = tk.LabelFrame(frame_remain, padx=26)
Ponstan500_remain = Ponstan500.resize((70, 70), Image.ANTIALIAS)
reset_Ponstan500_remain = ImageTk.PhotoImage(Ponstan500_remain)
pic_reset_Ponstan500_remain = tk.Label(
    frame_Ponstan500,
    image=reset_Ponstan500_remain,
    text="Ponstan 500 remain",
    compound=BOTTOM,
    pady=5,
)
po = tk.Label(frame_Ponstan500, text=num_po, font=("Helvetica", 10), fg="blue")

# Domperidone
frame_Domperidone = tk.LabelFrame(frame_remain, padx=21)
Domperidone_remain = Domperidone.resize((70, 70), Image.ANTIALIAS)
reset_Domperidone_remain = ImageTk.PhotoImage(Domperidone_remain)
pic_reset_Domperidone_remain = tk.Label(
    frame_Domperidone,
    image=reset_Domperidone_remain,
    text="Domperidone remain",
    compound=BOTTOM,
    pady=5,
)
do = tk.Label(frame_Domperidone, text=num_do, font=("Helvetica", 10), fg="blue")

# Allernix
frame_Allernix = tk.LabelFrame(frame_remain, padx=38)
Allernix_remain = Allernix.resize((70, 70), Image.ANTIALIAS)
reset_Allernix_remain = ImageTk.PhotoImage(Allernix_remain)
pic_reset_Allernix_remain = tk.Label(
    frame_Allernix,
    image=reset_Allernix_remain,
    text="Allernix remain",
    compound=BOTTOM,
    pady=5,
)
al = tk.Label(frame_Allernix, text=num_al, font=("Helvetica", 10), fg="blue")

# Norgesic
frame_Norgesic = tk.LabelFrame(frame_remain, padx=34)
Norgesic_remain = Norgesic.resize((70, 70), Image.ANTIALIAS)
reset_Norgesic_remain = ImageTk.PhotoImage(Norgesic_remain)
pic_reset_Norgesic_remain = tk.Label(
    frame_Norgesic,
    image=reset_Norgesic_remain,
    text="Norgesic remain",
    compound=BOTTOM,
    pady=5,
)
no = tk.Label(frame_Norgesic, text=num_no, font=("Helvetica", 10), fg="blue")

# Senokot
frame_Senokot = tk.LabelFrame(frame_remain, padx=36)
Senokot_remain = Senokot.resize((39, 70), Image.ANTIALIAS)
reset_Senokot_remain = ImageTk.PhotoImage(Senokot_remain)
pic_reset_Senokot_remain = tk.Label(
    frame_Senokot,
    image=reset_Senokot_remain,
    text="Senokot remain",
    compound=BOTTOM,
    pady=5,
)
se = tk.Label(frame_Senokot, text=num_se, font=("Helvetica", 10), fg="blue")

# Benda500
frame_Benda500 = tk.LabelFrame(frame_remain, padx=30)
Benda500_remain = Benda500.resize((70, 70), Image.ANTIALIAS)
reset_Benda500_remain = ImageTk.PhotoImage(Benda500_remain)
pic_reset_Benda500_remain = tk.Label(
    frame_Benda500,
    image=reset_Benda500_remain,
    text="Benda 500 remain",
    compound=BOTTOM,
    pady=5,
)
bd = tk.Label(frame_Benda500, text=num_bd, font=("Helvetica", 10), fg="blue")

# NAVAMED
frame_NAVAMED = tk.LabelFrame(frame_remain, padx=29)
NAVAMED_remain = NAVAMED.resize((70, 70), Image.ANTIALIAS)
reset_NAVAMED_remain = ImageTk.PhotoImage(NAVAMED_remain)
pic_reset_NAVAMED_remain = tk.Label(
    frame_NAVAMED,
    image=reset_NAVAMED_remain,
    text="NAVAMED remain",
    compound=BOTTOM,
    pady=5,
)
na = tk.Label(frame_NAVAMED, text=num_na, font=("Helvetica", 10), fg="blue")

# GOFEN400
frame_GOFEN400 = tk.LabelFrame(frame_remain, padx=28)
GOFEN400_remain = GOFEN400.resize((70, 70), Image.ANTIALIAS)
reset_GOFEN400_remain = ImageTk.PhotoImage(GOFEN400_remain)
pic_reset_GOFEN400_remain = tk.Label(
    frame_GOFEN400,
    image=reset_GOFEN400_remain,
    text="GOFEN 400 remain",
    compound=BOTTOM,
    pady=5,
)
go = tk.Label(frame_GOFEN400, text=num_go, font=("Helvetica", 10), fg="blue")

### Show of Drug remaining
frame_remain.grid(row=0, column=4, rowspan=4, columnspan=4)
frame_paracetamol325mg.grid(row=0, column=0)
pic_reset_paracetamol325mg_remain.grid(row=0)
para325.grid(row=1, column=0)

frame_paracetamol500mg.grid(row=0, column=1)
pic_reset_paracetamol500mg_remain.grid(row=0)
para500.grid(row=1, column=0)

frame_chlorpheniramine.grid(row=0, column=2)
pic_reset_chlorpheniramine_remain.grid(row=0)
chl.grid(row=1, column=0)

frame_CARBON.grid(row=0, column=3)
pic_reset_CARBON_remain.grid(row=0)
ca.grid(row=1, column=0)

frame_amoxicillin.grid(row=1, column=0)
pic_reset_amoxicillin_remain.grid(row=0)
am.grid(row=1, column=0)

frame_TIFFY_DEY.grid(row=1, column=1)
pic_reset_TIFFY_DEY_remain.grid(row=0)
tf.grid(row=1, column=0)

frame_airX.grid(row=1, column=2)
pic_reset_airX_remain.grid(row=0)
ax.grid(row=1, column=0)

frame_Solmax.grid(row=1, column=3)
pic_reset_Solmax_remain.grid(row=0)
so.grid(row=1, column=0)

frame_Ponstan500.grid(row=2, column=0)
pic_reset_Ponstan500_remain.grid(row=0)
po.grid(row=1, column=0)

frame_Domperidone.grid(row=2, column=1)
pic_reset_Domperidone_remain.grid(row=0)
do.grid(row=1, column=0)

frame_Allernix.grid(row=2, column=2)
pic_reset_Allernix_remain.grid(row=0)
al.grid(row=1, column=0)

frame_Norgesic.grid(row=2, column=3)
pic_reset_Norgesic_remain.grid(row=0)
no.grid(row=1, column=0)

frame_Senokot.grid(row=3, column=0)
pic_reset_Senokot_remain.grid(row=0)
se.grid(row=1, column=0)

frame_Benda500.grid(row=3, column=1)
pic_reset_Benda500_remain.grid(row=0)
bd.grid(row=1, column=0)

frame_NAVAMED.grid(row=3, column=2)
pic_reset_NAVAMED_remain.grid(row=0)
na.grid(row=1, column=0)

frame_GOFEN400.grid(row=3, column=3)
pic_reset_GOFEN400_remain.grid(row=0)
go.grid(row=1, column=0)

########## Frame Status ##########
frame_status = tk.LabelFrame(main_frame, text="Drug Status", padx=30, pady=10)
frame_status.grid(row=5, column=0, columnspan=4)
# frame_status.grid(row=0, column=4, rowspan=4) # row=5, column=0, columnspan=3

# Show Status Frame in Status Frame
### frame_show_machine
frame_show_machine = tk.LabelFrame(frame_status, padx=10, pady=10)
frame_show_machine.grid(row=0, column=0)
# frame_show_machine.pack() # grid(row=0, column=0)

num_machine = tk.Label(
    frame_show_machine, text="Machine Number", font=("Helvetica", 11), padx=30, pady=10
)  # M/C
num_machine.pack()

global machine
machine = tk.Label(
    frame_show_machine,
    text="Please Select Machine",
    font=("Helvetica", 10),
    fg="red",
    pady=5,
)
machine.pack(pady=5)

machine_op = ttk.Combobox(frame_show_machine, value=machine_options)
machine_op.current(0)
machine_op.bind("<<ComboboxSelected>>", click_machine)
machine_op.pack(pady=5)

### frame_show_channel
frame_show_channel = tk.LabelFrame(frame_status, padx=10, pady=25)
frame_show_channel.grid(row=0, column=1)
# frame_show_channel.pack() # grid(row=0, column=1)

channel = tk.Label(
    frame_show_channel, text="Drug Channel", font=("Helvetica", 11), padx=30, pady=10
)  # Channel
channel.pack()

global ch
ch = tk.Label(frame_show_channel, text="N/A", font=("Helvetica", 10), fg="red", pady=5)
ch.pack(pady=5)

### frame_show_qty
frame_show_qty = tk.LabelFrame(frame_status, padx=10, pady=10)
frame_show_qty.grid(row=0, column=2)
# frame_show_qty.pack() # grid(row=0, column=2)

num_qty = tk.Label(
    frame_show_qty, text="Quality", font=("Helvetica", 11), padx=30, pady=10
)  # Quality
num_qty.pack()

global qty
qty = tk.Label(
    frame_show_qty,
    text="Please Select Quality",
    font=("Helvetica", 10),
    fg="red",
    pady=5,
)
qty.pack(pady=5)

qty_op = ttk.Combobox(frame_show_qty, value=quality_options)
qty_op.current(0)
qty_op.bind("<<ComboboxSelected>>", click_qty)
qty_op.pack(pady=5)

### Load Button
load_button = tk.Button(frame_status, text="load", padx=260, command=loadButton)
load_button.grid(row=1, columnspan=3)
# load_button.pack()
load_button["state"] = DISABLED

########## Frame Your_Drug ##########
frame_your_drug = tk.LabelFrame(main_frame, text="Your Drug", padx=10, pady=10)
frame_your_drug.grid(row=5, column=5)

your_drug = tk.Label(
    frame_your_drug,
    text="Please check your drug!",
    font=("Helvetica", 11),
    fg="red",
    padx=10,
    pady=10,
    justify="center",
)
your_drug.grid(row=0, columnspan=3)

global cyd_m
text_machine = tk.Label(
    frame_your_drug, text="Machine:", font=("Helvetica", 10)
)  # justify="left"
text_machine.grid(row=1, column=0)
cyd_m = tk.Label(frame_your_drug, text="N/A", font=("Helvetica", 10), fg="red")
cyd_m.grid(row=1, column=2)

global cyd_drug
text_drug_channel = tk.Label(frame_your_drug, text="Drug:", font=("Helvetica", 10))
text_drug_channel.grid(row=2, column=0)
cyd_drug = tk.Label(frame_your_drug, text="N/A", font=("Helvetica", 10), fg="red")
cyd_drug.grid(row=2, column=2)

global cyd_qty
text_drug_quality = tk.Label(
    frame_your_drug, text="Drug Quality:", font=("Helvetica", 10)
)
text_drug_quality.grid(row=3, column=0)
cyd_qty = tk.Label(frame_your_drug, text="N/A", font=("Helvetica", 10), fg="red")
cyd_qty.grid(row=3, column=2)

check_button = tk.Button(
    frame_your_drug,
    text="OK",
    font=("Helvetica", 10),
    borderwidth=2,
    padx=50,
    command=ok_button,
)
check_button.grid(row=4, columnspan=3)
check_button["state"] = DISABLED

########## Start Button ##########
"""
Add check state
ACTIVE when have all option
"""
start_button = tk.Button(
    main_frame,
    text="Start",
    font=("Helvetica", 16),
    borderwidth=5,
    padx=30,
    pady=50,
    command=start_button,
)
start_button.grid(row=5, column=7)
start_button["state"] = DISABLED

root.mainloop()
