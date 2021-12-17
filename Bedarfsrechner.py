# Schreibe hier Deinen Code :-)

from tkinter import *
import tkinter.font as font
from math import *


root = Tk()
root.title('Bedarfsrechner')
# root.iconbitmap('DIRECTORY')
root.geometry("480x670")  # Fenstergröße in Pixeln

r = StringVar()
r.set("1") # Defaul value

# Auswahlbuttons für Geschlecht
Radiobutton(root, text= "Männlich", variable= r, value=1).grid(pady=10, row=0, column=0)
Radiobutton(root, text= "Weiblich", variable= r, value=2).grid(padx=20, row=0,column=1)

# Label und Eingabefeld für Gewicht
weight_entry = Entry(root, width=20, borderwidth=5)
weight_label = Label(root, text= "Gewicht (kg): ")
pal_label = Label(root, text= "Aktivitätslevel: ")

weight_entry.grid(row=1, column=1)
weight_label.grid(row=1, column=0)
pal_label.grid(row=2, column=0)

#r_label=Label(root, text=r.get())
#r_label.grid(row=0, column=3)
#Dropdown für Aktivität

def show():
    myLabel = Label(root, text=clicked.get())
    myLabel.grid(row=5, column=0, )
    pal = clicked.get()


pal_options = [ # Mit einer Liste ist es einfach Elemente zu bearbeiten und hinzuzufügen, statt in der Funktion zu bleiben
    "1.1 kaum aktiv",
    "1.2 wenig aktiv ",
    "1.3 bisschen aktiv",
    "1.4 aktiv ",
    "1.5 sehr aktiv",
    "1.6 ",
    "1.7 ",
    "1.8 ",
    "1.9 ",
]
#Dropdown Menü für PAL
global clicked

clicked = StringVar()
clicked.set(pal_options[2]) # 2 default
drop = OptionMenu(root, clicked, *pal_options ) # No default
drop.grid(row=2, column=1)

