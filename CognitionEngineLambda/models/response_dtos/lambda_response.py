from __future__ import annotations

class LambdaResponse:
    def __init__(self, status_code: int, body: dict | str):
        self.statusCode = status_code
        self.body = body