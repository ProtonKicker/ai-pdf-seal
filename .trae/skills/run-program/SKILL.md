---
name: "run-program"
description: "Runs the PDF seal program. Invoke when user wants to run the program."
---

# Run Program

This skill runs the PDF seal program (main.py).

## Usage

Run with default or custom parameters:

```bash
python main.py --pdf <pdf_file> --image <stamp_image> --width <width> --height <height> --x <x> --y <y>
```

## Required Parameters

| Parameter | Description |
|-----------|-------------|
| --pdf, -p | PDF file path |
| --image, -i | Stamp image path |
| --width | Stamp width in pixels |
| --height | Stamp height in pixels |
| --x | X coordinate on PDF page |
| --y | Y coordinate on PDF page |

## Optional Parameters

| Parameter | Description |
|-----------|-------------|
| --output, -o | Output file path |

## Example

```bash
python main.py --pdf test.pdf --image stamp.png --width 50 --height 50 --x 100 --y 100 -o output.pdf
```
