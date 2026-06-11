import json
from pathlib import Path


def save_report(results):

    Path(
        "data/reports"
    ).mkdir(
        parents=True,
        exist_ok=True
    )

    with open(
        "data/reports/report.json",
        "w",
        encoding="utf-8"
    ) as f:

        json.dump(
            results,
            f,
            indent=2,
            ensure_ascii=False
        )