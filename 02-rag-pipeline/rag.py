import sys
from pathlib import Path
# Add current directory to path so we can import src
sys.path.append(str(Path(__file__).parent))

from src.main import app

if __name__ == "__main__":
    app()
