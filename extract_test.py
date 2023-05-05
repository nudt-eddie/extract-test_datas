import os
import shutil

# 设置输入文件夹、输出文件夹和提取帧的间隔
input_folder = './fisheye_imgs_hr'
output_folder = './test2000'
interval = 10
count = 0

# 遍历输入文件夹中的所有文件，并按文件名数字顺序排序
file_list = sorted(os.listdir(input_folder), key=lambda x: int(x.split('_hr.')[0]))

for file in file_list:
    # 判断当前文件是否为png文件
    if file.endswith('_hr.png'):
        count += 1
        if count % interval == 0:
            # 将当前文件复制到输出文件夹中，并重命名为排序后的计数器值
            input_path = os.path.join(input_folder, file)
            output_path = os.path.join(output_folder, str(count//interval) + '.png')
            shutil.copyfile(input_path, output_path)
