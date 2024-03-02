import PySimpleGUI as sg

def main():

    layout = [
        [sg.Text("Hello from T")],
        [sg.Button("OK")]
    ]

    window = sg.Window("Demo", layout)

    while True:
        event, values = window.read()

        if event == "OK" or event == sg.WIN_CLOSED:
            break

    window.close()



if(__name__ == "__main__"):
    main()