"imap  a abc


fun! CM(findstart, base)
  let table = ['Jan 一月', 'Feb 二月', 'Mar 三月', 'Jon X月']
  if a:findstart
    " locate the start of the word
    let line = getline('.')
    let start = col('.') - 1
    while start > 0 && line[start - 1] =~ '\a'
      let start -= 1
    endwhile
    return start
  else
    " find months matching with "a:base"
    let res = []
    "for m in split("Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec")
    for m in table
      if m =~ '^' . a:base
    call add(res, split(m)[1])
      endif
    endfor
    return res
  endif
endfun

function InsertE()
    let s:mye = input('Input: ')
    return s:mye . ' '
endfunction
