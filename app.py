import time
import pandas as pd
import PySimpleGUI as sg


df_itens = pd.read_csv('data/item.csv')

sg.theme('Black')

layout = [ [sg.Text('    ━━━━━━━━━━━━━━━━ ∎\n    ┃ Monster Hunter - Database\n    ━━━━━━━━━━━━━━━━ ∎')],
           [sg.Text(' ')],
           [sg.Button('Quests'), sg.Button('Monstros'), sg.Button('Itens'), sg.Button('Mix Sets')],
           [sg.Text('_'*30)]  ]





window = sg.Window('MHFU - Database', layout,  element_justification='c')



while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break


    if event == 'Quests':
        layout_quest = [ [sg.Text('∎ Selecione Rank de Quest')],
                         [sg.Text(' ')],
                         [sg.Button('Elder Quests'), sg.Button('Nekoht Quests')],
                         [sg.Button('GH Low Quests'), sg.Button('GH High Quests'), sg.Button('GH High Quests')],
                         [sg.Text('_'*30)]  ]

        quest_window = sg.Window('MHFU - Quest List', layout_quest, element_justification='c')

        while True:
            event, values = quest_window.read()



            if event == sg.WIN_CLOSED:
                break




    if event == 'Monstros':
        layout_monster = [ [sg.Text('∎ Digite abaixo o nome do Monstro')],
                           [sg.Text(' ')],
                           [sg.Input()],
                           [sg.Button('Pesquisar')],
                           [sg.Text('_'*30)]  ]
        
        monster_window  = sg.Window('MHFU - Lista de Monstros', layout_monster, element_justification='c')
        
        while True:
            event, values = monster_window.read()

            if event == 'Pesquisar':
                print('Monstro')



            if event == sg.WIN_CLOSED:
                break
            


    if event == 'Itens':
        layout_item = [ [sg.Text('∎ Digite abaixo o nome do Item')],
                           [sg.Text(' ')],
                           [sg.Input(key='item_find')],
                           [sg.Button('Pesquisar')],
                           [sg.Text('_'*30)],
                           [sg.Output(size=(80, 10))]  ]

        item_window  = sg.Window('MHFU - Lista de Monstros', layout_item, element_justification='c')

        while True:
            event, values = item_window.read()
            
            print(df_itens[['name', 'description']].sample(6))

            if event == 'Pesquisar':
                item_find = values['item_find'].title()
                localize_item = df_itens[df_itens['name'] == item_find]

                if localize_item.empty:
                    sg.popup('Nenhum item com esse nome 🤔')

                else:
                    sg.Print( localize_item )

            if event == sg.WIN_CLOSED:
                break



    if event == 'Mix Sets':
        layout_mix = [ [sg.Text('∎ Selecione Rank de Quest')],
                         [sg.Text(' ')],
                         [sg.Button('LR Mix Sets'), sg.Button('HR Mix Sets'), sg.Button('GR Mix Sets')],
                         [sg.Text('_'*30)]  ]

        mix_window = sg.Window('MHFU - Quest List', layout_mix, element_justification='c')

        while True:
            event, values = mix_window.read()



            if event == sg.WIN_CLOSED:
                break