"自动切换到本目录
lcd %:p:h
noremap <F2> :!ruby <C-R>=expand("%:p")<CR><Enter>
set tabstop=2
set shiftwidth=2
set foldmethod=marker
