writefile =  open('Table_without_MHI.tex', 'w')

total_columns = 2 + 8 # includes names



column1 = ['Airbnb', '', 'Location', '', '', 'Demographic', '', '', 'Neighborhood level', 'Job accessibility', '', 'Constant',
           '\\addlinespace[-1.3em]\midrule\\addlinespace[0.5em] Tests and statistics', '', '', '', '']
column2 = ['Airbnb all rentals',
           'Airbnb composite score',
           'Log BART distance',
           'Log CBD distance',
           'Coastal tracts (dummy)',
           'Unemployment rate',
           'Percentage non-white',
           'Percentage foreign-born',
           #'Log median household income',
           'School district quality',
           'Accessibility by car',
           'Accessibility by transit',
           'Intercept',
           'Log likelihood',
           '$\sigma^2$',
           'Number of observations',
           'deg.\ of freedom',
           'AIC']
           
           
           
           
preamble = ['\documentclass[10pt, letterpaper, landscape]{amsart}',
            '\\usepackage[landscape, left=0.2cm, right=0.2cm, top=1cm]{geometry}', 
            '\\usepackage{booktabs}',
            '\\usepackage[justification=centering]{caption}']

commands = ['\n', '\\newcommand{\entry}[3]{\\begin{tabular}[t]{@{}l@{}} $#1^{#2}$ \\\ $#3$ \end{tabular}}']

begin = ['\n', '\\begin{document}',
         '\pagenumbering{gobble}',
         '',
         '\t\\begin{table}[!ht]',
         '\t\centering',
         '\t\caption{Coefficients and Standard errors for Spatial Lag models (with MHI)}',
         '\t\label{my-label}',
         '\t\\renewcommand{\\arraystretch}{0.7}',
         '\t\\begin{tabular}{@{}llllllllll@{}}',
         '\t\t\\toprule\\\[-2.4ex]\\toprule',
         '\t\t\multicolumn{2}{c}{Independent variables $(X)$} & \multicolumn{8}{c}{Dependent variable $(Y)$} \\\ \midrule',
         '\t\t\\addlinespace[0.5em]',
         '\t\tCategory & Variable name & \multicolumn{2}{c}{Rent burdened} & \multicolumn{2}{c}{Rent over-burdened}',
         '\t\t& \multicolumn{2}{c}{Log median rent} & \multicolumn{2}{c}{Log median house price} \\\ ',
         '\t\t\\addlinespace[0.5em]',
         '\t\t & &\multicolumn{1}{c}{Model 1} & \multicolumn{1}{c}{Model 2} & \multicolumn{1}{c}{Model 3}&\multicolumn{1}{c}{Model 4} &', 
         '\t\t\multicolumn{1}{c}{Model 5} & \multicolumn{1}{c}{Model 6} & \multicolumn{1}{c}{Model 7} & \multicolumn{1}{c}{Model 8}\\\ ', 
         '\t\t\midrule[.5pt]',
         '\t\t\\addlinespace[0.5em]']

end = ['',
       '\\\ \midrule\\\[-2.8ex]\\bottomrule',
       '\t\t\\\ ',
       '\t\t\emph{Notes:} & \multicolumn{9}{l}{${}^{*}p<0.1; \quad {}^{**}p<0.05;  \quad {}^{***}p<0.01 $ } \\\ ',
       '\t\t\end{tabular}',
       '\t\end{table}',
       '\end{document}']

readfile = open('Without_MHI_Cleaned.txt', 'r')
lines = readfile.readlines()
lines = [i.strip() for i in lines]

# Sanity checks:
for i in lines:
    if i[0] == '=':
        pass
    elif len(i.split(',')) != 3:
        print('Error: some lines are missing entries', i)
        quit()

counter = 0
columns = [[] for i in range(total_columns-2)]
for i in lines:
    if i[0] == '=':
        counter += 1
    else:
        columns[counter].append(i.split(','))

table = [[] for i in range(len(columns[0]))]
for i in range(len(columns[0])):
    table[i].append('\n\t\t\\addlinespace[0.5em]')
    if column1[i]:
        table[i][0] += '\n\t\t\\addlinespace[1.3em]' + column1[i]
    table[i].append(column2[i])


switch = 0
for row in range(len(columns[0])):
    for c in range(total_columns-2):
        if row >= 13:
            table[row].append('{}'.format(columns[c][row][0]))
        else:
            table[row].append('\entry{{{0}}}{{{1}}}{{{2}}}'.format(*columns[c][row]))
    table[row] = '\n\t\t\t & '.join(table[row])
table = ['\t' + '\\\\\n\t'.join(table)]




print(table)








writefile.write('\n'.join(preamble + commands + begin + table + end))


writefile.close()
readfile.close()
