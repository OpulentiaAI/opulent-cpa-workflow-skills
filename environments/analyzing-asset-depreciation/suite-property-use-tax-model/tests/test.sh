#!/bin/sh
set -eu
python3 "${HARBOR_TESTS_DIR:-/tests}/grade_text.py"
