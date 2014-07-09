lcd %:p:h

"定义用F2做pdflatex编译,F3看结果
"noremap <F2> :!pdflatex <C-R>=expand("%:p")<CR><Enter><Enter>
noremap <F2> :!fpc <C-R>=expand("%:p")<CR><Enter>
noremap <F3> :!./<C-R>=expand("%:t:r")<CR><Enter>

"pascal的缩进是2
set shiftwidth=2
set tabstop=2
