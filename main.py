from PIL import Image
import os
from tkcalendar import*
import customtkinter
from CTkMenuBar import *
from CTkTable import *
import reservas
from CTkMessagebox import CTkMessagebox

class ReservasScreen():
    client=""
    calendar=""
    periodo=""
    def reservasMenu():
        #Criação do frame
        HomeScreen.window1.reservas = customtkinter.CTkFrame(HomeScreen.window1, width=400,height=400)
        HomeScreen.window1.reservas.place(x= 25, y=50, in_=HomeScreen.window1)
        
        #Criação de label text
        title=  customtkinter.CTkLabel(HomeScreen.window1.reservas, text="Agendamento", font= customtkinter.CTkFont(family="Oswald", size=25, weight="bold"))
        title.place(x=20, y=10, in_=HomeScreen.window1.reservas)

        clientText = customtkinter.CTkLabel(HomeScreen.window1.reservas, text="ID do cliente:", font= customtkinter.CTkFont(family="Oswald", size= 18))
        clientText.place(x= 20, y=65, in_=HomeScreen.window1.reservas)

        roomText = customtkinter.CTkLabel(HomeScreen.window1.reservas, text="ID da sala:", font= customtkinter.CTkFont(family="Oswald",size= 18))
        roomText.place(x= 20, y= 110, in_=HomeScreen.window1.reservas)

        calendarText= customtkinter.CTkLabel(HomeScreen.window1.reservas, text="Data para agendar:", font= customtkinter.CTkFont(family="Oswald",size= 18))
        calendarText.place(x= 20, y= 160, in_=HomeScreen.window1.reservas)

        periodoText = customtkinter.CTkLabel(HomeScreen.window1.reservas, text="Periodo:", font= customtkinter.CTkFont(family="Oswald",size= 18))
        periodoText.place(x= 20, y=210, in_=HomeScreen.window1.reservas)

        #Criação de entrada de dados 
        HomeScreen.client= customtkinter.CTkEntry(HomeScreen.window1.reservas,  font= customtkinter.CTkFont("Oswald", 18))
        HomeScreen.client.place(x= 220, y=65, in_=HomeScreen.window1.reservas)
        
        HomeScreen.room = customtkinter.CTkEntry(HomeScreen.window1.reservas,  font= customtkinter.CTkFont("Oswald", 18))
        HomeScreen.room.place(x= 220, y=110, in_=HomeScreen.window1.reservas)
        
        HomeScreen.calendar= DateEntry(HomeScreen.window1.reservas, date_pattern= "yyyy-mm-dd", width= 10, height= 0,  font= customtkinter.CTkFont("Oswald", 18))
        HomeScreen.calendar.place(x= 220, y= 160)
        
        HomeScreen.periodo=  customtkinter.CTkOptionMenu(HomeScreen.window1.reservas, values=["Manhã", "Tarde", "Noite"],  font= customtkinter.CTkFont("Oswald", 18))
        HomeScreen.periodo.place(x= 220, y=210)

        #Botões para controle de input
        agendarButtom = customtkinter.CTkButton(HomeScreen.window1.reservas, text="Agendar",command=HomeScreen.collectDataA1, font= customtkinter.CTkFont("Oswald", 18))
        agendarButtom.place(x= 20, y=300, in_=HomeScreen.window1.reservas)

        closeButtom =  customtkinter.CTkButton(HomeScreen.window1.reservas, text="Fechar", command=HomeScreen.closeReservas, font= customtkinter.CTkFont("Oswald", 18))
        closeButtom.place(x=20, y=350, in_=HomeScreen.window1.reservas)


        atualizarButtom= customtkinter.CTkButton(HomeScreen.window1.reservas, text="Atualizar", command= HomeScreen.showReservasMenu, font=customtkinter.CTkFont("Oswald", 18))
        atualizarButtom.place(x=220, y= 300, in_=HomeScreen.window1.reservas)
        HomeScreen.showReservasMenu()

    def closeReservas():

        HomeScreen.window1.reservas.destroy()
        HomeScreen.window1.clientShow.destroy()
        HomeScreen.window1.reservaShow.destroy()
        HomeScreen.window1.roomShow.destroy()
    def collectDataA1():
        client= HomeScreen.client.get()
        room= HomeScreen.room.get()
        calendar= str(HomeScreen.calendar.get_date())
        periodo= HomeScreen.periodo.get()
        if True == reservas.consult("id_client", "client", client) or True ==  reservas.consult("id_room", "room", room):
            CTkMessagebox(title="Error", message="Informações divergentes com o banco de dados, verifique os dados ou cadastre dados novos!! ", icon="cancel")
        else:
            if True == reservas.colector(client, room, calendar, periodo):
                CTkMessagebox(title="Info", message="Existe um agendamento com essa data e periodo!")
            else:
                CTkMessagebox(message="Agendamento realizado com sucesso.", icon="check", option_1="Ok")
                HomeScreen.showReservasMenu()

    def showReservasMenu():
        try:
            HomeScreen.window1.clientShow.destroy()
            HomeScreen.window1.reservaShow.destroy()
            HomeScreen.window1.roomShow.destroy()

        except:
            True
        HomeScreen.window1.clientShow = customtkinter.CTkScrollableFrame(HomeScreen.window1, width=1000, height=810)
        HomeScreen.window1.clientShow.place(x= 450, y=50, in_=HomeScreen.window1)

        titleClient= customtkinter.CTkLabel(HomeScreen.window1.clientShow, text="Clientes", font= customtkinter.CTkFont(family="arial", size=25))
        titleClient.place(x=20, y=10, in_=HomeScreen.window1.clientShow)
        
        HomeScreen.matriz= reservas.readAll("SELECT * FROM client")
        HomeScreen.matriz.insert(0, ["Nome", "ID cliente", "Telefone", "E-mail", "Cargo"])
        table = CTkTable(master=HomeScreen.window1.clientShow, row=len(HomeScreen.matriz), column=5, values=HomeScreen.matriz)
        table.pack(expand=True, fill="both", padx=20, pady=50)

        HomeScreen.window1.reservaShow = customtkinter.CTkScrollableFrame(HomeScreen.window1 ,width=390, height= 390)
        HomeScreen.window1.reservaShow.place(x= 1490, y=50, in_=HomeScreen.window1)

        titleAgendamento= customtkinter.CTkLabel(HomeScreen.window1.reservaShow, text="Agendamentos realizados", font= customtkinter.CTkFont(family="arial", size=25))
        titleAgendamento.place(x=20, y=10, in_=HomeScreen.window1.reservaShow)

        HomeScreen.matriz= reservas.readAll("SELECT * FROM scheduling")
        HomeScreen.matriz.insert(0, ["ID client", "ID room", "Data", "Periodo"])
        table = CTkTable(master=HomeScreen.window1.reservaShow, row=len(HomeScreen.matriz), column=4, values=HomeScreen.matriz)
        table.pack(expand=True, fill="both", padx=20, pady=50)
        
        HomeScreen.window1.roomShow =  customtkinter.CTkScrollableFrame(HomeScreen.window1, width=390, height=390)
        HomeScreen.window1.roomShow.place(x=1490, y=470, in_=HomeScreen.window1)

        HomeScreen.matriz= reservas.readAll("SELECT * FROM room")
        HomeScreen.matriz.insert(0, ["ID room", "Tipo de sala"])
        table = CTkTable(master=HomeScreen.window1.roomShow, row=len(HomeScreen.matriz), column=2, values=HomeScreen.matriz)
        table.pack(expand=True, fill="both", padx=20, pady=50)

        tilteRoom= customtkinter.CTkLabel(HomeScreen.window1.roomShow, text="Salas", font= customtkinter.CTkFont(family="arial", size=25))
        tilteRoom.place(x=20, y=10, in_=HomeScreen.window1.roomShow)

