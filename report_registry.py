
from reports.handlers import generate_handlers_report

def get_report(name: str):
    reports = {
        "handlers": generate_handlers_report
    }
    return reports.get(name)
