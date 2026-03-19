---
name: "generate-test-files"
description: "Generates test PDF with 2 pages and a 50x50 stamp image. Invoke when user needs test files for PDF seal tool."
---

# Generate Test Files

This skill generates test files for the AI PDF Seal tool.

## What It Creates

1. **test.pdf** - A 2-page PDF document with test content
2. **stamp.png** - A 50x50 pixel red stamp image with Chinese character "章"

## Usage

Simply invoke this skill, and it will:
1. Create `test.pdf` with 2 pages of sample text
2. Create `stamp.png` with a red circular stamp design
3. Run the main program to create `test_sealed.pdf`

## Technical Details

- PDF: Uses reportlab to create multi-page PDF
- Stamp: Uses Pillow to create RGBA image with red ellipse and text
- Output location: Current working directory
