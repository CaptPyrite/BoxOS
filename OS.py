"""
Version: 1.0.0
"""
try:
    from tkinter import *
    from datetime import datetime
    from PIL import ImageTk
    import PIL.Image
    import pyautogui
    from sys import platform
    import tkinterweb
    import os
    import random
    from tkinter import ttk
    import subprocess
    from tkinter.ttk import Progressbar
    import html
    import requests
    
    bg = open("Data/Background.txt","r").read()
    x,y = pyautogui.size()
    apps=[]
    files_and_directories = []
    WIFI = True
    Update_required = False
    
    '''

    Update checker
    
    '''
    try:
        OS_URL = "https://raw.githubusercontent.com/FahimFerdous1/BoxOS/main/OS.py"
        n_os_code = requests.get(OS_URL, timeout=10)
        OS_code_lines = []
        version_on_github = str(html.unescape(n_os_code.text)).split("\n")[1]
        version_on_github = version_on_github.split('\t')[0].replace(" ","").replace("\r","").replace("\n","")        
        with open("OS.py","r") as os_source:
            for i in os_source.readlines():
                OS_code_lines.append(i)
        
        os_source.close()
        current_OS_ver = str(OS_code_lines[1].split(":")[1]).replace(" ","").replace("\n","")
        git_OS_ver = str(version_on_github.split(":")[1])
        
        if current_OS_ver==git_OS_ver:
            Update_required = False
            
        elif current_OS_ver!=git_OS_ver:
            Update_required = True
        
    except (requests.ConnectionError, requests.Timeout) as e:
        WIFI = False
    
    '''

    Core functions

    '''
    def get_dirs():
        del files_and_directories[:]
        for files in os.listdir("system_drive"):
            files_and_directories.append(str(files))
    
    def update_dirs():
        return(get_dirs())
    
    def delete_file(file):
        if os.path.exists(file):
            os.remove(file)
        else:pass
    
    def toggle():
        global start_btn_funtc
        if start_btn.config('text')[-1] == 'af':
            start_btn.config(text='rf')
            start_btn_funtc.place(x=0,y=y-420)
            
        else:
            start_btn.config(text='af')
            start_btn_funtc.place_forget()  
    
    def clear_screen():
       for widgets in tk.winfo_children():
           print(f"[sys update] removed {widgets}")
           widgets.destroy()
    
     
    
    #APPS
    class initials():  
      def check_if_exists(_list_,item):
        return(item in _list_)
        
      def make_hash(name):
        alphabet = ('abcdefghijklmnopqurstuvwxzABCDEFGHIJKLMNOPQURSTUVWXYZ1234567890')
        create_HASH = "_"+str("".join(random.sample(alphabet,18)))
        
        return(name.split(" ")[0]+create_HASH)
      
      def verifiy_hash(app_name,apps):
        OUTPUT_HASH = initials.make_hash(app_name)

        if initials.check_if_exists(apps,OUTPUT_HASH)==True:
          OUTPUT_HASH = initials.make_hash(app_name)
          apps.append(OUTPUT_HASH)
          return(OUTPUT_HASH)
          
        elif initials.check_if_exists(apps,OUTPUT_HASH)==False:  
          apps.append(OUTPUT_HASH)
          return(OUTPUT_HASH)
        
        
      def remove_from_apps(apps,hash_):
        apps.remove(hash_)
      
    
    def make_draggable(widget,btn="<Button-1>",motion="<B1-Motion>"):
        def __draggable__(widget):
            widget.bind(btn, on_drag_start)
            widget.bind(motion, on_drag_motion)
        
        def on_drag_start(event):
            widget = event.widget
            widget._drag_start_x = event.x
            widget._drag_start_y = event.y
        
        def on_drag_motion(event):   
            widget = event.widget
            x = widget.winfo_x() - widget._drag_start_x + event.x
            y = widget.winfo_y() - widget._drag_start_y + event.y
            widget.place(x=x, y=y)
            
        __draggable__(widget)


   #API
    def create_app(master,bg,title,app_ui,keep_in_initials=True):
        main = Frame(master,bg="#C0C0C0",width=750,height=500)
        make_draggable(main)
        if keep_in_initials == True:
            generated_hash = initials.verifiy_hash(title,app_ui)
            exit_btn = Button(main,text='X',bg='#FF0000',fg='black',width=4,height=2,borderwidth=0,command=lambda:[main.destroy(),initials.remove_from_apps(app_ui,generated_hash)])
        
        else:
            exit_btn = Button(main,text='X',bg='#FF0000',fg='black',width=4,height=2,borderwidth=0,command=lambda:main.destroy())
                    
        
        exit_btn.place(x=716,y=0)
        
        main.pack() 
        create_app.MAIN_ = Frame(main,bg=bg,width=750,height=463)
        create_app.MAIN_.place(x=0,y=37)
        return(create_app.MAIN_)   


    def create_app_type2(master,bg,title,X,Y,app_ui,keep_in_initials=True):
        main = Frame(master,bg="#C0C0C0",width=X,height=Y)
        if keep_in_initials == True:
            generated_hash = initials.verifiy_hash(title,app_ui)
            exit_btn = Button(main,text='X',bg='#FF0000',fg='black',width=4,height=2,borderwidth=0,command=lambda:[main.destroy(),initials.remove_from_apps(app_ui,generated_hash)])
        
        else:
            exit_btn = Button(main,text='X',bg='#FF0000',fg='black',width=4,height=2,borderwidth=0,command=lambda:main.destroy())
            
        
        exit_btn.place(x=(X-34), y=0)
        
        make_draggable(main)
        main.pack()
        
        MAIN_ = Frame(main,bg=bg,width=X,height=Y-37)
        MAIN_.place(x=0, y=37)
        
        return(main)
    
    
        
    #init
    tk = Tk()
    
    
    
    
    #login_screen
    tk.attributes("-fullscreen", True)
    tk.configure(cursor='left_ptr')
    tk.title('Box OS')
    
    tk.configure(background=bg)
    
    

    file1 = PIL.Image.open("Data/start.png")
    new_img1 = file1.resize((280,280),PIL.Image.ANTIALIAS)
    graph_img1 = ImageTk.PhotoImage(new_img1)
        
        
    bg_icon = Label(tk,image=graph_img1,
                    bg=bg,activebackground='#272822',
                    borderwidth=0)
        
     
    bg_icon.place(anchor="c",relx=.5,rely=.5)
  
    filename = 'Data/start.png'
    img = PIL.Image.open(filename)
    img.save('logo.ico')
    tk.iconbitmap('logo.ico')
    
    
    
    '''
    
    Settings
    
    '''
    
    #Apps.settigns{   (72-137) 
    
    #App template
    def TEMPLATE_APP_SETTIGNS():
        
        main = create_app(tk, "white", "Settings",apps)    
    
    
        
        Place_holder_frame1 = Frame(main,height=120,width=250,bg="white",highlightbackground="Black",highlightthickness=4,bd=0).place(x=50,y=80)
        Place_holder_frame2 = Frame(main,height=160,width=250,bg="white",highlightbackground="Black",highlightthickness=4,bd=0).place(x=480,y=80)
        #Place_holder_frame3 = Frame(main,height=170,width=250,bg="white",highlightbackground="Black",highlightthickness=4,bd=0).place(x=50,y=240)
     
        BGLABEL = Label(main,text="Background: ",font=("default", 15),bg="white").place(x=120,y=85)
        BGCOLOR = Label(main,text="Color: ",font=("default", 12),bg="white").place(x=65,y=125)
        
        
        bg_color_input = Entry(main,font=("default", 10),borderwidth=4)
        bg_color_input.insert(0, bg)
        bg_color_input.place(x=120,y=125)
        
        
        LOGINLABEL = Label(main,text="Login: ",font=("default", 15),bg="white").place(x=570,y=85)
        USRLABEL  = Label(main,text="Username: ",font=("default", 12),bg="white").place(x=490,y=125)
        USRLABEL_input = Entry(main,font=("default", 8),borderwidth=4,highlightthickness=0)
        USRLABEL_input.insert(0,open("Data/Login.txt").read())
        
        USRLABEL_input.place(x=575,y=125)
    
        PASSLABEL  = Label(main,text="Password: ",font=("default", 12),bg="white").place(x=490,y=175)  
        PASSLABEL_input = Entry(main,font=("default", 8),borderwidth=4,highlightthickness=0)
        PASSLABEL_input.insert(0,open("Data/Password.txt").read())
        
        PASSLABEL_input.place(x=575,y=175) 
        
        
        def FILE_UPDATE():
            
            PASSWORD_FILE = open("Data/Password.txt","w")
            LOGIN_ID_FILE = open("Data/Login.txt","w") 
            BG_FILE = open("Data/Background.txt","w")
            
            print(PASSLABEL_input.get(),USRLABEL_input.get(),bg_color_input.get())
            
            PASSWORD_FILE.write(PASSLABEL_input.get())
            LOGIN_ID_FILE.write(USRLABEL_input.get())
            BG_FILE.write(bg_color_input.get())        
            
    
        x = Button(main,text='Save Settings',font=("default",15),borderwidth=0,
                   bg="lime",
                   activebackground='LawnGreen',
                   fg="black",command=FILE_UPDATE)
        
        x.place(x=490,y=350)
        
        
    #clasic
    APP_1 = 'apps/settings.png'
    APP_1 = PIL.Image.open(APP_1)
    APP_1 = APP_1.resize((48,48),PIL.Image.ANTIALIAS)
    APP_1 = ImageTk.PhotoImage(APP_1)
    
    
    APP_start_btn1 = Button(tk,image=APP_1,
                            activebackground=bg,bg=bg,
                            borderwidth=0,command=TEMPLATE_APP_SETTIGNS)
    
    make_draggable(APP_start_btn1)
    APP_start_btn1.place(x=0,y=y-1070)
    
    
    #}
    
    '''
    
    Terminal
    
    '''
    
    #Apps.terminal{   (72-137) 
    
    #App template
    def TEMPLATE_APP_TERMINAL():
        number = 0
        main = create_app(tk, "#34495e", "Terminal",apps)
        INP = Entry(main,borderwidth=0,bg="#34495e",fg="lime",font=("bold 13"),width=150,highlightthickness=0)
        INP.place(x=45,y=50)
        LABEL = Label(main,text='>>>',fg="lime",bg="#34495e",font=("bold 11")).place(x=10,y=50)
        INP.focus_set()
        def COMMAND(x):
            if INP.get() != "":
                OUTPUT.config(state="normal")
                OUTPUT.delete('1.0', END)
                #OUTPUT.insert(END, )
                #str(INP.get())
                CMD_text = str(INP.get())#.lower()
                if CMD_text == "help":
                    OUTPUT.delete("1.0",END)
                    OUTPUT.insert(END,open("Data/Terminal_Help.txt","r").read())
                
                elif "cat" in CMD_text:
                    OUTPUT.delete("1.0",END)
                    try:
                        F_name = CMD_text.split(" ")[1]
                        OUTPUT.insert(END,open(f"system_drive/{F_name}","r").read())
                    except:
                        pass
                elif "python3" in CMD_text:
                    OUTPUT.delete("1.0",END)
                    try:
                        F_name = CMD_text.split(" ")[1]
                        command = f"python3 system_drive/{F_name}"
                        process = subprocess.Popen(command,stdout=subprocess.PIPE, stderr=subprocess.PIPE,shell=True)
                        output_result, error = process.communicate()
                        
                        
                        OUTPUT.insert("1.0",output_result)
                        OUTPUT.insert("1.0",error)
                        
                        
                    except:
                        pass
                    
                elif CMD_text == "ls":
                    OUTPUT.delete("1.0",END)
                    OUTPUT.insert(END,str(os.listdir("system_drive")).replace("[","").replace("]","").replace("'",""))
                
                elif CMD_text == "tm":
                    OUTPUT.delete("1.0",END)
                    for app_list in apps:
                       OUTPUT.insert(END,str(app_list).split("_")[0]+"\n")
               
                elif CMD_text == "clear":
                   OUTPUT.delete("1.0",END)
                
                elif CMD_text == "BoxOS-update":
                    if Update_required == False:
                        OUTPUT.insert(END,"BoxOS is on the latest verson")

                    elif Update_required == True:
                        OUTPUT.insert(END,"Install the newest version of BoxOS from: `https://github.com/FahimFerdous1/BoxOS`")
                
                elif CMD_text == "BoxOS-version -s":
                    OUTPUT.insert(END,f"BoxOS running on version {current_OS_ver}")

                    
                elif CMD_text == "BoxOS-version -g":
                    OUTPUT.insert(END,f"Newest version of BoxOS: {git_OS_ver}")

                    
                else:
                    OUTPUT.delete("1.0",END)
                    OUTPUT.insert(END,f"{CMD_text} is not a vaild command")                
                
                OUTPUT.config(state="disabled")
            else:
                pass
        #
        OUTPUT = Text(main,fg="lime",bg="#34495e",borderwidth=0,height=15,width=60,font=("bold 16"))
        OUTPUT.place(x=10,y=70)
        OUTPUT.config(state="disabled")

        
        
        INP.bind('<Return>', COMMAND)
        
        
        #clasic
    APP_2 = 'apps/Terminal.png'
    APP_2 = PIL.Image.open(APP_2)
    APP_2 = APP_2.resize((48,48),PIL.Image.ANTIALIAS)
    APP_2 = ImageTk.PhotoImage(APP_2)
    
    
    APP_start_btn2 = Button(tk,image=APP_2,
                            activebackground=bg,bg=bg,
                            borderwidth=0,command=TEMPLATE_APP_TERMINAL)
    
    make_draggable(APP_start_btn2)
    APP_start_btn2.place(x=0,y=y-1000)
    
    
    #}
    
    
    
    '''
    
    Calculator
    
    '''
    
    
    #App template
    
    def TEMPLATE_APP_CALCULATOR():
        main = create_app_type2(tk, "white", "calculator", 350, 600,apps)
        
        
        IN_OUT = Entry(main,font=("Bold 60"),borderwidth=7)
        IN_OUT.place(width=340,x=5,y=50)
        
        def NUMBER(x):
            current = IN_OUT.get()
            IN_OUT.delete(0, END)
            IN_OUT.insert(0,str(current)+str(x))
    
        def CLEAR():
            IN_OUT.delete(0, END)
            
        def MATH():
            math_expression = IN_OUT.get()
            CLEAR()
            IN_OUT.insert(0,str(eval(math_expression)))
            
            
        Button1 = Button(main,text="1",font=("Bold 20"),bd=15,highlightthickness=0,command=lambda: NUMBER(1)).place(x=20,y=200)
        Button2 = Button(main,text="2",font=("Bold 20"),bd=15,highlightthickness=0,command=lambda: NUMBER(2)).place(x=100,y=200)
        Button3 = Button(main,text="3",font=("Bold 20"),bd=15,highlightthickness=0,command=lambda: NUMBER(3)).place(x=180,y=200)
        Button4 = Button(main,text="4",font=("Bold 20"),bd=15,highlightthickness=0,command=lambda: NUMBER(4)).place(x=260,y=200)
        
        Button5 = Button(main,text="5",font=("Bold 20"),bd=15,highlightthickness=0,command=lambda: NUMBER(5)).place(x=20,y=300)
        Button6 = Button(main,text="6",font=("Bold 20"),bd=15,highlightthickness=0,command=lambda: NUMBER(6)).place(x=100,y=300)
        Button7 = Button(main,text="7",font=("Bold 20"),bd=15,highlightthickness=0,command=lambda: NUMBER(7)).place(x=180,y=300)
        Button8 = Button(main,text="8",font=("Bold 20"),bd=15,highlightthickness=0,command=lambda: NUMBER(8)).place(x=260,y=300)
        
        Button9 = Button(main,text="9",font=("Bold 20"),bd=15,highlightthickness=0,command=lambda: NUMBER(9)).place(x=20,y=400)
        Button0 = Button(main,text="0",font=("Bold 20"),bd=15,highlightthickness=0,command=lambda: NUMBER(0)).place(x=100,y=400)
    
    
        Button_Add = Button(main,text="+",font=("Bold 20"),highlightthickness=0,bd=15,command=lambda:NUMBER("+")).place(x=180,y=400)
        Button_Minus = Button(main,text="-",font=("Bold 20"),highlightthickness=0,bd=15,command=lambda:NUMBER("-")).place(x=260,y=400)
    
        Button_divid = Button(main,text="/",font=("Bold 20"),highlightthickness=0,bd=15,command=lambda:NUMBER("/")).place(x=20,y=500)
        Button_multiply = Button(main,text="*",font=("Bold 20"),highlightthickness=0,bd=15,command=lambda:NUMBER("*")).place(x=100,y=500)
        
        Button_CE = Button(main,text="CE",font=("Bold 17"),highlightthickness=0,bd=15,command=lambda:CLEAR()).place(height=83,x=170,y=500)
        
        Button_equal = Button(main,text="=",font=("Bold 20"),highlightthickness=0,bd=15,command=lambda:MATH()).place(x=260,y=500)
        
        
        
        
        
    #clasic
    APP_3 = 'apps/Calculator.png'
    APP_3 = PIL.Image.open(APP_3)
    APP_3 = APP_3.resize((48,48),PIL.Image.ANTIALIAS)
    APP_3 = ImageTk.PhotoImage(APP_3)
    
    
    APP_start_btn3 = Button(tk,image=APP_3,
                            activebackground=bg,bg=bg,
                            borderwidth=0,command=TEMPLATE_APP_CALCULATOR)
    
    make_draggable(APP_start_btn3)
    APP_start_btn3.place(x=0,y=y-930)
    
    
    #}
    
    
    
    '''
    Notepad
    
    '''
    
    #Apps.Notepad{   (72-137) 
    
    #App template
    
    def TEMPLATE_APP_NOTEPAD(on_start_file=False,file_name=None):
        def Save_file():
            INPUT = File_name_input.get()
            saved_file = open("system_drive/"+str(INPUT),"w")
            
            saved_file.write(str(__Text__.get(1.0, END)))
            
            saved_file.close()
            
        
        main = create_app(tk, "#DCDCDC", "Notepad",apps)
        
        Save_btn = Button(main,bg="lime",fg="black",text="Save File",height=1,bd=0,highlightthickness=0,command=Save_file)
        Save_btn.place(x=0,y=0)
        File_name_text = Button(main,bg="#DCDCDC",fg="black",text="File name:",height=1,highlightthickness=0,bd=0,activebackground="#DCDCDC").place(x=66,y=0)
        
        __Text__ = Text(main,width=700,height=15,font=("default 20"),bd=0,bg="white")
        __Text__.place(x=0,y=20)


        File_name_input = Entry(main,bd=0)
        File_name_input.place(x=135,y=0)
        
        
        if on_start_file != False:
            __Text__.insert("1.0", on_start_file)
            File_name_input.insert(0, file_name)
        
        
        
    #clasic
    APP_4 = 'apps/Notepad.png'
    APP_4 = PIL.Image.open(APP_4)
    APP_4 = APP_4.resize((48,48),PIL.Image.ANTIALIAS)
    APP_4 = ImageTk.PhotoImage(APP_4)
    
    
    APP_start_btn4 = Button(tk,image=APP_4,
                            activebackground=bg,bg=bg,
                            borderwidth=0,command=TEMPLATE_APP_NOTEPAD)
    
    make_draggable(APP_start_btn4)
    APP_start_btn4.place(x=0,y=y-860)
    
    
    #}
    
    #Apps.Google{   (72-137) 
    
    #App template
    
    def TEMPLATE_APP_GOOGLE():
        #pass
        main = create_app(tk, "white", "Google",apps)
        
        frame = tkinterweb.HtmlFrame(main)
        frame.load_website("google.com")
        frame.place(width=750,height=550)    
        
        frame.place(x=0,y=0)
        
        
    #clasic
    APP_5 = 'apps/Chrome.png'
    APP_5 = PIL.Image.open(APP_5)
    APP_5 = APP_5.resize((38,38),PIL.Image.ANTIALIAS)
    APP_5 = ImageTk.PhotoImage(APP_5)
    
    
    APP_start_btn5 = Button(tk,image=APP_5,
                            activebackground=bg,bg=bg,
                            borderwidth=0,command=TEMPLATE_APP_GOOGLE)
    
    make_draggable(APP_start_btn5)
    APP_start_btn5.place(x=5,y=y-790)
    
    
    #File
    def FILE_MANAGER(TYPE="no_return"):
        class File_manager:
            def __init__(self):
                #self.files_and_directories = os.listdir("system_drive")
                self.files_and_directories = get_dirs()
                self.clicked=[]
                self.New_y = 10
                self.APP = create_app(tk, "white", "File-manager",apps,keep_in_initials=False)
                
                for i in files_and_directories:
                    
                    button1 = Button(self.APP, text=str(i),bg="white",fg="black",width=110,borderwidth=0)
                    button1.place(x=0,y=self.New_y)
                    
                    if TYPE == "no_return":
                        button1.configure(command=lambda btn=button1: self.OnClick(btn))
                        
                    else:
                        button1.configure(command=lambda btn=button1: self.Return_press(btn))
                        
                    self.New_y += 30
                
                    
                    def menu_popup(event):
                        try:
                            self.popup.tk_popup(event.x_root, event.y_root, 0)        
                        finally:
                            self.popup.grab_release()
                    
                    def new_file():
                        new_file_gui = create_app_type2(tk, "#DCDCDC", "File-manager.create.new.file", 380, 130, apps, keep_in_initials=False)
                        def SAVE():
                            File = open("system_drive/"+str(f_name.get()),"w")
                            File.write("")
                            File.close()
                            
                        
                        Label(new_file_gui,text="File name: ",bg="#DCDCDC").place(x=15,y=55)
                        f_name = Entry(new_file_gui,bd=0)
                        f_name.place(x=75,y=55)
                        save_btn = Button(new_file_gui,text="Save",highlightthickness=0,bd=0,command=lambda:[SAVE(),self.APP.master.destroy(),File_manager(),new_file_gui.destroy()]).place(x=280,y=100)
                        cancel_btn = Button(new_file_gui,text="Cancel",highlightthickness=0,bd=0,command=lambda:new_file_gui.destroy()).place(x=320,y=100)
                        
                    
                    self.popup = Menu(self.APP, tearoff=0)
                    self.popup.add_command(label="New",command=new_file)
                    self.APP.bind("<Button-3>", menu_popup)
                    
                    if self.New_y > 0:
                        self.m = Menu(button1,tearoff=0)
                        self.m.add_command(label ="Delete",command=lambda:self.delete_delete_file()) 
                        self.m.add_command(label="New",command=new_file)
                        button1.bind("<Button-3>", lambda event, btn2=button1: self.delete_file(event,btn2))
                    
                        
                    
                    elif self.New_y == 0:
                        pass

                    
                    
                        
                    
                
            def delete_delete_file(self):
                #os.remove("system_drive/"+str(self.clicked)[1:-1][1:-1])
                delete_file("system_drive/"+str(self.clicked)[1:-1][1:-1])
                new_file_gui = create_app_type2(tk, "#DCDCDC", "File-manager.create.delete.file", 380, 130, apps, keep_in_initials=False)

                
                delete_ = Button(new_file_gui,highlightthickness=0,text="Delete",bd=0,command=lambda:[self.APP.master.destroy(),new_file_gui.destroy(),File_manager()]).place(x=120,y=50)
                cancel_btn = Button(new_file_gui,highlightthickness=0,text="Cancel",bd=0,command=lambda:new_file_gui.destroy()).place(x=190,y=50)
                #File_manager()
                
        
            def delete_file(self,event,btn):
                def do_popup(event):
                    try:
                        self.m.tk_popup(event.x_root, event.y_root)
                    finally:
                        self.m.grab_release()
        
        
                text = btn.cget("text")
                del self.clicked[:]
                self.clicked.append(text)
                print("Opening menu "+ str(self.clicked)[1:-1][1:-1]+f" X= {event.x} Y={event.y}")
                
                

                
                do_popup(event)                
                
                
            def OnClick(self, btn):
                text = btn.cget("text")
                del self.clicked[:]
                self.clicked.append(text)
                print("Opening system_drive/"+ str(self.clicked)[1:-1][1:-1])
                self.location = "system_drive/"+ str(self.clicked)[1:-1][1:-1]
                TEMPLATE_APP_NOTEPAD(on_start_file=open(self.location,"r").read(),file_name=text)  
                
            def Return_press():
                text = btn.cget("text")
                del self.clicked[:]
                self.clicked.append(text)
                return(self.clicked)                
        
        File_manager()
        

        
    APP_6 = 'apps/File.png'
    APP_6 = PIL.Image.open(APP_6)
    APP_6 = APP_6.resize((48,48),PIL.Image.ANTIALIAS)
    APP_6 = ImageTk.PhotoImage(APP_6)
    
    
    APP_start_btn6 = Button(tk,image=APP_6,
                            activebackground=bg,bg=bg,
                            borderwidth=0,command=FILE_MANAGER)
    
    make_draggable(APP_start_btn6)
    APP_start_btn6.place(x=5,y=y-735)    
    
    #bottom frame
    
    
    
    Bottomframe = Frame(tk,height=100,width=x+100,bg='#272822')
    Bottomframe.place(x=-10,y=y-40)
        
    
    '''
    
    START
    
    '''
    
    start_btn_funtc = Frame(tk,width=230,height=380,bg='#222222')
    
    #start_button
    
    
    
    start_btn_funtc = Frame(tk,width=230,height=380,bg='#222222')
    start_png = 'Data/start.png'
    file2 = PIL.Image.open(start_png)
    
    new_img2 = file2.resize((38,38),PIL.Image.ANTIALIAS)
    
    graph_img2 = ImageTk.PhotoImage(new_img2)
    
    start_btn = Button(tk,image=graph_img2,
                           bg='#272822',activebackground='#272822',
                              borderwidth=0,command=toggle,text='af')
    start_btn.place(x=0,y=y-40)
    
    
    
    
    
    def QUIT_Launcher():
        start_btn.config(text="af")
        start_btn_funtc.place_forget()
        
    #Notepad_starter
    NOTE_PAD_START = Button(start_btn_funtc,bg="#222222",text="Notepad",fg="white",
                            activeforeground="white",bd=0,activebackground="#272822",font=("default 15"),highlightthickness=0,
                            command=lambda:[QUIT_Launcher(),TEMPLATE_APP_NOTEPAD()]).place(x=0,y=0,width=230,height=40)
    
    file = PIL.Image.open("apps/Notepad.png")
    IMG = file.resize((35,35),PIL.Image.ANTIALIAS) 
    TK_PHOTO_IMAGE = ImageTk.PhotoImage(IMG)
    IMG_= Label(start_btn_funtc,image=TK_PHOTO_IMAGE,bg="#222222",highlightthickness=0,
                                  borderwidth=0).place(x=0,y=0)
    
    
    #Calculator_starter
    Calculator_START = Button(start_btn_funtc,bg="#222222",text="Calculator",fg="white",
                            activeforeground="white",bd=0,activebackground="#272822",font=("default 15"),highlightthickness=0,
                            command=lambda:[QUIT_Launcher(),TEMPLATE_APP_CALCULATOR()]).place(x=0,y=50,width=230,height=40)
    
    file__2 = PIL.Image.open("apps/Calculator.png")
    IMG__2 = file__2.resize((35,35),PIL.Image.ANTIALIAS) 
    TK_PHOTO_IMAGE__2 = ImageTk.PhotoImage(IMG__2)
    IMG___2= Label(start_btn_funtc,image=TK_PHOTO_IMAGE__2,bg="#222222",
                                  borderwidth=0).place(x=0,y=50)
    
    
    #Terminal_starter
    Terminal_START = Button(start_btn_funtc,bg="#222222",text="Terminal",fg="white",highlightthickness=0,
                            activeforeground="white",bd=0,activebackground="#272822",font=("default 15"),
                            command=lambda:[QUIT_Launcher(),TEMPLATE_APP_TERMINAL()]).place(x=0,y=100,width=230,height=40)
    
    file__3 = PIL.Image.open("apps/Terminal.png")
    IMG__3 = file__3.resize((35,35),PIL.Image.ANTIALIAS) 
    TK_PHOTO_IMAGE__3 = ImageTk.PhotoImage(IMG__3)
    IMG___3= Label(start_btn_funtc,image=TK_PHOTO_IMAGE__3,bg="#222222",
                                  borderwidth=0).place(x=0,y=100)
    
    
    
    #Settings_starter
    Settings_START = Button(start_btn_funtc,bg="#222222",text="Settings",fg="white",highlightthickness=0,
                            activeforeground="white",bd=0,activebackground="#272822",font=("default 15"),
                            command=lambda:[QUIT_Launcher(),TEMPLATE_APP_SETTIGNS()]).place(x=0,y=150,width=230,height=40)
    
    file__4 = PIL.Image.open("apps/Settings.png")
    IMG__4 = file__4.resize((35,35),PIL.Image.ANTIALIAS) 
    TK_PHOTO_IMAGE__4 = ImageTk.PhotoImage(IMG__4)
    IMG___4= Label(start_btn_funtc,image=TK_PHOTO_IMAGE__4,bg="#222222",
                                  borderwidth=0).place(x=0,y=150)
    
    #Google_starter
    Google_START = Button(start_btn_funtc,bg="#222222",text="Google",fg="white",highlightthickness=0,
                            activeforeground="white",bd=0,activebackground="#272822",font=("default 15"),
                            command=lambda:[QUIT_Launcher(),TEMPLATE_APP_GOOGLE()]).place(x=0,y=200,width=230,height=40)
    
    file__5 = PIL.Image.open("apps/Chrome.png")
    IMG__5 = file__5.resize((30,30),PIL.Image.ANTIALIAS) 
    TK_PHOTO_IMAGE__5 = ImageTk.PhotoImage(IMG__5)
    IMG___5= Label(start_btn_funtc,image=TK_PHOTO_IMAGE__5,bg="#222222",
                                  borderwidth=0).place(x=5,y=200)
    
    
    #shutdown
    def shutdown():
        clear_screen()
        SHUTDOWN_LABEL = Label(text="shuting down",bg="black",fg="white",font=("bold 30"))
        SHUTDOWN_LABEL.place(anchor="c",relx=.5,rely=.5)
        tk.configure(bg="black")
        tk.config(cursor="none")
        
    
    Button(start_btn_funtc,bg="#222222",text="Shutdown",font=("default 12"),borderwidth=0,activebackground="#272822",command=shutdown).place(x=150,y=330)
    
    
      
    #TIME
    
    time_label = Label(tk,font='ariel 20',bg='#272822',fg='#FFFFFF',text='')
    time_label.place(x=x-100,y=y-40)
    time_label.lift()
    
    
    formated_apps = []
    def app_btr():
        del formated_apps[:]
        for i in apps:
            formated_apps.append(i.split("_")[0])
        
    '''
    Crash Handeler
    
    '''
    def Crash():
        Frame(tk,bg="blue",width=x,height=y).place(x=0,y=0)
        bye_text = Label(tk,bg="blue",fg="white",text="System Crash",font=("default 50")).place(anchor="c",relx=.5,rely=.5)
        tk.config(cursor="none")
    '''
    Clock 1
    '''
    def TIME_GUI():
        app_btr()
        now = datetime.now()
        h = now.strftime('%I:%M')
        time_label.config(text=h)
        time_label.after(1000,TIME_GUI)
    
        if len(formated_apps) > 150:
            del formated_apps[:]
            formated_apps.append("CRASH")
            Crash()
        else:
            pass
    
        print(now.strftime('%I:%M:%S :'),formated_apps)
        
        
        tk.configure(background=open("Data/Background.txt","r").read(),cursor='left_ptr')
        APP_start_btn1.configure(bg=open("Data/Background.txt","r").read(),activebackground=open("Data/Background.txt","r").read())
        APP_start_btn2.configure(bg=open("Data/Background.txt","r").read(),activebackground=open("Data/Background.txt","r").read())
        APP_start_btn3.configure(bg=open("Data/Background.txt","r").read(),activebackground=open("Data/Background.txt","r").read())
        APP_start_btn4.configure(bg=open("Data/Background.txt","r").read(),activebackground=open("Data/Background.txt","r").read())
        APP_start_btn5.configure(bg=open("Data/Background.txt","r").read(),activebackground=open("Data/Background.txt","r").read())
        APP_start_btn6.configure(bg=open("Data/Background.txt","r").read(),activebackground=open("Data/Background.txt","r").read())
        bg_icon.configure(bg=open("Data/Background.txt","r").read())
        tk.attributes("-fullscreen", True)
        
        
        #directory update
        update_dirs()
    
        
        #Clearing up stuff in the terminal/ console
        if platform == "linux" or platform == "linux2":
            os.system("clear")
            
        elif platform == "win32":
            os.system("cls")
    
    
    '''
    
    LOGIN SCREEN
    
    '''
    
    
    LOGIN_SCREEN = Frame(tk,bg=bg,width=x,height=y)
    LOGIN_SCREEN.place(x=0,y=0)
    LOGIN_SCREEN.configure(cursor='left_ptr')
    
    LOGIN_FILE = PIL.Image.open('Data/User-img.png')
    LOGIN_FILE = LOGIN_FILE.resize((400,280),PIL.Image.ANTIALIAS)
    LOGIN_FILE = ImageTk.PhotoImage(LOGIN_FILE)
    
    LOGIN_PFP = Label(LOGIN_SCREEN,image=LOGIN_FILE,
                        bg=bg,
                        borderwidth=0)
        
    LOGIN_PFP.place(anchor="s", relx=.5, rely=.5)
    
    #login-main
    usr_name = open("Data/Login.txt").read()
    passw = open("Data/password.txt").read()
    
    def passw_checker(x):
        if passw_input.get() == passw:
            tk.unbind("<Return>")
            LOGIN_SCREEN.destroy()
                
        else:
            pass
      
    usr_label = Label(LOGIN_SCREEN,text=str(usr_name))
    usr_label.place(anchor='c', relx=.5, rely=.52,width=300)
    usr_label.config(font=("Arial", 30))
        
    passw_input = Entry(LOGIN_SCREEN,show='*',justify='center')
    passw_input.place(anchor='c', relx=.5, rely=.6,width=300)
    passw_input.config(font=("Arial", 30))     
    
    tk.bind('<Return>', passw_checker)
    
    
    ACTIVATION = False
    
    def Delete_splash():
        SPLASH_BUTTON.destroy()
        TIME2.place_forget()
        Date.place_forget()
        TIME2.place_forget()
        remainder.place_forget()
    
    SPLASH_BUTTON = Button(tk,bg=bg,width=x-500,height=y-500,activebackground=bg,borderwidth=0,command=Delete_splash)
    SPLASH_BUTTON.place(x=0,y=0)
    TIME2 = Button(tk,text="0:000",fg="white",bg=bg,font=("bold 80"),activeforeground="white",highlightthickness=0,activebackground=bg, borderwidth=0,command=Delete_splash)
    TIME2.place(anchor="c", relx=.5,rely=.5)
    Date = Button(tk,text="%TIME%",fg="white",bg=bg,font=("bold 30"),activeforeground="white",highlightthickness=0,activebackground=bg, borderwidth=0,command=Delete_splash)
    Date.place(anchor="c", relx=.5,rely=.598)
    
    
    remainder = Button(tk,text="(Click to go to login)",fg="white",bg=bg,font=("bold 10"),highlightthickness=0,activeforeground="white",activebackground=bg, borderwidth=0,command=Delete_splash)
    remainder.place(anchor="c", relx=.5,rely=.97)
        
    
    def Clock_2():
        TIME2.after(1000,Clock_2)
        now = datetime.now()
        s = now.strftime('%I:%M %p').lstrip("0").replace(" 0", " ")
        TIME2.config(text=s)
        days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        months = ["Unknown","January","Febuary","March","April","May","June","July","August","September","October","November","December"]
        
        Date.config(text=f"{days[now.weekday()]}, {months[now.month]} {now.day}")
        
        
    '''

    Boot screen
    
    '''
    
    Boot_screen = Frame(bg='#222222',width=x,height=y)
    Boot_screen.pack()
    s = ttk.Style()
    s.theme_use('default')
    s.configure("black.Horizontal.TProgressbar", background='#6a9662',borderwidth=0)
    bar = Progressbar(Boot_screen, length=400, s='black.Horizontal.TProgressbar')
    
    BOOT_ICN = PIL.Image.open("Data/start.png")
    BOOT_ICN = BOOT_ICN.resize((280,280),PIL.Image.ANTIALIAS)
    BOOT_ICN = ImageTk.PhotoImage(BOOT_ICN)
    
    Current_index = 0
    
    def growth_to_bar():
        global Current_index
        bar['value'] += 10
        Current_index += 1
    
    def boot_loading():
        global Current_index
        bar.after(1000,boot_loading)

        if Current_index >= 10:
            Boot_screen.destroy()
            pyautogui.moveTo(x/2,y/2)
            
        else:
            growth_to_bar()
        
    
        
    BOOT_icon = Label(Boot_screen,image=BOOT_ICN,
                    bg="#222222",
                    borderwidth=0)
        
     
    BOOT_icon.place(anchor="c",relx=.5,rely=.5)    
    Boot_screen.config(cursor="none")
    
    bar['value'] = 0
    bar.place(relx=0.5,rely=0.8,anchor="center")


    #End
    Clock_2()
    boot_loading()
    TIME_GUI()
    tk.mainloop()
    delete_file('logo.ico')
    
    
except Exception as e:
    raise Exception(e)
