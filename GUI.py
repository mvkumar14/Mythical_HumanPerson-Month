import PySimpleGUI as sg

# theme colors:
sg.theme('DarkAmber')

# all the stuff inside the window

layout = [
    [sg.Text('Assumptions')],
    [sg.Text('Number of people:'),sg.InputText()]
    ]

# create window
window = sg.Window('Mythical Person-Month',layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Exit': # if the user closes the window or clicks exit button
        break

window.close()