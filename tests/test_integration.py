
import subprocess
import tempfile
import os

def test_cli_generates_correct_report():
    with tempfile.NamedTemporaryFile("w+", delete=False) as f1, \
         tempfile.NamedTemporaryFile("w+", delete=False) as f2:

        f1.write("INFO 2024 django.request \"GET /test1/\" 200\nDEBUG 2024 django.request \"GET /test1/\" 200\n")
        f2.write("ERROR 2024 django.request \"GET /test1/\" 500\nINFO 2024 django.request \"GET /test2/\" 200\n")

        f1.flush()
        f2.flush()

        result = subprocess.run(
            ["python3", "main.py", f1.name, f2.name, "--report", "handlers"],
            capture_output=True,
            text=True
        )

        os.unlink(f1.name)
        os.unlink(f2.name)

        assert result.returncode == 0
        assert "/test1/" in result.stdout
        assert "Total requests: 4" in result.stdout
