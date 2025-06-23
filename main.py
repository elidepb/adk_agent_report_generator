import os
import uvicorn
from google.adk.cli.fast_api import get_fast_api_app

# Obtiene el directorio donde se encuentra main.py
AGENT_DIR = os.path.dirname(os.path.abspath(__file__))

# Poner en True para servir la interfaz web y poder probar en el navegador
SERVE_WEB_INTERFACE = True

# Llama a la función del ADK para obtener la instancia de la app FastAPI
app = get_fast_api_app(
    agents_dir=AGENT_DIR,
    web=SERVE_WEB_INTERFACE
)

if __name__ == "__main__":
    # Usa la variable de entorno PORT proporcionada por Cloud Run
    port = int(os.environ.get("PORT", 8080))
    uvicorn.run(app, host="0.0.0.0", port=port)