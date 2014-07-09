"      File: f4chinese.vim
"    Author: Yesheng Zou <yeshengzou@gmail.com>
"   License: GNU Lesser General Public License
"    Latest: 2010-01-11
"   Version: 1.0
"      Need: f4chinese_*.txt (table file)
"            f4chinese.py (python 2.6) or f4chinese.exe

nnoremap<silent><expr> <M-f> <SID>F4chinese(0)
"nnoremap<silent><expr> <M-;> <SID>F4chinese(1)
"上面的写法是比较好的.但是,我必须要先<Right>一下才行.因为当前字不
"用去管,否则就无法找到下一个匹配了.
"还有,这里若用i而不是a的话,如果光标在行尾就会出问题.
"直接写下面这个map,从quickfix列表中打开的文件就不能用
"nnoremap<buffer><silent> <M-;> a<C-R>=<SID>F4chinese(1)<CR>
nnoremap<silent><expr> <M-;> <SID>R_F4chinese()

let s:table = 'f4chinese_wubi.txt'
let s:path = expand("<sfile>:p:h")."/"
let s:firstChar = ''

function s:SID()
  return matchstr(expand('<sfile>'), '<SNR>\zs\d\+\ze_SID$')
endfun

function s:Debug(var)
    let a = inputdialog(a:var)
endfunction

function s:R_F4chinese()
    "自己通过 s:SID() 来构造一个类似于 <SNR>22_Add 的调用形式
    sil!exe 'sil!return "' . "a\<C-R>=<SNR>" . <SID>SID() . "_F4chinese(1)\<CR>"  . '"'
endfunction

function s:F4chinese(after)
    "after表示三种状态
    " 0 查找整个当前行,要输入首字母
    " 1 查找当前行中,光标后的内容,不输入首字母
    " 2 查找整个当前行,不输入首字母
    " 不输入首字母的情况就是使用上一次的输入
    if a:after == 0
        let s:firstChar = input('Input the First Char: ')
        redraw!
        if s:firstChar == ''
            sil!exe 'sil!return "' . "\<Esc>"  . '"'
        endif

        let line = getline('.')
    elseif a:after == 1
        let line = getline('.')[getpos('.')[2] - 1:]
    else
        "if a:after == 2
        let line = getline('.')
    endif

    let r = system('python ' . s:path . 'f4chinese.py' . ' "' . s:path . s:table . '" "' . line . '" "' . s:firstChar . '"')

    if r == '' || r == '0'
        " r == '0' 是表示程序执行有错
        if a:after == 0 || a:after == 2
            echohl warningmsg
            echomsg '在本行没有找到 ' . s:firstChar
            echohl normal

            sil!exe 'sil!return "' . "\<Esc>"  . '"'
        else
            return <SID>F4chinese(2)
        endif
    else
        if a:after != 1
            sil!exe 'sil!return "' . "\<Esc>0" . r . '"'
        else
            sil!exe 'sil!return "' . "\<Esc>\<Right>" . r . '"'
        endif
    endif
endfunction
