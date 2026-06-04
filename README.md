
# 🏆 Фототурнир

Простое, игровое приложение для настольных компьютеров, предназначенное для фотографов и любителей, позволяющее отбирать лучшие фотографии. Вместо того чтобы просматривать сотни изображений, пусть они сразятся в турнирной сетке, пока не останутся только самые лучшие.

# ✨ Особенности

- **Игровой отбор**: Фотографии соревнуются в поединках 1 на 1.
- **Автоматическая сортировка**: проигравшие автоматически переименовываются с добавлением префиксов (`zz_`, `1_`, `2_` и т. д.), а победитель получает `WIN_`.
- **Темная и светлая темы**: Комфортная для глаз, подходит для длительных сеансов отбора.
- **Двуязычный**: Переключайтесь между английским и русским языками на ходу.
- **Отслеживание прогресса**: Очистить индикатор выполнения и счетчик оставшихся фотографий.

# 🚀 Как использовать

1. **Скачать**: Загрузите файл `tournament.exe` из этого репозитория.
2. **Запуск**: Дважды щелкните файл `tournament.exe`. *(Если Windows SmartScreen выдаст предупреждение, нажмите «Подробнее» -> «Запустить в любом случае»).*
3. **Выберите папку**: Выберите папку, содержащую ваши фотографии.
4. **Битва**: Выберите свою любимую фотографию из каждой пары.
5. **Результат**: В конце отображается абсолютный победитель, а все файлы в папке сортируются по их месту в турнирной таблице.

# 🛠️ Для разработчиков

Если вы хотите изменить код или собрать исполняемый файл самостоятельно:

**Требования:**
- Python 3.10+
- Pillow (`pip install Pillow`)

**Запуск из исходного кода:**
```bash
python tournament.py
```

**Собрать исполняемый файл:**
```bash
pip install pyinstaller
pyinstaller --noconsole --onefile tournament.py
```
**Программа созданна с помошью ии**



___
# 🏆 Photo Tournament

A simple, gamified desktop application for photographers and enthusiasts to cull and select their best photos. Instead of scrolling through hundreds of images, let them battle it out in a tournament bracket until only the absolute best remains.

## ✨ Features

- **Gamified Culling**: Photos compete in 1v1 battles.
- **Automatic Sorting**: Losers are automatically renamed with prefixes (`zz_`, `1_`, `2_`, etc.), and the winner gets `WIN_`.
- **Dark & Light Themes**: Easy on the eyes for long culling sessions.
- **Bilingual**: Switch between English and Russian on the fly.
- **Progress Tracking**: Clear progress bar and remaining photo counter.

## 🚀 How to Use

1. **Download**: Download `tournament.exe` from this repository.
2. **Run**: Double-click `tournament.exe`. *(If Windows SmartScreen warns you, click "More info" -> "Run anyway").*
3. **Select Folder**: Choose a folder containing your photos.
4. **Battle**: Choose your favorite photo from each pair.
5. **Result**: At the end, the absolute winner is displayed, and all files in the folder are sorted by their tournament rank.

## 🛠️ For Developers

If you want to modify the code or build the executable yourself:

**Requirements:**
- Python 3.10+
- Pillow (`pip install Pillow`)

**Run from source:**
```bash
python tournament.py
```

**Build executable:**
```bash
pip install pyinstaller
pyinstaller --noconsole --onefile tournament.py
```
**The program was created using AI.**

