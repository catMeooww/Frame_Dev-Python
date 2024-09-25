from tkinter import *
import json

windowItens = {
    "properties": [],
    "itens": []
    }

#functions
def addItem(type,textinside,bg,relief,color,width,height,size,place):
    frame = Frame(editor,bg="gray",relief="solid",borderwidth=2)
    what_is = Label(frame,text=type,bg="gray",width=130)

    textInput = StringVar(frame)
    textInput.set(textinside)
    bgInput = StringVar(frame)
    bgInput.set(bg)
    reliefInput = StringVar(frame)
    reliefInput.set(relief)
    colorInput = StringVar(frame)
    colorInput.set(color)
    widthInput = StringVar(frame)
    widthInput.set(width)
    heightInput = StringVar(frame)
    heightInput.set(height)
    sizeInput = StringVar(frame)
    sizeInput.set(size)
    placeInput = StringVar(frame)
    placeInput.set(place)

    frame.pack(side=TOP,pady=5)
    what_is.pack(side=TOP)

    match type:
        case "label"|"button"|"entry"|"checkbox":
            label1 = Label(frame,text="Text:",bg="gray")
            textEntry = Entry(frame,textvariable=textInput,width=10)
            label1.pack(side=LEFT)
            textEntry.pack(side=LEFT)
    match type:
        case "label"|"button"|"entry"|"space"|"checkbox":
            label2 = Label(frame,text="Background:",bg="gray")
            bgEntry = Entry(frame,textvariable=bgInput,width=10)
            label2.pack(side=LEFT)
            bgEntry.pack(side=LEFT)
    match type:
        case "label"|"button"|"entry"|"checkbox":
            label3 = Label(frame,text="Border:",bg="gray")
            reliefEntry = Entry(frame,textvariable=reliefInput,width=10)
            label3.pack(side=LEFT)
            reliefEntry.pack(side=LEFT)
    match type:
        case "label"|"button"|"entry"|"checkbox":
            label4 = Label(frame,text="Color:",bg="gray")
            colorEntry = Entry(frame,textvariable=colorInput,width=10)
            label4.pack(side=LEFT)
            colorEntry.pack(side=LEFT)
    match type:
        case "label"|"button"|"entry"|"space"|"checkbox":
            label5 = Label(frame,text="Width:",bg="gray")
            widthEntry = Entry(frame,textvariable=widthInput,width=10)
            label5.pack(side=LEFT)
            widthEntry.pack(side=LEFT)
    match type:
        case "label"|"button"|"space"|"checkbox":
            label6 = Label(frame,text="Height:",bg="gray")
            heightEntry = Entry(frame,textvariable=heightInput,width=10)
            label6.pack(side=LEFT)
            heightEntry.pack(side=LEFT)
    match type:
        case "label"|"button"|"entry"|"checkbox":
            label7 = Label(frame,text="Font Size:",bg="gray")
            sizeEntry = Entry(frame,textvariable=sizeInput,width=10)
            label7.pack(side=LEFT)
            sizeEntry.pack(side=LEFT)

    label8 = Label(frame,text="Place:",bg="gray")
    placeEntry = Entry(frame,textvariable=placeInput,width=10)
    label8.pack(side=LEFT)
    placeEntry.pack(side=LEFT)
    
    windowItens["itens"].append([type,textInput,bgInput,reliefInput,colorInput,widthInput,heightInput,sizeInput,placeInput])


def startDev():
    name = nameInput.get()
    if name == "":
        nameInput["bg"] = "red"
    else:
        nameInput["bg"] = "white"
        readerBtn['text'] = "Save this Window"
        writerBtn['text'] = "Run Window"
        buildBtn['text'] = "Build Python"
        readerBtn['bg'] = "cyan"
        writerBtn['bg'] = "green"
        buildBtn['bg'] = "orange"
        readerBtn['command'] = saveWindow
        writerBtn['command'] = runWindow
        buildBtn['command'] = buildWindow
        windowConfigs.pack(side=TOP)
        addThings.pack()

