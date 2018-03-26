all: lista-1.pdf lista-2.pdf lista-3.pdf

lista-%.pdf: lista-%.tex
	pdflatex $^

clean:
	@rm lista-*.pdf *.log *.aux