#button für PAL berechnen
def pal_berechnen():
    top = Toplevel()
    top.geometry("650x300")
    top.title('PAL berechnen')
    #label PAL schlafen, PAL arbeit, PAL Freizeit, Aktivität in stunden, PAL
    frame_pal_toplevel = LabelFrame(top, text="Bitte PAL einstellen")
    frame_pal_toplevel.grid(padx=20, pady=10, columnspan=3)

    label_schlafen = Label(frame_pal_toplevel, text="PAL Schlafen: ")
    label_schlafen.grid(row=2, column=0)
    label_arbeit = Label(frame_pal_toplevel, text="PAL Arbeit: ")
    label_arbeit.grid(row=3, column=0)
    label_freizeit = Label(frame_pal_toplevel, text="PAL Freizeit: ")
    label_freizeit.grid(row=4, column=0)
    label_pal = Label(frame_pal_toplevel, text="PAL")
    label_pal.grid(row=0, column=2)
    label_stunden = Label(frame_pal_toplevel, text= "Aktivität in Stunden")
    label_stunden.grid(row=0, column=3)
    
    #Scale PAL
    schlafen_scale = Scale(frame_pal_toplevel, from_=1, to=12, orient=HORIZONTAL, length=300, resolution=1, )
    arbeit_scale = Scale(frame_pal_toplevel, from_=1, to=12, orient=HORIZONTAL, length=300, resolution=1,  )
    freizeit_scale = Scale(frame_pal_toplevel, from_=1, to=12, orient=HORIZONTAL, length=300, resolution=1,  )
    
    freizeit_scale.grid(row=4, column=3)
    arbeit_scale.grid(row=3, column=3)
    schlafen_scale.grid(row=2, column=3)
    
    
    freizeit_scale.set(8)
    schlafen_scale.set(8)
    arbeit_scale.set(8)
    
    #schlafen_drop = OptionMenu(top, clicked, *pal_options ) # No default
    #drop.grid(row=2, column=1)
    
    pal_arbeit_clicked = StringVar(frame_pal_toplevel)
    pal_freizeit_clicked = StringVar(frame_pal_toplevel)
    pal_arbeit_clicked.set(pal_options[2])
    pal_freizeit_clicked.set(pal_options[3])
    
    arbeit_drop = OptionMenu(frame_pal_toplevel, pal_arbeit_clicked, *pal_options ) # No default
    arbeit_drop.grid(padx=30, row=3, column=2)
    schlafen_drop_label = Label(frame_pal_toplevel, text="0.95")
    schlafen_drop_label.grid(row=2, column=2)
    freizeit_drop = OptionMenu(frame_pal_toplevel, pal_freizeit_clicked, *pal_options ) # No default
    freizeit_drop.grid(row=4, column=2)
    
    """
    
    """
    def ergebnis_pal():
        arbeit_std = arbeit_scale.get()
        schlafen_std = schlafen_scale.get()
        freizeit_std = freizeit_scale.get()
        stunden = int(arbeit_std) + int(schlafen_std) + int(freizeit_std)
        
        if stunden == 24:     
            ergebnis_pal_arbeit = pal_arbeit_clicked.get()
            ergebnis_pal_arbeit = ergebnis_pal_arbeit[0:3]
            ergebnis_pal_freizeit = pal_freizeit_clicked.get()
            ergebnis_pal_freizeit = ergebnis_pal_freizeit[0:3]
            arbeit_std = arbeit_scale.get()
            schlafen_std = schlafen_scale.get()
            freizeit_std = freizeit_scale.get()
            global ergebnis_pal_summe
            ergebnis_pal_summe= ((int(arbeit_std)* float(ergebnis_pal_arbeit)) + (int(freizeit_std)* float(ergebnis_pal_freizeit)) + (int(schlafen_std)* 0.95))/24
            ergebnis_pal_summe = "{:.1f}".format(ergebnis_pal_summe) # auf eine nachkommastelle kürzen
            ergebnis_label_berechnung = Label(top, text=str(ergebnis_pal_summe)) # printet das ergebnis vom Pal
            ergebnis_label_berechnung.grid(sticky=W, padx=10, row=6, column=2)
        else: # Label wenn nicht 24std
            
            fail_label = Label(top, fg="red", text="Bitte auf 24 std anpassen")
            fail_label.grid(row=6, column=2)
            fail_label.after(3000, fail_label.destroy)                  
        
        if float(ergebnis_pal_summe) ==1.1:
            clicked.set(pal_options[0])
            #print("1.option")
        elif float(ergebnis_pal_summe) == 1.2:
            clicked.set(pal_options[1])
            #print("2.option")
        elif float(ergebnis_pal_summe) == 1.3:
            clicked.set(pal_options[2])
            #print("3.option")
        elif float(ergebnis_pal_summe) == 1.4:
            clicked.set(pal_options[3])
            #print("4.option")
        elif float(ergebnis_pal_summe) == 1.5:
            clicked.set(pal_options[4])
            #print("5.option")
        elif float(ergebnis_pal_summe) == 1.6:
            clicked.set(pal_options[5])
            #print("6.option")
        elif float(ergebnis_pal_summe) == 1.7:
            clicked.set(pal_options[6])
            #print("7.option")
        elif float(ergebnis_pal_summe) == 1.8:
            clicked.set(pal_options[7])
            #print("8.option")
        else :
            clicked.set(pal_options[8])
            #print("9.option")
            
    ergebnis_label_anzeige = Label(top, text="PAL entspricht: ")
    ergebnis_label_anzeige.grid(sticky=E, padx=10, pady=10, row=6,column=0, columnspan=2)
    pal_berechnen_button = Button(top, text="Pal ermitteln", command=ergebnis_pal)
    pal_berechnen_button.grid(sticky=W, row=5, column=2, columnspan=1)
           
   
    #uebernehmen_und_schliessen = lambda: clicked_set_options + top.destroy()
    button2 = Button(top, text="Pal übernehmen und Fenster schließen", command=top.destroy )
    button2.grid(row=7,column=1, columnspan=2)
    
    
#PAL button öffnet zweites Fenster zur detaillierten Einstellung
pal_button = Button(root, fg="blue", text="PAL berechnen", command=pal_berechnen)
pal_button.grid(pady=10, row=2, column=3)

goal = StringVar()
goal.set("100") # Defaul value
#goal_int = float(goal.get()) /100
#print(goal.get())
# Auswahl ob männlich oder weiblich

