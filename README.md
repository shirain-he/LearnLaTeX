# LearnTex

## 介绍

1. 本仓库收录 ***Latex+Vscode+Zotero+Git*** 论文撰写超级工具链的详细配置和使用说明。
2. 提供了本人实战的一篇用该工具撰写的论文可供测试。
3. 本文搜集了目前可用的大部分实用工具和极速入门教程。
4. 该工具链优点如下：

- 实现论文文本与格式分离，文献快速交叉引用。
- 实时查看pdf！代码公式表格极速插入。
- 目录图片表格公式参考文献自动编号引用。
- 更改局部编号或相关格式，全文自动更新索引。
- 借助git一键上传，不怕电脑坏，不用再命名各种版本，随时回看想看的版本！


5. 本仓库也是本人作为LaTeX初学者的经验总结，欢迎大家参与、分享并Stared！
6. 相关资源均标明出处，如有不当之处可联系我修改！<br>侵删 please contact with me delete it if infringing!

### 软件架构说明

- 首先需要下载Tex Live、VS Code、Zotero三个软件
- 而后需要在VS Code中下载Latex WorkShop插件，Zotero LaTeX插件。
- 在Zotero中安装Better Bib ZeteroTeX For Zotero插件。
- 以VS Code为中心，借助Latex WorkShop插件联动Tex live、借助Zotero LaTeX联动Zetoro（主要用于参考文献的快速交叉引用）。

### 文章架构说明

- 我们只需要关注 *.tex* 文件和 *.pdf* 文件;
- **.tex** 是我们编辑latex代码和填充文字的主文件;
- **.pdf** 文件是我们的论文成果显示，其他文件是latex编译链自动生成;
- *.py* 文件是我们需要插入的代码文件;
- **allpicture** 存放所有用到的图片的文件夹 （需要自己将图片拖入源文件夹）。

### VS Code配置即settings.json文件配置
1. Vscode的设置分别参考自：

