'''
Author: Nomastart
Github: git@github.com:Nomastart/Golang_Noma.git
Date: 2026-10-19 12:35:48
LastEditors: Nomastart
LastEditTime: 2026-10-19 12:41:27
Name: Do not edit
FilePath: /undefined/Users/a1234/codex-practice/hello.py
Description: Do not edit
'''
# import 用于导入模块；sys 提供命令行参数、标准错误输出和退出等功能。
import sys


# sys.argv 是命令行参数列表；[0] 是脚本名，[1] 是第一个参数。
# len(...) 获取列表长度；if 条件在参数不足时执行缩进代码块。
if len(sys.argv) < 2:
    # f"...{表达式}..." 是格式化字符串；sys.stderr 表示标准错误输出流。
    print(f"用法: python {sys.argv[0]} <姓名>", file=sys.stderr)
    # sys.exit(1) 以非零状态码结束程序，表示发生了使用错误。
    sys.exit(1)

# sys.argv[1] 读取姓名参数；f-string 将它插入问候语中。
print(f"Hello, {sys.argv[1]}")
