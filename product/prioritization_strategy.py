# product/prioritization_strategy.py
from typing import List, Dict
import math

class BaseStrategy:
    def apply(self, features: List[str]) -> List[Dict]:
        """
        Convert feature list into scored dicts: {"feature": ..., "score": ...}
        """
        raise NotImplementedError


class RICEStrategy(BaseStrategy):
    def apply(self, features: List[str]) -> List[Dict]:
        scored = []
        for f in features:
            # heuristic: reach ~ number of words, impact ~ keyword count, effort ~ length
            reach = max(1, len(f.split()))
            impact = 1 + sum(1 for kw in ["improve","optimize","fix","reduce","enhance"] if kw in f.lower())
            confidence = 0.7
            effort = max(1, math.ceil(len(f) / 30))
            score = (reach * impact * confidence) / effort
            scored.append({"feature": f, "score": round(score, 3)})
        return scored


class ICEStrategy(BaseStrategy):
    def apply(self, features: List[str]) -> List[Dict]:
        scored = []
        for f in features:
            # simpler heuristic for ICE
            impact = 1 + sum(1 for kw in ["improve","optimize","fix","reduce","increase","add"] if kw in f.lower())
            confidence = 0.6 + 0.1 * min(3, sum(1 for kw in ["analytics","telemetry","logs"] if kw in f.lower()))
            ease = max(1, 5 - sum(1 for kw in ["small","quick","minor"] if kw in f.lower()))
            score = (impact * confidence) / ease
            scored.append({"feature": f, "score": round(score, 3)})
        return scored


class MoSCoWStrategy(BaseStrategy):
    def apply(self, features: List[str]) -> List[Dict]:
        # Map features to Must/Should/Could/Won't based on keywords then to numeric score
        mapping = {
            "must": 100,
            "should": 75,
            "could": 50,
            "won't": 10
        }
        scored = []
        for f in features:
            text = f.lower()
            if any(w in text for w in ["fix","critical","blocker","reliabil"]):
                cat = "must"
            elif any(w in text for w in ["improve","enhance","optimize","better"]):
                cat = "should"
            elif any(w in text for w in ["optional","nice","could","maybe"]):
                cat = "could"
            else:
                cat = "could"
            scored.append({"feature": f, "score": mapping[cat], "moscow": cat})
        return scored


class KanoStrategy(BaseStrategy):
    def apply(self, features: List[str]) -> List[Dict]:
        # Kano categories -> convert to scores (lower = delight, higher = basic requirements prioritised lower/higher depending on approach)
        mapping = {
            "basic": 80,
            "performance": 60,
            "delighter": 40
        }
        scored = []
        for f in features:
            text = f.lower()
            if any(w in text for w in ["fix","error","crash","reliabil","checkout"]):
                cat = "basic"
            elif any(w in text for w in ["optimize","performance","speed","latency"]):
                cat = "performance"
            else:
                cat = "delighter"
            scored.append({"feature": f, "score": mapping[cat], "kano_category": cat})
        return scored
