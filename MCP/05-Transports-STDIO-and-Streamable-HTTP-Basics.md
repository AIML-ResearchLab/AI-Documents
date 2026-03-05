# 05 - Transports: STDIO and Streamable HTTP Basics

## 5.1 Supported Transports
- stdio for local process communication
- Streamable HTTP for remote communication

## 5.2 Streamable HTTP Basics
POST/GET patterns with optional SSE streaming support.

## 5.3 Security Baseline
Validate `Origin` headers and bind local servers to localhost where possible.

## 5.4 Compatibility Note
Streamable HTTP replaces older HTTP+SSE design from prior revisions.

