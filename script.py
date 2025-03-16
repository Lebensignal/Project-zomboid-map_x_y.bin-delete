import os
import re
import argparse

def main():
    parser = argparse.ArgumentParser(description='删除指定方形区域内的map文件')
    parser.add_argument('directory', help='目标目录路径')
    parser.add_argument('x1', type=int, help='X坐标起始点')
    parser.add_argument('y1', type=int, help='Y坐标起始点')
    parser.add_argument('x2', type=int, help='X坐标结束点')
    parser.add_argument('y2', type=int, help='Y坐标结束点')
    parser.add_argument('--dry-run', action='store_true', help='试运行模式，不实际删除文件')
    args = parser.parse_args()

    # 确定坐标范围
    x_min, x_max = sorted([args.x1, args.x2])
    y_min, y_max = sorted([args.y1, args.y2])

    # 验证目录是否存在
    if not os.path.isdir(args.directory):
        print(f"错误：目录 '{args.directory}' 不存在")
        return

    # 编译正则表达式匹配文件名
    pattern = re.compile(r'^map_(\d+)_(\d+)\.bin$')
    deleted_count = 0
    error_count = 0

    # 遍历目录中的文件
    for filename in os.listdir(args.directory):
        match = pattern.match(filename)
        if match:
            # 提取坐标并转换为整数
            try:
                x = int(match.group(1))
                y = int(match.group(2))
            except ValueError:
                continue
            
            # 检查坐标是否在目标范围内
            if x_min <= x <= x_max and y_min <= y <= y_max:
                filepath = os.path.join(args.directory, filename)
                
                # 执行删除操作或dry-run
                if args.dry_run:
                    print(f"[试运行] 将删除：{filepath}")
                    deleted_count += 1
                else:
                    try:
                        if os.path.isfile(filepath):
                            os.remove(filepath)
                            print(f"已删除：{filepath}")
                            deleted_count += 1
                        else:
                            print(f"警告：{filepath} 不是文件")
                            error_count += 1
                    except Exception as e:
                        print(f"删除失败：{filepath} - {str(e)}")
                        error_count += 1

    # 输出结果统计
    print("\n操作统计：")
    print(f"匹配文件总数: {deleted_count + error_count}")
    print(f"成功删除数量: {deleted_count}")
    print(f"错误数量: {error_count}")
    if args.dry_run:
        print("注意：当前为试运行模式，未执行实际删除操作")

if __name__ == '__main__':
    main()