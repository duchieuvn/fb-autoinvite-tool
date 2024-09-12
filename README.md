# fb-autoinvite-tool

## Build with NUITKA:

nuitka --standalone --onefile --include-data-file=icon.png=./icon.png --include-data-file=img.png=./img.png --windows-icon-from-ico=app_icon.ico --enable-plugin=tk-inter tool_101.py

## Build with PYINSTALLER:

pyinstaller --onefile --windowed --icon=app_icon.ico --add-data "icon.png;." --add-data "img.png;." tool_101.py
