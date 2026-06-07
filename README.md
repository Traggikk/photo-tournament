<img width="640" height="480" alt="изображение" src="https://github.com/user-attachments/assets/6568d4cd-813e-4bb8-83a2-0178de0e8233" />
<img width="640" height="480" alt="изображение" src="https://github.com/user-attachments/assets/5af12660-ddb1-4bd5-b0b1-e96e4c433796" />
<img width="640" height="480" alt="изображение" src="https://github.com/user-attachments/assets/a4c82901-e7cd-4616-98bf-a251cb7a1af6" />



___
# 🏆 Фототурнир

Простое, игровое приложение для настольных компьютеров, предназначенное для фотографов и любителей, позволяющее отбирать лучшие фотографии. Вместо того чтобы просматривать сотни изображений, пусть они сразятся в турнирной сетке, пока не останутся только самые лучшие.

## ✨ Возможности

- **Геймифицированный отбор**: Фотографии соревнуются в динамичных дуэлях 1 на 1 или тройных сравнениях.
- **Рейтинг по очкам**: Победители накапливают баллы. В конце файлы сортируются с помощью префикса `score_XX_` в зависимости от количества побед.
- **Управление раундами**: После каждого раунда можно выбрать «Продолжить турнир» или «Закончить досрочно».
- **Поддержка RAW**: Нативная обработка форматов камер (CR2, NEF, ARW, DNG и др.) без предварительной конвертации.
- **Тёмная и светлая темы**: Комфорт для глаз при длительной работе.
- **Двуязычный интерфейс**: Мгновенное переключение между русским и английским языками.
- **Умный прогресс-бар**: Отслеживание статуса турнира и количества отсеянных фото в реальном времени.

## 🚀 Как пользоваться

1. **Скачать**: Загрузите актуальную версию `tournament.exe` из раздела [Releases](../../releases).
2. **Запуск**: Дважды кликните по `tournament.exe`. *(Если Защитник Windows предупредит об издателе, нажмите «Подробнее» → «Выполнить в любом случае»)*.
3. **Выбор папки**: Укажите директорию с вашими фотографиями (JPG, PNG, RAW и т.д.).
4. **Битва и выбор**: Выбирайте понравившиеся фото в каждом сравнении. После завершения раунда появится выбор: **Продолжить турнир** или **Завершить досрочно**.
5. **Результат**: Все файлы автоматически переименуются с префиксом `score_XX_` согласно набранным очкам, что позволяет мгновенно отсортировать их по качеству в проводнике.

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

- **Gamified Culling**: Photos compete in dynamic 1v1 or 3-way battles.
- **Points-Based Ranking**: Winners accumulate points. Files are sorted at the end using `score_XX_` prefixes based on their total wins.
- **Round Control**: Choose to continue to the next round or end the tournament early at any checkpoint.
- **RAW Support**: Native processing for camera RAW formats (CR2, NEF, ARW, DNG, etc.) without prior conversion.
- **Dark & Light Themes**: Easy on the eyes for long culling sessions.
- **Bilingual UI**: Switch between English and Russian on the fly.
- **Smart Progress Tracking**: Real-time progress bar and accurate elimination counter.

## 🚀 How to Use

1. **Download**: Get the latest `tournament.exe` from the [Releases](../../releases) section.
2. **Run**: Double-click `tournament.exe`. *(If Windows SmartScreen warns you, click "More info" → "Run anyway")*.
3. **Select Folder**: Choose a directory containing your photos (JPG, PNG, RAW, etc.).
4. **Battle & Choose**: Pick your favorite photo(s) from each comparison. After each round, a prompt will appear allowing you to **Continue** or **End Tournament**.
5. **Result**: Files are automatically renamed with `score_XX_` prefixes based on points earned, allowing instant sorting by performance in your file explorer.

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

