from bdb import BdbQuit
import sys
import os

def read_password(help_text=''):
    """
    Read password from stdin
    """
    import getpass
    while True:
        if help_text:
            print(help_text)
        pw = getpass.getpass("密码：")
        if len(pw) > 1:
            print("请输入一位字符")
        elif pw:
            break
    return pw


class HiddenPrints:
    def __enter__(self):
        self._original_stdout = sys.stdout
        sys.stdout = open(os.devnull, 'w')

    def __exit__(self, exc_type, exc_val, exc_tb):
        sys.stdout.close()
        sys.stdout = self._original_stdout


if __name__ == '__main__':
    try:
        pwds = ''
        total = 4
        print(f"请新娘设置金库{total}位密码：")
        for i in range(total):
            pwds += read_password(f"第{i + 1}位")
        print("设置完成，密码已保存至`pwds`中!!!")
    except (KeyboardInterrupt, EOFError) as err:
        pass
    else:
        print(f"\n\n!!!新郎求解金库{total}位密码!!!")
        print(f"将猜测存到`guess`变量中")
        guess = ''
        __counter = 0
        while True:
            try:
                while True:
                    __counter += 1
                    print(f"开始第{__counter}次尝试...")
                    with HiddenPrints():
                        import pdb
                        pdb.set_trace()
                        if guess == pwds:
                            break
            except (KeyboardInterrupt, EOFError, BdbQuit) as err:
                continue
            else:
                print(f"恭喜求解完成{'!'*(i+1)}")
                print(f"密码是：{pwds}")
                break

