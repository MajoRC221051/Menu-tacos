import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
from tkinter import*
from tkinter.messagebox import showinfo
import ast
from tkVideoPlayer import TkinterVideo
from tkVideoPlayer import TkinterVideo
import pygame
pygame.init()
import tkinter as tk
from tkinter import ttk
import sqlite3
from tkinter import font

from tkinter import scrolledtext


class Main(tk.Tk):
    def __init__(self, *args, **kwargs):

        tk.Tk.__init__(self, *args, **kwargs)
        self.title('Reacciona')
        self.geometry("1000x600")
        self.resizable(False, False)
        
        paginas = tk.Frame(self)
        paginas.pack(side="top", fill="both", expand=True)
        paginas.grid_rowconfigure(0, weight=1)
        paginas.grid_columnconfigure(0, weight=1)
        
        self.frames = {}
        for Paginas in (App, Registro, Login, Ordenar):
            frame = Paginas(paginas, self)
            self.frames[Paginas] = frame
            frame.grid(row=0, column=0, sticky="nsew")
            self.show_Ventana(App)
            
        
            
    def show_Ventana(self, paginas):
        ventana = self.frames[paginas]
        ventana.tkraise()
            
class Registro(tk.Frame):
    def __init__(self, parent, controller):
        
        tk.Frame.__init__(self, parent, bg = "white" )
        self.image1 = tk.PhotoImage(file="Registro.png")
        self.w = self.image1.width()
        self.h = self.image1.height()


        self.panel1 = tk.Label(self, image=self.image1)
        self.panel1.pack(side='top', fill='both', expand='yes')

        self.panel1.image = self.image1
        
        
        
                
        self.username = StringVar()
        self.contraseña = StringVar()
        self.email = StringVar()
        self.confirm = StringVar()
        
        
        
        self.entrada_username= tk.Entry(self, textvariable=self.username, width=29,bd=0,font=("League Spartan",13)).place(x=50,y=185)
        
        
        self.entrada_contraseña = tk.Entry(self, textvariable=self.contraseña, width=25,bd=0,  font=("League Spartan",15),show="*").place(x=45,y=335)
        
        self.entrada_email= tk.Entry(self, textvariable=self.email, width=29,bd=0, font=("League Spartan",13)).place(x=50,y=263)
        self.confirm_entrada = tk.Entry(self, textvariable=self.confirm, width=25,bd=0,  font=("League Spartan",15),show="*").place(x=45,y=422)

        self.label = tk.Label(self, text = "Already have an account?", fg = "black", bg = "white", font = ('Microsoft YaHei UI Light', 11)).place(x=70, y=520)
    
        self.button2 = tk.Button(self,text="Sign in", cursor="hand2", bg = "white", border = 0,  fg = "#28847F", font=("League Spartan underline",11), command = (lambda: self.cambiar_Pagina(controller))).place(x=264,y=520)

        self.button = tk.Button(self,text="Create new Account", bg = "#E16B52", width = 45, pady = 7,  relief = "flat", border = 0, font = ("League Spartan",12), command = (lambda: self.save())).place(x=20,y=465)
           
            
    def save(self):
        self.name = self.username.get()
        self.contra = self.contraseña.get()
        self.em = self.email.get()
        conn = sqlite3.connect("Reacciona1.db")
        with conn:
            cur=conn.cursor()
            cur.execute("CREATE TABLE IF NOT EXISTS Info(username, contraseña, email)")
            cur.execute("INSERT INTO Info(username, email, contraseña) VALUES(?,?,?)", (self.name, self.contra, self.em))
            conn.commit()
            


    def cambiar_Pagina(self, controller):
        controller.show_Ventana(Login)
        self.button2.config()


