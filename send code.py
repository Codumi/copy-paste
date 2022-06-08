import shutil

# D드라이브 Code파일을 없애줌 (이미 있으면 error 발생)
try:   
    shutil.rmtree(r"D:\정리\Code")
except:
    pass

# C드라이브 'Code'폴더 복사 -> D드라이브 '정리'폴더 내에 붙여넣기
shutil.copytree(r"C:\Users\surface\OneDrive - hansung.ac.kr\바탕 화면\Ust\Code",
                r"D:\정리\Code")
