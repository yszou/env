"自动切换到本目录
noremap <F2> :!rustc <C-R>=expand("%:p")<CR><Enter>
noremap <F3> :!<C-R>=expand("%:p:r")<CR><Enter>

