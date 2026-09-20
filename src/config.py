from pathlib import Path
from dotenv import load_dotenv
import os

# --------------------------------------------------
# Rutas del proyecto
# --------------------------------------------------

ROOT_DIR = Path(__file__).resolve().parent.parent

DATA_DIR = ROOT_DIR / "data"
RAW_DATA_DIR = DATA_DIR / "raw"
PROCESSED_DATA_DIR = DATA_DIR / "processed"
OUTPUT_DIR = ROOT_DIR / "outputs"

# Cargar variables del .env ubicado en la raíz
load_dotenv(ROOT_DIR / ".env")

# --------------------------------------------------
# Configuración general
# --------------------------------------------------

SEED = 42

# Modelos del taller
GPT2_MODEL = "openai-community/gpt2"
OPENAI_ECONOMIC_MODEL = "gpt-4o-mini"
OPENAI_REASONING_MODEL = "gpt-5.6"

# API Key
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")


def validate_environment() -> None:
    """
    Verifica que las variables críticas existan antes de ejecutar
    las partes que utilizan OpenAI.
    """
    if not OPENAI_API_KEY:
        raise EnvironmentError(
            "No se encontró OPENAI_API_KEY. "
            "Créala dentro del archivo .env en la raíz del proyecto."
        )