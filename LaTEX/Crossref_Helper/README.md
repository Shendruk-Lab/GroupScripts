# Crossref helper
Allows for crossreferencing between different .tex files on both local LaTeX and Overleaf. 
Particularly useful for referencing text or figures in the SM.

Adapted from cyberSingularity at [StackExchange](http://tex.stackexchange.com/a/69832/226).

## Instructions
1. Add both the crossref_helper.tex and latexmkrc file to your repo. Latexmkrc must be at the repo root.
2. Call `\input{/path/to/crossref_helper.tex}` in your source .tex file
3. Following the input, add calls of `\myexternaldocument{path/to/file[without extension]}` to each external file you wish to reference.