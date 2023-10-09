from __future__ import annotations

class AnswerRetrievalResponseBuilder:
    def __init__(self, question: str, answer: str):
        self.question = question
        self.answer = answer

class AnswerRetrievalResponse():
    def __init__(self, status_code: int, body: AnswerRetrievalResponseBuilder | str):
        self.statusCode = status_code
        self.body = body