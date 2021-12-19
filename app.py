import time
import pandas as pd
import numpy  as np
import PySimpleGUI as sg


df_itens   = pd.read_csv('data/item.csv')
df_monster = pd.read_csv('data/monster.csv')
#df_elder_all = pd.read_csv('data/all_quests_elder.csv')
#df_hall_all  = pd.read_csv('data/all_quests_elder.csv')
df_elder_key  = pd.read_csv('data/key_quests_elder.csv')
df_hall_key   = pd.read_csv('data/key_quests_hall.csv')

sg.theme('Black')

def create_table( data, headers, title ):
    layout = [ [sg.Table( values=data,
                          headings=headers,
                          font=('sans-serif', 10),
                          justification='left',
                          display_row_numbers=False,
                          hide_vertical_scroll=True,
                          auto_size_columns=True,
                          num_rows=min(30, len(data)),
                          pad=(25,25) ) ] ]

    window = sg.Window( title, layout, grab_anywhere=False )
    event, values = window.read()
    window.close()

    return None

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
                           [sg.Text('∎ Ou deixe em branco para toda a lista')],
                           [sg.Text(' ')],
                           [sg.Input(key='monster_find')],
                           [sg.Button('Pesquisar')],
                           [sg.Text('_'*30)]  ]
        
        monster_window  = sg.Window('MHFU - Lista de Monstros', layout_monster, element_justification='c')
        
        while True:
            event, values = monster_window.read()

            if event == 'Pesquisar':
                monster = values['monster_find'].title()
                localize_monster = df_monster[df_monster['name'].str.contains(monster)][['name', 'jp_name', 'element', 'weak']]

                if localize_monster.empty:
                    sg.popup('Nenhum monstro com esse nome 🤔')
                
                else:
                    create_table( localize_monster.values.tolist(), list( localize_monster.columns ), 'Monster Data' )

            if event == sg.WIN_CLOSED:
                break
            


    if event == 'Itens':
        layout_item = [ [sg.Text('∎ Digite abaixo o nome do Item')],
                        [sg.Text('∎ Ou deixe em branco para toda a lista')],
                        [sg.Text(' ')],
                        [sg.Input(key='item_find')],
                        [sg.Button('Pesquisar')],
                        [sg.Text('_'*30)] ]

        item_window  = sg.Window('MHFU - Lista de Monstros', layout_item, element_justification='c')

        while True:
            event, values = item_window.read()

            if event == 'Pesquisar':
                item_find = values['item_find'].title()
                df_itens['description'] = df_itens['description'].apply( lambda x: x[:25] + '...')
                df_itens['found']       = df_itens['found'].apply( lambda x: x[:25] + '...')
                localize_item = df_itens[df_itens['name'].str.contains(item_find)][['name', 'found', 'description', 'value']]

                if localize_item.empty:
                    sg.popup('Nenhum item com esse nome 🤔')

                else:
                    create_table( localize_item.values.tolist(), list( localize_item.columns ), 'Item Data' )

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