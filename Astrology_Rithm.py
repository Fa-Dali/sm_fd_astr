import tkinter as tk
import math
import winsound  # Для воспроизведения звуков на Windows

# Если используете другую ОС, рассмотрите библиотеку pygame

# Данные планет для примера
planet_data = {
    "01.01.2025": {
        'sun': 15.0,
        'moon': 25.0,
        'mercury': 35.0,
        'venus': 45.0,
        'mars': 55.0,
        'jupiter': 65.0,
        'saturn': 75.0,
        'uranus': 85.0,
        'neptune': 95.0,
        'pluto': 105.0,
    }
}

dispositor_map = {
    '♈️': 'Марс',
    '♉️': 'Венера',
    '♊️': 'Меркурий',
    '♋️': 'Луна',
    '♌️': 'Солнце',
    '♍️': 'Меркурий',
    '♎️': 'Венера',
    '♏️': 'Плутон',
    '♐️': 'Юпитер',
    '♑️': 'Сатурн',
    '♒️': 'Уран',
    '♓️': 'Нептун',
}


class ZodiacApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Круг Зодиака и Координаты планет")

        self.canvas = tk.Canvas(root, width=400, height=400, bg='white')
        self.canvas.pack()

        self.angle = 0
        self.rotation_speed = 1
        self.rotating = False
        self.planet_positions = {}

        self.create_controls()

    def create_controls(self):
        """Создает элементы управления в окне."""
        control_frame = tk.Frame(self.root)
        control_frame.pack()

        self.birthday_entry = tk.Entry(control_frame)
        self.birthday_entry.insert(0, 'Введите дату (ГГГГ-ММ-ДД)')
        self.birthday_entry.pack(side=tk.LEFT)

        get_coords_button = tk.Button(control_frame,
                                      text="Получить координаты планет",
                                      command=self.get_coordinates)
        get_coords_button.pack(side=tk.LEFT)

        self.start_button = tk.Button(control_frame, text="Вращать стрелку",
                                      command=self.start_rotation)
        self.start_button.pack(side=tk.LEFT)

        self.stop_button = tk.Button(control_frame, text="Стоп",
                                     command=self.stop_rotation)
        self.stop_button.pack(side=tk.LEFT)

        self.volume_scale = tk.Scale(control_frame, from_=0, to=1,
                                     resolution=0.1, orient=tk.HORIZONTAL,
                                     label="Громкость")
        self.volume_scale.set(1)  # Установка громкости по умолчанию на 1
        self.volume_scale.pack(side=tk.LEFT)

        self.result_table = tk.Text(self.root, height=10, width=50)
        self.result_table.pack()

        self.metronome_sound = 'metronome.wav'  # Путь к звуковому файлу

    def get_zodiac_sign(self, degree):
        """Получает знак зодиака по углу."""
        sign_names = [
            "♈️", "♉️", "♊️", "♋️", "♌️", "♍️",
            "♎️", "♏️", "♐️", "♑️", "♒️", "♓️"
        ]
        index = math.floor(degree / 30)
        return sign_names[index % 12]

    def get_coordinates(self):
        """Получает координаты планет на основе введенной даты."""
        input_date = self.birthday_entry.get()

        if input_date in planet_data:
            self.planet_positions = planet_data[input_date]
            self.result_table.delete('1.0', tk.END)  # Очистить текстовое поле

            for planet, degree in self.planet_positions.items():
                sign = self.get_zodiac_sign(degree)
                self.result_table.insert(tk.END,
                                         f"{sign} | {planet} | {degree:.2f}\n")

            self.update_zodiac_circle()
        else:
            self.result_table.delete('1.0', tk.END)
            self.result_table.insert(tk.END,
                                     "Нет данных для указанной даты.\n")

    def draw_zodiac_circle(self):
        """Рисует круг зодиака."""
        self.canvas.delete("all")
        self.canvas.create_oval(50, 50, 350, 350)

        for i in range(12):
            angle_rad = (i * 30) * (math.pi / 180)
            x = 200 + 130 * math.cos(angle_rad)
            y = 200 + 130 * math.sin(angle_rad)
            self.canvas.create_text(x, y, text=f"{i + 1}")

        self.draw_planet_positions()

    def draw_planet_positions(self):
        """Рисует положения планет на круге зодиака."""
        for planet, degree in self.planet_positions.items():
            angle_rad = (degree * math.pi) / 180
            x = 200 + 150 * math.cos(angle_rad)
            y = 200 + 150 * math.sin(angle_rad)
            self.canvas.create_oval(x - 5, y - 5, x + 5, y + 5, fill='blue')

    def update_zodiac_circle(self):
        """Обновляет круг зодиака."""
        self.draw_zodiac_circle()

    def rotate_arrow(self):
        """Функция для вращения стрелки."""
        if self.rotating:
            self.canvas.delete("arrow")
            angle_rad = (self.angle * math.pi) / 180
            x1 = 200 + 100 * math.cos(angle_rad)
            y1 = 200 + 100 * math.sin(angle_rad)
            x2 = 200 + 130 * math.cos(angle_rad)
            y2 = 200 + 130 * math.sin(angle_rad)

            self.canvas.create_line(200, 200, x1, y1, fill="red", tags="arrow")
            self.canvas.create_line(x1, y1, x2, y2, fill="red", tags="arrow")

            self.angle += self.rotation_speed
            self.angle %= 360  # Нормализуем угол

            current_angle_normalized = self.angle % 360  # Нормализуем текущий угол
            previous_angle = (self.angle - self.rotation_speed) % 360

            # Проверка на пересечение углов с координатами планет
            for planet, coordinate in self.planet_positions.items():
                normalized_coordinate = coordinate % 360  # Нормализуем координату
                if (
                        previous_angle < normalized_coordinate and current_angle_normalized >= normalized_coordinate) or \
                        (
                                previous_angle > normalized_coordinate and current_angle_normalized <= normalized_coordinate):
                    winsound.Beep(440, 500)  # Проигрываем звук

            self.root.after(50, self.rotate_arrow)  # Продолжить вращение

    def start_rotation(self):
        """Запускает вращение стрелки."""
        self.rotating = True
        self.rotate_arrow()

    def stop_rotation(self):
        """Останавливает вращение стрелки."""
        self.rotating = False
        self.canvas.delete("arrow")
        self.update_zodiac_circle()


if __name__ == "__main__":
    root = tk.Tk()
    app = ZodiacApp(root)
    root.mainloop()
