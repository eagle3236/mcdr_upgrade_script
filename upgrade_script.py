import os
import shutil
from colorama import Fore, Back, Style, init
from platform import python_version
from sys import exit, executable
from subprocess import call

useless_files = ['utils', 'resources', 'requirements.txt', 'LICENSE', 'readme.md', 'readme_cn.md',
                 'mcdreforged.py']
start_script = '''
import sys
from mcdreforged.__main__ import main
if __name__ == '__main__':
    sys.exit(main())
'''.strip()
welcome_msg = '''

    --- MCDReforged 0.x -> 1.x Upgrade Script By Alex3236 ---
    请确认满足以下条件：
    1. 以管理员身份运行此脚本（非必须）
    2. PyPi 包管理器(pip) 已安装（非 Linux 用户请无视） 
    3. 在 MCDR 根目录运行此脚本
'''

if __name__ == '__main__':
    if python_version() < '3.6.0':
        print('\n\n 你的 Python 版本过低。请更新到 3.6.0 以上版本。')
        exit()
    if not os.path.exists('utils'):
        print('\n\n 未检测到 MCDReforged 0.x。请确认在 MCDR 根目录运行。是否忽略警告继续执行？', end='')
        if not input('[y/N] ') in ['y', 'Y']:
            exit()
    try:
        # 初始化
        init(autoreset=True)
        print(welcome_msg)
        if input('是否继续执行？ [Y/n] ') in ['n', 'N']:
            exit()

        # 删除旧版文件
        print('\n\n删除无用文件...', end='')
        for i in useless_files:
            if os.path.exists(i):
                if os.path.isdir(i):
                    shutil.rmtree(i)
                else:
                    os.remove(i)
        for i in os.listdir():
            if i.endswith('.bat'):
                os.remove(i)
        print(Fore.GREEN + '完成')

        # 安装 MCDR
        print('安装 MCDReforged...', end='')
        if call([executable, '-m', 'pip', 'install', 'mcdreforged', '-qqq']):
            print(Fore.RED + '安装失败！')
        else:
            print(Fore.GREEN + '完成')

        # 创建启动入口
        print('创建入口文件 MCDReforged.py ...', end='')
        with open('MCDReforged.py', 'w', encoding='utf8') as f:
            f.write(start_script)
        print(Fore.GREEN + '完成')

        # 结束
        input('脚本执行结束，按 Enter 退出...\n')
    except:
        print(Fore.RED + '失败\n')
        raise
