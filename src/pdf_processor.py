import os
from io import BytesIO

from pypdf import PdfReader, PdfWriter
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter


class PdfSealProcessor:
    def __init__(self, pdf_path: str, image_path: str, width: int, height: int, x: int, y: int):
        self.pdf_path = pdf_path
        self.image_path = image_path
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def validate(self) -> bool:
        if not os.path.exists(self.pdf_path):
            raise FileNotFoundError(f"PDF 文件不存在: {self.pdf_path}")
        if not os.path.exists(self.image_path):
            raise FileNotFoundError(f"印章图片不存在: {self.image_path}")
        if self.width <= 0 or self.height <= 0:
            raise ValueError("印章尺寸必须大于 0")
        if self.x < 0 or self.y < 0:
            raise ValueError("印章坐标必须大于等于 0")
        return True

    def _create_stamp_pdf(self, page_width: float, page_height: float) -> bytes:
        packet = BytesIO()
        c = canvas.Canvas(packet, pagesize=(page_width, page_height))
        c.drawImage(
            self.image_path,
            self.x,
            self.y,
            width=self.width,
            height=self.height,
            preserveAspectRatio=True
        )
        c.save()
        packet.seek(0)
        return packet.getvalue()

    def process(self, output_path: str = None) -> str:
        self.validate()

        if output_path is None:
            base, ext = os.path.splitext(self.pdf_path)
            output_path = f"{base}_sealed{ext}"

        reader = PdfReader(self.pdf_path)
        writer = PdfWriter()

        for i, page in enumerate(reader.pages):
            page_width = page.mediabox.width
            page_height = page.mediabox.height

            stamp_pdf_bytes = self._create_stamp_pdf(float(page_width), float(page_height))
            stamp_reader = PdfReader(BytesIO(stamp_pdf_bytes))
            stamp_page = stamp_reader.pages[0]

            page.merge_page(stamp_page)
            writer.add_page(page)

        with open(output_path, "wb") as f:
            writer.write(f)

        return output_path