def readWindow():
    file = nameInput.get()
    if file == "":
        nameInput["bg"] = "red"
    else:
        try:
            with open(file + ".frame","r") as selected:
                fileData = json.load(selected)
                windowBg.set(fileData["properties"][0])
                windowWidth.set(fileData["properties"][1])
                windowHeight.set(fileData["properties"][2])
                windowBorder.set(fileData["properties"][3])
                for line in fileData["itens"]:
                    print(line)
                    addItem(line[0],line[1],line[2],line[3],line[4],line[5],line[6],line[7],line[8])
        except FileNotFoundError:
            headerInfo["text"] = "Could not find file, creating a new one..."
        startDev()
                
def saveWindow():
    global windowItens
    file = nameInput.get()
    if file == "":
        nameInput["bg"] = "red"
    else:
        savingItens = {
            "properties":[],
            "itens":[]
        }
        savingItens["properties"].extend([windowBg.get(),windowWidth.get(),windowHeight.get(),windowBorder.get()])
        for line in range(len(windowItens["itens"])):
            print(f"Saving: Type:{windowItens["itens"][line][0]}|Text:{windowItens["itens"][line][1].get()}|Bg:{windowItens["itens"][line][2].get()}|Relief:{windowItens["itens"][line][3].get()}|Color:{windowItens["itens"][line][4].get()}|Width:{windowItens["itens"][line][5].get()}|Height:{windowItens["itens"][line][6].get()}|Size:{windowItens["itens"][line][7].get()}|Pos:{windowItens["itens"][line][8].get()}")
            savingItens["itens"].append([windowItens["itens"][line][0],windowItens["itens"][line][1].get(),windowItens["itens"][line][2].get(),windowItens["itens"][line][3].get(),windowItens["itens"][line][4].get(),windowItens["itens"][line][5].get(),windowItens["itens"][line][6].get(),windowItens["itens"][line][7].get(),windowItens["itens"][line][8].get()])
        with open(file + ".frame", "w") as outfile:
            outfile.write(json.dumps(savingItens))

def runWindow():
    testWindow = Tk()
    testWindow.title(f"Running Test: {nameInput.get()}")
    try:
        if windowWidth.get() != "" and windowHeight.get() != "":
            testWindow.geometry(f"{windowWidth.get()}x{windowHeight.get()}")
        testWindowFrame = Frame(testWindow,bg=windowBg.get(),relief=windowBorder.get(),borderwidth=3)
        testWindowFrame.pack(fill=BOTH)
        testingItens = []
        loop = 0
        for thing in windowItens["itens"]:
            borderSize = 0
            match thing[3].get():
                case "ridge"|"raised"|"groove"|"sunken":
                    borderSize = 8
                case "solid"| "flat":
                    borderSize = 2
            
            match thing[0]:
                case "label":
                    testingItens.append(Label(testWindowFrame,text=thing[1].get(),bg=thing[2].get(),relief=thing[3].get(),fg=thing[4].get(),width=int(thing[5].get()),height=int(thing[6].get()),font=("Arial",int(thing[7].get())),borderwidth=borderSize))
                case "button":
                    testingItens.append(Button(testWindowFrame,text=thing[1].get(),bg=thing[2].get(),relief=thing[3].get(),fg=thing[4].get(),width=int(thing[5].get()),height=int(thing[6].get()),font=("Arial",int(thing[7].get())),borderwidth=borderSize))
                case "entry":
                    testingItens.append(Frame(testWindowFrame))
                    if thing[1].get() != "":
                        secondaryItem = Label(testingItens[loop],text=thing[1].get(),font=("Times",7),width=int(int(thing[5].get())*1.4),height=0)
                        secondaryItem.pack(side=TOP)
                    mainItem = Entry(testingItens[loop],bg=thing[2].get(),relief=thing[3].get(),fg=thing[4].get(),width=int(thing[5].get()),font=("Arial",int(thing[7].get())),borderwidth=borderSize)
                    mainItem.pack(side=TOP)
                case "space":
                    testingItens.append(Label(testWindowFrame,text="",bg=thing[2].get(),width=int(thing[5].get()),height=int(thing[6].get())))
                case "checkbox":
                    testingItens.append(Checkbutton(testWindowFrame,text=thing[1].get(),bg=thing[2].get(),relief=thing[3].get(),fg=thing[4].get(),width=int(thing[5].get()),height=int(thing[6].get()),font=("Arial",int(thing[7].get())),borderwidth=borderSize))

            match thing[8].get():
                case "left":
                    testingItens[loop].pack(side=LEFT)
                case "right":
                    testingItens[loop].pack(side=RIGHT)
                case "bottom":
                    testingItens[loop].pack(side=BOTTOM)
                case _:
                    testingItens[loop].pack(side=TOP)
            loop = loop + 1
    except ValueError:
        testWindow.title("Error")
        errorLabel = Label(testWindow,text="Something went wrong (Invalid Value)",bg="red",fg="white",font=("Times",15))
        errorLabel.pack(side=TOP)
    except TclError:
        testWindow.title("Error")
        errorLabel = Label(testWindow,text="Something went wrong (Invalid Property)",bg="red",fg="white",font=("Times",15))
        errorLabel.pack(side=TOP)
    testWindow.mainloop()

