from  tkinter import *
from tkinter import Tk
import ast
import load_save_defs

class root_window:
    
    def exitf(self):
        self.window.destroy()
        #esto lo usare en un futuro lejano xd
    def move_window(self,event):
        self.window.geometry(f"+{event.x_root}+{event.y_root}")

    def pulsar_pkb(self):
        self.pkblb.config(image=self.pkb_pr)
    def soltar_pkb(self):
        self.pkblb.config(image=self.pkb)
    
    #funcion para contador de clicks
    def contwtf(self):
        self.contador = self.contador + 1
        self.varcont.set(str(self.contador))
        self.window.after(10,self.pulsar_pkb)
        self.window.after(100,self.soltar_pkb)

    """funciones para carga y salvado de archivos (data se refiere a los datos de clicks y entradas)
    (sets se refiere a los ajustes y cosas de personalización)"""
    def load_data(self):
        load_main = ast.literal_eval(load_save_defs.loadValue(self.data_main_path))
        load_sets = ast.literal_eval(load_save_defs.loadValue(self.data_sets_path))

        
    def save_data(self,main_path,sets_path):
        ##main
        get_main_data = self.varcont.get()
        get_main_data = load_save_defs.saveValue(get_main_data,main_path)
        ##sets
        get_sets_data = 1
        get_sets_data = 1 #load_save_defs.saveValue(get_sets_data,sets_path)
        
        

    def __init__(self):

        #configurando la ventana / setting up the window LOL
        self.window = Tk()
        self.window.title('PsoftresK 1.0') # este sera el nombre XD
        self.window.geometry('350x350+100+100')
        self.window.maxsize(350,350)
        self.window.minsize(350,350)
        self.window.configure(bg='#ab78f4') #color de fondo de la ventana

        '''abajo overredirect queda al descubierto por acciones en la ventana los cuales
        tenian como objetivo ocultar la barra de titulo para crear una dentro de la interfaz, esta idea
        fue descartada por cuestiones de tiempo y esfuerzo.
        Mas abajo vemos wm_attributes que era la solucion para que la ventana siguiera estando activa
        ya que al minimizarla desaparece de la barra de tareas y no hay manera de abrirla aunque el proceso
        siga activo y consumiendo recursos. Todo fue una cuestion de personalizacion y no tiene que ver
        con el programa final...'''

        self.window.overrideredirect(False)
        self.window.wm_attributes("-topmost", 1) #superposicion de la ventana

        #LOAD DATA FILES
        try:
            self.load_data()
        except:
            pass


        ##textvariable
        self.contador = 0
        self.varcont = StringVar()
        self.varcont.set(str(self.contador))

        #asset
            #titlebar resources
        self.titlebar_path = './assets/tbar/titlebar.png'
        self.mv_w_path = './assets/tbar/move_w.png'
        self.exit_w_path = './assets/tbar/exit_w.png'
        self.titlebar_PoI = PhotoImage(file=self.titlebar_path)
        self.mv_w_PoI = PhotoImage(file=self.mv_w_path)
        self.exit_w_PoI = PhotoImage(file=self.exit_w_path)

        #DAT FILES PATH
        self.data_main_path = './data/main.dat'
        self.data_sets_path = './data/settings.dat'

            #premierbll ico
        self.pkico1_path = './assets/b1.png'
        self.pkico2_path = './assets/b2.png'

        #esto es para dar el efecto de presionar el icono de pokeball
        self.pkb = PhotoImage(file=self.pkico1_path)
        self.pkb_pr = PhotoImage(file=self.pkico2_path)

        #Frame o marco para la barra de titulo
        self.window_bar = Frame(self.window,bg='#87477e',width=350,height=23)

        self.window_bar.grid_rowconfigure(0,weight=1)
        self.window_bar.grid_columnconfigure(0,weight=1)
        self.window_bar.grid_columnconfigure(1,weight=1)
        self.window_bar.grid_columnconfigure(2,weight=1)
        self.window_bar.pack(side=TOP)

        #Frame o marco lo q sea para agregar widgets (botones, texto, imagenes... ya saben)
        self.ultraframe = Frame(self.window,bg='#ab78f4',width=350,height=350)
            ##Frame grid conf
        self.ultraframe.grid_columnconfigure(0,weight=1)
        self.ultraframe.grid_rowconfigure(0,weight=1)
        self.ultraframe.grid_columnconfigure(1,weight=1)
        self.ultraframe.grid_rowconfigure(1,weight=1)
        self.ultraframe.grid_columnconfigure(2,weight=1)
        self.ultraframe.grid_rowconfigure(2,weight=1)
        self.ultraframe.grid_rowconfigure(3,weight=1)
        self.ultraframe.pack(side=BOTTOM)

        #custom titlebar
        self.wtitle = Label(self.window_bar,
                            image=self.titlebar_PoI,
                            text=' PsoftresK ',
                            font=('Arial',12),
                            bg='#87477e')
        self.wtitle.grid(column=1,row=0)

            ##move window button
        self.mv_w = Label(self.window_bar,
                        image=self.mv_w_PoI,
                        bg='#87477e')
        self.mv_w.grid(column=0,row=0)

            ##close window button
        self.exit_w = Label(self.window_bar,
                            image=self.exit_w_PoI,
                            bg='#87477e')
        self.exit_w.grid(column=2,row=0)
            ##titlebar_binds
        self.mv_w.bind('<B1-Motion>', self.move_window)
        self.exit_w.bind('<Button>', lambda event: self.exitf())

        #morelabels
        self.label1 = Label(self.ultraframe,text='CLICKS',font=('Arial',24),bg='#ab78f4')
        self.label1.grid(column=1,row=2)
            ##contador
        self.label2 = Label(self.ultraframe,textvariable=self.varcont,font=('Arial',32),bg='#ab78f4')
        self.label2.grid(column=1,row=3)
        self.label2.bind('<Button>', lambda event: self.save_data(self.data_main_path,self.data_sets_path))

        #boton para el contador lol
            ##set it as a label and place it
        self.pkblb = Label(self.ultraframe,image=self.pkb, bg='#ab78f4')
        self.pkblb.grid(column=1,row=1)

        #setting bindings
        self.pkblb.bind('<Button>', lambda event: self.contwtf())
            

        self.window.mainloop()