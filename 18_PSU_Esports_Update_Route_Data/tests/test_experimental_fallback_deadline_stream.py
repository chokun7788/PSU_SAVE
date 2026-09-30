from __future__ import annotations

import time
import unittest
from unittest.mock import patch

from app.pipeline.experimental_fallback import _call_ollama


class _SlowResponse:
    def __iter__(self):
        while True:
            time.sleep(0.03)
            yield b'{"response":"token","done":false}\n'

    def close(self):
        pass


class ExperimentalFallbackDeadlineStreamTests(unittest.TestCase):
    def test_stream_has_total_budget_not_only_socket_idle_timeout(self) -> None:
        with patch("app.pipeline.experimental_fallback.urllib.request.urlopen", return_value=_SlowResponse()):
            started = time.perf_counter()
            with self.assertRaisesRegex(TimeoutError, "total call budget"):
                _call_ollama("test", timeout_sec=0.05)
        self.assertLess(time.perf_counter() - started, 0.5)


if __name__ == "__main__":
    unittest.main()
