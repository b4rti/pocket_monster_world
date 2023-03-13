import os
import platform
import shutil
import subprocess


if os.name == 'nt':
    dir_sep = ';'
else:
    dir_sep = ':'


def run():
    subprocess.run([
        'pyinstaller',
        '-n', 'pocket_monster_world',
        '--paths', 'pocket_monster_world',
        '--add-data', f'config.py{dir_sep}.',
        '--add-data', f'plugins{dir_sep}plugins',
        '--noconfirm', '--windowed',
        os.path.join('pocket_monster_world', 'main.py')
    ])

    shutil.copytree('assets', os.path.join('dist', 'pocket_monster_world', 'assets'))
    package = f'pocket_monster_world-{platform.system().lower()}'
    shutil.make_archive(package, 'zip', 'dist', 'pocket_monster_world')