frame_pal = LabelFrame(root, text="Ziel auswählen")
frame_pal.grid(row=4,columnspan=2)
Radiobutton(frame_pal, text= " Schnell Gewicht verlieren", variable= goal, value=80).grid(sticky=W, row=4, column=0)
Radiobutton(frame_pal, text= " Moderat Gewicht verlieren", variable= goal, value=90).grid(sticky=W, row=5,column=0)
Radiobutton(frame_pal, text= " Gewicht halten           ", variable= goal, value=100).grid(sticky=W, row=6, column=0)
Radiobutton(frame_pal, text= " moderat Gewicht aufbauen ", variable= goal, value=110).grid(sticky=W, row=7,column=0)
Radiobutton(frame_pal, text= " Schnell Gewicht aufbauen ", variable= goal, value=115).grid(sticky=W, row=8,column=0)


# DIe Funktion bestimmt den Kalorienbedarf anhand des Gewichts, PAL und Zielsetzung
def kcalbedarf_berechnen():
    goal_int = float(goal.get()) /100
    if weight_entry.get() == '' or  40>int(weight_entry.get())<200: 
        print("ungültige Gewichtseingabe. Bitte Gewicht eingeben")
        label = Label(root, fg="red", text="Ungültige Gewichtseingabe. Bitte trage ein Gewicht zwischen 40 und 200kg ein")
        label.grid(padx=10, pady=15, sticky=E, row=9,columnspan=4)
        label.after(3000, label.destroy)
    elif r.get() == "1":
        global kcalbedarf
        pal = clicked.get()
        pal_int = pal[:3]
        kcalbedarf = float(weight_entry.get()) * 24 * float(pal_int) * float(goal_int)
        label = Label(root, anchor=W, text="Dein Kalorienbedarf beträgt: " + str('{:.0f}'.format(kcalbedarf)) + " kcal" + "\n \n Die Regler stehen bereits bei deiner Makronährstoffempfehlung")
        label.grid(row=9, column=0, columnspan=2)
        if int(goal.get())== 80:
            protein_scale.set(50)
            carb_scale.set(20)
            fat_scale.set(30)
            #print("80")
        elif int(goal.get())== 90:
            protein_scale.set(45)
            carb_scale.set(25)
            fat_scale.set(30)
            #print("90")
        elif int(goal.get())== 100:
            protein_scale.set(40)
            carb_scale.set(30)
            fat_scale.set(30)
            #print("100")
        elif int(goal.get())== 110:
            protein_scale.set(35)
            carb_scale.set(35)
            fat_scale.set(30)
            #print("110")
        elif int(goal.get())==115:
            protein_scale.set(20)
            carb_scale.set(20)
            fat_scale.set(20)
            #print("XXX")
            

        #myLabel = Label(root, text=pal[:3])
        #myLabel.grid(row=5, columnspan=2 )
    else:
        pal = clicked.get()
        pal_int = pal[:3]
        kcalbedarf = float(weight_entry.get()) * 24 * 9 / 10 * float(pal_int) * float(goal_int)
        label = Label(root, text= "Dein Grundumsatz beträgt: " + '{:.0f}'.format(kcalbedarf) + " kcal")
        label.grid(row=9, columnspan=2)
        
        if int(goal.get())== 80:
            protein_scale.set(50)
            carb_scale.set(20)
            fat_scale.set(30)
            print("80")
        elif int(goal.get())== 90:
            protein_scale.set(45)
            carb_scale.set(25)
            fat_scale.set(30)
            print("90")
        elif int(goal.get())== 100:
            protein_scale.set(35)
            carb_scale.set(35)
            fat_scale.set(30)
            print("100")
        elif int(goal.get())== 110:
            protein_scale.set(35)
            carb_scale.set(35)
            fat_scale.set(30)
            print("110")
        #myLabel = Label(root, text=pal[:3])
        #myLabel.grid(row=5, columnspan=2, )

#   weight = weight_entry.get()
#   kcalbedarf_label = Label(root, text= weight).grid(row=4, column=0, columnspan=2)

kcalbedarf_button = Button(root, text="Kalorienbedarf berechnen",command= kcalbedarf_berechnen)
kcalbedarf_button.grid(pady=10, row=3, column=0, columnspan=2)

#Slider für Makronährstoffverteilung

