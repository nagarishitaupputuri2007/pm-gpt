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
    # BASIC ROADMAP ONLY
    # --------------------------------------------------
    def export(self, roadmap: dict) -> str:
        filename = f"pm_gpt_roadmap_{datetime.now().strftime('%Y%m%d_%H%M%S')}.pdf"
        path = os.path.join(self.export_dir, filename)

        doc = SimpleDocTemplate(path, pagesize=A4)
        elements = []

        elements.append(Paragraph("Product Roadmap", self.styles["Title"]))
        elements.append(Spacer(1, 12))

        for phase, items in roadmap.items():
            elements.append(Paragraph(str(phase), self.styles["Heading2"]))
            elements.append(Spacer(1, 6))

            if items:
                elements.append(
                    ListFlowable(
                        [
                            ListItem(
                                Paragraph(str(item), self.styles["Normal"])
                            )
                            for item in items
                        ]
                    )
                )
            else:
                elements.append(
                    Paragraph("No items", self.styles["Normal"])
                )

            elements.append(Spacer(1, 12))

        doc.build(elements)
        return path

    # --------------------------------------------------
    # FULL ANALYSIS EXPORT (STABLE & SAFE)
    # --------------------------------------------------
    def export_full_analysis(self, analysis: dict) -> str:
        """
        Exports the entire PM-GPT analysis into ONE PDF.
        SAFE for dicts, lists, and strings.
        """

        filename = f"pm_gpt_full_analysis_{datetime.now().strftime('%Y%m%d_%H%M%S')}.pdf"
        path = os.path.join(self.export_dir, filename)

        doc = SimpleDocTemplate(path, pagesize=A4)
        elements = []

        # -------------------------
        # TITLE
        # -------------------------
        elements.append(
            Paragraph("PM-GPT – Full Product Analysis", self.styles["Title"])
        )
        elements.append(Spacer(1, 14))

        # -------------------------
        # PROBLEM SUMMARY
        # -------------------------
        elements.append(
            Paragraph("Problem Summary", self.styles["Heading2"])
        )

        problem = analysis.get("problem", {})
        problem_text = (
            problem.get("summary", "")
            if isinstance(problem, dict)
            else str(problem)
        )

        elements.append(
            Paragraph(str(problem_text), self.styles["Normal"])
        )
        elements.append(Spacer(1, 12))

        # -------------------------
        # FEATURES
        # -------------------------
        elements.append(
            Paragraph("Generated Features", self.styles["Heading2"])
        )

        features = analysis.get("features", [])
        if features:
            elements.append(
                ListFlowable(
                    [
                        ListItem(
                            Paragraph(str(feature), self.styles["Normal"])
                        )
                        for feature in features
                    ]
                )
            )
        else:
            elements.append(
                Paragraph("No features generated.", self.styles["Normal"])
            )

        elements.append(Spacer(1, 12))

        # -------------------------
        # FRAMEWORK
        # -------------------------
        elements.append(
            Paragraph("Framework Selected", self.styles["Heading2"])
        )
        elements.append(
            Paragraph(str(analysis.get("framework", "")), self.styles["Normal"])
        )
        elements.append(Spacer(1, 6))

        elements.append(
            Paragraph("Framework Explanation", self.styles["Heading3"])
        )
        elements.append(
            Paragraph(
                str(analysis.get("framework_explanation", "")),
                self.styles["Normal"]
            )
        )
        elements.append(Spacer(1, 12))

        # -------------------------
        # PRIORITIZATION
        # -------------------------
        elements.append(
            Paragraph("Prioritized Features", self.styles["Heading2"])
        )

        for item in analysis.get("prioritization", []):
            text = f"{item.get('feature', '')} — Score: {item.get('score', 'N/A')}"
            elements.append(
                Paragraph(str(text), self.styles["Normal"])
            )

        elements.append(Spacer(1, 12))

        # -------------------------
        # ROADMAP
        # -------------------------
        elements.append(
            Paragraph("6-Month Roadmap", self.styles["Heading2"])
        )

        roadmap = analysis.get("roadmap", {})
        for phase, items in roadmap.items():
            elements.append(
                Paragraph(str(phase), self.styles["Heading3"])
            )

            if items:
                elements.append(
                    ListFlowable(
                        [
                            ListItem(
                                Paragraph(str(item), self.styles["Normal"])
                            )
                            for item in items
                        ]
                    )
                )
            else:
                elements.append(
                    Paragraph("No items", self.styles["Normal"])
                )

            elements.append(Spacer(1, 8))

        # -------------------------
        # BUILD PDF
        # -------------------------
        doc.build(elements)

        return path
