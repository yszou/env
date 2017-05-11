set textwidth=0

noremap <F2> :!python /home/zys/bin/txt2tags -t xhtml --toc-level=3 --encoding=utf-8 --enum-title --mask-email -o /home/zys/temp/<C-R>=expand("%:t:r")<CR>.html <C-R>=expand("%:p")<CR> <Enter>
noremap <F3> :!firefox /home/zys/temp/<C-R>=expand("%:t:r").".html"<CR><Enter><Enter>
noremap <F4> :!google-chrome /home/zys/temp/<C-R>=expand("%:t:r").".html"<CR><Enter><Enter>
noremap <F5> :!txt2tags -t tex --toc-level=2 --encoding=utf-8 --enum-title --mask-email -o /home/zys/temp/<C-R>=expand("%:t:r")<CR>.tex <C-R>=expand("%:p")<CR> <Enter>
noremap <F6> :!gvim /home/zys/temp/<C-R>=expand("%:t:r")<CR>.tex<CR><CR>
noremap <F7> :!python /home/zys/bin/revealjs.py <C-R>=expand("%:p")<CR> /home/zys/temp/<C-R>=expand("%:t:r")<CR>.revealjs.html  <Enter>
noremap <F8> :!google-chrome /home/zys/temp/<C-R>=expand("%:t:r").".revealjs.html"<CR><Enter><Enter>

inoremap <M-o> <C-R>=<SID>FormatText('**')<CR>
inoremap <M-p> <C-R>=<SID>FormatText('``')<CR>
inoremap <M-i> <C-R>=<SID>FormatText('*')<CR>
inoremap <M-=> <C-R>=<SID>FormatText('# ')<CR>
inoremap <M--> <C-R>=<SID>FormatText('## ')<CR>
inoremap <Leader>= ========================================================
inoremap <Leader>- --------------------------------------------------------
inoremap <Leader>` ```<CR><CR>```<CR><++><UP><UP>
inoremap <Leader>" """<CR><CR>"""<CR><++><UP><UP>
inoremap <Leader>' '''<CR><CR>'''<CR><++><UP><UP>
"vnoremap ` o<ESC>0i```<CR><ESC>gvo<ESC>o<ESC>i```<ESC>
vnoremap ` o<ESC>0O```<ESC>gvo<ESC>o```<ESC>

function! <SID>FormatText(mark)
    let columnNum = col('.')
    if columnNum == 1
        return ''
    endif
    let lineNum = line('.')
    let line = getline('.')
    "前置的空格在处理时会被忽略,所以最后要单独加上
    let preSpace = matchstr(line, '^\s\+')
    let lineToCurrent = line[:columnNum - 2]
    let mark = a:mark
    call setline(lineNum, preSpace . s:getResult(lineToCurrent, mark) . line[columnNum - 1:])
    call cursor(lineNum, columnNum + strlen(getline('.')) - strlen(line))
    "let a = inputdialog(line)
    return ''
endfunction


function! s:reverseStr(s)
    let s = a:s
    let l = []
    for i in range(strlen(s))
        call add(l, s[i])
    endfor
    call reverse(l)
    return join(l, '')
endfunction

call s:reverseStr('123')

function! s:getResult(lineToCurrent, mark)
    let lineToCurrent = a:lineToCurrent
    let mark = a:mark
    let markLen = strlen(mark)

    let lineToCurrentList = split(lineToCurrent, ' ')

    let s = lineToCurrentList[-1]
    let l = len(lineToCurrentList)

    if s[(0-markLen):-1] != s:reverseStr(mark)
        " mark <- 这种情况
        " other other mark <- 或这种情况
        let lineToCurrentList[-1] = mark . s
        return join(lineToCurrentList, ' ') . s:reverseStr(mark)
    else
        if l == 1
            if s[:(markLen-1)] != mark
                " mark`` <- 这种情况
                return mark . s
            endif

            if s[:(markLen-1)] == mark
                " ``mark`` <- 这种情况
                return s
            endif
        endif

        for i in range(l-1, 0, -1)
            let s = lineToCurrentList[i]

            if s[:(markLen-1)] == mark
                if i == 0
                    " ``other other mark`` <- 这种情况
                    return join(lineToCurrentList, ' ')
                else
                    " other other ``mark`` <- 这种情况
                    " other ``other mark`` <- 或这种情况
                    let lineToCurrentList[i] = lineToCurrentList[i][(markLen):]
                    let lineToCurrentList[i-1] = mark . lineToCurrentList[i-1]
                    return join(lineToCurrentList, ' ')
                endif
            endif
        endfor
    endif

endfunction


