from Frog import *
from Cars import *
from Buttons import Winner,Failer
from Lane import *
from tkinter import *
import time
import keyboard



def Game(start_time):
    points=0

    WIDTH = 800
    HEIGHT = 400

    def stop(answer):
        if answer is True:
            answer = False
        else:
            answer = True


    LANE_HEIGHT = 60
    TOP_WINDOW_SPACE = 40

    speeds = [5, -5, 3, -4, 5]

    lanes = [None] * 5
    for i in range(len(lanes)):
        if i == 4:
            lanes[i] = Lane(0, TOP_WINDOW_SPACE + LANE_HEIGHT * i, 2, 2, speeds[i], LANE_HEIGHT)
        else:
            lanes[i] = Lane(0, TOP_WINDOW_SPACE + LANE_HEIGHT * i, 1, 3, speeds[i], LANE_HEIGHT)

    frog = Frog(WIDTH / 2, lanes[-1].y + LANE_HEIGHT + LANE_HEIGHT / 4, 0, 0, WIDTH, HEIGHT, step=LANE_HEIGHT)



    root = Tk()
    w = Canvas(root, width=WIDTH, height=HEIGHT)

    paused = Button(root, text="PAUSE", command=stop)



    w.pack()



    state=None
    answer= True
    while answer is True:

        points = round(100 - (time.time() - start_time), 1)

        for lane in lanes:
            lane.moveCars()

        # move the frog
        if keyboard.is_pressed("up arrow"):
            frog.moveUp()
        if keyboard.is_pressed("down arrow"):
            frog.moveDown()
        if keyboard.is_pressed("left arrow"):
            frog.moveLeft()
        if keyboard.is_pressed("right arrow"):
            frog.moveRight()

        w.delete("all")
        w.create_rectangle(0, 0, WIDTH, HEIGHT, fill="white")
        w.create_text(400, 15, text=str("POINTS: " + str(points)))
        pausedw = w.create_window(700, 20, window=paused)

        for lane in lanes:
            lane.draw(w)
        frog.draw(w)
        w.update()


        for lane in lanes:
            for vehicle in lane.cars:
                if frog.collision(vehicle) is True:
                    state= False
                    break

        if state== False:
            break

        if points == 0:
            state = False
            break

        if frog.y <= TOP_WINDOW_SPACE:
            state= True
            break

        time.sleep(50 / 1000)

    paused.destroy()

    if state is False:  # if the player has failed
        Failer(w, root)

    elif state is True:  # if the player won
        Winner(w, points, root)
    w.mainloop()


#EXECUTE

start_time = time.time()
Game(start_time)






