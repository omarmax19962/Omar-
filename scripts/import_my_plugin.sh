#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
TARGET_DIR="${ROOT_DIR}/external/My-Plugin"
URL="https://github.com/omarmax19962/My-Plugin.git"

rm -rf "${TARGET_DIR}"
git clone --depth 1 "${URL}" "${TARGET_DIR}"

echo "Imported My-Plugin into ${TARGET_DIR}"
