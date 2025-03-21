# 地图坐标文件清理工具

这是一个用于批量删除指定坐标范围内地图文件的Python脚本工具，适用于清理符合`map_x_y.bin`格式的文件。

## 功能特性

- **坐标范围清理**  
  通过指定矩形区域的起始坐标(x1,y1)和结束坐标(x2,y2)，精确删除目标区域文件

- **安全防护机制**  
  - 试运行模式(`--dry-run`)预览操作结果  
  - 详细的删除前确认提示

- **操作可视化**  
  实时显示处理进度，最终生成包含以下数据的统计报告：  
  ✅ 匹配文件总数  
  ✅ 成功删除数量  
  ❌ 错误操作数量

## 环境要求

- Python 3.6+
- 标准库依赖：`os`, `re`, `argparse`

## 快速开始

### 基础用法
```bash
python map_cleaner.py /data/maps 470 1045 485 1060
