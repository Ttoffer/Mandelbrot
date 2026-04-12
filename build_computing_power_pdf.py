from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.platypus import Paragraph, SimpleDocTemplate, Spacer, Table, TableStyle


PROJECT_DIR = Path(__file__).resolve().parent
OUTPUT = PROJECT_DIR / "Computing Power.pdf"


def draw_page_chrome(canvas, doc) -> None:
    page_width, page_height = A4

    canvas.saveState()
    canvas.setFillColor(colors.HexColor("#07111f"))
    canvas.rect(0, 0, page_width, page_height, fill=1, stroke=0)

    canvas.setFillColor(colors.HexColor("#0f172a"))
    canvas.roundRect(12 * mm, 12 * mm, page_width - 24 * mm, page_height - 24 * mm, 7 * mm, fill=1, stroke=0)

    canvas.setFillColor(colors.HexColor("#10253f"))
    canvas.roundRect(18 * mm, page_height - 46 * mm, page_width - 36 * mm, 24 * mm, 5 * mm, fill=1, stroke=0)

    canvas.setStrokeColor(colors.HexColor("#38bdf8"))
    canvas.setLineWidth(2)
    canvas.line(24 * mm, page_height - 30 * mm, 68 * mm, page_height - 24 * mm)

    canvas.setStrokeColor(colors.HexColor("#a78bfa"))
    canvas.line(page_width - 80 * mm, page_height - 24 * mm, page_width - 24 * mm, page_height - 34 * mm)

    canvas.setFillColor(colors.HexColor("#ecfeff"))
    canvas.setFont("Helvetica-Bold", 13)
    canvas.drawString(24 * mm, page_height - 31 * mm, "Hal AI")

    canvas.setFillColor(colors.HexColor("#cbd5e1"))
    canvas.setFont("Helvetica-Bold", 7.5)
    canvas.drawString(24 * mm, page_height - 36.5 * mm, "CJF")

    canvas.setFillColor(colors.HexColor("#64748b"))
    canvas.setFont("Helvetica", 8.5)
    canvas.drawRightString(page_width - 24 * mm, 18 * mm, "Mandelbrot project note")
    canvas.restoreState()


def build_pdf() -> None:
    doc = SimpleDocTemplate(
        str(OUTPUT),
        pagesize=A4,
        leftMargin=24 * mm,
        rightMargin=24 * mm,
        topMargin=52 * mm,
        bottomMargin=24 * mm,
        title="Computing Power - Mandelbrot",
        author="CJF Hal AI",
        subject="A formal comparison of early 1980s computing power and present-day mobile hardware.",
    )

    styles = getSampleStyleSheet()
    title_style = ParagraphStyle(
        "Title",
        parent=styles["Title"],
        alignment=TA_CENTER,
        fontName="Helvetica-Bold",
        fontSize=18.5,
        leading=23,
        textColor=colors.HexColor("#f8fafc"),
        spaceAfter=6,
    )
    subtitle_style = ParagraphStyle(
        "Subtitle",
        parent=styles["BodyText"],
        alignment=TA_CENTER,
        fontName="Helvetica",
        fontSize=10.5,
        leading=14,
        textColor=colors.HexColor("#cbd5e1"),
        spaceAfter=14,
    )
    heading_style = ParagraphStyle(
        "Heading",
        parent=styles["Heading2"],
        fontName="Helvetica-Bold",
        fontSize=13,
        leading=16,
        textColor=colors.HexColor("#7dd3fc"),
        spaceBefore=7,
        spaceAfter=6,
    )
    body_style = ParagraphStyle(
        "Body",
        parent=styles["BodyText"],
        fontName="Helvetica",
        fontSize=10.5,
        leading=15,
        textColor=colors.HexColor("#e2e8f0"),
        spaceAfter=8,
    )
    note_style = ParagraphStyle(
        "Note",
        parent=body_style,
        fontName="Helvetica-Oblique",
        textColor=colors.HexColor("#cbd5e1"),
        backColor=colors.HexColor("#13263d"),
        borderColor=colors.HexColor("#38bdf8"),
        borderWidth=0.6,
        borderPadding=8,
        borderRadius=6,
        leftIndent=4,
        rightIndent=4,
        spaceBefore=6,
    )

    story = [
        Paragraph("Computing Power and the Mandelbrot Set", title_style),
        Paragraph(
            "A formal comparison between early-1980s computing systems and a present-day premium mobile device.",
            subtitle_style,
        ),
        Paragraph("Historical context", heading_style),
        Paragraph(
            "Early images of the Mandelbrot Set were generated on machines whose computational resources were extremely limited by present standards. "
            "A high-end mainframe of the early 1980s typically operated in the range of about 10<super>6</super> to 10<super>7</super> elementary operations per second, "
            "while the most powerful supercomputers of the period were on the order of 10<super>8</super> floating-point operations per second.",
            body_style,
        ),
        Paragraph("Present-day mobile hardware", heading_style),
        Paragraph(
            "A contemporary high-end mobile processor can provide throughput on the order of 10<super>11</super> to 10<super>12</super> arithmetic operations per second for this kind of highly parallel image generation "
            "- that is, roughly hundreds of billions to about one trillion operations per second, depending on implementation, precision, and whether graphics hardware is used. "
            "This matters for Mandelbrot rendering because the computation is naturally parallel: each pixel can be evaluated independently.",
            body_style,
        ),
        Spacer(1, 4),
    ]

    table = Table(
        [
            ["System", "Approximate performance"],
            ["High-end early-1980s mainframe", "10^6 to 10^7 operations per second"],
            ["Leading early-1980s supercomputer", "About 10^8 floating-point operations per second"],
            ["Present-day premium mobile device", "About 10^11 to 10^12 operations per second, i.e. hundreds of billions to about one trillion"],
        ],
        colWidths=[66 * mm, 104 * mm],
        hAlign="LEFT",
    )
    table.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#0b2038")),
                ("TEXTCOLOR", (0, 0), (-1, 0), colors.whitesmoke),
                ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
                ("FONTSIZE", (0, 0), (-1, -1), 10),
                ("LEADING", (0, 0), (-1, -1), 13),
                ("TEXTCOLOR", (0, 1), (-1, -1), colors.HexColor("#e2e8f0")),
                ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.HexColor("#10253d"), colors.HexColor("#0e2137")]),
                ("GRID", (0, 0), (-1, -1), 0.5, colors.HexColor("#334155")),
                ("BOX", (0, 0), (-1, -1), 0.75, colors.HexColor("#38bdf8")),
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("LEFTPADDING", (0, 0), (-1, -1), 8),
                ("RIGHTPADDING", (0, 0), (-1, -1), 8),
                ("TOPPADDING", (0, 0), (-1, -1), 7),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 7),
            ]
        )
    )
    story.extend([table, Spacer(1, 10)])

    story.extend(
        [
            Paragraph("Assessment", heading_style),
            Paragraph(
                "It is reasonable to say that, for Mandelbrot-style computation and other highly parallel numerical work, a present-day premium mobile device is at least comparable with a leading Cray-class supercomputer of the early 1980s. "
                "That broad comparison is sound and can be stated confidently in educational material.",
                body_style,
            ),
            Paragraph(
                "It is also reasonable to say that such hardware exceeds the capability of several IBM System/370-class mainframes combined for this type of workload. "
                "The exact multiple depends on the model chosen and on how performance is measured, but the general conclusion is secure.",
                note_style,
            ),
        ]
    )

    doc.build(story, onFirstPage=draw_page_chrome, onLaterPages=draw_page_chrome)


if __name__ == "__main__":
    build_pdf()
