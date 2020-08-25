THIS = bempp-website-pdf

.PHONY: all tex pdf

all: tex pdf

tex:
	python make_tex.py

pdf:
	pdflatex handbook.tex
	pdflatex handbook.tex

