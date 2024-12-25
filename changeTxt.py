import os
import shutil

def get_label_changes():
    # 读取两个文件
    with open('classes.txt', 'r', encoding='utf-8') as f1:
        original_lines = [line.strip() for line in f1.readlines()]
    
    with open('classes_change.txt', 'r', encoding='utf-8') as f2:
        new_lines = [line.strip() for line in f2.readlines()]
    
    # 创建标签映射关系 {原始位置: 新位置}
    label_mapping = {}
    
    # 创建原始文件内容的映射表 {内容: 行号}
    original_map = {line: i for i, line in enumerate(original_lines)}
    
    # 检查每一行的变化
    for i, new_line in enumerate(new_lines):
        if new_line in original_map:
            if original_map[new_line] != i:
                print(f"行 '{new_line}' 从位置 {original_map[new_line]} 移动到了位置 {i}")
                label_mapping[original_map[new_line]] = i
        else:
            print(f"新增行: 位置 {i} - '{new_line}'")
    
    # 检查是否有被删除的行
    for i, old_line in enumerate(original_lines):
        if old_line not in new_lines:
            print(f"删除行: 原位置 {i} - '{old_line}'")
    
    return label_mapping

def update_label_files(folder_path, label_mapping):
    modified_files = []  # 记录被修改的文件
    # 遍历指定文件夹中的所有txt文件
    for root, _, files in os.walk(folder_path):
        for file in files:
            if file.endswith('.txt') and file != 'classes_change.txt':
                file_path = os.path.join(root, file)
                
                # 如果是classes.txt文件，直接用classes_change.txt替换
                if file == 'classes.txt':
                    shutil.copy2('classes_change.txt', file_path)
                    print(f"已更新文件夹中的classes.txt: {file_path}")
                    modified_files.append(file_path)
                    continue
                
                # 读取并更新其他txt文件内容
                with open(file_path, 'r', encoding='utf-8') as f:
                    lines = f.readlines()
                
                updated_lines = []
                file_modified = False  # 标记文件是否被修改
                for line in lines:
                    parts = line.strip().split()
                    if parts:  # 确保行不为空
                        old_label = int(parts[0])
                        # 如果标签在映射中，则更新它
                        if old_label in label_mapping:
                            parts[0] = str(label_mapping[old_label])
                            file_modified = True
                        updated_lines.append(' '.join(parts) + '\n')
                
                # 只有当文件实际被修改时才写入并记录
                if file_modified:
                    with open(file_path, 'w', encoding='utf-8') as f:
                        f.writelines(updated_lines)
                    modified_files.append(file_path)
    
    # 打印修改总结
    print("\n文件修改总结:")
    print(f"共修改了 {len(modified_files)} 个文件:")
    for file_path in modified_files:
        print(f"- {file_path}")

def compare_files():
    # 获取标签变化映射
    label_mapping = get_label_changes()
    
    # 询问用户是否要替换文件
    while True:
        choice = input("\n是否要用classes_change.txt替换classes.txt文件并更新标签文件？(yes/y/no/n): ").lower()
        if choice in ['yes', 'y']:
            # 替换当前目录的classes文件内容
            with open('classes_change.txt', 'r', encoding='utf-8') as source:
                content = source.read()
            with open('classes.txt', 'w', encoding='utf-8') as target:
                target.write(content)
            print("当前目录的classes.txt已更新")
            
            # 询问标签文件夹路径
            folder_path = input("请输入需要更新的标签文件所在的文件夹路径: ").strip()
            if os.path.exists(folder_path):
                update_label_files(folder_path, label_mapping)
                print("所有文件更新完成！")
            else:
                print("文件夹路径不存在！")
            break
        elif choice in ['no', 'n']:
            print("操作已取消。")
            break
        else:
            print("无效输入，请输入 yes/y 或 no/n")

if __name__ == "__main__":
    compare_files()
