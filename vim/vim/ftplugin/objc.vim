noremap <F5> :!gcc -o /tmp/app <C-R>=expand("%:p")<CR> `gnustep-config --objc-flags` -lgnustep-base<CR>
noremap <F6> :!/tmp/app
