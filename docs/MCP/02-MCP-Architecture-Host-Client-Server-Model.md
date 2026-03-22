# 02 - MCP Architecture: Host, Client, Server Model

## 2.1 Participants
- Host: AI application coordinating integrations
- Client: connection manager per server
- Server: provider of tools/resources/prompts

## 2.2 Connection Model
One host can run multiple MCP clients, each linked to one MCP server session.

## 2.3 Layers
- data layer (JSON-RPC protocol semantics)
- transport layer (stdio or Streamable HTTP)

## 2.4 Practical Rule
Treat each MCP server as an isolated capability boundary.

