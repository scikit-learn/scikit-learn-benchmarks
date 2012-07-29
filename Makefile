# Makefile for scikit-learn-speed benchmarks and documentation
#
# You can set these variables from the command line.
PYTHON        ?= python
VBENCH_PYTHON ?= $PYTHON
SPHINXOPTS    ?=
SPHINXBUILD   ?= sphinx-build
PAPER         ?=
BUILDDIR      ?= benchmarks/build

# Internal variables.
SKL_SPEED_ARGS ?= quick
PAPEROPT_a4     = -D latex_paper_size=a4
PAPEROPT_letter = -D latex_paper_size=letter
ALLSPHINXOPTS   = -P -d $(BUILDDIR)/doctrees $(PAPEROPT_$(PAPER)) $(SPHINXOPTS)
WEB_REPO_ALIAS  = origin

.PHONY: help clean clean_db clean_all html rst run

all: run rst html

help:
	@echo "Please use make <target> where <target> is one of"
	@echo "  clean     to clean the results of a previous documentation build"
	@echo "  clean_db  to remove the database resulted from a benchmark run"
	@echo "  clean_all to do both of the above"
	@echo "  html      to make standalone HTML files"
	@echo "  rst       to generate the Sphinx RST sources"
	@echo "  run       to run the benchmarks"

clean_all: clean clean_db

clean_db:
	rm -f benchmarks/benchmarks.db

clean:
	rm -rf $(BUILDDIR)/*
	rm -rf doc/index.rst
	rm -rf doc/vb*.rst
	rm -rf doc/vbench/

html:
	$(SPHINXBUILD) -b html $(ALLSPHINXOPTS) doc $(BUILDDIR)/html
	@echo
	@echo "Build finished. The HTML pages are in $(BUILDDIR)/html."

rst:
	$(PYTHON) benchmarks/generate_rst_files.py $(SKL_SPEED_ARGS)

run:
	$(PYTHON) benchmarks/run_suite.py $(SKL_SPEED_ARGS)

github:
	@echo "Send to github"
	ghp-import -p $(BUILDDIR)/html -r ${WEB_REPO_ALIAS}

# latex:
#	$(SPHINXBUILD) -b latex $(ALLSPHINXOPTS) $(BUILDDIR)/latex
#	@echo
#	@echo "Build finished; the LaTeX files are in $(BUILDDIR)/latex."
#   @echo "Run \`make' in that directory to run these through (pdf)latex" \
#	      "(use \`make latexpdf' here to do that automatically)."

#latexpdf:
#	$(SPHINXBUILD) -b latex $(ALLSPHINXOPTS) $(BUILDDIR)/latex
#	@echo "Running LaTeX files through pdflatex..."
#	make -C $(BUILDDIR)/latex all-pdf
#	@echo "pdflatex finished; the PDF files are in $(BUILDDIR)/latex."