def buildWindow():
    file = nameInput.get()
    if file == "":
        nameInput["bg"] = "red"
    else:
        if windowWidth.get() != "" and windowHeight.get() != "":
            winSize = f"win.geometry('{windowWidth.get()}x{windowHeight.get()}')\n"
        else:
            winSize = " "
        
        createCode = f"""
from tkinter import *

#Code generated by FrameDev
#CatMeooww10

#Here's your window {file}:

win = Tk()
win.title('{file}')
{winSize}
mainFrame = Frame(win,bg='{windowBg.get()}',relief='{windowBorder.get()}',borderwidth=3)
mainFrame.pack(fill=BOTH)

#Define functions here:

#Window Elements:

"""

        borderSize = 0
        loop = 1
        for thing in windowItens["itens"]:
            match thing[3].get():
                case "ridge"|"raised"|"groove"|"sunken":
                    borderSize = 8
                case "solid"| "flat":
                    borderSize = 2
            
            match thing[0]:
                case "label":
                    createCode += f"item{loop} = Label(mainFrame,text='{thing[1].get()}',bg='{thing[2].get()}',relief='{thing[3].get()}',fg='{thing[4].get()}',width={thing[5].get()},height={thing[6].get()},font=('Arial',{thing[7].get()}),borderwidth={borderSize})\n"
                case "button":
                    createCode += f"item{loop} = Button(mainFrame,text='{thing[1].get()}',bg='{thing[2].get()}',relief='{thing[3].get()}',fg='{thing[4].get()}',width={thing[5].get()},height={thing[6].get()},font=('Arial',{thing[7].get()}),borderwidth={borderSize})\n"
                case "entry":
                    createCode += f"item{loop} = Frame(mainFrame)\n"
                    if thing[1].get() != "":
                        createCode += f"secondaryItem{loop} = Label(item{loop},text='{thing[1].get()}',font=('Times',7),width=int({thing[5].get()}*1.4),height=0)\n"
                        createCode += f"secondaryItem{loop}.pack(side=TOP)\n"
                    createCode += f"mainItem{loop} = Entry(item{loop},bg='{thing[2].get()}',relief='{thing[3].get()}',fg='{thing[4].get()}',width={thing[5].get()},font=('Arial',{thing[7].get()}),borderwidth={borderSize})\n"
                    createCode += f"mainItem{loop}.pack(side=TOP)\n"
                case "space":
                    createCode += f"item{loop} = Label(mainFrame,text='',bg='{thing[2].get()}',width={thing[5].get()},height={thing[6].get()})\n"
                case "checkbox":
                    createCode += f"item{loop} = Checkbutton(mainFrame,text='{thing[1].get()}',bg='{thing[2].get()}',relief='{thing[3].get()}',fg='{thing[4].get()}',width={thing[5].get()},height={thing[6].get()},font=('Arial',{thing[7].get()}),borderwidth={borderSize})\n"

            match thing[8].get():
                case "left":
                    createCode += f"item{loop}.pack(side=LEFT)\n"
                case "right":
                    createCode += f"item{loop}.pack(side=RIGHT)\n"
                case "bottom":
                    createCode += f"item{loop}.pack(side=BOTTOM)\n"
                case _:
                    createCode += f"item{loop}.pack(side=TOP)\n"
            createCode += "\n"

            loop += 1

        createCode += "\nwin.mainloop()\n"

        with open(file + "_build.py", "w") as outfile:
            outfile.write(createCode)
            print("Generated Python Suscessfuly")

#AddButtons
def addingLabel():
    addItem("label","label","white","flat","black","30","2","10","top")
def addingButton():
    addItem("button","click here","white","ridge","black","30","5","10","top")
