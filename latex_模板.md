### paragraph首行缩进
<p>
 LaTeX 默认的第一段不是首行缩进的, 这不符合我们的中文习惯. <br>
要实现首行缩进也很简单, <br>
在导言区加入宏包首行 \usepackage{indentfirst} 就可以了. (LaTeX 学习博客 (http://latex.yo2.cn) , 白色印记.) <br>
使用命令 设置 缩进的距离 \setlength{\parindent}{2em}  , <br>
这里的 2em 表示缩进 2 个字符位置. <br>
如果有一个段落你不想首行缩进, 在段落前使用命令 \noindent . <br>
同样的, 你要保证这一段是首行缩进, 使用命令 \indent, 如果使用了 CJK 宏包, 还可以用\CJKindent. <br>
</p>

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

### 模板3
```
\documentclass[UTF8]{ctexart}
\usepackage{amsmath}
\usepackage{graphicx}

\CTEXsetup[format={\Large\bfseries}]{section}

\title{磁盘故障预测简报}
\author{Zhao Liqiang}
\date{\today}

\begin{document}
%\tableofcontents
\maketitle

\section{数据描述}
\paragraph{}~{数据字段包含了63个SMART特征，有归一化及原始两个版本。目前使用的为归一化版本，主要原因是目前对原始值及其含义并不了解。对数据处理后，每一天的csv提取为一个 $m*n$ 的矩阵，矩阵的行为记录条数，前$n-1$列为63个特征值，最后一列为$label$。}\\

\centerline{\includegraphics[scale=0.6]{data_fields.PNG}}

\paragraph{缺失值填充}~{特征中还有很多$nan$值，目前的处理方式是将所有的$nan$值置零。}\\
\paragraph{特征采样}~{由于正样本（磁盘出现错误）占整体数据的比例非常少，大概十几万条的数据中，只有个位数的样本报错；因此数据是严重偏斜的。目前做了1:1，1:2，1:5，1:10配比的正负样本采样对比。}\\

\section{xgboost初步分类测试}
\paragraph{}~{目前的测试使用了经过归一化后的全部特征，几种配比训练出的模型效果如下：}\\

\begin{figure}[htbp]
\begin{minipage}[t]{0.35\linewidth}
\centering
\includegraphics[height=3.5cm,width=6cm]{res1-1.PNG}
\caption{正负 1:1}
\end{minipage}%
\hfill
\begin{minipage}[t]{0.35\linewidth}
\centering
\includegraphics[height=3.5cm,width=6cm]{res1-2.PNG}
\caption{正负 1:2}
\end{minipage}
\end{figure}
\begin{figure}[htbp]
\begin{minipage}[t]{0.35\linewidth}
\centering
\includegraphics[height=3.5cm,width=6cm]{res1-5.PNG}
\caption{正负 1:5}
\end{minipage}%
\hfill
\begin{minipage}[t]{0.35\linewidth}
\centering
\includegraphics[height=3.5cm,width=6cm]{res1-10.PNG}
\caption{正负 1:10}
\end{minipage}
\end{figure}

\paragraph{特征权重及选择}~{如下图所示，最重要的前9个特征有：f0(smart\_1\_normalized), f2(smart\_3\_normalized), f5(smart\_7\_normalized), f7(smart\_9\_normalized), f29(smart\_187\_normalized), f32(smart\_190\_normalized), f35(smart\_193\_normalized), f36(smart\_194\_normalized), f37(smart\_195\_normalized)}\\

\begin{figure}[htbp]
\centering
\includegraphics[scale=0.6]{feature_imp_1-1.png}
\caption{正负配比 1:1}

\centering
\includegraphics[scale=0.6]{feature_imp_1-2.png}
\caption{正负配比 1:2}
\end{figure}

\begin{figure}[htbp]
\centering
\includegraphics[scale=0.6]{feature_imp_1-5.png}
\caption{正负配比 1:5}

\centering
\includegraphics[scale=0.6]{feature_imp_1-10.png}
\caption{正负配比 1:10}
\end{figure}

\section{下一步打算}
\paragraph{精选特征}~{只使用比较重要的特征，减少噪音数据的影响。}\\
\paragraph{使用概率预测}~{不在xgboost中使用类别，通过调整概率预测的阈值提高故障检测能力。}\\
\paragraph{使用异常检测}~{数据偏斜实在非常严重，接下来将对重点特征尝试进行异常检测，并尽可能挖掘特征值与后续事件磁盘故障的相关性。}\\
\paragraph{考虑时序数据的影响，尝试使用hmm等去改进预测性能。}

\end{document}

```
