import pandas as pd
import PySimpleGUI as sg
from texts import TextsList

sg.theme('Black')

class MhApp( object ):

    def load_data( self ):
        df_itens = pd.read_csv('data/item.csv')
        df_monster = pd.read_csv('data/monster.csv')
        df_hall_all = pd.read_csv('data/all_quests_hall.csv')
        df_elder_key = pd.read_csv('data/key_quests_elder.csv')
        df_hall_key = pd.read_csv('data/key_quests_hall.csv')

        df_hall_all = df_hall_all[['title', 'goal', 'area', 'reward', 'notes']]
        df_hall_all = df_hall_all.iloc[-3:, :]

        df_elder_key = df_elder_key[['title', 'goal',
                                    'area', 'time', 'reward', 'required', 'star']]
        df_hall_low = df_hall_key[df_hall_key['rank'] < 5][[
            'title', 'goal', 'area', 'time', 'reward', 'rank']]
        df_hall_high = df_hall_key[(df_hall_key['rank'] > 4) & (df_hall_key['rank'] <= 6)][[
            'title', 'goal', 'area', 'time', 'reward', 'rank']]
        df_hall_g = df_hall_key[df_hall_key['rank'] >= 7][[
            'title', 'goal', 'area', 'time', 'reward', 'rank']]

        return df_itens, df_monster, df_hall_all, df_elder_key, df_hall_low, df_hall_high, df_hall_g

    def create_table( self, data, headers, title):
        layout = [[sg.Table(values=data,
                            headings=headers,
                            font=('sans-serif', 10),
                            justification='left',
                            display_row_numbers=False,
                            hide_vertical_scroll=True,
                            auto_size_columns=True,
                            num_rows=min(30, len(data)),
                            pad=(25, 25))]]

        window = sg.Window(title, layout, grab_anywhere=False)
        event, values = window.read()
        window.close()

        return None

    def quests_window( self ):
        layout_quest = [[sg.Text('∎ Selecione Rank de Quest')],
                        [sg.Text(' ')],
                        [sg.Button('Elder Quests'), sg.Button('Nekoht Quests')],
                        [sg.Button('GH Low Quests'), sg.Button(
                            'GH High Quests'), sg.Button('GH G Quests')],
                        [sg.Button('Special Quests')],
                        [sg.Text('_'*30)]]

        quest_window = sg.Window(
            'MHFU - Quest List', layout_quest, element_justification='c')

        while True:
            event, values = quest_window.read()

            if event == 'Elder Quests':
                self.create_table(df_elder_key.sort_values('star').values.tolist(),
                            list(df_elder_key.columns),
                            'Elder Key Quest List')

            if event == 'Nekoht Quests':
                sg.popup('cT ficou com preguiça de pegar :D')

            if event == 'GH Low Quests':
                self.create_table(df_hall_low.sort_values('rank').values.tolist(),
                            list(df_hall_low.columns),
                            'GH Low Key Quest List')

            if event == 'GH High Quests':
                self.create_table(df_hall_high.sort_values('rank').values.tolist(),
                            list(df_hall_high.columns),
                            'GH High Key Quest List')

            if event == 'GH G Quests':
                self.create_table(df_hall_g.sort_values('rank').values.tolist(),
                            list(df_hall_g.columns),
                            'GH G Key Quest List')

            if event == 'Special Quests':
                self.create_table(df_hall_all.values.tolist(),
                            list(df_hall_all.columns),
                            'Special Quest List')

            if event == sg.WIN_CLOSED:
                break

        return None

    def monster_window( self ):
        layout_monster = [[sg.Text('∎ Digite abaixo o nome do Monstro')],
                        [sg.Text('∎ Ou deixe em branco para toda a lista')],
                        [sg.Text(' ')],
                        [sg.Input(key='monster_find')],
                        [sg.Button('Pesquisar')],
                        [sg.Text('_'*30)]]

        monster_window = sg.Window(
            'MHFU - Lista de Monstros', layout_monster, element_justification='c')

        while True:
            event, values = monster_window.read()

            if event == 'Pesquisar':
                monster = values['monster_find'].title()
                localize_monster = df_monster[df_monster['name'].str.contains(
                    monster)][['name', 'jp_name', 'element', 'weak']]

                if localize_monster.empty:
                    sg.popup('Nenhum monstro com esse nome 🤔')

                else:
                    self.create_table(localize_monster.values.tolist(), list(
                        localize_monster.columns), 'Monster Data')

            if event == sg.WIN_CLOSED:
                break

        return None

    def itens_window( self ):
        layout_item = [[sg.Text('∎ Digite abaixo o nome do Item')],
                    [sg.Text('∎ Ou deixe em branco para toda a lista')],
                    [sg.Text(' ')],
                    [sg.Input(key='item_find')],
                    [sg.Button('Pesquisar')],
                    [sg.Text('_'*30)]]

        item_window = sg.Window(
            'MHFU - Lista de Monstros', layout_item, element_justification='c')

        while True:
            event, values = item_window.read()

            if event == 'Pesquisar':
                item_find = values['item_find'].title()
                df_itens['description'] = df_itens['description'].apply(
                    lambda x: x[:25] + '...')
                df_itens['found'] = df_itens['found'].apply(
                    lambda x: x[:25] + '...')
                localize_item = df_itens[df_itens['name'].str.contains(
                    item_find)][['name', 'found', 'description', 'value']]

                if localize_item.empty:
                    sg.popup('Nenhum item com esse nome 🤔')

                else:
                    self.create_table(localize_item.values.tolist(), list(
                        localize_item.columns), 'Item Data')

            if event == sg.WIN_CLOSED:
                break

        return None


    def geral_blade_one(self, img, text):
        geral_blade_window = [[sg.Text("∎ MHFU Mix Sets")], 
                              [sg.Text(" ")], 
                              [sg.Image(img, size=(269,400)), 
                               sg.VerticalSeparator(), 
                               sg.Text(text)]]

        geral_blade = sg.Window('MHFU - Blademaster', geral_blade_window)

        while True:
            event, values = geral_blade.read()

            if event == sg.WIN_CLOSED:
                break
            
        return None

    def mix_type_gr_blade_window( self ):
        layout_mix_type = [[sg.Text("∎ Lista de Mix de Blademaster")], 
                           [sg.Text(" ")], 
                           [sg.Button('Geral Blade 1'), sg.Button('Geral Blade 2'), sg.Button('Geral Blade Guru')],
                           [sg.Button('GS Classic'), sg.Button("GS Guru")],
                           [sg.Button('Geral Element'), sg.Button("Geral Element Guru")],
                           [sg.Button('Geral Earplug'), sg.Button("Geral Earplug Guru")],
                           [sg.Text("_"*30)]]

        mix_gr_blade_window = sg.Window('MHFU - Blademaster', layout_mix_type)

        while True:
            event, values = mix_gr_blade_window.read()

            if event == 'Geral Blade 1':
                self.geral_blade_one(t.blade_geral_one[0], t.blade_geral_one[1])

            if event == 'Geral Blade 2':
                self.geral_blade_one(t.blade_geral_two[0], t.blade_geral_two[1])

            if event == 'Geral Blade Guru':
                self.geral_blade_one(t.blade_geral_guru[0], t.blade_geral_guru[1])

            if event == 'GS Classic':
                self.geral_blade_one(t.gs_classic[0], t.gs_classic[1])

            if event == 'GS Guru':
                self.geral_blade_one(t.gs_guru[0], t.gs_guru[1])

            if event == 'Geral Element':
                self.geral_blade_one(t.blade_elemental_one[0], t.blade_elemental_one[1])

            if event == 'Geral Element Guru':
                self.geral_blade_one(t.blade_elemental_guru[0], t.blade_elemental_guru[1])

            if event == 'Geral Earplug':
                self.geral_blade_one(t.earplug_one[0], t.earplug_one[1])

            if event == 'Geral Earplug Guru':
                self.geral_blade_one(t.earplug_guru_one[0], t.earplug_guru_one[1])

            if event == sg.WIN_CLOSED:
                break
            
        return None

    def mix_window( self ):
        layout_mix = [[sg.Text('∎ Selecione Rank & a Classe do Mix Set')],
                      [sg.Text(' ')],
                      [sg.Button('GR Mix Sets Gunner'), sg.Button('GR Mix Sets Blade')],
                      [sg.Text('_'*30)]]

        mix_window = sg.Window('MHFU - Quest List',
                            layout_mix, element_justification='c')

        while True:
            event, values = mix_window.read()

            if event == 'GR Mix Sets Gunner':
                sg.popup('cT ficou com preguiça de pegar :D')

            if event == 'GR Mix Sets Blade':
                self.mix_type_gr_blade_window()
                #sg.popup('cT ficou com preguiça de pegar :D')

            if event == sg.WIN_CLOSED:
                break

        return None

    def geral_window( self ):
        layout = [[sg.Text(" ")],
                  [sg.Text('▃▃▃▃▃▃▃▃    ▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃ \n\n◈ MHFU Database ◈\nSimples App com informações\nEssenciais para todas as caçadas!\n\n▃▃▃▃▃▃▃▃    ▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃')],
                  [sg.Text(' ')],
                  [sg.Button('Quests'), sg.Button('Monstros'),
                  sg.Button('Itens'), sg.Button('Mix Sets')],
                  [sg.Text('_'*30)]]

        window = sg.Window('MHFU - Database', layout,  element_justification='c')

        while True:
            event, values = window.read()

            if event == sg.WIN_CLOSED:
                break

            if event == 'Quests':
                self.quests_window()

            if event == 'Monstros':
                self.monster_window()

            if event == 'Itens':
                self.itens_window()

            if event == 'Mix Sets':
                self.mix_window()

        return None

if __name__ == '__main__':
    t = TextsList()

    mh = MhApp()

    df_itens, df_monster, df_hall_all, df_elder_key, df_hall_low, df_hall_high, df_hall_g = mh.load_data()

    mh.geral_window()