#### Latex标题左对齐
```tex
\documentclass[UTF8]{ctexart}
\CTEXsetup[format={\Large\bfseries}]{section}
\title{题目}
\begin{document}
\maketitle
\section{标题一}
    内容
\section{标题二}
    内容
\end{document}
```

#### 双列显示
```tex
\documentclass[twocolumn]{article}
\usepackage{ctex}
\usepackage{multicol}

\begin{document}
....
\end{document}
```
