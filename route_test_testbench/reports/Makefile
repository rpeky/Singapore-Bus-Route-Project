TEXFILES := $(wildcard *.tex)
PDFFILES := $(TEXFILES:.tex=.pdf)

.PHONY: all clean distclean

all: $(PDFFILES)
	latexmk -c

%.pdf: %.tex
	latexmk -pdf $<

clean:
	latexmk -c

distclean:
	latexmk -C
