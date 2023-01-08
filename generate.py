import click
import describe
import glob
import re

intro="""\documentclass{article}
\usepackage[utf8]{inputenc}
\usepackage{graphicx}
\usepackage{markdown}

\begin{document}
"""

template = r"""
\begin{figure}[t]
\includegraphics[width=0.9\textwidth]{%02d/map.png}
\end{figure}
\input{%02d/map.md}
"""

@click.command()
@click.argument("directory")
@click.option("-n", default=100)
def main(directory, n):
    describe.do_novel(directory, n)
    with open(directory + "/contents.tex", "w") as f:
        f.write(intro)
        for i in range(n):
            f.write(template % (i,i))
        f.write("\end{document}")
if __name__ == '__main__':
    main()