def sel():
    selection =  protein_scale.get() + carb_scale.get() + fat_scale.get()
    if selection ==100 :
        #label = Label(root, bg="grey", text = selection)
        #label.grid(row=13,columnspan=3) # 100% müssen nicht angezeigt werden
        frame_selection = LabelFrame(text = "Deine Makronährstoffempfehlung: ")
        frame_selection.grid(sticky=W, padx=15, columnspan=4, rowspan=4)
        protein_angabe_label = Label(frame_selection, text="Proteine: ")
        carb_angabe_label= Label(frame_selection, text="Kohlenhydrate: ")
        fat_angabe_label = Label(frame_selection, text="Fette: ")

        protein_angabe_label.grid(pady=10, row=18, column=0)
        carb_angabe_label.grid(pady=10, row=18, column=1)
        fat_angabe_label.grid(pady=10, row=18, column=2)
        #protein_angabe_kcal = protein_scale.get()/100*int(kcalbedarf)
        #protein_angabe_kcal_label = Label(frame_selection, text= '{:.0f}'.format(protein_angabe_kcal)+ " kcal")
        #protein_angabe_kcal_label.grid(row=19, column=0)
        
        protein_angabe_g = protein_scale.get()/100*int(kcalbedarf)/4
        protein_angabe_g_label = Label(frame_selection, font=10, text= '{:.0f}'.format(protein_angabe_g) + " g")
        protein_angabe_g_label.grid(row=20, column=0)
        
        #carb_angabe_kcal = carb_scale.get()/100*int(kcalbedarf)
        #carb_angabe_kcal_label = Label(frame_selection, text='{:.0f}'.format(carb_angabe_kcal) + " kcal")
        #carb_angabe_kcal_label.grid(row=19, column=1)
        
        carb_angabe_g = carb_scale.get()/100*int(kcalbedarf)/4
        carb_angabe_g_label = Label(frame_selection, font=10, text= "{:.0f}".format(carb_angabe_g) + " g")
        carb_angabe_g_label.grid(row=20, column=1)
        
        #fat_angabe_kcal = fat_scale.get()/100*int(kcalbedarf)
        #fat_angabe_kcal_label = Label(frame_selection, text="{:.0f}".format(fat_angabe_kcal) + " kcal")
        #fat_angabe_kcal_label.grid(row=19, column=2)
        
        fat_angabe_g = protein_scale.get()/100*int(kcalbedarf)/9
        fat_angabe_g_label = Label(frame_selection, font=10, text="{:.0f}".format(fat_angabe_g) + " g")
        fat_angabe_g_label.grid(row=20, column=2)
        


    elif selection != 100:
        label = Label(root, fg="red", text = "Deine Makroverteilung ergibt " + str(selection) + "%")
        label.grid(row=13, columnspan=3)
        label.after(3000, label.destroy) # Label verschwindet wieder
"""else:
        label = Label(root, fg="red", text = "Deine Makroverteilung ergibt " + str(selection) + "%")
        label.grid(row=13,columnspan=3)
        label.after(3000, label.destroy)# Label verschwindet wieder
"""
var1 = IntVar()
var2 = IntVar()
var3 = IntVar()

"""
Makro Label erscheinen noch nicht richtig


"""
frame_scale = LabelFrame(text = "Makro-Slider")
frame_scale.grid( pady=10, padx=15 )

protein_label = Label(frame_scale, text="Protein")
carb_label= Label(frame_scale, text="Kohlenhydrate")
fat_label = Label(frame_scale, text="Fette")

carb_label.grid(padx=10, row=11, column=0)
protein_label.grid(row=10, column=0)
frame_scale.grid(columnspan=2)
fat_label.grid(row=12, column=0)


protein_scale = Scale(frame_scale, from_=5, to=90, orient=HORIZONTAL, length=200, resolution=5, variable = var1 )
carb_scale = Scale(frame_scale, from_=5, to=90, orient=HORIZONTAL, length=200, resolution=5, variable = var2 )
fat_scale = Scale(frame_scale, from_=5, to=90, orient=HORIZONTAL, length=200, resolution=5, variable = var3 )

protein_scale.grid(row=10, column=1, columnspan=2)
carb_scale.grid(row=11, column=1, columnspan=2)
fat_scale.grid(row=12, column=1, columnspan=2)

carb_scale.set(35)
protein_scale.set(35)
fat_scale.set(30)




set_button = Button(root, text= "Makronährstoffverteilung einstellen", command=sel)
set_button.grid(pady=10, row=14, columnspan=2)





root.mainloop()