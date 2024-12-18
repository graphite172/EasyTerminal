# Windwos-Git-bash-Select-Partition
윈도우 터미널(git bash)에서 파티션 선택

## 프로젝트 설명
이 프로젝트는 Windows 환경에서 WSL(Windows Subsystem on Linux)을 사용하지 않고 Git Bash를 활용하여 Linux 터미널과 유사한 환경을 구현하는 Python 프로그램입니다.

---

## 주요 기능
1. 파티션 탐색
2. 드라이브 선택
3. Git Bash 쉘 실행행

## 실행 방법



## 날 괴롭히는 문제(Error)
### 1. Pyinstaller의 ModuleNotFoundError: No module named 'imp' 문제
  - 파이썬 3.x부터 imp 모듈 전체 삭제
  - 에러 내용을 보면 다음과 같음.
 ```
    File "C:\Users\carbo\AppData\Local\Programs\Python\Python314\Scripts\pyinstaller.exe\__main__.py", line 7, in <module>
    sys.exit(run())
             ~~~^^
    File "C:\Users\username\AppData\Local\Programs\Python\Python314\Lib\site-packages\PyInstaller\__main__.py", line 107, in run
    parser = generate_parser()
  File "C:\Users\username\AppData\Local\Programs\Python\Python314\Lib\site-packages\PyInstaller\__main__.py", line 78, in generate_parser
    import PyInstaller.building.build_main
  File "C:\Users\username\AppData\Local\Programs\Python\Python314\Lib\site-packages\PyInstaller\building\build_main.py", line 35, in <module>
    from PyInstaller.depend import bindepend
  File "C:\Users\username\AppData\Local\Programs\Python\Python314\Lib\site-packages\PyInstaller\depend\bindepend.py", line 26, in <module>
    from PyInstaller.depend import dylib, utils
  File "C:\Users\username\AppData\Local\Programs\Python\Python314\Lib\site-packages\PyInstaller\depend\utils.py", line 28, in <module>
    from PyInstaller.lib.modulegraph import util, modulegraph
  File "C:\Users\username\AppData\Local\Programs\Python\Python314\Lib\site-packages\PyInstaller\lib\modulegraph\modulegraph.py", line 103, in <module>
  ```
### 해결방안
