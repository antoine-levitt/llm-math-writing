#!/bin/sh
set -eu
paper_dir=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
cd -- "$paper_dir"
build_dir="$paper_dir/../prompt-version-build"
mkdir -p -- "$build_dir"
timeout 55 /usr/bin/pdflatex -interaction=nonstopmode -halt-on-error -file-line-error -no-shell-escape -output-directory="$build_dir" main.tex > "$build_dir/compile.log" 2>&1
(
  cd -- "$build_dir"
  BIBINPUTS="$paper_dir:" timeout 55 /usr/bin/bibtex main > bibtex.log 2>&1
)
timeout 55 /usr/bin/pdflatex -interaction=nonstopmode -halt-on-error -file-line-error -no-shell-escape -output-directory="$build_dir" main.tex > "$build_dir/compile.log" 2>&1
timeout 55 /usr/bin/pdflatex -interaction=nonstopmode -halt-on-error -file-line-error -no-shell-escape -output-directory="$build_dir" main.tex > "$build_dir/compile.log" 2>&1
cp -- "$build_dir/main.pdf" "$paper_dir/main.pdf"
