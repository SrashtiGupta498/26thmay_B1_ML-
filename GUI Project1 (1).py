import tkinter as tk
from tkinter import ttk
from PIL import ImageTk,Image

app=tk.Tk()
app.title('Restaurant Revenue Predictor')
app.iconbitmap(r'C:\Users\Chouhan\Desktop\Project1\icon-01 (2).ico')
app.maxsize(632,395)
app.minsize(632,395)

bg_image= tk.PhotoImage(file=r'C:\Users\Chouhan\Desktop\Project1\restaurant_image.png')
bg_label= tk.Label(app, image=bg_image)
bg_label.place(x=0, y=0)
bg_label.pack()

canvas=tk.Canvas(app, height=325, width=632)
canvas.pack()


#Bottom part(rest of bottom part below function)
frame=tk.Frame(app, bg='#80c1ff', bd=5,)
frame.place(relx=0.5,rely= 0.85,relwidth=0.75,relheight=0.1,anchor='n')


#Opening year

Opening_date = tk.Variable(app)

tk.Label(app, text='Opening year', bg='#ddf0d3', font=('Helvetica',11)).place(x=25,y=30)
tk.Entry(app,width=20,bg='#ffffff', textvariable=Opening_date).place(x=150,y=30)


#Big city

tk.Label(app, text='Big City', bg='#ddf0d3', font=('Helvetica',11)).place(x=25,y=110)
var=tk.IntVar()
r_button=tk.Radiobutton(app, text="YES",padx = 5, variable=var, value=1, bg='#ddf0d3').place(x=150,y=110)
r_button=tk.Radiobutton(app, text="NO",padx = 20, variable=var, value=2, bg='#ddf0d3').place(x=195,y=110)


#Drop box for type
tk.Label(app, text='Type', bg='#ddf0d3', font=('Helvetica',11)).place(x=25,y=190)
ty=tk.StringVar()
Type=ttk.Combobox(app,width=12,text="Type",values=["Food Court","Inline","Drive Thru","Mobile"],textvariable=ty,state="readonly")
Type.place(x=150,y=190)
Type.current(0)

#linking main file
def register():
    f=open(r'C:\Users\Chouhan\Desktop\Project1\teamproject1 (1).ipynb')
    data=[Opening_date.get(),var.get(),ty.get()]
    query=pd.DataFrame({'Open Date':[Opening_date],
                        'Big Cities':[var],
                        'Type':[ty]
                        })
    x=print(model.predict(query))
    return int(x)

#Bottom part 2

button=tk.Button(frame, text='Genrate Revenue',font=40,command=register)
button.place(relx=0.7,relheight=1,relwidth=0.3,)

label=tk.Label(frame)
label.place(relwidth=0.65,relheight=1)


    
app.mainloop()
