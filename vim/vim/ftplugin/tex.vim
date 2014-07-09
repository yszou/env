"把工作目录切换到当前文件的目录
"noremap <F12> cd <C-R>=expand("%:p:h")<CR><Enter>
"set autochdir
lcd %:p:h

set makeprg=make

"定义用F2做pdflatex编译,F3看结果
"noremap <F2> :!pdflatex <C-R>=expand("%:p")<CR><Enter><Enter>
noremap <F2> :!xelatex --output-directory=/home/zys/temp <C-R>=expand("%:p")<CR><Enter><Enter>
noremap <F3> :!evince /home/zys/temp/<C-R>=expand("%:t:r").".pdf"<CR><Enter><Enter>
noremap <F4> :!acroread /home/zys/temp/<C-R>=expand("%:t:r").".pdf"<CR><Enter><Enter>
