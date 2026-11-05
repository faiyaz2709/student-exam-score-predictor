# PyInstaller recipe. Run from the repository root on Windows.
from PyInstaller.utils.hooks import collect_submodules


a = Analysis(
    ["app.py"],
    pathex=[],
    binaries=[],
    datas=[("models/student_score_model.pkl", "models")],
    hiddenimports=collect_submodules("sklearn"),
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=["streamlit"],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)
exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name="StudentScorePredictor",
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,
    disable_windowed_traceback=False,
)
