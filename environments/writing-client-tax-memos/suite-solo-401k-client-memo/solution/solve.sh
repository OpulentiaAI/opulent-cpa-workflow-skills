#!/bin/sh
set -eu
workspace="${HARBOR_WORKSPACE:-/workspace}"
solution_dir="${HARBOR_SOLUTION_DIR:-/solution}"
mkdir -p "$workspace/output"
cp "$solution_dir/reference_answer.md" "$workspace/output/answer.md"
