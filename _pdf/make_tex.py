import os
import re


def preamble():
    return """
\\documentclass[a4paper]{book}
\\usepackage{amsfonts}
\\usepackage{amsmath}
\\usepackage{graphicx}
\\usepackage{pythonhighlight}
\\usepackage{hyperref}
\\title{The Bempp Handbook}
\\author{Timo Betcke and Matthew W. Scroggs}
\\begin{document}
\\maketitle
"""


def postamble():
    return """
\\end{document}
"""

sections = ["", "part", "chapter", "section", "subsection", "subsubsection"]

def title(level):
    return lambda matches: "\\" + sections[level] + "{" + matches[1] + "}"


def pyth_to_verb(matches):
    return "\\verb@" + matches[1] + "@"


def parse_markdown_tables(md):
    table = False
    out = ""
    for line in (md + "\n\n").split("\n"):
        if table:
            if "|" in line:
                if re.match(r"^\|? ?---+(?: ?\|? ? ---+)+ ?\|?$", line.strip()):
                    out += "\\hline\n"
                else:
                    line = re.sub(r"\\pyth\{([^\}]+)\}", pyth_to_verb, line)
                    line = line.replace("\\[", "$\\displaystyle ")
                    line = line.replace("\\]", "$")
                    line = line.replace("|", "&")
                    out += line + "\\\\\n"
            else:
                out += "\\end{tabular}\n\\end{center}\n"
                table = False
        else:
            if re.match(r"^\|? ?---+(?: ?\|? ? ---+)+ ?\|?$", line.strip()):
                out += "\\begin{center}\n\\begin{tabular}{"
                out += "|l" * (line.strip()[1:-1].count("|") + 1) + "|"
                out += "}\n\\hline\n"
                table = True
            else:
                out += line + "\n"
    return out


def markdown_to_tex(md, level):
    md = re.sub(r"###([^\n]+)\n", title(level + 2), md)
    md = re.sub(r"##([^\n]+)\n", title(level + 1), md)
    md = md.replace("[[", "\\[")
    md = md.replace("]]", "\\]")
    while re.search(r"(```python[^`]*)\\\[([^`]*```)", md):
        md = re.sub(r"(```python[^`]*)\\\[([^`]*```)", r"\1[[\2", md)
    while re.search(r"(```python[^`]*)\\\]([^`]*```)", md):
        md = re.sub(r"(```python[^`]*)\\\]([^`]*```)", r"\1]]\2", md)
    md = md.replace("```python", "\\begin{python}")
    md = md.replace("```", "\\end{python}")
    md = re.sub(r"`([^`]+)`", r"\\pyth{\1}", md)
    md = md.replace("&times;", "$\\times$")
    md = md.replace("\\\\{", "\\{")
    md = md.replace("\\\\}", "\\}")
    md = md.replace("\\\\\\\\", "\\\\")
    md = md.replace("{% raw %}", "")
    md = md.replace("{% raw %}", "")
    md = md.replace("{% endraw %}", "")
    md = re.sub(r"!\[([^\]]+)\]\(([^\)]+)\)(?:\{[^\}]+\})?",
                r"\\begin{center}\n\\includegraphics[width=0.6\\textwidth]{\2}\n\n\\footnotesize{\1}\\end{center}", md)
    md = re.sub(r"\[([^\]]+)\]\(([^\)]+)\)", r"\\href{\2}{\1}", md)
    md = parse_markdown_tables(md)
    return html_to_tex(md)


def html_to_tex(html):
    for vowel in ["a", "e", "i", "o", "u"]:
        html = html.replace(f"&{vowel}acute;", f"\\'{vowel}")
        html = html.replace(f"&{vowel}grave;", f"\\`{vowel}")
    html = html.replace("<em>", "\\emph{")
    html = html.replace("</em>", "}")
    return html


def parse_yaml_data(data):
    out = {}
    if "title:" in data:
        out["title"] = data.split("title:")[1].split("\n")[0].strip()
    if "layout:" in data:
        out["layout"] = data.split("layout:")[1].split("\n")[0].strip()
    out["children"] = []
    if "children:\n" in data:
        for line in data.split("children:\n")[1].split("\n"):
            if not line.strip().startswith("- "):
                break
            out["children"].append(line.strip()[1:].strip())
    return out


def parse_file(filename, folder="..", level=0):
    out = ""
    if level == 0:
        out += preamble()
    with open(os.path.join(folder, filename)) as f:
        content = f.read().strip()
    if content.startswith("---\n"):
        data, content = content[3:].split("---", 1)
    else:
        data = ""
    data = parse_yaml_data(data)
    if level > 0:
        out += "\\" + sections[level] + "{" + html_to_tex(data["title"]) + "}\n"
    out += markdown_to_tex(content, level)
    for file in data["children"]:
        out += parse_file(file, folder, level + 1)
    if level == 0:
        out += postamble()
    return out


with open("handbook.tex", "w") as f:
    f.write(parse_file("index.md"))
