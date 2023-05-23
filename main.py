import json
import ast
import time

import unique

from utils import Colors, float_input


class Database:

    def __init__(self, file_path):
        with open(file_path, 'r', encoding='utf-8') as f:
            self.json = json.load(f)

    def get_themes(self):
        return self.json.keys()

    def get_subthemes_by_theme(self, theme):
        return self.json[theme]


class ChatBot:

    def __init__(self):
        self.states = {
            'theme': None,
            'subtheme': None
        }
        self.db = Database('data.json')
        self.Colors = Colors

    def theme_input(self):
        data = str(input(f'{self.Colors.OKCYAN}'))
        themes = self.db.get_themes()
        text = '\n' + "\n".join(map(lambda x: x.capitalize(), self.db.get_themes()))
        if data.lower() in themes:
            self.states['theme'] = data
        else:
            print(f'{self.Colors.OKGREEN}Я не знаю цієї теми, натомість, '
                  f'ви можете задати мені питання з наступних тем: '
                  f'{text}.')
            self.theme_input()

    def subtheme_input(self):
        current_theme = self.states['theme']
        subthemes = self.db.get_subthemes_by_theme(current_theme.lower())

        data = input(f'{self.Colors.OKCYAN}')
        if data.lower() == 'назад':
            self.states['theme'] = None
            return
        elif data.lower() in [x.lower() for x in subthemes]:
            self.states['subtheme'] = data
        else:
            print(f'{self.Colors.OKGREEN}Я не знаю цієї теми, натомість, '
                  f'ви можете задати мені питання з наступних тем: '
                  f'{"; ".join(subthemes)}.')
            self.subtheme_input()

    def loop(self):

        if self.states['theme'] is None:
            text = '\n' + "\n".join(map(lambda x: x.capitalize(), self.db.get_themes()))
            print(f'{self.Colors.OKGREEN}Вітаю, мене звати ____. '
                  f'Ви можете задати мені питання з наступних тем: '
                  f'{text}')
            self.theme_input()
        else:
            if self.states['subtheme'] is None:
                current_theme: str or None = self.states['theme']
                subthemes = self.db.get_subthemes_by_theme(current_theme.lower())
                text = '\n' + "\n".join(subthemes)

                print(f'{self.Colors.OKGREEN}Ви обрали тему «{current_theme}». '
                      f'Ви можете задати мені питання з наступних тем: '
                      f'{text}')

                self.subtheme_input()

            else:
                current_theme: str or None = self.states['theme']
                subthemes = self.db.get_subthemes_by_theme(current_theme.lower())

                subtheme = subthemes[self.states['subtheme']]

                match subtheme['action']:
                    case 'formula':
                        print(f'{self.Colors.OKGREEN}Формула: {subtheme["value"]}')
                        var_list = {}
                        formula = subtheme['value'].split('=')
                        final_var = formula[0].strip()
                        formula = formula[1].strip()

                        parsed = ast.parse(formula)

                        for elt in ast.walk(parsed):
                            if isinstance(elt, ast.Name):
                                var_list[elt.id] = None

                        float_input(var_list)

                        exec_text: str = formula
                        for var, val in var_list.items():
                            exec_text = exec_text.replace(var, str(val))
                        print(f'Результат: {final_var} = {eval(exec_text)}')
                    case 'unique':
                        func = getattr(unique, subtheme['value'])
                        func()

                    case 'text':
                        print(self.Colors.OKGREEN, subtheme['value'], sep='')

                self.states['subtheme'] = None
                time.sleep(2)


if __name__ == '__main__':
    bot = ChatBot()

    while True:
        bot.loop()
