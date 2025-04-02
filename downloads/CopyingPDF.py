import shutil
import os

source_file = "C:\\Users\\Yichuan.Zhang\\Documents\Haining_Page\\hai-ning-liang.github.io-main\\downloads\\PDF0.pdf"  # 原始文件
target_folder = "C:\\Users\\Yichuan.Zhang\\Documents\Haining_Page\\hai-ning-liang.github.io-main\\downloads"  # 存放复制结果的文件夹

# 创建目标文件夹（如果不存在）
os.makedirs(target_folder, exist_ok=True)

# 复制 100 份，文件名从 PDF1.pdf 到 PDF100.pdf
for i in range(1, 101):
    target_file = os.path.join(target_folder, f"PDF{i}.pdf")
    shutil.copyfile(source_file, target_file)

print("复制完成，共100个PDF文件。")
