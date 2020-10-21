import requests
import PySimpleGUI as sg
from colorama import init, Fore

init()
yellow = Fore.YELLOW
green = Fore.GREEN

sg.theme('Dark Purple 7')

layout = [
    [sg.Text('Reading BARCODE..............',
             font='Courier 20', key='-TEXT-', pad=(0, 10))],
    [sg.In(enable_events=True, focus=True,
           font='Verdana 20', key="-MESSAGE-", border_width=0, pad=(0, 10))],
]


def request_to(text):
    payload = {'token': 'TEST_TOKEN_123', 'data': text}
    url = "https://api-test.technofield.net/api/data?"
    res = requests.get(url, params=payload)
    sg.popup("Your reading is sent", f"{res.text}")


window = sg.Window('Bar Code listener', layout, margins=(20, 80),
                   text_justification='l',
                   grab_anywhere=False,
                   auto_size_text=False,
                   auto_size_buttons=False,
                   default_button_element_size=(12, 1),
                   finalize=True)

while True:
    event, values = window.read()
    length_of_bar_code = 13  # yesma barcode ko length hala
    if event == "-MESSAGE-":
        text = values['-MESSAGE-']
        if text[-1]=="\n":
            window['-TEXT-'].update('BARCODE successfully read.')
            request_to(text)
            window['-MESSAGE-'].update('')
            window['-TEXT-'].update('Reading BARCODE..............')
    if event == "Exit" or event == sg.WIN_CLOSED:
        break
window.close()
