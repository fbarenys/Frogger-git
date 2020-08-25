import tkinter as tk
import time

def Winner (canvas,points,root):

    def saveRecord():
        x1 = myEntry.get()
        f = open('puntuations.txt', 'a')
        f.write(f'\n{x1}, {str(points)}')
        f.close()

    def Punct():

        myEntry.destroy()
        insertname.destroy()
        showrec.destroy()

        punctuation=canvas.create_rectangle(200, 100, 600, 300, fill="blue")
        canvas.tag_raise(punctuation)
        f = open('/Users/felixbarenysmarimon/Desktop/UNIVERISTAT/SEGON SEMESTRE/JOC2/puntuations.txt', 'r')
        scores = []
        for i in f.readlines():
            n = i.strip().split(',')
            scores.append(n)

        ordered = sorted(scores, key=lambda x: x[-1], reverse=True)[0:7]
        text = []
        for i in range(len(ordered)):
            text.append(f"{ordered[i][0]} - {ordered[i][1]}")

        canvas.create_text(400, 200, text=str("RECORDS\n\n"+"\n".join(text)))

        returnbt= tk.Button(root,text="Return",command=lambda: [Winner(canvas,points,root), returnbt.destroy()])
        canvas.create_window(400,290,window=returnbt)



    #####BUTTONS AND INSERT ENTRY
    gained = canvas.create_rectangle(200, 100, 600, 300, fill="green")
    canvas.tag_raise(gained)
    canvas.create_text(400, 170,font=14 ,text=str("YOU WON WITH: " + str(points) + " points"))


    canvas.create_text(300,230,text="INSERT YOUR NAME:")
    myEntry = tk.Entry(root,width=20)
    canvas.create_window(300, 260, window=myEntry)

    insertname = tk.Button(root,text="Insert punctuation",command=saveRecord)
    canvas.create_window(500, 260, window=insertname)

    showrec = tk.Button(root,text="Show points record",command=Punct)
    canvas.create_window(400,375 , window=showrec)

    canvas.pack()
    root.update()



def Failer(canvas,root):
    def tryAgain():
        from Main import Game
        start_time = time.time()
        Game(start_time)


    failed = canvas.create_rectangle(200, 100, 600, 300, fill="red")
    canvas.tag_raise(failed)
    canvas.create_text(400,200,font=16,text="YOU FAILED")

    again= tk.Button(root,text="TRY AGAIN",command= lambda: [tryAgain(),again.destroy()] )
    canvas.create_window(400, 250, window=again)
    canvas.update()
