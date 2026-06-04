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