- [知乎 Ali-loner](https://zhuanlan.zhihu.com/p/166523064)
- [知乎 超级懒的小周](https://zhuanlan.zhihu.com/p/397280207)
- [Latex+VSCode 正向搜索和反向搜索](https://jintaolee-roger.github.io/posts/latexsearch/)

2. 将下面的代码复制到你的VS Code settings.json文件中。

```json
    //定义要在配方中使用的 LaTeX 编译工具。每个工具都标有其名称。 
    //调用时，命令会使用 args 中定义的参数和 env 中定义的环境变量生成。 
    //通常，除非在路径中，否则每个参数中不应出现空格。
    //占位符 %DOC%、%DOC_W32%、%DOC_EXT%、%DOC_EXT_W32%、%DOCFILE%、%DOCFILE_EXT%、%DIR%、%DIR_W32%、%TMPDIR% 和 %OUTDIR%、%OUTDIR_W32% 可用.
    "latex-workshop.latex.tools": [
        {
            "name": "xelatex",
            "command": "xelatex",
            "args": [
                "-synctex=1",
                "-interaction=nonstopmode",
                "-file-line-error",
                "%DOC%"
            ]
        },
        {
            "name": "xelatex-with-shell-escape",
            "command": "xelatex",
            "args": [
                "--shell-escape",
                "-synctex=1",
                "-interaction=nonstopmode",
                "-file-line-error",
                "%DOC%"
            ]
        },
        {
            "name": "xelatex-latexmk",
            "command": "latexmk",
            "args": [
                "-synctex=1",
                "-interaction=nonstopmode",
                "-file-line-error",
                "-xelatex",
                "-outdir=%OUTDIR%",
                "%DOC%"
            ]
        },
        {
            "name": "xelatex-latexmk-with-shell-escape",
            "command": "latexmk",
            "args": [
                "--shell-escape",
                "-synctex=1",
                "-interaction=nonstopmode",
                "-file-line-error",
                "-xelatex",
                "-outdir=%OUTDIR%",
                "%DOC%"
            ]
        },
        {
            "name": "pdflatex",
            "command": "pdflatex",
            "args": [
                "-synctex=1",
                "-interaction=nonstopmode",
                "-file-line-error",
                "%DOC%"
            ]
        },
        {
            "name": "pdflatex-with-shell-escape",
            "command": "pdflatex",
            "args": [
                "--shell-escape",
                "-synctex=1",
                "-interaction=nonstopmode",
                "-file-line-error",
                "%DOC%"
            ]
        },
        {
            "name": "pdflatex-latexmk",
            "command": "latexmk",
            "args": [
                "-synctex=1",
                "-interaction=nonstopmode",
                "-file-line-error",
                "-pdf",
                "-outdir=%OUTDIR%",
                "%DOC%"
            ]
        },
        {
            "name": "pdflatex-latexmk-with-shell-escape",
            "command": "latexmk",
            "args": [
                "--shell-escape",
                "-synctex=1",
                "-interaction=nonstopmode",
                "-file-line-error",
                "-pdf",
                "-outdir=%OUTDIR%",
                "%DOC%"
            ]
        },
        {
            "name": "latexmk",
            "command": "latexmk",
            "args": [
                "-synctex=1",
                "-interaction=nonstopmode",
                "-file-line-error",
                "-pdf",
                "%DOC%"
            ]
        },
        {
            "name": "bibtex",
            "command": "bibtex",
            "args": [
                "%DOCFILE%"
            ]
        },
    ],
     // 用于配置编译链
    "latex-workshop.latex.recipes": [
        {
            "name": "PDFLaTeX",
            "tools": [
                "pdflatex"
            ]
        },
        {
            "name": "PDFLaTeX with Shell Escape",
            "tools": [
                "pdflatex-with-shell-escape"
            ]
        },
        {
            "name": "PDFLaTeX Auto",
            "tools": [
                "pdflatex-latexmk"
            ]
        },
        {
            "name": "PDFLaTeX Auto with Shell Escape",
            "tools": [
                "pdflatex-latexmk-with-shell-escape"
            ]
        },
        {
            "name": "XeLaTeX",
            "tools": [
                "xelatex"
            ]
        },
        {
            "name": "XeLaTeX with Shell Escape",
            "tools": [
                "xelatex-with-shell-escape"
            ]
        },
        {
            "name": "XeLaTeX Auto",
            "tools": [
                "xelatex-latexmk"
            ]
        },
        {
            "name": "XeLaTeX Auto with Shell Escape",
            "tools": [
                "xelatex-latexmk-with-shell-escape"
            ]
        },
        {
            "name": "PDFLaTeX -> BibTeX -> PDFLaTeX*2",
            "tools": [
                "pdflatex",
                "bibtex",
                "pdflatex",
                "pdflatex"
            ]
        },
        {
            "name": "XeLaTeX -> BibTeX -> XeLaTeX*2",
            "tools": [
                "xelatex",
                "bibtex",
                "xelatex",
                "xelatex"
            ]
        },
        {
            "name": "latexmk",
            "tools": [
                "latexmk"
            ]
        },
        {
            "name": "BibTeX",
            "tools": [
                "bibtex"
            ]
        },
    ],
    //文件清理。此属性必须是字符串数组
    "latex-workshop.latex.clean.fileTypes": [
        "*.aux",
        "*.bbl",
        "*.blg",
        "*.idx",
        "*.ind",
        "*.lof",
        "*.lot",
        "*.out",
        "*.toc",
        "*.acn",
        "*.acr",
        "*.alg",
        "*.glg",
        "*.glo",
        "*.gls",
        "*.ist",
        "*.fls",
        "*.log",
        "*.fdb_latexmk"
    ],
    //设置为onFaild 在构建失败后清除辅助文件
    "latex-workshop.latex.autoClean.run": "onFailed",
    // 使用上次的recipe编译组合
    "latex-workshop.latex.recipe.default": "lastUsed",
    // 用于反向同步的内部查看器的键绑定。ctrl/cmd +点击(默认)或双击
    "latex-workshop.view.pdf.internal.synctex.keybinding": "double-click",

    //使用 SumatraPDF 预览编译好的PDF文件
    // 设置VScode内部查看生成的pdf文件
    "latex-workshop.view.pdf.viewer": "external",
    // PDF查看器用于在\ref上的[View on PDF]链接
    "latex-workshop.view.pdf.ref.viewer":"auto",
    // 使用外部查看器时要执行的命令。此功能不受官方支持。
    "latex-workshop.view.pdf.external.viewer.command": "F:/sumatra/SumatraPDF/SumatraPDF.exe", // 注意修改路径
    // 使用外部查看器时，latex-workshop.view.pdf.external.view .command的参数。此功能不受官方支持。%PDF%是用于生成PDF文件的绝对路径的占位符。
    "latex-workshop.view.pdf.external.viewer.args": [
        "%PDF%"
    ],
    // 将synctex转发到外部查看器时要执行的命令。此功能不受官方支持。
    "latex-workshop.view.pdf.external.synctex.command": "F:/sumatra/SumatraPDF/SumatraPDF.exe", // 注意修改路径
    // latex-workshop.view.pdf.external.synctex的参数。当同步到外部查看器时。%LINE%是行号，%PDF%是生成PDF文件的绝对路径的占位符，%TEX%是触发syncTeX的扩展名为.tex的LaTeX文件路径。
    "latex-workshop.view.pdf.external.synctex.args": [
        "-forward-search",
        "%TEX%",
        "%LINE%",
        "-reuse-instance",
        "-inverse-search",
        "\"D:/VSCODE/Microsoft VS Code/Code.exe\" \"D:/VSCODE/Microsoft VS Code/resources/app/out/cli.js\" -r -g \"%f:%l\"", // 注意修改路径
        "%PDF%"
    ],
    //右键菜单
    "latex-workshop.showContextMenu":true,
    //从使用的包中自动补全命令和环境
    "latex-workshop.intellisense.package.enabled": true,
    //将 glob 模式配置到编辑器(例如 "*十六进制": "hexEditor.hexEdit")。这些优先顺序高于默认行为。
    // "workbench.editorAssociations": {
    //     "*.ipynb": "jupyter-notebook"
    // },
    // 应在何处显示单元格工具栏，或是否隐藏它。
    // "notebook.cellToolbarLocation": {
    //     "default": "right",
    //     "jupyter-notebook": "left"//为特定文件类型配置单元格工具栏位置
    // },
    // //若设置为 true，则自动从当前 Git 存储库的默认远程库提取提交。若设置为“全部”，则从所有远程库进行提取。
    // "git.autofetch": true,
    // //始终信任工作区
    // "security.workspace.trust.untrustedFiles": "open",
    // // 不显示新版本消息
    // "vsicons.dontShowNewVersionMessage": true,
    //针对某种语言，配置替代编辑器设置
    "[latex]": {
        "editor.formatOnPaste": false,//针对某种语言，配置替代编辑器设置
        "editor.suggestSelection": "recentlyUsedByPrefix" //控制在建议列表中如何预先选择建议。recentlyUsedByPrefix: 根据之前补全过的建议的前缀来进行选择。例如，co -> console、con -> const。
    },
```

### 其他资源（非常实用的latex学习教程和实用工具）

- 关于Latex极速入门视频推荐: [B站up主circlelq](https://www.bilibili.com/video/BV1nv4y1Q7fz/?spm_id_from=333.337.search-card.all.click&vd_source=857cbb7cbeb544de1acad66a29b6fbf8)
- Latex+Vscode+Zotero联动实现文献快速交叉引用的教程: [B站up主一个林子漾](https://www.bilibili.com/video/BV1ug411W7nY/?spm_id_from=333.337.search-card.all.click&vd_source=857cbb7cbeb544de1acad66a29b6fbf8)
- **最常用** 公式快速识别并转化为latex代码:[Mathpix Snipping Tool](https://blog.csdn.net/Yu_X_Q/article/details/117391844)
- Zotero所有插件镜像下载:[Zotero中文社区](https://zotero-chinese.gitee.io/zotero-plugins/#/)
- Latex代码插入解决方案:[知乎littleNewton](https://zhuanlan.zhihu.com/p/65441079)
- Latex 表格生成工具网站:[table generator](https://www.tablesgenerator.com/)
- 在线LaTeX公式编辑器: [手动构造单个公式](https://www.latexlive.com/)
- 图片格式转换为eps工具网站:[PNG/JPG转EPS](https://www.aconvert.com/cn/image/)
- Latex GB/T 7714中文文献相关格式包见[Github zepinglee](https://github.com/zepinglee/gbt7714-bibtex-style)

### 使用说明

1. 编译链用的是Xelatex-Bibtex-Xelatex*2
2. 论文即时显式用的是外部pdf显示器SumatrPDF(也可以不用)
3. 插入文献借助Zotero插件Alt+Z实现。
4. 文献格式GB/T 7714-numerical-2015。

- 文章末尾添加下面代码实现交叉引用和指定文献格式。

```latex
\bibliographystyle{gbt7714-numerical} % 你的文献样式包bst文件的名字，本文使用gbt7714-numerical.bst
\bibliography{F:/BibTeXref/zoterorepo.bib} % 你从zotero导出的bib文件
```

### 参与贡献

1. Fork 本仓库
2. 新建 Feat_TexContributor_00X 分支
3. 提交代码
4. 新建 Pull Request
