# Importing all needed packages
import PySimpleGUI as sg
import matplotlib
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# setting up the size of graph
fig = matplotlib.figure.Figure(figsize=(3, 2), dpi=100)
# data to be rendered
t = np.arange(0, 3, .01)
# plotting data
fig.add_subplot(111).plot(t, 2 * np.sin(2 * np.pi * t))

matplotlib.use("TkAgg")

sg.theme('Dark Blue 3')  # please make your windows colorful
# login credentials for testing purposes
user = 'Noel'
password = '1234'
# scene Variable to indicate where the program is in its lifecycle
current = 'login'

# function that draws the graph onto the canvas
# must be executed after the canvas has been rendered.
def draw_figure(canvas, figure):
    figure_canvas_agg = FigureCanvasTkAgg(figure, canvas)
    figure_canvas_agg.draw()
    figure_canvas_agg.get_tk_widget().pack(side="top", fill="both", expand=1)
    return figure_canvas_agg

# function that returns the layout i need by the screen number 0 being login, 1 being screen 1, 2 being screen 2 and 3 being screen 3.
def des(screen=0):
    login = [
        [sg.Text('Please enter your login credentials', justification='center', size=(100, 1))],
        # input values are there but later will add login finctionality.
        [sg.Text('Username', justification='center', size=(35, 1)), sg.InputText('Noel', key='-USER-')],
        [sg.Text('Password', justification='center', size=(35, 1)), sg.InputText('1234', key='-PASSWORD-')],
        [sg.Button('Submit', key='loginEvent', expand_x=True), sg.Cancel()]
    ]
    screen1 = [
        [sg.Button("DES 1", key='#1', mouseover_colors=('yellow', 'green')),
         sg.Button("DES 2", key='#2', mouseover_colors=('yellow', 'green')),
         sg.Button("DES 3", key='#3', mouseover_colors=('yellow', 'green')),
         sg.Text('', size=(50, 1)),
         sg.Button('Logout', key='logout')],
        [sg.Text("Plot test 1", expand_x=True, justification='center')],
        [sg.Canvas(key="-CANVAS-", expand_x=True)],
        [sg.Text('Chat Below', size=(20, 2), expand_x=True, justification='center')],
        [sg.Text('Messages are shown here!', key='msg', size=(50, 3), expand_x=True)],
        [sg.Input(key='choice', do_not_clear=False, expand_x=True)],
        [sg.Button("Ok", key='Send', expand_x=True)],
    ]
    screen2 = [
        [sg.Button("DES 1", key='#1', mouseover_colors=('yellow', 'green')),
         sg.Button("DES 2", key='#2', mouseover_colors=('yellow', 'green')),
         sg.Button("DES 3", key='#3', mouseover_colors=('yellow', 'green')),
         sg.Text('', size=(50, 1)),
         sg.Button('Logout', key='logout')],
        [sg.Text("Plot test 2", expand_x=True)],
        [sg.Canvas(key="-CANVAS-", expand_x=True)],
        [sg.Text('Chat Below', expand_x=True, justification='center')],
        [sg.Text('Mssages are shown here!', key='msg', size=(50, 3), expand_x=True)],
        [sg.Input(key='choice', do_not_clear=False, expand_x=True)],
        [sg.Button("Ok", key='Send', expand_x=True)],
    ]
    screen3 = [
        [sg.Button("DES 1", key='#1', mouseover_colors=('yellow', 'green')),
         sg.Button("DES 2", key='#2', mouseover_colors=('yellow', 'green')),
         sg.Button("DES 3", key='#3', mouseover_colors=('yellow', 'green')),
         sg.Text('', size=(50, 1)),
         sg.Button('Logout', key='logout')],
        [sg.Text("Plot test 3", expand_x=True)],
        [sg.Canvas(key="-CANVAS-", expand_x=True)],
        [sg.Text('Chat Below', size=(20, 2), expand_x=True, justification='center')],
        [sg.Text('Mssages are shown here!', key='msg', size=(50, 3), expand_x=True)],
        [sg.Input(key='choice', do_not_clear=False, expand_x=True)],
        [sg.Button("Ok", key='Send', expand_x=True)],
    ]
    if screen == 1:
        return screen1
    if screen == 2:
        return screen2
    if screen == 3:
        return screen3
    return login

# initial login layout on start up
layout = des()


def event_checker(w):
    if event == '#1':
        print('Rendering: Screen1')
        return 'des1'
    elif event == '#2':
        print('Rendering: Screen2')
        return 'des2'
    elif event == '#3':
        print('Rendering: Screen3')
        return 'des3'
    elif event == 'logout':
        # if it is a logout event we close the current window by passing it as an arg
        w.close()
        # login_screen becomes a layout list by calling the des func which returns a login list layout if no args or 0 is input
        login_screen = des()
        # create new global window
        global window
        # open new window, with new layout
        window = sg.Window('New', login_screen, size=(700, 500))
        print('User is logged out.')
        return 'login'

# closes the current 
# takes the window obj and a number presumed to be either 0, 1, 2 or 3

def des_render(w, num):
    w.close()
    # VARIABLE equals a new layout that corresponds to function num value
    layout_instance = des(num)
    # new global window obj 
    global window
    # window equals a new PySimpleGUI.Window(screen name, layout, other methods)
    window = sg.Window('Data exploration Screen #' + str(num), layout_instance, size=(700, 500), finalize=True)
    # added draw figure for the graph to render properly
    draw_figure(window["-CANVAS-"].TKCanvas, fig)
    # returns the event checker function with window as the first arguement
    return event_checker(window)

# first window instance
window = sg.Window('Simple data entry window', layout, size=(700, 500))

while True:
    event, values = window.read()
    # if user clicks exit or the x button break from loop
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    # if current scene is equal to login or the loginEvent is fired
    if current == 'login' or event == 'loginEvent':
        # if the username and password entered match local data
        if values['-USER-'] == user and values['-PASSWORD-'] == password:
            # print logged in and change current scene to des1
            print('User logged in')
            current = 'des1'

    if current == 'des1' or event == '#1':
        current = des_render(window, 1)
    if current == 'des2' or event == '#2':
        current = des_render(window, 2)
    if current == 'des3' or event == '#3':
        current = des_render(window, 3)
window.close()