class Login(tk.Frame):


    def __init__(self, parent, controller):
    
    

        tk.Frame.__init__(self, parent, bg = "white" )
        self.image1 = tk.PhotoImage(file="Login.png")
        self.w = self.image1.width()
        self.h = self.image1.height()


        self.panel1 = tk.Label(self, image=self.image1)
        self.panel1.pack(side='top', fill='both', expand='yes')

        self.panel1.image = self.image1
        
        self.username = StringVar()
        self.contraseña = StringVar()
        
        self.entrada_username= tk.Entry(self, textvariable=self.username, width=29,bd=0,font=("League Spartan",13)).place(x=70,y=270)
        
        self.entrada_contraseña = tk.Entry(self, textvariable=self.contraseña, width=29,bd=0,font=("League Spartan",15),show="*").place(x=70,y=400)

        self.label = tk.Label(self, text = "Don´t have an account yet?", fg = "black", bg = "white", font = ('Microsoft YaHei UI Light', 11)).place(x=70, y=520)
        self.button2 = tk.Button(self,text="Sign up", cursor="hand2", bg = "white", border = 0, fg = "#28847F", font=("League Spartan underline",11), command = (lambda: self.cambiar_Pagina(controller))).place(x=266,y=521)
        
        self.button = tk.Button(self,text="Ingresar", bg = "#E16B52", width = 39,pady = 10,  relief = "flat", border = 0, font = ("League Spartan",12), command = (lambda: self.login(controller))) .place(x=50,y=450)
        
    def login(self, controller):
       
        conn = sqlite3.connect("Mentally.db")
        c = conn.cursor()
        
        self.name = self.username.get()
        self.contra = self.contraseña.get()
        
        c.execute('SELECT * FROM Info WHERE username = ? AND contraseña = ?', (self.name, self.contra))

        if c.fetchall():
            controller.show_Ventana(App)
            self.button2.config()

        c.close()

        
            
    def cambiar_Pagina(self, controller):
        controller.show_Ventana(Registro)
        self.button2.config()
        
    
        
class App(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg = "white" )
        self.image1 = tk.PhotoImage(file="Página.png")
        self.w = self.image1.width()
        self.h = self.image1.height()
        
        self.panel1 = tk.Label(self, image=self.image1)
        self.panel1.pack(side='top', fill='both', expand='yes')

        self.panel1.image = self.image1
        
        self.league_spartan_font = font.Font(family="Roboto", size=12, weight = "bold")
    
        
        self.button = Button(self,text="ORDENA YA", bg = "#FFCE4A", fg = "black", width = 25, pady = 7,  relief = "flat", border = 0, font = self.league_spartan_font, command = (lambda: self.ordenar(controller))).place(x=160,y=360)
        self.button2 = tk.Button(self,text="Inicio", cursor="hand2", bg = "white", border = 0,  fg = "grey", font=("League Spartan underline",12, "bold")).place(x=264,y=30)
        self.button2 = tk.Button(self,text="Conocenos", cursor="hand2", bg = "white", border = 0,  fg = "grey", font=("League Spartan underline",12, "bold")).place(x=330,y=30)
        self.button2 = tk.Button(self,text="Promociones", cursor="hand2", bg = "white", border = 0,  fg = "grey", font=("League Spartan underline",12, "bold")).place(x=440,y=30)
        self.button2 = tk.Button(self,text="Llamar mesero", cursor="hand2", bg = "white", border = 0,  fg = "grey", font=("League Spartan underline",12, "bold")).place(x=560,y=30)
        self.button2 = tk.Button(self,text="🛒", cursor="hand2", bg = "white", border = 0,  fg = "black", font=("League Spartan underline",16, "bold")).place(x=850,y=23)
        self.button2 = tk.Button(self,text="👤", cursor="hand2", bg = "white", border = 0,  fg = "black", font=("League Spartan underline",16, "bold")).place(x=950,y=23)
        self.button2 = tk.Button(self,text="★", cursor="hand2", bg = "white", border = 0,  fg = "black", font=("League Spartan underline",14, "bold")).place(x=900,y=24)

    def ordenar(self, controller):
        controller.show_Ventana(Ordenar)
        self.button2.config()
        
