# Rough word count of abstract.tex (text, captions, references; excludes comments, preamble and appendix).
import re

with open(r"D:\MAIO\abstract.tex", encoding="utf-8") as f:
    tex = f.read()

body = tex.split(r"\begin{document}")[1].split(r"\clearpage")[0]
body = re.sub(r"(?<!\\)%.*", "", body)                                  # comments
body = re.sub(r"\\SI\{([^}]*)\}\{[^}]*\}", r"\1 unit", body)             # \SI{8.1}{...} -> 8.1 unit
body = re.sub(r"\\(includegraphics|label|ref|begin|end|bibitem)(\[[^\]]*\])?\{[^}]*\}", " ", body)
body = re.sub(r"\\[a-zA-Z]+\*?", " ", body)                              # other commands
body = re.sub(r"[{}$\\^_~]", " ", body)
words = [w for w in body.split() if re.search(r"[A-Za-z0-9]", w)]
print("approximate word count:", len(words))
