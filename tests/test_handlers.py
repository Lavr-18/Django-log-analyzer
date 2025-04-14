
from reports.handlers import generate_handlers_report

def test_generate_handlers_report(capsys):
    data = {
        "/api/v1/test/": {"DEBUG": 1, "INFO": 2, "WARNING": 0, "ERROR": 1, "CRITICAL": 0}
    }
    generate_handlers_report(data)
    captured = capsys.readouterr()
    assert "/api/v1/test/" in captured.out
    assert "Total requests: 4" in captured.out
