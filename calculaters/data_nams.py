# подсказка
# ⛎
# ♈︎
# 🌑 🌒 🌓 🌔 🌕 🌖 🌗 🌘

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
# подсказка
#     'position' = "поле в Знаке Зодиака",
#         'sign' = "Знак Зодиака",
#       'planet' = "Планета",
#       'note_#' = "Нота или Нота-#,
#       'note_b' = "Нота-b,
#        'minor' = "Минорный аккорд",
#      'element' = "Стихия",
#     'name_zoo' = "Название Зодиака",
# 'degree_range' = "Границы поля Зодиака"


# Определяем именованный кортеж для астрологических объектов
AstrologicalObject = namedtuple(
    'AstrologicalObject',
    ['position', 'sign', 'planet', 'note_#', 'note_b', 'minor', 'element',
                'name_zoo', 'degree_range'
])

# Создаём словарь с астрологическими объектами, включая поля созвездий и диапазоны градусов
astrology_data = {
    "mars":      AstrologicalObject(1, "♈", "♂", "C", "C", "m", "огонь",
                                    "Овен", (0, 29.99999)),
    "e_venus":   AstrologicalObject(2, "♉", "♀", "G", "G", "m", "земля",
                                    "Телец", (30, 59.99999)),
    "a_mercury": AstrologicalObject(3, "♊", "☿", "D", "D", "m", "воздух",
                                    "Близнецы", (60, 89.99999)),
    "moon":      AstrologicalObject(4, "♋", "☽", "A", "A", "m", "вода",
                                    "Рак", (90, 119.99999)),
    "sun":       AstrologicalObject(5, "♌", "☉", "E", "E", "m", "огонь",
                                    "Лев", (120, 149.99999)),
    "e_mercury": AstrologicalObject(6, "♍", "☿", "B", "B", "m", "воздух",
                                    "Дева", (150, 179.99999)),
    "a_venus":   AstrologicalObject(7, "♎", "♀", "Gb", "F#", "m", "земля",
                                    "Весы", (180, 209.99999)),
    "pluton":    AstrologicalObject(8, "♏", "♇", "C#", "Db", "m", "вода",
                                    "Скорпион", (210, 239.99999)),
    "jupiter":   AstrologicalObject(9, "♐", "♃", "G#", "Ab", "m", "огонь",
                                    "Стрелец", (240, 269.99999)),
    "saturn":    AstrologicalObject(10, "♑", "♄", "D#", "Eb", "m", "земля",
                                    "Козерог", (270, 299.99999)),
    "uran":      AstrologicalObject(11, "♒", "♅", "A#", "Bb", "m", "воздух",
                                    "Водолей", (300, 329.99999)),
    "neptun":    AstrologicalObject(12, "♓", "♆", "F", "F", "m", "вода",
                                    "Рыбы", (330, 359.99999)),
}

# Пример доступа к данным
print(astrology_data["mars"])                     # Вывод: AstrologicalObject(...)
print(astrology_data["sun"].constellation)        # Вывод: 'Лев' (созвездие для Солнца)
print(astrology_data["e_venus"].degree_range)     # Вывод: (30, 59.99999)