class RoomScreen():
    idname = ""
    typeText = ""
    entry = ""
    def cadastrarSalas():
        #Criação do frame
        HomeScreen.window1.cadastroSalas = customtkinter.CTkFrame(HomeScreen.window1, width=450,height= 500)
        HomeScreen.window1.cadastroSalas.place(x= 25, y=70, in_=HomeScreen.window1)
        
        #Criação de label text
        title=  customtkinter.CTkLabel(HomeScreen.window1.cadastroSalas, text="Cadastro de Salas", font= customtkinter.CTkFont(family="Oswald", size=25, weight="bold"))
        title.place(x=20, y=10, in_=HomeScreen.window1.cadastroSalas)

        idText= customtkinter.CTkLabel(HomeScreen.window1.cadastroSalas, text="Nome da sala:", font= customtkinter.CTkFont(family="Oswald", size= 18))
        idText.place(x= 20, y=65, in_=HomeScreen.window1.cadastroSalas)

        typeText = customtkinter.CTkLabel(HomeScreen.window1.cadastroSalas, text="Tipo da sala:", font= customtkinter.CTkFont(family="Oswald",size= 18))
        typeText.place(x= 20, y= 110, in_=HomeScreen.window1.cadastroSalas)

        descriptionText= customtkinter.CTkLabel(HomeScreen.window1.cadastroSalas, text="Descrição:", font= customtkinter.CTkFont(family="Oswald",size= 18))
        descriptionText.place(x= 20, y= 160, in_=HomeScreen.window1.cadastroSalas)


        #Criação de entrada de dados 
        HomeScreen.idname= customtkinter.CTkEntry(HomeScreen.window1.cadastroSalas,width= 200,  font= customtkinter.CTkFont("Oswald", 18))
        HomeScreen.idname.place(x= 220, y=65, in_=HomeScreen.window1.cadastroSalas)
        
        HomeScreen.typeText = customtkinter.CTkEntry(HomeScreen.window1.cadastroSalas,width=200,  font= customtkinter.CTkFont("Oswald", 18))
        HomeScreen.typeText.place(x= 220, y=110, in_=HomeScreen.window1.cadastroSalas)

        HomeScreen.entry = customtkinter.CTkTextbox(HomeScreen.window1.cadastroSalas)
        HomeScreen.entry.insert("0.0", "")
        HomeScreen.entry.place(x= 220, y=150, in_=HomeScreen.window1.cadastroSalas)
        

        #Botões para controle de input
        cadastrarButtom = customtkinter.CTkButton(HomeScreen.window1.cadastroSalas, text="cadastrar",command=HomeScreen.collectDataA2 ,font= customtkinter.CTkFont("Oswald", 18))
        cadastrarButtom.place(x= 20, y=400, in_=HomeScreen.window1.cadastroSalas)

        closeButtom =  customtkinter.CTkButton(HomeScreen.window1.cadastroSalas, text="Fechar",command= HomeScreen.closeRoom, font= customtkinter.CTkFont("Oswald", 18))
        closeButtom.place(x=20, y=450, in_=HomeScreen.window1.cadastroSalas)


        atualizarButtom= customtkinter.CTkButton(HomeScreen.window1.cadastroSalas, text="Atualizar", command= HomeScreen.showRoomMenu, font=customtkinter.CTkFont("Oswald", 18))
        atualizarButtom.place(x=220, y= 400, in_=HomeScreen.window1.cadastroSalas)

        HomeScreen.showRoomMenu()
    def collectDataA2():
        collectidName=  HomeScreen.idname.get()
        collectType= HomeScreen.typeText.get()
        collectEntry= HomeScreen.entry.get("0.0", "end")
        if True == reservas.consult("id_room", "room", collectidName):
            reservas.armazenar((f"INSERT INTO room(id_room, type, description) VALUES('{collectidName}', '{collectType}', '{collectEntry}')"))
            CTkMessagebox(message="Cadastro realizado com sucesso.", icon="check", option_1="Ok")
            HomeScreen.showRoomMenu()
        else:
            CTkMessagebox(title="Info", message="Existe uma sala com essa identificação !")

    def closeRoom():
        HomeScreen.window1.cadastroSalas.destroy()
        HomeScreen.window1.showRoomData.destroy()

    def showRoomMenu():
        try:
            HomeScreen.window1.showRoomData.destroy()
        except:
            True
        HomeScreen.window1.showRoomData = customtkinter.CTkScrollableFrame(HomeScreen.window1, width=1000, height=810)
        HomeScreen.window1.showRoomData.place(x= 500, y=50, in_=HomeScreen.window1)

        titleRoom= customtkinter.CTkLabel(HomeScreen.window1.showRoomData, text="Salas", font= customtkinter.CTkFont(family="arial", size=25))
        titleRoom.place(x=20, y=10, in_=HomeScreen.window1.showRoomData)

        HomeScreen.matriz= reservas.readAll("SELECT * FROM room")
        HomeScreen.matriz.insert(0, ["ID da sala", "Tipo  de sala", "Descrição"])
        table = CTkTable(master=HomeScreen.window1.showRoomData, row=len(HomeScreen.matriz), column=3, values=HomeScreen.matriz)
        table.pack(expand=True, fill="both", padx=20, pady=50)





