import argparse
import sys

from src.pdf_processor import PdfSealProcessor


def main():
    parser = argparse.ArgumentParser(
        description="AI PDF Seal - 给 PDF 文件添加图片印章"
    )
    parser.add_argument(
        "--pdf", "-p",
        required=True,
        help="PDF 文件路径"
    )
    parser.add_argument(
        "--image", "-i",
        required=True,
        help="印章图片路径"
    )
    parser.add_argument(
        "--width",
        type=int,
        required=True,
        help="印章宽度（像素）"
    )
    parser.add_argument(
        "--height",
        type=int,
        required=True,
        help="印章高度（像素）"
    )
    parser.add_argument(
        "--x",
        type=int,
        required=True,
        help="印章 X 坐标"
    )
    parser.add_argument(
        "--y",
        type=int,
        required=True,
        help="印章 Y 坐标"
    )
    parser.add_argument(
        "--output", "-o",
        help="输出文件路径（可选）"
    )

    args = parser.parse_args()

    try:
        processor = PdfSealProcessor(
            pdf_path=args.pdf,
            image_path=args.image,
            width=args.width,
            height=args.height,
            x=args.x,
            y=args.y
        )
        output_path = processor.process(args.output)
        print(f"成功！输出文件: {output_path}")
    except FileNotFoundError as e:
        print(f"错误: {e}", file=sys.stderr)
        sys.exit(1)
    except ValueError as e:
        print(f"错误: {e}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"未知错误: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
