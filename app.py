#!/usr/bin/env python3
import os

import aws_cdk as cdk

from cognition_engine.cognition_engine_stack import CognitionEngineStack


app = cdk.App()
CognitionEngineStack(app, "CognitionEngineStack")

app.synth()
