"      File: varname.vim
"    Author: Yesheng Zou <yeshengzou@gmail.com>
"   License: GNU Lesser General Public License
"    Latest: 2010-11-26
"   Version: 0.1
"   Project: 
"      Need: var_names.txt
" -----------------------------------------------------------
"    Readme: 根据码表, 进行变量名提示的工具.
"
"

inoremap<buffer><silent> <M-f> <C-X><C-U>

let &l:completefunc = 'VarComplate'
let &l:completeopt = 'menuone'
let &l:pumheight = 9
highlight! lCursor guifg=bg guibg=green
set cpo&vim
set nolazyredraw "使用宏时是不是要重绘屏幕
set nopaste

"哪些算是单词的界线,正则表达式
let s:WORD_SPACE = '[ ()]'

"备查码表
if !exists('g:VAR_NAME_TIPS')
    let tableFile = expand("<sfile>:p:h") . "/" . 'var_names.txt'
    try
        let g:VAR_NAME_TIPS = readfile(tableFile)
    catch /E484:/
        echo 'Counld not open the table file `' . tableFile . '`'
    endtry
endif

"主要的补全函数
function VarComplate(findstart, keyboard)
if a:findstart
    "查找前面需要待查的词
    
    let columnNum = col('.') - 1
    let currentLineStr = getline('.')
    for i in range(columnNum, 1, -1)
        if currentLineStr[i - 1] =~ s:WORD_SPACE
            return i
        endif
    endfor
    return 0

else
    if a:keyboard == ''
        return ''
    endif

    let toSelectList = []
    for line in g:VAR_NAME_TIPS
        let _tempList = split(line, ' ')

        for item in _tempList
            if item =~ '.\{-}' . a:keyboard . '.*'
                if _tempList[0] == item
                    call add(toSelectList, {'word': _tempList[0], 'menu': join(_tempList[1:], ' ')})
                else
                    call add(toSelectList, {'word': _tempList[0], 'menu': item})
                endif
            endif
        endfor

    endfor

    if len(toSelectList) != 0
        return toSelectList
    else
        return ''
    endif

endif
endfunction
