# Overview
Simple 3D visualization of points by dragging files into the UI.


## Installation
Run the following commands.
```
poetry config virtualenvs.in-project true  # optional
poetry install
```


## Todo list
- Enable more file types.
- Generates a executable.


# Development environment
## Installation
Run the following commands.
```
poetry self add poetry-bumpversion
poetry install --with dev
```

## Design
Generates python file from Designer using PyQt6 module.
```
poetry run pyuic6 src/ui/design/main.ui -o src/ui/design/_main.py
```

## Executable
### Setup Bootloader
To avoid false positive by the precompiled bootloader, it is recommended to
install [MSVC build tools](https://visualstudio.microsoft.com/visual-cpp-build-tools/)
and [build a compiler](https://pyinstaller.org/en/stable/bootloader-building.html#building-for-windows).

Once the tools are installed, continue with the following commands.
```
git clone git@github.com:pyinstaller/pyinstaller.git

cd "%ProgramFiles(x86)%\Microsoft Visual Studio\2022\BuildTools\VC\Auxiliary\Build"
vcvarsall.bat x64

cd %REPOS%\PyInstaller\bootloader
python ./waf distclean all --target-arch 64bit
```
It is advice to disable the antivirus or add a exception, due to a preventive
quarantine of some file, such as *run_d.exe*, *run_w.exe*, among others.

### Install Bootloader
With the newly compiled bootloader it needs to be installed in the project's
virtual environment.
```
%PROJ_DIR%\.venv\Scripts\activate

cd %REPOS%\PyInstaller
pip install .
```

### Run PyInstaller
Finally, all that is left is to generate the executable.
```
pyinstaller src/installer.spec --clean --noconfirm
```
