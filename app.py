#!/usr/bin/env python3

from aws_cdk import core

from s3proj.s3proj_stack import S3ProjStack


app = core.App()
S3ProjStack(app, "s3proj")

app.synth()
