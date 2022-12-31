# LearnTex

#### 介绍
LearnTex and write the course thesis.

#### 软件架构
软件架构说明


#### vscode settings.json文件
[参考自](https://zhuanlan.zhihu.com/p/166523064)
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

上述代码全是latex配置文件，加到vscode settings.json文件。

#### 使用说明

1.  编译链用的是Xelatex-Bibtex-Xelatex*2
2.  论文即时显式用的是外部pdf显示器SumatrPDF(也可以不用)
3.  插入文献借助Zotero插件Alt+Z实现。
4.  文献格式GB/T 7714-numerical-2015.
即\bibliographystyle{gbt7714-numerical}
5.  ![输入图片说明](https://foruda.gitee.com/images/1672459540424413823/8df11a3a_10448467.png "屏幕截图")
这是Zotero插件信息，箭头为快捷插入文献插件，必备。
#### 参与贡献

1.  Fork 本仓库
2.  新建 Feat_xxx 分支
3.  提交代码
4.  新建 Pull Request