class HomeScreen(ReservasScreen, RoomScreen):
    window=""
    window1=""
    matriz= []

    __login=""
    __entryPass= ""
    __entryUser=""
    __current_path = os.path.dirname(os.path.realpath(__file__))
    a= customtkinter.CTkImage(Image.open(__current_path + "/assets/visibility.png"), size=(28,28))
    app= False

    def __init__(self):

        HomeScreen.window = customtkinter.CTk()
        HomeScreen.window.geometry("2000x1000")
        oswaldTitle= customtkinter.CTkFont(family= "Oswald", size=50, weight= "bold")
        oswaldTitle2= customtkinter.CTkFont(family= "Oswald", size=30, weight= "bold")
        oswaldSubtitle= customtkinter.CTkFont(family= "Oswald", size=30, weight= "normal")

        HomeScreen.window.menul= customtkinter.CTkFrame(HomeScreen.window, width= 890, height= 1024)
        HomeScreen.window.menul.grid(row=0, column=0)

        self.window.frame_image=customtkinter.CTkFrame(HomeScreen.window, width=1024, height=1024)
        self.window.frame_image.grid(row=0, column= 1)

        self.window.frame_image.bg = customtkinter.CTkImage(Image.open(HomeScreen.__current_path + "/assets/bg.jpeg"), size=(1024, 1024))
        self.window.frame_image.bg_image_label = customtkinter.CTkLabel(self.window.frame_image, image=self.window.frame_image.bg, text= "")
        self.window.frame_image.bg_image_label.grid(row=0, column=0)

        title = customtkinter.CTkLabel(HomeScreen.window.menul, text="Bem vindo ao Aloctech", font= oswaldTitle)
        title.place(relx=0.5, rely=0.1,anchor= "center", in_= HomeScreen.window.menul)

        title = customtkinter.CTkLabel(HomeScreen.window.menul, text="sistema de gestão de salas", font= oswaldSubtitle)
        title.place(relx=0.5, y=150,anchor= "center", in_= HomeScreen.window.menul)

        title = customtkinter.CTkLabel(HomeScreen.window.menul, text="Login", font= oswaldTitle2)
        title.place(relx=0.5, rely=0.3,anchor= "center", in_= HomeScreen.window.menul)

        HomeScreen.__entryUser= customtkinter.CTkEntry(HomeScreen.window.menul,placeholder_text= "Username",  font= oswaldSubtitle, width= 300)
        HomeScreen.__entryUser.place(x=300, y=400, in_=HomeScreen.window.menul)

        HomeScreen.__entryPass= customtkinter.CTkEntry(HomeScreen.window.menul,placeholder_text= "Password",  font= oswaldSubtitle, width= 300, show='*')
        HomeScreen.__entryPass.place(x=300, y=475, in_=HomeScreen.window.menul)

        HomeScreen.button= customtkinter.CTkButton(HomeScreen.window.menul,text="" ,width=0, height=0,fg_color= "transparent", image= HomeScreen.a, command=HomeScreen.toggle_password)
        HomeScreen.button.place(x= 610, y=479, in_=HomeScreen.window.menul)

        buttonLogin= customtkinter.CTkButton(HomeScreen.window.menul, text="Login", font= oswaldSubtitle, command= HomeScreen.acess)
        buttonLogin.place(x= 300, y= 550, in_= HomeScreen.window.menul)

        HomeScreen.buttonClose= customtkinter.CTkButton(HomeScreen.window.menul, text="Close", font=oswaldSubtitle)
        HomeScreen.buttonClose.place(x= 460, y= 550, in_= HomeScreen.window.menul)
        HomeScreen.window.mainloop()


        if 1 == HomeScreen.app:
            HomeScreen.window1 = customtkinter.CTk()
            HomeScreen.window1.geometry("2000x1000")
            menu = CTkMenuBar(master=HomeScreen.window1, height= 25, pady= 5)
            
            reservasBt = menu.add_cascade("Reservas", font= customtkinter.CTkFont(family="arial", size=20))
            reservasBt = CustomDropdownMenu(widget= reservasBt, font= customtkinter.CTkFont(family="arial", size= 15))
            reservasBt.add_option(option="Agendar", command=HomeScreen.reservasMenu, font= customtkinter.CTkFont(family="arial", size= 15))
            
            salasBt= menu.add_cascade("Salas", font= customtkinter.CTkFont(family="arial", size=20))
            salasBt = CustomDropdownMenu(widget= salasBt, font= customtkinter.CTkFont(family="arial", size=15))
            salasBt.add_option(option="Cadastrar", command=HomeScreen.cadastrarSalas, font = customtkinter.CTkFont(family="arial", size= 15))

            HomeScreen.window1.mainloop()
        
        
    
    def toggle_password():
        if HomeScreen.__entryPass.cget('show') == '':
            HomeScreen.__entryPass.configure(show='*')
            HomeScreen.button.configure(image=customtkinter.CTkImage(Image.open(HomeScreen.__current_path + "/assets/visibility.png"), size=(28,28)))
            HomeScreen.a=customtkinter.CTkImage(Image.open(HomeScreen.__current_path + "/assets/visibility.png"), size=(28,28))
        else:
            HomeScreen.__entryPass.configure(show='')
            HomeScreen.button.configure(image=customtkinter.CTkImage(Image.open(HomeScreen.__current_path + "/assets/visibility_off.png"), size=(28,28)))
            HomeScreen.a= customtkinter.CTkImage(Image.open(HomeScreen.__current_path + "/assets/visibility_off.png"), size=(28,28))
    def acess():
        psw= HomeScreen.__entryPass.get()
        user= HomeScreen.__entryUser.get()
        if True == reservas.validar(psw, user):
            print("errado")
        else:
            HomeScreen.window.frame_image.destroy()
            HomeScreen.window.destroy()
            HomeScreen.app = 1
            print(HomeScreen.app)



a= HomeScreen
a()