def addingEntry():
    addItem("entry","input:","white","solid","black","30"," ","10","top")
def addingSpace():
    addItem("space","","white","","","30","10","","top")
def addingCheckbox():
    addItem("checkbox","is true?","white","flat","black","30","2","10","top")

creator = Tk()
creator.title("Frame Dev")
creator.geometry("1200x580")

#frames
management = Frame(creator)
management.pack(side=TOP,pady=2,padx=1)
title = Label(management,text="Frame Dev - Window Creator",background="blue",relief="raised",fg="white",borderwidth=8,width=1500,font=("Arial",20))
title.pack(side=TOP)
windowConfigs = Frame(management)
footerLabel = Label(creator,text="Created by CatMeooww10 using Python and tkinter",relief="solid",borderwidth=2,width=900)
footerLabel.pack(side=BOTTOM)
itens = Frame(creator,relief="solid",borderwidth=2)
itens.pack(side=LEFT,fill=Y)
itensInfo = Label(itens,text="Add itens to your Window!", width=25)
itensInfo.pack(side=TOP)
box = Canvas(creator)
box.pack(side=LEFT,fill=BOTH,expand=1)
editor = Frame(box,relief="sunken",borderwidth=5)
editor.pack(side=TOP)
editorInfo = Label(editor,text="Itens in your Window",width=135)
editorInfo.pack(side=TOP)

# scrollbar
my_scrollbar = Scrollbar(box, orient=VERTICAL, command=box.yview)
my_scrollbar.pack(side=RIGHT, fill=Y)
box.configure(yscrollcommand=my_scrollbar.set)
box.bind(
    '<Configure>', lambda e: box.configure(scrollregion=box.bbox("all"))
)

box.create_window((0, 0), window=editor, anchor="nw")

#Main Things
windowLoader = Frame(management)
readerBtn = Button(windowLoader,text="Open an existent Window",command=readWindow)
writerBtn = Button(windowLoader,text="Start a new Window",command=startDev)
buildBtn = Button(windowLoader,text="|")
headerInfo = Label(windowLoader,text="<- Name of the file to open or create. (must be in the same folder of the program)          |")
nameInput = Entry(windowLoader,relief="solid",borderwidth=2,width=50,bg="cyan")
nameInput.pack(side=LEFT,padx=4)
buildBtn.pack(side=RIGHT,padx=6)
readerBtn.pack(side=RIGHT,padx=4)
writerBtn.pack(side=RIGHT,padx=4)
headerInfo.pack(side=LEFT)
windowLoader.pack(side=TOP)

windowBg = StringVar(creator,"white")
windowWidth = StringVar(creator,"")
windowHeight = StringVar(creator,"")
windowBorder = StringVar(creator,"flat")
windowBgLabel = Label(windowConfigs,text="Window Background: ")
windowBgEntry = Entry(windowConfigs,textvariable=windowBg)
windowSizeLabel = Label(windowConfigs,text="Window Size: ")
windowWidthEntry = Entry(windowConfigs,textvariable=windowWidth)
windowHeightEntry = Entry(windowConfigs,textvariable=windowHeight)
windowBorderLabel = Label(windowConfigs,text="Border: ")
windowBorderEntry = Entry(windowConfigs,textvariable=windowBorder)
windowBgLabel.pack(side=LEFT)
windowBgEntry.pack(side=LEFT,padx=2)
windowSizeLabel.pack(side=LEFT,padx=2)
windowWidthEntry.pack(side=LEFT)
windowHeightEntry.pack(side=LEFT)
windowBorderLabel.pack(side=LEFT)
windowBorderEntry.pack(side=LEFT,padx=2)

addThings = Frame(itens)
addLabel = Button(addThings,text="Label",width=20,command=addingLabel)
addButton = Button(addThings,text="Button",width=20,command=addingButton)
addEntry = Button(addThings,text="Input",width=20,command=addingEntry)
addSpace = Button(addThings,text="Space",width=20,command=addingSpace)
addCheckbox = Button(addThings,text="Checkbox",width=20,command=addingCheckbox)
addLabel.pack(side=TOP)
addButton.pack(side=TOP)
addEntry.pack(side=TOP)
addSpace.pack(side=TOP)
addCheckbox.pack(side=TOP)

creator.mainloop()