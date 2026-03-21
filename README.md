# AI PDF Seal

一个用于对 PDF 文件批量添加图片印章的工具。原始需求如下：

```
对PDF文件进行盖章，章子是一个图片文件，可以控制章子大小，并且可以指定在PDF页面中的位置。图片大小是参数，位置也作为参数。PDF文件可能有多页，每页都盖章，不同页面中的盖章位置相同。
```

## 功能特性

- 支持对 PDF 文件添加图片印章
- 可控制印章图片的大小
- 可指定印章在 PDF 页面中的位置
- 支持多页 PDF，每页自动添加相同位置的印章

## 参数说明

| 参数 | 必填 | 说明 |
|------|------|------|
| --pdf, -p | 否 | PDF 文件路径（与 --dir 二选一） |
| --dir, -d | 否 | 目录路径（批量处理模式） |
| --image, -i | 是 | 印章图片路径 |
| --width | 是 | 印章宽度（像素） |
| --height | 是 | 印章高度（像素） |
| --x | 是 | 印章 X 坐标 |
| --y | 是 | 印章 Y 坐标 |
| --output, -o | 否 | 输出文件路径（仅单文件模式有效） |

## 使用示例

### 基本用法

```bash
python main.py --pdf contract.pdf --image stamp.png --width 100 --height 100 --x 400 --y 100
```

### 指定输出文件

```bash
python main.py -p contract.pdf -i stamp.png --width 100 --height 100 --x 400 --y 100 -o signed_contract.pdf
```

### 批量处理目录

```bash
python main.py -d ./pdfs -i stamp.png --width 100 --height 100 --x 400 --y 100
```

批量处理时会自动跳过已盖章的文件（检测 `*_sealed.pdf` 文件是否存在）。

### 参数说明

- `width` 和 `height`：印章图片的目标尺寸（像素）
- `x` 和 `y`：印章在 PDF 页面中的坐标（左下角为原点 (0, 0)）

## 使用场景

- 合同文档加盖电子印章
- 证明文件添加认证标记
- 批量处理多页 PDF 文档的盖章需求

## 技术栈

- **Python 3.8+**
- [pypdf](https://github.com/py-pdf/pypdf) - PDF 文件处理
- [Pillow](https://github.com/python-pillow/Pillow) - 图片处理
- [reportlab](https://www.reportlab.com/) - PDF 生成

## 安装

```bash
pip install -e .
```

或直接运行：

```bash
pip install pypdf Pillow reportlab
```
