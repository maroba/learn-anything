#!/bin/bash
# SessionStart hook for Claude Code on the web: installs Quarto, activates the
# git hooks and checks that the private repo is available.
set -euo pipefail

if [ "${CLAUDE_CODE_REMOTE:-}" != "true" ]; then
  exit 0
fi

QUARTO_VERSION=1.10.18
PROJECT_DIR="${CLAUDE_PROJECT_DIR:-$(cd "$(dirname "$0")/../.." && pwd)}"
PRIVATE_DIR="$(dirname "$PROJECT_DIR")/learn-anything-private"

# Quarto (from the GitHub release; the API is not reachable, the download is)
if [ ! -x "$HOME/.local/opt/quarto-$QUARTO_VERSION/bin/quarto" ]; then
  mkdir -p "$HOME/.local/opt"
  curl -fsSL "https://github.com/quarto-dev/quarto-cli/releases/download/v$QUARTO_VERSION/quarto-$QUARTO_VERSION-linux-amd64.tar.gz" \
    | tar xz -C "$HOME/.local/opt"
fi
mkdir -p "$HOME/.local/bin"
ln -sf "$HOME/.local/opt/quarto-$QUARTO_VERSION/bin/quarto" "$HOME/.local/bin/quarto"
if [ -n "${CLAUDE_ENV_FILE:-}" ]; then
  echo "export PATH=\"\$HOME/.local/bin:\$PATH\"" >> "$CLAUDE_ENV_FILE"
fi

python3 -c "import yaml" 2>/dev/null || pip install --quiet pyyaml

# Guard against committing learner data to the public repo
git -C "$PROJECT_DIR" config core.hooksPath .githooks

# Output goes into Claude's context
if [ -d "$PRIVATE_DIR/.git" ]; then
  echo "learn-anything: Quarto $QUARTO_VERSION ready. Private repo found at $PRIVATE_DIR."
else
  echo "learn-anything: Quarto $QUARTO_VERSION ready. WARNING: the private repo is missing at $PRIVATE_DIR." \
       "Before working on a book, attach maroba/learn-anything-private with the add_repo tool and clone it there."
fi
