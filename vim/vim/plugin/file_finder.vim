function s:FileFinder(filename)
    "locate找出所有的filename,然后取出当前路径
    "对每一个结果文件,把它和当前路径从左到右进行匹配比较,取匹配结果最大的结果文件
    "最后在一个新的buf中打开这个结果文件

    let result_list = split(system("locate " . a:filename), '\n')

    "没找到的话就直接打开(新建文件)
    if len(result_list) == 0
        exe 'new ' . a:filename
        return
    endif

    let cwd_step = split(getcwd(), '/')
    let file_index = 0 "结果文件名在result_list中的索引
    let max_match_count = 0 "路径的最大匹配
    let cwd_step_length = len(cwd_step)

    for i in range(len(result_list))
        let step = split(result_list[i], '/')
        let match_count = 0
        for j in range(min([cwd_step_length, len(step)]))
            if cwd_step[j] == step[j]
                let match_count += 1
            else
                break
            endif
        endfor

        if match_count > max_match_count
            let max_match_count = match_count
            let file_index = i
        endif
    endfor

    return result_list[file_index]
endfunction


function AceVimFileFinder(filename)
    exe 'new ' . s:FileFinder(a:filename)
endfunction


function PythonEnvActive()
    let activate_this = s:FileFinder('activate_this.py')
    if activate_this != ''
        exe 'python activate_this = "' . activate_this . '"'
        exe 'python execfile(activate_this, dict(__file__=activate_this))'
    endif
endfunction

