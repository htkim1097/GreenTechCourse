#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Threads SNS 클라이언트 실행 스크립트
"""

import subprocess
import sys

def main():
    print("=== Threads SNS 클라이언트 시작 ===")
    print("GUI 창이 열립니다...")
    print("=" * 37)

    try:
        subprocess.run([sys.executable, "threads_client.py"])
    except FileNotFoundError:
        print("threads_client.py 파일이 없습니다!")
        print("현재 디렉토리에 threads_client.py가 있는지 확인하세요.")

if __name__ == "__main__":
    main()
