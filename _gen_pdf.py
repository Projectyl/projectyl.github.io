#!/bin/python

import csv
import os
import pypandoc

folder = "./_data/summer/"
files = os.listdir(folder)
files = [file for file in files if ".csv" in file]
md_file = "./_data/summer/summer.md"
pdf_file = "./_data/summer/summer.pdf"

f = open(md_file, 'w')
f.close()
f = open(md_file, 'a')
pandoc_options = ['fontfamily: FiraSans', 'fontfamilyoptions: sfdefault', 'fontsize: 11pt', 'header-includes: |', '\t\\usepackage{hyperref,booktabs,colortbl,color,xcolor}', '\t\\usepackage[textheight=70cm,margin=2cm]{geometry}']
frontmatter = '---\n' + '\n'.join(pandoc_options) + '\n---\n'
f.write(frontmatter)

f.write('\\definecolor{lyellow}{RGB}{255,239,213}\n')
f.write('\\def\\arraystretch{1.2}\n')
f.write('\\pagecolor{lyellow}\n')

f.write("\\section*{\\textcolor{blue}{Summer Internship Programs}}\n")
f.write('\\vspace{-20pt}\n\\rule{\\textwidth}{2pt}\n\n')
f.write('The institute names in the left columns are hyperlinks to the respective webpages.\n')
titles = ['Active Programs', 'Yet to be Declared', 'Currently Inactive/Closed']
assert len(titles) == len(files)

for title,file in zip(titles,files):
    f.write('\\vspace{10pt}\n')
    f.write('\\begin{minipage}{\\textwidth}\n')
    f.write('\\subsection*{\\textcolor{purple}{' + title + '}}' + '\n\n')
    f.write('\\vspace{-15pt}\n\\rule{\\textwidth}{1.5pt}\\\\\n')
    data = list(csv.reader(open(folder+file, 'r'), delimiter=','))
    ncols = len(data[0])
    f.write('\\begin{center}\n\\begin{tabular}{l'+'c'*(ncols-2)+'}\n')
    head = ['\\textcolor{white}{\\textbf{'+datum+'}}' for datum in data[0]]
    f.write('\\rowcolor{darkgray}\n')
    f.write(' & '.join(head[:-1]) + '\\\\\n')
    colors = ['lyellow', 'lightgray']
    for row in data[1:]:
        colors = [colors[-1]] + [colors[0]]
        if len(row) == 0: continue
        inst = row[0]
        link = row[-1]
        f.write('\\rowcolor{' + colors[0] + '}\n')
        f.write('\href{' + link + '}{' + inst + '} & ' + ' & '.join(row[1:-1]) + ' \\\\\n')

    f.write('\\end{tabular}\n\\end{center}\n')
    f.write('\\end{minipage}\\\n')

f.write('\\rule{\\textwidth}{2pt}\n')
f.close()

out = os.system('pandoc ' + md_file + ' -t latex ' + ' -o ' + pdf_file)
assert out == 0
