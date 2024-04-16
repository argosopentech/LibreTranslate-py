import json
import sys
from typing import Any, Dict
from urllib import request, parse


class LibreTranslateAPI:
    """Connect to the LibreTranslate API"""

    """Example usage:
    from libretranslatepy import LibreTranslateAPI

    lt = LibreTranslateAPI("https://translate.terraprint.co/")

    print(lt.translate("LibreTranslate is awesome!", "en", "es"))
    # LibreTranslate es impresionante!

    print(lt.detect("Hello World"))
    # [{"confidence": 0.6, "language": "en"}]
    
    print(lt.languages())
    # [{"code":"en", "name":"English"}]
    """

    DEFAULT_URL = "https://translate.terraprint.co/"

    def __init__(self, url: str | None = None, api_key: str | None = None):
        """Create a LibreTranslate API connection.

        Args:
            url (str): The url of the LibreTranslate endpoint.
            api_key (str): The API key.
        """
        self.url = LibreTranslateAPI.DEFAULT_URL if url is None else url
        self.api_key = api_key

        # Add trailing slash
        assert len(self.url) > 0
        if self.url[-1] != "/":
            self.url += "/"

    def translate(self, q: str, source: str = "en", target: str = "es", timeout: int | None = None) -> Any:
        """Translate string

        Args:
            q (str): The text to translate
            source (str): The source language code (ISO 639)
            target (str): The target language code (ISO 639)
            timeout (int): Request timeout in seconds

        Returns:
            str: The translated text
        """
        url = self.url + "translate"
        params: Dict[str, str] = {"q": q, "source": source, "target": target}
        if self.api_key is not None:
            params["api_key"] = self.api_key
        url_params = parse.urlencode(params)
        req = request.Request(url, data=url_params.encode())
        response = request.urlopen(req, timeout = timeout)
        response_str = response.read().decode()
        return json.loads(response_str)["translatedText"]

    def detect(self, q: str, timeout: int | None = None) -> Any:
        """Detect the language of a single text.

        Args:
            q (str): Text to detect
            timeout (int): Request timeout in seconds

        Returns:
            The detected languages ex: [{"confidence": 0.6, "language": "en"}]
        """
        url = self.url + "detect"
        params: Dict[str, str] = {"q": q}
        if self.api_key is not None:
            params["api_key"] = self.api_key
        url_params = parse.urlencode(params)
        req = request.Request(url, data=url_params.encode())
        response = request.urlopen(req, timeout = timeout)
        response_str = response.read().decode()
        return json.loads(response_str)

    def languages(self, timeout: int | None = None) -> Any:
        """Retrieve list of supported languages.

        Args:
            timeout (int): Request timeout in seconds

        Returns:
            A list of available languages ex: [{"code":"en", "name":"English"}]
        """
        url = self.url + "languages"
        params: Dict[str, str] = dict()
        if self.api_key is not None:
            params["api_key"] = self.api_key
        url_params = parse.urlencode(params)
        req = request.Request(url, data=url_params.encode(), method="GET")
        response = request.urlopen(req, timeout = timeout)
        response_str = response.read().decode()
        return json.loads(response_str)
