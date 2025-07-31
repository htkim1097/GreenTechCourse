#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Threads SNS 서버 실행 스크립트
"""

import subprocess
import sys

def main():
    print("=== Threads SNS 서버 시작 ===")
    print("Ctrl+C를 눌러 서버를 종료할 수 있습니다.")
    print("=" * 35)

    try:
        subprocess.run([sys.executable, "threads_server.py"])
    except KeyboardInterrupt:
        print("\n서버를 종료합니다.")
    except FileNotFoundError:
        print("threads_server.py 파일이 없습니다!")
        print("현재 디렉토리에 threads_server.py가 있는지 확인하세요.")

if __name__ == "__main__":
    main()
