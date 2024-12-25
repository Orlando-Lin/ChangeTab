# 标签文件更新工具使用说明

## 功能介绍
这个工具用于更新YOLO格式的数据集标签文件。主要功能包括：
1. 对比并显示classes.txt文件的变化
2. 更新classes.txt文件内容
3. 自动更新指定文件夹中的所有标签文件
4. 显示所有修改的文件清单

## 使用前准备
1. 确保有以下文件（自己进行替换）：
   - `classes.txt`：原始类别文件
   - `classes_change.txt`：新的类别文件
   - `changeTxt.py`：程序主文件

2. 文件要求：
   - classes.txt 和 classes_change.txt 必须在程序同一目录下
   - 标签文件必须是YOLO格式（每行第一个数字为类别编号）

## 使用步骤
1. 运行程序：
   ```bash
   python changeTxt.py
   ```

2. 程序会显示类别文件的变化情况：
   - 显示移动的行："`行 '类别名' 从位置 X 移动到了位置 Y`"
   - 显示新增的行："`新增行: 位置 X - '类别名'`"
   - 显示删除的行："`删除行: 原位置 X - '类别名'`"

3. 确认是否进行更新：
   - 输入 `yes` 或 `y` 进行更新
   - 输入 `no` 或 `n` 取消操作

4. 如果选择更新：
   - 输入需要更新的标签文件所在的文件夹路径
   - 程序会自动处理该文件夹下的所有txt文件 ,只会将标签文件的类别信息（第一个数字）进行更新 eg：0 0.xxx 2.xxx

5. 更新完成后会显示：
   - 修改的文件总数
   - 所有被修改文件的具体路径

## 注意事项
1. 程序会同时更新：
   - 当前目录下的classes.txt
   - 指定文件夹中的classes.txt
   - 指定文件夹中的所有标签文件

2. 只有实际发生变化的文件才会被更新和记录

3. 建议在更新前备份重要文件

4. 确保有足够的文件读写权限

## 错误处理
- 如果文件夹路径不存在，程序会提示错误并退出
- 如果输入无效的选项，程序会要求重新输入

## 示例输出 
- 行 'car' 从位置 1 移动到了位置 0
- 新增行: 位置 3 - 'truck'
- 删除行: 原位置 2 - 'bike'
- 是否要用classes_change.txt替换classes.txt文件并更新标签文件？(yes/y/no/n): y
- 当前目录的classes.txt已更新
- 请输入需要更新的标签文件所在的文件夹路径: /path/to/labels
- 文件修改总结:
  - 共修改了 3 个文件:
  - /path/to/labels/classes.txt
  - /path/to/labels/image1.txt
  - /path/to/labels/image2.txt
