# roadmap/roadmap_exporter.py

from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    ListFlowable,
    ListItem
)
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import A4
from datetime import datetime
import os


class RoadmapExporter:
    """
    Exports PM-GPT outputs into PDF documents.
    """

    def __init__(self, export_dir: str = "exports"):
        os.makedirs(export_dir, exist_ok=True)
        self.export_dir = export_dir
        self.styles = getSampleStyleSheet()

    # --------------------------------------------------
    # BASIC ROADMAP ONLY (already working)
    # --------------------------------------------------
    def export(self, roadmap: dict) -> str:
        filename = f"pm_gpt_roadmap_{datetime.now().strftime('%Y%m%d_%H%M%S')}.pdf"
        path = os.path.join(self.export_dir, filename)

        doc = SimpleDocTemplate(path, pagesize=A4)
        elements = []

        elements.append(Paragraph("<b>Product Roadmap</b>", self.styles["Title"]))
        elements.append(Spacer(1, 12))

        for phase, items in roadmap.items():
            elements.append(Paragraph(f"<b>{phase}</b>", self.styles["Heading2"]))
            elements.append(Spacer(1, 6))

            if items:
                elements.append(
                    ListFlowable(
                        [ListItem(Paragraph(item, self.styles["Normal"])) for item in items]
                    )
                )
            else:
                elements.append(Paragraph("No items", self.styles["Normal"]))

            elements.append(Spacer(1, 12))

        doc.build(elements)
        return path

    # --------------------------------------------------
    # ✅ FULL ANALYSIS EXPORT (THIS FIXES YOUR ERROR)
    # --------------------------------------------------
    def export_full_analysis(self, analysis: dict) -> str:
        """
        Exports the entire PM-GPT analysis into ONE PDF.
        """

        filename = f"pm_gpt_full_analysis_{datetime.now().strftime('%Y%m%d_%H%M%S')}.pdf"
        path = os.path.join(self.export_dir, filename)

        doc = SimpleDocTemplate(path, pagesize=A4)
        elements = []

        # Title
        elements.append(Paragraph("PM-GPT – Full Product Analysis", self.styles["Title"]))
        elements.append(Spacer(1, 14))

        # Problem
        elements.append(Paragraph("<b>Problem Summary</b>", self.styles["Heading2"]))
        elements.append(Paragraph(analysis["problem"], self.styles["Normal"]))
        elements.append(Spacer(1, 12))

        # Features
        elements.append(Paragraph("<b>Generated Features</b>", self.styles["Heading2"]))
        elements.append(
            ListFlowable(
                [ListItem(Paragraph(f, self.styles["Normal"])) for f in analysis["features"]]
            )
        )
        elements.append(Spacer(1, 12))

        # Framework
        elements.append(Paragraph("<b>Framework Selected</b>", self.styles["Heading2"]))
        elements.append(Paragraph(analysis["framework"], self.styles["Normal"]))
        elements.append(Spacer(1, 6))
        elements.append(Paragraph(analysis["explanation"], self.styles["Normal"]))
        elements.append(Spacer(1, 12))

        # Prioritization
        elements.append(Paragraph("<b>Prioritized Features</b>", self.styles["Heading2"]))
        for item in analysis["prioritization"]:
            text = f"{item['feature']} — Score: {item.get('score', 'N/A')}"
            elements.append(Paragraph(text, self.styles["Normal"]))
        elements.append(Spacer(1, 12))

        # Roadmap
        elements.append(Paragraph("<b>Roadmap</b>", self.styles["Heading2"]))
        for phase, items in analysis["roadmap"].items():
            elements.append(Paragraph(phase, self.styles["Heading3"]))
            if items:
                elements.append(
                    ListFlowable(
                        [ListItem(Paragraph(i, self.styles["Normal"])) for i in items]
                    )
                )
            else:
                elements.append(Paragraph("No items", self.styles["Normal"]))
            elements.append(Spacer(1, 8))

        doc.build(elements)
        return path
