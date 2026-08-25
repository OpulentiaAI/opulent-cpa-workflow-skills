FROM python:3.13-slim
WORKDIR /workspace
COPY source_docs/ /workspace/source_docs/
RUN mkdir -p /workspace/output && chmod -R a+rX /workspace/source_docs && chmod a+rwx /workspace/output
