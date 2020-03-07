import argparse
from minitools.github.blog import BlogManager, GatherManager

if __name__ == '__main__':
    parse = argparse.ArgumentParser(description='Command for operating blog')
    parse.add_argument('cmd', help='指定执行命令')
    parse.add_argument('--author', default="CzaOrz", help='博客作者')
    parse.add_argument('--html', default=False, help='以.html格式编译')
    args = parse.parse_args()
    cmd, html, author = args.cmd, args.html, args.author
    if cmd == 'create':
        BlogManager(__file__).create()
    elif cmd == 'gather':
        gm = GatherManager(__file__, html=html)
        gm.config.author = author
        gm.gather()
    else:
        raise Exception(f'不支持 {cmd} 命令')
