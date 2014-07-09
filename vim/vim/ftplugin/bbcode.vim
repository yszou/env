"自动切换到本目录
lcd %:p:h
noremap <F2> :%s/^ *//g<CR>:g/^$/d<CR>:%s/^\(.*\)$/[align=left]    \1[\/align]\r<CR>gg:nohlsearch<CR>
noremap <F3> :%s/^ *//g<CR>:g/^$/d<CR>:%s/^\(.*\)$/[p=20, 2, left]\1[\/p]<CR>gg:nohlsearch<CR>
noremap <M-i> a[*]
inoremap<buffer> <M-i> <C-R>='[*] '<CR><BS>
