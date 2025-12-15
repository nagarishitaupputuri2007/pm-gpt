# roadmap/roadmap_exporter.py

import json
from datetime import datetime
from pathlib import Path


class RoadmapExporter:
    """
    Exports a generated roadmap to a file (JSON / placeholder for PDF).
    """

    def export(self, roadmap: dict) -> str:
        """
        Saves the roadmap as a JSON file.
        Returns the saved file path.
        """

        export_dir = Path("exports")
        export_dir.mkdir(exist_ok=True)

        filename = f"roadmap_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        file_path = export_dir / filename

        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(roadmap, f, indent=2)

        return str(file_path)
