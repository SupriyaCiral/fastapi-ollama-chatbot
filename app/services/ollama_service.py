import time
import httpx

from app.config import settings
from app.core.logger import logger


class OllamaService:
    """
    Service class responsible for communicating with the
    local Ollama REST API.
    """

    def __init__(self):
        self.base_url = settings.OLLAMA_BASE_URL
        self.model = settings.MODEL_NAME

    def generate_response(self, prompt: str) -> str:
        """
        Sends a prompt to the Ollama model and returns the generated response.

        Args:
            prompt (str): User question

        Returns:
            str: AI generated answer
        """

        url = f"{self.base_url}/api/generate"

        payload = {
            "model": self.model,
            "prompt": prompt,
            "stream": False
        }

        logger.info("=" * 60)
        logger.info(f"Using Model : {self.model}")
        logger.info(f"Prompt      : {prompt}")

        start_time = time.time()

        try:

            response = httpx.post(
                url=url,
                json=payload,
                timeout=180
            )

            # Raises exception if HTTP status is not 200
            response.raise_for_status()

            elapsed = time.time() - start_time

            logger.info(f"Response Time : {elapsed:.2f} seconds")

            result = response.json()

            logger.info("Response received successfully from Ollama")

            return result["response"]

        except httpx.ReadTimeout:
            logger.error("Request timed out while waiting for Ollama.")

            raise Exception(
                "Ollama took too long to respond. Increase timeout or use a smaller model."
            )

        except httpx.ConnectError:
            logger.error("Unable to connect to Ollama server.")

            raise Exception(
                "Could not connect to Ollama. Make sure Ollama is running."
            )

        except httpx.HTTPStatusError as e:
            logger.error(f"HTTP Error: {e}")

            raise Exception(
                f"Ollama returned HTTP Status {e.response.status_code}"
            )

        except Exception as e:
            logger.exception("Unexpected Error")

            raise Exception(str(e))