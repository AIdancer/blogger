### 模板1
```

\documentclass[UTF8]{ctexart}
\usepackage{amsmath}
\usepackage{graphicx}

\title{你好,world!}
\author{Moon}
\date{\today}

\begin{document}
\tableofcontents
\maketitle
\section{你好中国}


中国在East Asia.
\subsection{Hello Beijing}


北京是capital of China.
\subsubsection{Hello Dongcheng District}
\paragraph{Tian'anmen Square}
is in the center of Beijing
\subparagraph{Chaiman Mao}


is in the center of 天安门广场。
\subsection{Hello 山东}
\paragraph{hahaha}

is one of the best university in 山东。

\section{插入公式}
这是行内公式：$a^{n} + b^{n} = c^{n}$

\section{这是行间公式}
\begin{equation}
a^2 + b^2 = c^2
\end{equation}
$
a^3 + b^3 = c^3\\
a^{p} + b^{m} = c^{k}
$

\section{换行}
\paragraph{看看换行效果}
哈哈哈哈哈哈，要换行了哦\\
已换行。

\section{上下标}
Einstein 's $E=mc^2$.

\[ E=mc^2. \]
\[ H = m^3. \]

\[ z = r\cdot e^{2\pi i}. \]

\[ \sqrt{x}, \frac{1}{2}. \]

\[ \sqrt{x}, \]

\[ \frac{1}{2}. \]

\begin{equation}
E=mc^2.
\end{equation}

\paragraph{运算符}
\[ \pm\; \times \; \div\; \cdot\; \cap\; \cup\;
\geq\; \leq\; \neq\; \approx \; \equiv \]

$ \sum_{i=1}^n i\quad \prod_{i=1}^n $
$ \sum\limits _{i=1}^n i\quad \prod\limits _{i=1}^n $
\[ \lim_{x\to0}x^2 \quad \int_a^b x^2 dx \]
\[ \lim\nolimits _{x\to0}x^2\quad \int\nolimits_a^b x^2 dx \]
多重积分\\
\[ \iint\quad \iiint\quad \iiiint\quad \idotsint \]

\paragraph{定界符}
\[ \Biggl(\biggl(\Bigl(\bigl((x)\bigr)\Bigr)\biggr)\Biggr) \]
\[ \Biggl[\biggl[\Bigl[\bigl[[x]\bigr]\Bigr]\biggr]\Biggr] \]
\[ \Biggl \{\biggl \{\Bigl \{\bigl \{\{x\}\bigr \}\Bigr \}\biggr \}\Biggr\} \]
\[ \Biggl\langle\biggl\langle\Bigl\langle\bigl\langle\langle x
\rangle\bigr\rangle\Bigr\rangle\biggr\rangle\Biggr\rangle \]
\[ \Biggl\lvert\biggl\lvert\Bigl\lvert\bigl\lvert\lvert x
\rvert\bigr\rvert\Bigr\rvert\biggr\rvert\Biggr\rvert \]
\[ \Biggl\lVert\biggl\lVert\Bigl\lVert\bigl\lVert\lVert x
\rVert\bigr\rVert\Bigr\rVert\biggr\rVert\Biggr\rVert \]

\paragraph{省略号}
\[ x_1,x_2,\dots ,x_n\quad 1,2,\cdots ,n\quad
\vdots\quad \ddots \]

\paragraph{矩阵}
\[ \begin{pmatrix} a&b\\c&d \end{pmatrix} \quad
\begin{bmatrix} a&b\\c&d \end{bmatrix} \quad
\begin{Bmatrix} a&b\\c&d \end{Bmatrix} \quad
\begin{vmatrix} a&b\\c&d \end{vmatrix} \quad
\begin{Vmatrix} a&b\\c&d \end{Vmatrix} \]

\paragraph{多行公式}
\begin{multline}
x = a+b+c+{} \\
d+e+f+g
\end{multline}

\paragraph{公式组}
\begin{gather}
a = b+c+d \\
x = y+z
\end{gather}
\begin{align}
a &= b+c+d \\
x &= y+z
\end{align}

\paragraph{分段函数}
\[ y= \begin{cases}
-x,\quad x\leq 0 \\
x,\quad x>0
\end{cases} \]

\section{插入图片}
\includegraphics[width = .8\textwidth]{a.jpg}

\paragraph{表格}
\begin{tabular}{|l|c|r|}
 \hline
操作系统& 发行版& 编辑器\\
 \hline
Windows & MikTeX & TexMakerX \\
 \hline
Unix/Linux & teTeX & Kile \\
 \hline
Mac OS & MacTeX & TeXShop \\
 \hline
通用& TeX Live & TeXworks \\
 \hline
\end{tabular}

\section{浮动体}
\begin{figure}[htbp]
\centering
\includegraphics{a.jpg}
\caption{有图有真相}
\label{fig:myphoto}
\end{figure}

\end{document}
```

### 模板2
```
\documentclass[UTF8]{ctexart}
\usepackage{amsmath}
\usepackage{graphicx}
\usepackage{subfigure}

\title{策略简介}
\author{Zhao Liqiang}
\date{\today}

\begin{document}
\maketitle
\section{策略简介}
\paragraph{多因子模型}
\begin{gather}
score(stock) = \sum_{i=1}^n w_i*factor_i(stock) \\
\sum_{i=1}^n w_i = 1.0
\end{gather}
\begin{enumerate}
\item 股票池初选(初步打分/排除st/机器学习及深度学习分类、聚类/1000只)
\item 基本面因子(60\%)
\item 量价因子(40\%)
\item 参数搜索，组合优化
\item 基金经理组合检验及人工排雷
\item vwap下单
\item 交易员手工T0
\item 按周换仓
\item 等权
\item 打新、期指CTA
\end{enumerate}

\section{收益统计}
\begin{figure}
\centering
\subfigure{\includegraphics[width = \textwidth]{backtest.png}}
\subfigure{\includegraphics[width = \textwidth]{real.png}}
\caption{策略回测超额及2020年实盘股票组合超额}
\end{figure}

\end{document}
```