class Ordenar(tk.Frame):
     def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg = "white" )
        self.image1 = tk.PhotoImage(file="Menu1.png")
        self.w = self.image1.width()
        self.h = self.image1.height()
        
        self.panel1 = tk.Label(self, image=self.image1)
        self.panel1.pack(side='top', fill='both', expand='yes')

        self.panel1.image = self.image1
        
        self.foto33 = PhotoImage(file = "Entradas.png")
        self.button3333 = tk.Button(self,  image = self.foto33, borderwidth=0, highlightthickness=0)
        self.button3333.place(x=20, y=380)
        
        self.foto1 = PhotoImage(file = "Taco.png")
        self.button1 = tk.Button(self,  image = self.foto1, borderwidth=0, highlightthickness=0)
        self.button1.place(x=260, y=380)
        
        self.foto2 = PhotoImage(file = "Flan (1).png")
        self.button2 = tk.Button(self,  image = self.foto2, borderwidth=0, highlightthickness=0)
        self.button2.place(x=480, y=380)
            
        self.foto22 = PhotoImage(file = "Bebidas.png")
        self.button22 = tk.Button(self,  image = self.foto22, borderwidth=0, highlightthickness=0)
        self.button22.place(x=730, y=380)
        
        self.button2 = tk.Button(self,text="Entradas", cursor="hand2", bg = "white", border = 0,  fg = "black", font=("League Spartan underline",12, "bold")).place(x=110,y=560)
        self.button2 = tk.Button(self,text="Platos Fuertes", cursor="hand2", bg = "white", border = 0,  fg = "black", font=("League Spartan underline",12, "bold")).place(x=320,y=560)
        self.button2 = tk.Button(self,text="Postres", cursor="hand2", bg = "white", border = 0,  fg = "black", font=("League Spartan underline",12, "bold")).place(x=560,y=560)
        self.button2 = tk.Button(self,text="Bebidas", cursor="hand2", bg = "white", border = 0,  fg = "black", font=("League Spartan underline",12, "bold")).place(x=810,y=560)

        self.button2 = Label(self,text="Inicio", cursor="hand2", bg = "white", border = 0,  fg = "grey", font=("League Spartan underline",12, "bold")).place(x=264,y=12)
        self.button2 = Label(self,text="Conocenos", cursor="hand2", bg = "white", border = 0,  fg = "grey", font=("League Spartan underline",12, "bold")).place(x=330,y=12)
        self.button2 = Label(self,text="Promociones", cursor="hand2", bg = "white", border = 0,  fg = "grey", font=("League Spartan underline",12, "bold")).place(x=440,y=12)
        self.button2 = Label(self,text="Llamar mesero", cursor="hand2", bg = "white", border = 0,  fg = "grey", font=("League Spartan underline",12, "bold")).place(x=560,y=12)
                
        self.button2 = tk.Button(self,text="🛒", cursor="hand2", bg = "white", border = 0,  fg = "black", font=("League Spartan underline",16, "bold")).place(x=850,y=5)
        self.button2 = tk.Button(self,text="👤", cursor="hand2", bg = "white", border = 0,  fg = "black", font=("League Spartan underline",16, "bold")).place(x=950,y=5)
        self.button2 = tk.Button(self,text="★", cursor="hand2", bg = "white", border = 0,  fg = "black", font=("League Spartan underline",14, "bold")).place(x=900,y=8)






        
        

