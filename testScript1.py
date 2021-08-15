import PySimpleGUI as sg
import matplotlib
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

fig = matplotlib.figure.Figure(figsize=(3, 2), dpi=100)
t = np.arange(0, 3, .01)
fig.add_subplot(111).plot(t, 2 * np.sin(2 * np.pi * t))

matplotlib.use("TkAgg")

sg.theme('Dark Blue 3')  # please make your windows colorful
user = 'Noel'
password = '1234'
current = 'login'
layout = [
                [sg.Text('Please enter your Name, Address, Phone', justification='center', size=(100, 1))],
                [sg.Text('Username', justification='center', size=(35, 1)), sg.InputText('Noel', key='-USER-')],
                [sg.Text('Password', justification='center', size=(35, 1)), sg.InputText('1234', key='-PASSWORD-')],
                [sg.Button('Submit', expand_x=True), sg.Cancel()]
                ]


def draw_figure(canvas, figure):
    figure_canvas_agg = FigureCanvasTkAgg(figure, canvas)
    figure_canvas_agg.draw()
    figure_canvas_agg.get_tk_widget().pack(side="top", fill="both", expand=1)
    return figure_canvas_agg


def des(screen=0):
    login = [
                [sg.Text('Please enter your Name, Address, Phone', justification='center', size=(100, 1))],
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
        [sg.Text("Plot test 1")],
        [sg.Canvas(key="-CANVAS-")],
        [sg.Text('Chat Below', size=(20, 2))],
        [sg.Text('', key='msg', size=(50, 3))],
        [sg.Input(key='choice', do_not_clear=False)],
        [sg.Button("Ok", key='Send')],
        ]
    screen2 = [
        [sg.Button("DES 1", key='#1', mouseover_colors=('yellow', 'green')),
         sg.Button("DES 2", key='#2', mouseover_colors=('yellow', 'green')),
         sg.Button("DES 3", key='#3', mouseover_colors=('yellow', 'green')),
         sg.Text('', size=(50, 1)),
         sg.Button('Logout', key='logout')],
        [sg.Text("Plot test 2")],
        [sg.Canvas(key="-CANVAS-")],
        [sg.Text('Chat Below', size=(20, 2))],
        [sg.Text('', key='msg', size=(50, 3))],
        [sg.Input(key='choice', do_not_clear=False)],
        [sg.Button("Ok", key='Send')],
    ]
    screen3 = [
        [sg.Button("DES 1", key='#1', mouseover_colors=('yellow', 'green')),
         sg.Button("DES 2", key='#2', mouseover_colors=('yellow', 'green')),
         sg.Button("DES 3", key='#3', mouseover_colors=('yellow', 'green')),
         sg.Text('', size=(50, 1)),
         sg.Button('Logout', key='logout')],
        [sg.Text("Plot test 3")],
        [sg.Canvas(key="-CANVAS-")],
        [sg.Text('Chat Below', size=(20, 2))],
        [sg.Text('', key='msg', size=(50, 3))],
        [sg.Input(key='choice', do_not_clear=False)],
        [sg.Button("Ok", key='Send')],
    ]
    if screen == 1:
        return screen1
    if screen == 2:
        return screen2
    if screen == 3:
        return screen3
    return login


def eventChecker(w):
    global current
    if event == '#1':
        print('numero uno')
        current = 'des1'
    if event == '#2':
        print('numero dos')
        current = 'des2'
    if event == '#3':
        print('numero dos')
        current = 'des3'
    if event == 'logout':
        w.close()
        current = 'login'
        lay = des()
        global window
        window = sg.Window('New', lay, size=(700, 500))
        print('logged out!')


window = sg.Window('Simple data entry window', layout, size=(700, 500))

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    if current == 'login' or event == 'loginEvent':
        if values['-USER-'] == user and values['-PASSWORD-'] == password:
            print('Your logged in')
            isLoggedIn = True
            current = 'des1'
    if current == 'des1' or event == '#1':
        window.close()
        lay = des(1)
        window = sg.Window('Data exploration Screen #1', lay, size=(700, 500), finalize=True)
        draw_figure(window["-CANVAS-"].TKCanvas, fig)
        eventChecker(window)
    if current == 'des2' or event == '#2':
        window.close()
        lay = des(2)
        window = sg.Window('Data exploration Screen #2', lay, size=(700, 500), finalize=True)
        draw_figure(window["-CANVAS-"].TKCanvas, fig)
        eventChecker(window)
    if current == 'des3' or event == '#3':
        lay = des(3)
        window.close()
        window = sg.Window('Data exploration Screen #3', lay, size=(700, 500), finalize=True)
        draw_figure(window["-CANVAS-"].TKCanvas, fig)
        eventChecker(window)
window.close()
