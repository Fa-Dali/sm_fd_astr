# ⛎
# ♈︎
# 🌑 🌒 🌓 🌔 🌕 🌖 🌗 🌘

#       mars = [1, ♈, "♂", "C", "C", "огонь"]
#    e_venus = [2, ♉, "♀", "G", "G", "земля"]
#  a_mercury = [3, ♊, "☿", "D", "D", "воздух"]
#       moon = [4, ♋, "☽", "A", "A", "вода"]
#        sun = [5, ♌, "☉", "E", "E", "огонь"]
#  e_mercury = [6, ♍, "☿", "B", "B", "воздух"]
#    a_venus = [7, ♎, "♀", "Gb", "F#", "земля"]
#     pluton = [8, ♏, "♇", "C#", "Db", "вода"]
#    jupiter = [9, ♐, "♃", "G#", "Ab", "огонь"]
#    saturn = [10, ♑, "♄", "D#", "Eb", "земля"]
#      uran = [11, ♒, "♅", "A#", "Bb", "воздух"]
#    neptun = [12, ♓, "♆", "F", "F", "вода"]


#     cerera = "⚳"
#     palada = "⚴"
#      unona = "⚵"
#      vesta = "⚶"
#      hiron = "⚷"
# black_moon = "⚸"
#    fortuna = "☸"
#     in_yan = "☯"
# south_node = "☋"
# north_node = "☊"
#  ascendent = "Asc"
#      earth = "♁"
# ⛢


# ⚹ (60°) ⚺ (30°) ⚼ (135°) ⚻
#  ☌ ☍

from collections import namedtuple

# Определяем именованный кортеж для астрологических объектов
AstrologicalObject = namedtuple('AstrologicalObject',
                                ['position', 'sign',
                                 'symbol', 'note_#', 'note_b',
                                 'minor', 'element'])

# Создаём словарь с астрологическими объектами
astrology_data = {
    "mars": AstrologicalObject(1, "♈", "♂", "C", "C", "m", "огонь"),
    "e_venus": AstrologicalObject(2, "♉", "♀", "G", "G", "m", "земля"),
    "a_mercury": AstrologicalObject(3, "♊", "☿", "D", "D", "m", "воздух"),
    "moon": AstrologicalObject(4, "♋", "☽", "A", "A", "m", "вода"),
    "sun": AstrologicalObject(5, "♌", "☉", "E", "E", "m", "огонь"),
    "e_mercury": AstrologicalObject(6, "♍", "☿", "B", "B", "m", "воздух"),
    "a_venus": AstrologicalObject(7, "♎", "♀", "Gb", "F#", "m", "земля"),
    "pluton": AstrologicalObject(8, "♏", "♇", "C#", "Db", "m", "вода"),
    "jupiter": AstrologicalObject(9, "♐", "♃", "G#", "Ab", "m", "огонь"),
    "saturn": AstrologicalObject(10, "♑", "♄", "D#", "Eb", "m", "земля"),
    "uran": AstrologicalObject(11, "♒", "♅", "A#", "Bb", "m", "воздух"),
    "neptun": AstrologicalObject(12, "♓", "♆", "F", "F", "m", "вода"),
}

# Пример доступа к данным
# print(astrology_data["mars"])
# Вывод: AstrologicalObject(
#           position=5,
#           sign='♈',
#           symbol='♂',
#           note_#='C',
#           note_b='C',
#           element='огонь')
# print(astrology_data["sun"].sign)        # Вывод: '♌' (знак солнца)
# print(astrology_data["moon"].element)    # Вывод: 'вода'