#     def cambiar_Pagina1(self, controller):
#         controller.show_Ventana(Relajate)
#         self.button2.config()
#         
#     def cambiar_Regresa(self, controller):
#         controller.show_Ventana(Regresa)
#         self.button3.config()
#         
#     def cambiar_Alegrate(self, controller):
#         controller.show_Ventana(Alegrate)
#         self.button4.config()
#         
#     def cambiar_Duermete(self, controller):
#         controller.show_Ventana(Duermete)
#         self.button.config()
#         
#  
#         
#     
#     
# 
# #         
# # class Relajate(tk.Frame):
# # 
# #         
# #     def __init__(self, parent, controller):
# #         tk.Frame.__init__(self, parent, bg = "white" )
# #         self.image1 = tk.PhotoImage(file="Relajate.png")
# #         self.w = self.image1.width()
# #         self.h = self.image1.height()
# #         
# #         self.panel1 = tk.Label(self, image=self.image1)
# #         self.panel1.pack(side='top', fill='both', expand='yes')
# # 
# #         self.panel1.image = self.image1
# #     
# # 
# # 
# # 
# #         self.foto = PhotoImage(file = "Meditalo.png")
# #         self.button = tk.Button(self,  image = self.foto, borderwidth=6, highlightthickness=0, command=self.video1)
# #         self.button.place(x=60, y=380)
# #         
# #         self.foto1 = PhotoImage(file = "Escribelo.png")
# #         self.button1 = tk.Button(self,  image = self.foto1, borderwidth=6, highlightthickness=0, command = self.escribelo)
# #         self.button1.place(x=350, y=380)
# #         
# #         self.foto2 = PhotoImage(file = "Agradece.png")
# #         self.button2 = tk.Button(self,  image = self.foto2, borderwidth=6, highlightthickness=0, command = self.gratitud)
# #         self.button2.place(x=640, y=380)
# #         
# #         self.button5 = tk.Button(self,text="⌂ ", cursor="hand2", bg = "#EFEFEF", border = 0,  fg = "black", font=("League Spartan underline",30), command = (lambda: self.cambiar_Pagina(controller))).place(x=900,y=10)
# #     
# #     def video1(self):
# #         self.videoplayer = tk.Toplevel()
# #         self.videoplayer = TkinterVideo(master=self.videoplayer, scaled=True)
# #         self.videoplayer.load(r"1.mp4")
# #         self.videoplayer.pack(expand=True, fill="both")
# #         self.videoplayer.play()
# #         self.mainloop()
# #         
# #     def escribelo(self):
# #         window = self.newWindow1 = tk.Toplevel()
# #         self.newWindow1.geometry("850x750")
# #      
# #         self.bg1 = Label(window, bg = "Pink").place(x=0, y=0, relwidth=1, relheight=1)
# #         self.entrada = StringVar()
# #         self.text_area = scrolledtext.ScrolledText(window, 
# #                                  wrap = tk.WORD, 
# #                                       width = 120, 
# #                                       height = 35, 
# #                                       font = ("League Spartan",
# #                                               13))
# #         self.text_area.grid(column = 0, pady = 50, padx = 80)
# #         self.text_area.focus()
# #         window.mainloop()
# #         
# #     def gratitud(self):   
# #        self.newWindow = tk.Toplevel()
# #        self.newWindow.geometry("850x750")
# #        self.newWindow.resizable(False,False)
# #        self.bg6 = PhotoImage(file="G.png")
# #        self.bg7 = Label(self.newWindow, image=self.bg6).place(x=0, y=0, relwidth=1, relheight=1)
# #        
# #                 
# #     def cambiar_Pagina(self, controller):
# #         controller.show_Ventana(App)
# #         self.button5.config()
# #         
# # 
# # class Duermete(tk.Frame):
# #     
# #     def __init__(self, parent, controller):
# #         
# #         tk.Frame.__init__(self, parent, bg = "white" )
# #         self.image1 = tk.PhotoImage(file="sueño.png")
# #         self.w = self.image1.width()
# #         self.h = self.image1.height()
# # 
# # 
# #         self.panel1 = tk.Label(self, image=self.image1)
# #         self.panel1.pack(side='top', fill='both', expand='yes')
# # 
# #         self.panel1.image = self.image1
# # 
# #         
# #         
# #         self.label3 = Label(self, text = "Modo Lluvia", fg = "black", bg = "white", font = ("Microsoft YaHei UI Bold", 14)).place(x=258, y=610)
# # 
# #         self.foto = PhotoImage(file = "2.png")
# #         self.button = tk.Button(self,  image = self.foto, borderwidth=0, highlightthickness=0, command = self.video1)
# #         self.button.place(x=45, y=400)
# #         
# #         self.foto2 = PhotoImage(file = "1.png")
# #         self.button2 = tk.Button(self,  image = self.foto2, borderwidth=0, highlightthickness=0, command = self.video2)
# #         self.button2.place(x=270, y=400)
# #         
# #         self.label = Label(self, text = "Modo Bosque", fg = "black", bg = "white", font = ("Microsoft YaHei UI Bold", 14)).place(x=458, y=610)
# # 
# #         
# #         self.foto3 = PhotoImage(file = "Bosque2.png")
# #         self.button3 = tk.Button(self,  image = self.foto3, borderwidth=0, highlightthickness=0, command = self.video3)
# #         self.button3.place(x=520, y=400)
# #         self.label4 = Label(self, text = "Modo Noche", fg = "black", bg = "white", font = ("Microsoft YaHei UI Bold", 14)).place(x=658, y=610)
# # 
# #         
# #         self.foto4 = PhotoImage(file = "4.png")
# #         self.button4 = tk.Button(self,  image = self.foto4, borderwidth=0, highlightthickness=0, command = self.video4)
# #         self.button4.place(x=760, y=400)
# #         
# #         self.button6 = tk.Button(self,text="⌂ ", cursor="hand2", bg = "#EFEFEF", border = 0,  fg = "black", font=("League Spartan underline",20), command = (lambda: self.cambiar_Pagina(controller))).place(x=950,y=5)
# #         
# #     def cambiar_Pagina(self, controller):
# #         controller.show_Ventana(App)
# #         self.button6.config()
# #     
# #     def video1(self):
# #         self.newWindow = tk.Toplevel()
# #         self.newWindow.geometry("850x750")
# #         self.newWindow.resizable(False,False)
# #         self.bg6 = PhotoImage(file="Oceano.png")
# #         self.bg7 = Label(self.newWindow, image=self.bg6).place(x=0, y=0, relwidth=1, relheight=1)
# # 
# #         self.mybutton4 = tk.Button(self.newWindow, text='        ▷          ', bg = "white", border = 0, width = 0, font=("League Spartan underline",15), command = self.play1).place(x=250, y=590)
# # 
# #         self.mybutton3 = tk.Button(self.newWindow, text='        ||          ',  bg = "black", fg = "white", border = 0, width = 0, font=("League Spartan underline",15), command = self.stop1).place(x=400, y=590) 
# #        
# #     
# #     def play1(self):
# #         pygame.mixer.music.load("2.mp3") #Loading File Into Mixer
# #         pygame.mixer.music.play()
# #     def stop1(self):
# #         pygame.mixer.music.stop()
# #         
# #     def video2(self):
# #         self.newWindow6 = tk.Toplevel()
# #         self.newWindow6.geometry("850x750")
# #         self.newWindow6.resizable(False,False)
# #         self.bg6 = PhotoImage(file="rain.png")
# #         self.bg7 = Label(self.newWindow6, image=self.bg6).place(x=0, y=0, relwidth=1, relheight=1)
# # 
# #         self.mybutton10 = tk.Button(self.newWindow6, text='        ▷          ', bg = "white", border = 0, width = 0, font=("League Spartan underline",15), command = self.play2).place(x=250, y=590)
# # 
# #         self.mybutton11 = tk.Button(self.newWindow6, text='        ||          ',  bg = "black", fg = "white", border = 0, width = 0, font=("League Spartan underline",15), command = self.stop2).place(x=400, y=590) 
# #  
# #        
# # 
# #        
# #     
# #     def play2(self):
# #         pygame.mixer.music.load("3l.mp3") #Loading File Into Mixer
# #         pygame.mixer.music.play()
# #     def stop2(self):
# #         pygame.mixer.music.stop()
# #     
# #     
# #     def video3(self):
# #         self.newWindow3 = tk.Toplevel()
# #         self.newWindow3.geometry("850x750")
# #         self.newWindow3.resizable(False,False)
# #         self.bg8 = PhotoImage(file="Bosque.png")
# #         self.bg9 = Label(self.newWindow3, image=self.bg8).place(x=0, y=0, relwidth=1, relheight=1)
# # 
# #         self.mybutton5 = tk.Button(self.newWindow3, text='        ▷          ', bg = "white", border = 0, width = 0, font=("League Spartan underline",15), command = self.play3).place(x=250, y=590)
# # 
# #         self.mybutton6 = tk.Button(self.newWindow3, text='        ||          ',  bg = "black", fg = "white", border = 0, width = 0, font=("League Spartan underline",15), command = self.stop3).place(x=400, y=590) 
# #        
# #     
# #     def play3(self):
# #         pygame.mixer.music.load("forest.mp3") #Loading File Into Mixer
# #         pygame.mixer.music.play()
# #     def stop3(self):
# #         pygame.mixer.music.stop()
# #         
# #     def video4(self):
# #         self.newWindow4 = tk.Toplevel()
# #         self.newWindow4.geometry("850x750")
# #         self.newWindow4.resizable(False,False)
# #         self.bg11 = PhotoImage(file="maxresdefault.png")
# #         self.bg12 = Label(self.newWindow4, image=self.bg11).place(x=0, y=0, relwidth=1, relheight=1)
# # 
# #         self.mybutton66 = tk.Button(self.newWindow4, text='        ▷          ', bg = "white", border = 0, width = 0, font=("League Spartan underline",15), command = self.play4).place(x=250, y=590)
# # 
# #         self.mybutton55 = tk.Button(self.newWindow4, text='        ||          ',  bg = "black", fg = "white", border = 0, width = 0, font=("League Spartan underline",15), command = self.stop4).place(x=400, y=590)   
# #     def play4(self):
# #         pygame.mixer.music.load("1.mp3") #Loading File Into Mixer
# #         pygame.mixer.music.play()
# #     def stop4(self):
# #         pygame.mixer.music.stop()
# #         
# # 
# # class Regresa(tk.Frame):
# # 
# #     def __init__(self, parent, controller):
# #         
# #         tk.Frame.__init__(self, parent, bg = "white" )
# # 
# # 
# #         
# #         self.image5 = tk.PhotoImage(file="MM.png")
# #         self.w5 = self.image5.width()
# #         self.h5 = self.image5.height()
# # 
# #         self.panel = tk.Label(self, image=self.image5)
# #         self.panel.pack(side='top', fill='both', expand='yes')
# # 
# #         self.panel.image = self.image5
# # 
# #         self.foto = PhotoImage(file = "BOTONR1.png")
# #         self.button = tk.Button(self, image = self.foto, borderwidth=0, highlightthickness=0, command = self.video2)
# #         self.button.place(x=280, y=325)
# # 
# #         self.foto2 = PhotoImage(file = "BOTONR2.png")
# #         self.button2 = tk.Button(self, image=self.foto2, borderwidth=0, highlightthickness=0, command = self.video3)
# #         self.button2.place(x=540, y=325)
# #         
# #         self.button6 = tk.Button(self,text="⌂ ", cursor="hand2", bg = "#D9D9D9", border = 0,  fg = "black", font=("League Spartan underline",20), command = (lambda: self.cambiar_Pagina(controller))).place(x=950,y=5)
# # 
# #     
# #         
# #     def video2(self):
# #         video = self.videoplayer2 = tk.Toplevel()
# #         self.videoplayer2 = TkinterVideo(master=self.videoplayer2, scaled = True)
# #         self.videoplayer2.load(r"AUDIO-REGRESA.mp4")
# #         self.videoplayer2.pack(expand=True, fill="both")
# #         self.mybutton57 = tk.Button(video, text='        ▷          ', bg = "white", border = 0, width = 0, font=("League Spartan underline",20), command = self.audiovideo1).place(x=350, y=550)
# #         self.mybutton67 = tk.Button(video, text='        ||          ', bg = "white", border = 0, width = 0, font=("League Spartan underline",20), command = self.stopaudio1).place(x=700, y=550)
# #         self.videoplayer2.play()
# #         video.mainloop
# #     
# #     def audiovideo1(self):
# #         pygame.mixer.music.load("AUDIO-REGRESA.mp3") #Loading File Into Mixer
# #         pygame.mixer.music.play()
# #     def stopaudio1(self):
# #         pygame.mixer.music.stop()
# #         statusbar['text'] = "Music Stopped"
# # 
# # 
# # 
# #     def video3(self):
# #         video22 = self.videoplayer112 = tk.Toplevel()
# #         self.videoplayer112 = TkinterVideo(master=video22,scaled = True)
# #         self.videoplayer112.load(r"AUDIO REGRESAMOMENTO.mp4")
# #         self.videoplayer112.pack(expand=True, fill="both")
# #         self.mybutton54 = tk.Button(video22, text='        ▷          ', bg = "white", border = 0, width = 0, font=("League Spartan underline",20), command = self.audiovideo3).place(x=350, y=550)
# #         self.mybutton64 = tk.Button(video22, text='        ||          ', bg = "white", border = 0, width = 0, font=("League Spartan underline",20), command = self.stopaudio3).place(x=700, y=550)
# #         self.videoplayer112.play()
# #         video22.mainloop()
# # 
# #     def audiovideo3(self):
# #         pygame.mixer.music.load("REGRESA AL MOMENTO.mp3") #Loading File Into Mixer
# #         pygame.mixer.music.play()
# #     def stopaudio3(self):
# #         pygame.mixer.music.stop()
# #         statusbar['text'] = "Music Stopped"
# # 
# #     def cambiar_Pagina(self, controller):
# #         controller.show_Ventana(App)
# #         self.button6.config()
# # 
# # class Alegrate(tk.Frame):
# #       
# #     def __init__(self, parent, controller):
# #         
# #         tk.Frame.__init__(self, parent, bg = "white" )
# # 
# # 
# #         
# #         self.image5 = tk.PhotoImage(file="Alegrate (1000 × 600 px) (1).png")
# #         self.w5 = self.image5.width()
# #         self.h5 = self.image5.height()
# # 
# #         self.panel = tk.Label(self, image=self.image5)
# #         self.panel.pack(side='top', fill='both', expand='yes')
# # 
# #         self.panel.image = self.image5
# # 
# #         self.foto = PhotoImage(file = "ALEGRATE1.png")
# #         self.button = tk.Button(self, image = self.foto, borderwidth=0, highlightthickness=0, command = self.videoalegrate)
# #         self.button.place(x=440, y=330)
# #         self.button6 = tk.Button(self,text="⌂ ", cursor="hand2", bg = "#F6FF8F", border = 0,  fg = "black", font=("League Spartan underline",20), command = (lambda: self.cambiar_Pagina(controller))).place(x=950,y=5)
# #         
# #         
# # 
# #     def videoalegrate(self):
# #         video300 = self.videoplayer4 = tk.Toplevel()
# #         self.videoplayer45 = TkinterVideo(master=self.videoplayer4,scaled = True)
# #         self.videoplayer45.load(r"VIDEOALEGRATE1.mp4")
# #         self.videoplayer45.pack(expand=True, fill="both")
# #         self.mybutton55 = tk.Button(video300, text='        ▷          ', bg = "white", border = 0, width = 0, font=("League Spartan underline",20), command = self.audiovideo2).place(x=350, y=550)
# #         self.mybutton65 = tk.Button(video300, text='        ||          ', bg = "white", border = 0, width = 0, font=("League Spartan underline",20), command = self.stopaudio2).place(x=700, y=550)
# #         self.videoplayer45.play()
# #         video300.mainloop()
# # 
# #     def audiovideo2(self):
# #         pygame.mixer.music.load("AUDIO ALEGRATE.mp3") #Loading File Into Mixer
# #         pygame.mixer.music.play()
# #     def stopaudio2(self):
# #         pygame.mixer.music.stop()
# # 
# #     def cambiar_Pagina(self, controller):
# #         controller.show_Ventana(App)
# #         self.button6.config()
# # 
# #         
if __name__ == '__main__':
    app = Main()
    app.mainloop()
        
        
        
        
        



