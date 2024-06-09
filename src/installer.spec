#!/usr/bin/env python3

# Core
import logging
import os
import sys
sys.setrecursionlimit(sys.getrecursionlimit() * 5)

# 3rd party
from vedo import installdir as vedo_installdir


vedo_fontsdir = os.path.join(vedo_installdir, 'fonts')
logging.debug(f"vedo installation is in {vedo_installdir}")
logging.debug(f"fonts are in {vedo_fontsdir}")

block_cipher = None

added_files = [
    # (os.path.join('tuning', '*'), 'tuning'),
    (os.path.join(vedo_fontsdir, '*'), os.path.join('vedo', 'fonts')),
]


a = Analysis(
    ['main.py'],
    pathex=[],
    binaries=[],
    datas=added_files,
    hiddenimports=[
        'vtkmodules',
        'vtkmodules.all',
        'vtkmodules.util',
        'vtkmodules.util.numpy_support',
        'vtkmodules.qt.QVTKRenderWindowInteractor',
    ],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='visualizer',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=True,
)
coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='visualizer'
)
