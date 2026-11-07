#!/usr/bin/env bash
# Arranca la interfaz web de OpenCode. Solo escucha dentro del Codespace.
exec opencode serve --hostname 127.0.0.1 --port 4096
