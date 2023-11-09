
import customtkinter as ctk
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from mysql.connector import (connection)
import time
from reportlab.lib.enums import TA_JUSTIFY
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch

ctk.set_appearance_mode('dark')

class App():
    dados = {'Nome':'','Telefone':'','Minibio':'','Entrevista':'','Teorico':'','Pratico':'','Soft_Skills':''}
    dadosSearch = {'Entrevista':'','Teorico':'','Pratico':'','Soft_Skills':''}
    data = []
    formated = ['Id','Nome', 'Telefone', 'Minibio', 'Entrevista', 'Teorico', 'Pratico', 'Soft_Skills']
    formated_select = ['Nome', 'Entrevista', 'Teorico', 'Pratico', 'Soft_Skills']
    def __init__(self):

        self.__db_conn = connection.MySQLConnection(host='localhost',user='root',password='',database='ent_database')
        self.__cursor = self.__db_conn.cursor()

        self.listarend()
        self.window = ctk.CTk()
        self.window.geometry("800x620")
        self.window.title("Python Work")
        self.window.resizable(False,False)
        self.sidebar()
        self.main_frames()
        self.a = ctk.CTkLabel(self.main_frame,text='Bom Dia!, Seja bem vindo ao sistema de Armazenamento de notas')
        self.a.grid(row=0,column=0, padx=(50, 50), pady=10)
        self.listar()
        
    def cadCreate(self):
        numx = 1
        for item in self.dados.keys():
            ctk.CTkLabel(self.sub_main_frame, text=item).grid(row=numx, padx=(200, 200))
            self.dados[item] = self.entrys(numx+1, item)
            numx+=2
        self.btn = ctk.CTkButton(self.sub_main_frame, text='Cadastrar', fg_color='green', hover_color='darkgreen', command=self.insert).grid(row=numx+2, pady=(50, 20), padx=(200, 200))

    def entrys(self, pad, text):
        stks = ctk.CTkEntry(self.sub_main_frame, placeholder_text=text+': ')
        stks.grid(row=pad, padx=(200, 200))
        return stks

    def only(self):
        self.__cursor.execute(self.createSQLListagem())
        data = self.__cursor.fetchall()
        formated_data = []
        for item in data:
            num = 0
            sub_formated_data = {}
            for i in item:
                sub_formated_data[self.formated_select[num]] = i
                num+=1
            formated_data.append(sub_formated_data)

        self.createPDF(formated_data, 'Candidatos Selecionados')
        # self.pdf.createPDF()
    
    def all(self):
        self.__cursor.execute('SELECT * FROM user')
        data = self.__cursor.fetchall()
        formated_data = []
        sub_formated_data = {}
        for item in data:
            sub_formated_data = {}
            num = 0
            for i in item:
                sub_formated_data[self.formated[num]] = i
                num+=1
            formated_data.append(sub_formated_data)

        self.createPDFAll(formated_data, 'Todos os candidatos')

    def listar(self):
        num = 1
        for item in self.dadosSearch.keys():
            self.dadosSearch[item] = self.entrys(num+1, item)
            num+=1
        self.btn = ctk.CTkButton(self.sub_main_frame, text='Listar', fg_color='green', hover_color='darkgreen', command=self.seleciona).grid(row=num+1)
        self.btn1 = ctk.CTkButton(self.sub_main_frame, text='Pdf Somente Notas', fg_color='green', hover_color='darkgreen', command=self.only).grid(row=num+2 )
        self.btn2 = ctk.CTkButton(self.sub_main_frame, text='Pdf Tudo', fg_color='green', hover_color='darkgreen', command=self.all).grid(row=num+3)
        self.txt = ctk.CTkTextbox(self.sub_main_frame, height=300, width=500, wrap='none')
        self.txt.grid(row=1, column=0, sticky="nsew", pady=(60,0))
        self.lis()

    def lis(self):
        self.txt.configure(state='normal')
        num = 1
        for item in self.data:
            texto = ''
            for i in item.keys():
                if(type(item[i] is int)):
                    texto = texto + i + ': ' + str(item[i]) + ' | '
                else:
                    texto = texto + i + ': ' + item[i]+ ' | '
            self.txt.insert(str(float(num)), texto+'\n')
            num+=1
        self.txt.configure(state='disabled')

    def deleteSelect(self):
        self.txt.configure(state='normal')
        num = self.txt.index('end')
        if(float(num) > 0.0):
            for item in range(int(float(num))):
                self.txt.delete(str(float(item)), "end-1c")
        self.txt.configure(state='disabled')

    def main_frames(self):
        self.main_frame = ctk.CTkFrame(self.window,width=600,height=580)
        self.main_frame.grid(row=0, column=1, padx=90, pady=(10, 0), sticky="ns")
        self.sub_main_frame = ctk.CTkFrame(self.main_frame)
        self.sub_main_frame.grid(row=1, column=0, padx=0, pady=10, sticky="sew")

    def change(self, who):
        if (who):
            self.destruir()
            self.cadCreate()
        else:
            self.destruir()
            self.listar()

    def createPDF(self, dados, name):
        doc = SimpleDocTemplate(name+".pdf",pagesize=letter,
                        rightMargin=72,leftMargin=72,
                        topMargin=72,bottomMargin=18)
        Story = []
        formatted_time = time.ctime()
        styles=getSampleStyleSheet()
        styles.add(ParagraphStyle(name='Justify', alignment=TA_JUSTIFY))
        ptext = '<font size=24>Candidatos Selecionados</font>'
        Story.append(Paragraph(ptext, styles["Justify"]))
        Story.append(Spacer(1, 24))
        ptext = '<font size=12>Data de Criação do Documento: %s</font>' % formatted_time
        Story.append(Paragraph(ptext, styles["Normal"]))
        Story.append(Spacer(1, 12))
        for item in dados:
            ptext = '<font size=12>------------------------------------------------------------------------</font>' 
            Story.append(Paragraph(ptext, styles["Normal"]))
            Story.append(Spacer(1, 6))

            ptext = '<font size=12>Nome: %s </font>' % (item['Nome'])
            Story.append(Paragraph(ptext, styles["Normal"]))
            Story.append(Spacer(1, 6))

            ptext = '<font size=12>Notas de Entrevista: %s | Notas do Teorico: %s |\
            Notas do Pratico: %s | Notas de Soft Skills: %s </font>' % (item['Entrevista'],item['Teorico'],item['Pratico'],item['Soft_Skills'])
            Story.append(Paragraph(ptext, styles["Justify"]))
            Story.append(Spacer(1, 12))
        doc.build(Story)

    def createPDFAll(self, dados , name):
        try:
            doc = SimpleDocTemplate(name+".pdf",pagesize=letter,
                        rightMargin=72,leftMargin=72,
                        topMargin=72,bottomMargin=18)
            Story = []
            formatted_time = time.ctime()
            styles=getSampleStyleSheet()
            styles.add(ParagraphStyle(name='Justify', alignment=TA_JUSTIFY))
            ptext = '<font size=24>Todos os Usuarios</font>'
            Story.append(Paragraph(ptext, styles["Justify"]))
            Story.append(Spacer(1, 24))
            ptext = '<font size=12>Data de Criação do Documento: %s</font>' % formatted_time
            Story.append(Paragraph(ptext, styles["Normal"]))
            Story.append(Spacer(1, 12))
            for item in dados:
                ptext = '<font size=12>------------------------------------------------------------------------</font>' 
                Story.append(Paragraph(ptext, styles["Normal"]))
                Story.append(Spacer(1, 6))

                ptext = '<font size=12>Nome: %s | Telefone: %s </font>' % (item['Nome'],item['Telefone'])
                Story.append(Paragraph(ptext, styles["Normal"]))
                Story.append(Spacer(1, 6))

                ptext = '<font size=12>Minibio: %s</font>' % item['Minibio']
                Story.append(Paragraph(ptext, styles["Normal"]))
                Story.append(Spacer(1, 6))

                ptext = '<font size=12>Notas de Entrevista: %s | Notas do Teorico: %s |\
                Notas do Pratico: %s | Notas de Soft Skills: %s </font>' % (item['Entrevista'],item['Teorico'],item['Pratico'],item['Soft_Skills'])
                Story.append(Paragraph(ptext, styles["Justify"]))
                Story.append(Spacer(1, 12))
            doc.build(Story)
        except Exception as e:
            self._message(e,'Geração do pdf')

    def destruir(self):
        for widgets in self.sub_main_frame.winfo_children():
            widgets.destroy()

    def sidebar(self):
        self.frame = ctk.CTkFrame(self.window)
        self.frame.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="nsw")
        self.img_btn_1 = tk.PhotoImage(file='./img/add.png')
        self.checkbox_1 = ctk.CTkButton(self.frame, width=50,text='', fg_color='gray', image=self.img_btn_1, hover_color='darkgrey', command=lambda: self.change(True))
        self.checkbox_1.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="w")
        self.frame.bind('<Enter>',lambda e: self.getBigger())
        self.frame.bind('<Leave>',lambda e: self.getSmall())
        self.img_btn_2 = tk.PhotoImage(file='./img/list.png')
        self.checkbox_2 = ctk.CTkButton(self.frame, text="", width=55, fg_color='gray', image=self.img_btn_2, hover_color='darkgrey', command=lambda: self.change(False))
        self.checkbox_2.grid(row=1, column=0, padx=10, pady=(10, 380), sticky="w")
        self.checkbox_1.bind('<Enter>',lambda e: self.getBigger())
        self.checkbox_1.bind('<Leave>',lambda e: self.getSmall())
        self.checkbox_2.bind('<Enter>',lambda e: self.getBigger())
        self.checkbox_2.bind('<Leave>',lambda e: self.getSmall())
        self.img_btn_3 = tk.PhotoImage(file='./img/close.png')
        self.btn_3 = ctk.CTkButton(self.frame, text="", width=55, fg_color='gray', image=self.img_btn_3, hover_color='darkgrey', command=self.window.quit)
        self.btn_3.grid(row=5, column=0, padx=10, pady=(10, 10), sticky="w")
        self.btn_3.bind('<Enter>',lambda e: self.getBigger())
        self.btn_3.bind('<Leave>',lambda e: self.getSmall())

    def getBigger(self):
        self.checkbox_1.configure(text='Adiciconar novo Entrevistado')
        self.checkbox_2.configure(text='Listar Entrevistados', width=235)
        self.btn_3.configure(text='Fechar Sistema', width=235)
        self.a.grid(padx=(30, 30))
        self.main_frame.grid(padx=50)
        self.main_frame.configure(width=450)
        
    def getSmall(self):
        time.sleep(0.2)
        self.checkbox_1.configure(text='')
        self.a.grid(padx=(50, 50))
        self.main_frame.grid(padx=90)
        self.checkbox_2.configure(text='', width=60)
        self.btn_3.configure(text='', width=60)
        self.main_frame.configure(width=600)

    # Back-End starts here :)

    def _message(self, message, where, status = False):
        try:
            if(status):
                messages = tk.messagebox.showinfo('Info: '+where,message)
            else:
                messages = tk.messagebox.showerror('Error in '+where,message)
        except Exception as e:
            messages = tk.messagebox.showerror('erro',e)
    

    def insert(self):
        try:
            if(self.testdata()):
                dataD = getattr(self, 'dados')
                sql = self.createSql('user', dataD)
                self.__cursor.execute(sql)
                self.__db_conn.commit()
                self._message('sucesso','insert',True)
            else:
                self._message('Houve um erro inesperado','Inserir')
        except Exception as e:
            self._message(e,'insert')

    def createSQLListagem(self):
        try:
            entry = []
            sql = 'SELECT Nome, Entrevista, Teorico, Pratico, Soft_Skills FROM user WHERE '
            for item in self.dadosSearch.keys():
                if(self.dadosSearch[item].get() != ''):
                    if(type(self.whatType(self.dadosSearch[item].get())) is int):
                        entry.append((self.dadosSearch[item].get(), item))
                    else:
                        raise Exception(f'Os dados do Campo {item} Não é Um numero inteiro. ')
            time = entry[-1]
            for item in range(len(entry)):
                if(entry[item] == time):
                    sql = sql + "( "+str(entry[item][1]) + " BETWEEN " + str(entry[item][0]) + ' AND 10 )'
                else:
                    sql = sql + "( " + str(entry[item][1]) + " BETWEEN " + str(entry[item][0]) + ' AND 10 ) AND '
            return sql
        except Exception as e:
            self._message(f' ERROR: {e} ','Listagem - Back-end')
                

    def listarend(self):
        self.__cursor.execute('SELECT * FROM user')
        data = self.__cursor.fetchall()
        formated_data = []
        sub_formated_data = {}
        for item in data:
            sub_formated_data = {}
            num = 0
            for i in item:
                sub_formated_data[self.formated[num]] = i
                num+=1
            formated_data.append(sub_formated_data)
        self.data = formated_data

    def testdata(self):
        test = 0
        for item in self.dados.keys():
            if(self.dados[item].get() != ''):
                if(test >= 3):
                    try:
                        float(self.dados[item].get())
                        if(self.dado[item].get() >= 11):
                            self._message(self.dados[item].get()+' deveria ser um numero entre 10 e 0','Campos de Notas')
                            return False
                    except:
                        self._message(self.dados[item].get()+' deveria ser numero','Campos de Notas')
                        return False
                test+=1
            else:
                self._message('Existem campos vazios', 'Campos')
                return False
        if(test == 7):
            return True
                    
    def seleciona(self):
        self.__cursor.execute(self.createSQLListagem())
        data = self.__cursor.fetchall()
        formated_data = []
        for item in data:
            num = 0
            sub_formated_data = {}
            for i in item:
                
                sub_formated_data[self.formated_select[num]] = i
                num+=1
            formated_data.append(sub_formated_data)
        self.data = formated_data
        self.deleteSelect()
        self.lis()


    def whatType(self, dados):
        try:
            return int(dados)
        except:
            return str(dados)

    def createSql(self, table, data):
        start = 'INSERT INTO '+table+' ('
        end = ') VALUES ('
        numOfCampos = len(data)
        last = 0
        for item in data.keys():
            last+=1
            if (type(self.whatType(data[item].get())) is int):
                if (last == numOfCampos):
                    start = start+item
                    end = end+data[item].get()
                else:
                    start = start+item+', '
                    end = end+data[item].get()+', '
            else:
                if (last == numOfCampos):
                    start = start+item
                    end = end+"'"+data[item].get()+"'"
                else:
                    start = start+item+', '
                    end = end+"'"+data[item].get()+"', "
        sql = start + end + ')'
        return sql
