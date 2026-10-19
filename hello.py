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
import sys


if len(sys.argv) < 2:
    print(f"用法: python {sys.argv[0]} <姓名>", file=sys.stderr)
    sys.exit(1)

print(f"Hello, {sys.argv[1]}")
