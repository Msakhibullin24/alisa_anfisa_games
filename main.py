def get_together_games(anfisa_games,alisa_games):
    together_games = set(anfisa_games).intersection(set(alisa_games))
    return together_games


anfisa_games = [
    'Online-chess',
    'Города',
    'DOOM',
    'Крестики-нолики'
]
alisa_games = [
    'DOOM',
    'Online-chess',
    'Города',
    'GTA',
    'World of tanks'
]
# Вызовите функцию со списками игр в качестве параметров
together_games = get_together_games(anfisa_games, alisa_games)


# Напечатайте итоговый перечень игр в цикле
for game in together_games:
    print('👾', game)



'''
Допишите функцию get_together_games(): она должна принимать на вход два списка, а возвращать — множество игр, названия которых есть в обоих списках.
Получите из функции это множество и построчно напечатайте его элементы (названия игр); перед названием каждой игры поставьте эмоджи 👾 и пробел. Эмоджи — это текстовый символ, как дефис или буква, его можно скопировать из условия и вставить в код.
Результат должен выглядеть примерно так:

👾 Super Hero Developer
👾 Python Shooter
👾 Online-backgammon 

'''
