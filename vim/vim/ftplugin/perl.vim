"自动切换到本目录
lcd %:p:h
noremap <F2> :!perl <C-R>=expand("%:p")<CR><Enter>
