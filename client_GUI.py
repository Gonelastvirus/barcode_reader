import requests
import PySimpleGUI as sg
from colorama import init, Fore
import sys
import keyboard
init()
yellow = Fore.YELLOW
green = Fore.GREEN

sg.theme('Dark Purple 7')

layout = [
     [sg.Text('Reading BARCODE..............',
             font='Courier 20', key='-TEXT-', pad=(0, 10))],
    [sg.In(size=(30, 1), enable_events=True,focus=True, font='Verdana 20', key="-MESSAGE-",border_width=0)],
    [sg.Button('Exit', border_width=0,focus=True, font='Calibri 16')]
]

def request_to(text):
    payload = {'token': 'TEST_TOKEN_123', 'data': text}
    url = "https://api-test.technofield.net/api/data?"
    res = requests.get(url, params=payload)

window = sg.Window('Bar Code listener', layout, margins=(20, 80),
                   text_justification='l',
                   grab_anywhere=False,
                   auto_size_text=False,
                   auto_size_buttons=False,
                   default_button_element_size=(12, 1),
                   finalize=True)
while True:
    event, values = window.read()
    if event=="-MESSAGE-": 
        text = values["-MESSAGE-"]
        if keyboard.is_pressed(57):
            if text=="\n":
                sg.popup("Fill textbox","textbox empty")
            window['-TEXT-'].update('BARCODE successfully read.')
            request_to(text)
            window['-MESSAGE-'].update('')
            window['-TEXT-'].update('Reading BARCODE..............')
        #     request_to(text)
        #     keyboard.press_and_release('ctrl+a')
        #     keyboard.press_and_release('backspace')
        #     keyboard.unhook_all()
        # window['-MESSAGE-'].update()
    if event == "Exit" or event == sg.WIN_CLOSED:
        break
window.close()
