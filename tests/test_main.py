from src.main import handler

def test_handler(capsys):
    handler()
    captured = capsys.readouterr()
    assert "Hello from provisioned Python repo!" in captured.out
