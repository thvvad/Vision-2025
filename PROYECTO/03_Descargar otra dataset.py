# Instala la librería de datasets si no está
import subprocess
import sys

subprocess.check_call([sys.executable, "-m", "pip", "install", "datasets", "huggingface_hub", "Pillow"])
