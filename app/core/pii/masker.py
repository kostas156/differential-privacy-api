from presidio_analyzer import AnalyzerEngine
from presidio_anonymizer import AnonymizerEngine
from presidio_anonymizer.entities import OperatorConfig

DEFAULT_ENTITIES = [
    "PERSON",
    "EMAIL_ADDRESS",
    "PHONE_NUMBER",
    "LOCATION",
    "DATE_TIME",
]

class PIIMasker:
    """
    Wraps Microsoft Presidio to detect and mask PII in unstructured text.
    Initializes engines once at startup to avoid repeated overhead.
    """

    def __init__(self):
        self.analyzer = AnalyzerEngine()
        self.anonymizer = AnonymizerEngine()
    
    def mask(self, text: str, entities: list[str] | None = None) -> dict:
        """
        Detects and masks PII entities in the provided text.

        Args:
            text (str): The unstructured text to anonymize.
            entities (list[str] | None): PII types to detect. Defaults to DEFAULT_ENTITIES.

        Returns:
            Dictionary with masked text, detected entities and detection count.
        """

        entities_to_detect = entities if entities is not None else DEFAULT_ENTITIES

        analyzer_results = self.analyzer.analyze(
            text=text,
            entities=entities_to_detect,
            language="en"
        )

        operators = {
            entity: OperatorConfig("replace", {"new_value": f"[{entity}]"})
            for entity in entities_to_detect
        }

        anonymized = self.anonymizer.anonymize(
            text=text,
            analyzer_results=analyzer_results,
            operators=operators
        )

        detections = [
            {
                "entity_type": result.entity_type,
                "start": result.start,
                "end": result.end,
                "score": round(result.score, 4)
            }
            for result in analyzer_results
        ]

        return {
            "masked_text": anonymized.text,
            "detections": detections,
            "detection_count": len(detections)
        }

  
masker = PIIMasker()