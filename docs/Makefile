TEXDIR := tex

TEXFILES := $(wildcard $(TEXDIR)/*.tex)
PDFFILES := $(patsubst $(TEXDIR)/%.tex,%.pdf,$(TEXFILES))

.PHONY: all clean distclean

all: $(PDFFILES)
	$(MAKE) clean

%.pdf: $(TEXDIR)/%.tex
	latexmk -pdf -jobname=$(basename $@) $<

clean:
	rm -f *.aux *.log *.out *.toc *.fls *.fdb_latexmk *.synctex.gz

distclean: clean
	rm -f *.pdf
