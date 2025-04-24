vim.keymap.set('n', '<Leader>fs', '<cmd>lua require"fzf-lua".fzf_live("./filtercs.py <query> 2>/dev/null", { prompt="scs> " , exec_empty_query=true })<cr>')
vim.keymap.set('n', '<Leader>cs', '<cmd>!python calcchar.py<cr><cr>')
