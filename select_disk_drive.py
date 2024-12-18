import subprocess
import psutil
import os
import tkinter

from tkinter import ttk, messagebox


#############################################################################################
#                                                                                           #
#                                 Windows 11 (24H2)에서 작성됨                               #
#                                   OS 빌드: 26100.2605                                     #
#                                                                                           #
#                                                                                           #
#############################################################################################

# 사용 가능한 파티션 확인
def get_available_partitions():
    drives = []
    partitions = psutil.disk_partitions()

    ## print(f"실제 파티션 목록:{partitions}")
    
    for partition in partitions:
        if os.path.exists(partition.mountpoint):
            drive_letter = partition.device.strip("\\")
            drives.append(drive_letter[0])
    ## print(f"실제 파티션 목록:{drives}")
    return drives


# Windows Terminal Git bash 실행
# 터미널로 실행할때 사용용
def open_terminal_partition(drive_paths):
    try:
        "드라이브 루트 경로"
        print(f"현재 드라이브 {drive_paths}")
        if not os.path.exists(f"{drive_paths}"):
            print(f"{drive_paths}를 찾을 수 없습니다.")
            return 
        
        command = f'start wt -p "Git Bash" --title "현재 위치: {drive_paths}" -d "{drive_paths}'

        subprocess.run(command, shell=True, check=True)
        #print(f"파워쉘 스크립트 실행성공, 선택된 파티션 {drive_letter}: 드라이브")
        
        # messagebox.showinfo("성공", f"{drive_letter} 드라이브")
    except subprocess.CalledProcessError as e: 
        #print(f"파워쉘 스크립트 실행 실패: {e}")

        messagebox.showerror("오류", f"드라이브 불러오기 실패: {e}")


# 드라이브 선택
def display_drive_menu():

    drive_letter = get_available_partitions()

    if not drive_letter:
        #print("파티션이 존재하지 않습니다.")
        messagebox.showinfo
        return None

    print("파티션을 선택하세요:")
    for i, partition in enumerate(drive_letter, start=1):
        print(f"[{i}] - {partition} 드라이브")

    while True:
        try:
            choice = int(input("숫자를 입력하여 드라이브를 선택하세요: "))

            if 1 <= choice <= len(drive_letter):
                return drive_letter[choice - 1]
            else:
                print("존재하지 않는 파티션입니다. 다시 선택해주세요.")
        
        except ValueError:
            print("숫자로 입력하세요.")

# gui 실행기
def create_drive_selector():
    def on_select_drive():
        selected_idx = drive_list.curselection()
        if selected_idx:
            selected_drive = drive_list.get(selected_idx)
            drive_letter = selected_drive.replace(" 드라이브", "")
            drive_path = f"{drive_letter}:\\\\"

            print(f"{drive_path}")
            #messagebox.showinfo("정상", f"현재 선택된 드라이브 {selected_drive}") 
            open_terminal_partition(drive_path)
        else:
            messagebox.showerror("경고", "드라이브를 선택하세요.")

    # GUI 실행기 인스턴스 생성
    win = tkinter.Tk()

    win.title("파티션 선택")
    win.geometry("400x170+700+100")
    win.resizable(False, False)

    # 레이블 생성 및 화면 배치
    drive_label = tkinter.Label(win, text="사용 가능한 드라이브 목록", font=("Arial",15))

    drives = get_available_partitions()
    
    # 드라이브 개수 만큼 박스 크기 설정
    listbox_height = len(drives)

    drive_list = tkinter.Listbox(win, relief="flat", selectmode="single", font=("Arial",12), activestyle="none", height=listbox_height)

    for drive in drives:
        drive_list.insert(tkinter.END, f"{drive} 드라이브")
       

    select_btn = ttk.Button(win, text="선택", width=15, takefocus=True, command=on_select_drive)
    exit_btn = ttk.Button(win, text="종료", width=15, takefocus=True, command=win.destroy)

    # 컴포넌트 배치
    drive_label.grid(row=0, column=0, columnspan=2, rowspan=1, pady=10, padx=10, sticky="w") 
    drive_list.grid(row=1, column=0, columnspan=1, rowspan=2, pady=10, padx=10, sticky="n")  
    select_btn.grid(row=1, column=2, padx=10, pady=1, sticky="e")  # 오른쪽에 선택 버튼 배치
    exit_btn.grid(row=2, column=2, padx=10, pady=1, sticky="e")  # 오른쪽에 종료 버튼 배치

    
    # 메인화면 표시
    win.mainloop()


# def select_terminal_profile()

if __name__ == "__main__":
    create_drive_selector()
   # selected_drive = display_drive_menu()
   # print(f"선택된 드라이브{selected_drive}")
   # if selected_drive:
   #    open_terminal_partition(selected_drive)