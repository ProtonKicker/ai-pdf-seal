# AI PDF Seal

一个用于对 PDF 文件批量添加图片印章的工具，支持命令行和图形界面两种使用方式。

## 功能特性

- 支持对 PDF 文件添加图片印章
- 可控制印章图片的大小
- 可指定印章在 PDF 页面中的位置
- 支持多页 PDF，每页自动添加相同位置的印章
- **支持图形界面（GUI），操作更便捷**
- 支持配置文件，参数一次配置多次使用

## 快速开始

### GUI 图形界面（推荐）

下载 `dist/ai-pdf-seal.exe` 双击运行即可。

界面功能：
- 目录选择：选择要处理的 PDF 文件所在目录
- 印章图片：选择印章图片文件
- 印章尺寸：设置印章宽度和高度
- 印章位置：设置 X 和 Y 坐标
- 强制覆盖：勾选后重新生成所有文件
- 立即执行：开始处理

### 命令行模式

```bash
python main.py --pdf contract.pdf --image stamp.png --width 100 --height 100 --x 400 --y 100
```

### 配置文件模式

创建 `config.yaml`：

```yaml
directory: ./pdfs
image: stamp.png
width: 50
height: 50
x: 450
y: 150
force: false
```

然后直接运行：

```bash
python main.py
```

或使用 GUI：

```bash
python main_gui.py
```

## 参数说明

| 参数 | 说明 |
|------|------|
| --pdf, -p | PDF 文件路径（与 --dir 二选一） |
| --dir, -d | 目录路径（批量处理模式） |
| --image, -i | 印章图片路径 |
| --width | 印章宽度（像素） |
| --height | 印章高度（像素） |
| --x | 印章 X 坐标 |
| --y | 印章 Y 坐标 |
| --output, -o | 输出文件路径（仅单文件模式有效） |
| --force | 强制覆盖已盖章文件 |

## 使用示例

### 命令行批量处理

```bash
python main.py -d ./pdfs -i stamp.png --width 50 --height 50 --x 450 --y 150
```

批量处理时会自动跳过已盖章的文件（检测 `*_sealed.pdf` 文件是否存在）。

### 坐标说明

- `x` 和 `y`：印章在 PDF 页面中的坐标（左下角为原点 (0, 0)）

## 技术栈

- **Python 3.8+**
- [pypdf](https://github.com/py-pdf/pypdf) - PDF 文件处理
- [Pillow](https://github.com/python-pillow/Pillow) - 图片处理
- [reportlab](https://www.reportlab.com/) - PDF 生成
- Tkinter - GUI 图形界面（Python 内置）

## 安装

```bash
pip install -e .
```

或直接运行：

```bash
pip install pypdf Pillow reportlab PyYAML
```

## 版本

- v1.0.0: 初始版本，支持 GUI 和命令行
