call plug#begin('~/.config/nvim/autoload/plugged')
	" Completion
	Plug 'Shougo/deoplete.nvim', { 'do': ':UpdateRemotePlugins' }
	Plug 'neoclide/coc.nvim', { 'branch': 'release' }
	Plug 'chriskempson/base16-vim'
	" Files
	Plug 'junegunn/fzf', { 'dir': '~/.fzf', 'do': './install --all' }
	Plug 'junegunn/fzf.vim'
	Plug 'scrooloose/nerdTree'
	Plug 'ctrlpvim/ctrlp.vim'
	" Code highlights
	Plug 'jiangmiao/auto-pairs'
	Plug 'machakann/vim-sandwich'
	" Plug 'tpope/vim-surround'
	" Movement
	Plug 'easymotion/vim-easymotion'
call plug#end()

" COC shortcuts
inoremap <expr> <Tab> pumvisible() ? "\<C-n>" : "\<Tab>"
inoremap <expr> <S-Tab> pumvisible() ? "\<C-p>" : "\<S-Tab>"

inoremap <silent><expr> <C-space> coc#refresh()

"GoTo code navigation
nmap <leader>g <C-o>
nmap <silent> gd <Plug>(coc-definition)
nmap <silent> gt <Plug>(coc-type-definition)
nmap <silent> gi <Plug>(coc-implementation)
nmap <silent> gr <Plug>(coc-references)

nmap <leader>rn <Plug>(coc-rename)

"show all diagnostics.
nnoremap <silent> <space>d :<C-u>CocList diagnostics<cr>
"manage extensions.
nnoremap <silent> <space>e :<C-u>CocList extensions<cr>

" remap c-j and c-h to arrow keys for completion
inoremap <expr> <C-j> pumvisible() ? "\<C-n>" : "\<C-j>"
inoremap <expr> <C-k> pumvisible() ? "\<C-p>" : "\<C-k>"

" Toggle NerdTree with C-n
nmap <C-e> :NERDTreeToggle<CR>

" Put Leader as the prefix for easy motion plugin
map <Leader> <Plug>(easymotion-prefix)

" fzf
map ; :Files<CR>
