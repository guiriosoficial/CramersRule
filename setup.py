from cx_Freeze import setup, Executable

setup(
    name='CRC',
    options={'build_exe': {}},
    version='1.0',
    description='Cramers Rule Calculator with Laplace Theorem to Square Matrices Systems',
    executables=[Executable('main.py', base=None)]
)