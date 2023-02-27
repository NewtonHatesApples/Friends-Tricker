import PySimpleGUI as Psg
import sys


layout_init = [
    [Psg.Text('Are you dumb?', expand_x=True)],
    [Psg.Button('Yes', expand_x=True)], [Psg.Button('No', expand_x=True)]
]

Psg.theme_global('TealMono')
window_init = Psg.Window("Are you dumb?", layout=layout_init, size=(300, 200))
i = 0
kill = False


def create_no():
    global i
    global kill
    while kill is False:
        layout = [
            [Psg.Text('Are you dumb?', expand_x=True)],
            [Psg.Button('Yes', expand_x=True)], [Psg.Button('No', expand_x=True)]
        ]
        window_no = Psg.Window('Are you dumb?', layout=layout, size=(300, 200), relative_location=(20 + 20 * i, 20 + 20 * i))
        event_no, values_no = window_no.read()
        while True:
            if event_no == 'Yes':
                window_no.close()
                create_yes()
                i = i + 1
                break
            elif event_no == 'No':
                no_loop()
                i = i + 1
            elif event_no == Psg.WINDOW_CLOSED:
                break
    else:
        sys.exit()


def create_yes():
    global i
    global kill
    layout_yes = [
        [Psg.Text('I know you are dumb!', expand_x=True)],
        [Psg.Button('Quit', expand_x=True)]
    ]
    window_yes = Psg.Window("Are you dumb?", layout=layout_yes, size=(300, 200), relative_location=(20 + 20 * i, 20 + 20 * i))
    event_yes, values_yes = window_yes.read()
    while True:
        if event_yes == 'Quit' or event_yes == Psg.WINDOW_CLOSED:
            window_yes.close()
            kill = True
            i = i + 1
            break


def no_loop():
    global i
    global kill
    i = i + 1
    while kill is False:
        layout = [
            [Psg.Text('Are you dumb?', expand_x=True)],
            [Psg.Button('Yes', expand_x=True)], [Psg.Button('No', expand_x=True)]
        ]
        window_no = Psg.Window('Are you dumb?', layout=layout, size=(300, 200),
                               relative_location=(20 + 20 * i, 20 + 20 * i))
        event_no, values_no = window_no.read()
        while True:
            if event_no == 'Yes':
                window_no.close()
                i = i + 1
                create_yes()
                break
            elif event_no == 'No':
                i = i + 1
                create_no()
            elif event_no == Psg.WINDOW_CLOSED:
                break
    else:
        sys.exit()


while True:
    event_init, values_init = window_init.read()
    if event_init == 'Yes':
        create_yes()
        break
    elif event_init == 'No':
        create_no()
    elif event_init == Psg.WINDOW_CLOSED:
        window_init.close()
        no_loop()
