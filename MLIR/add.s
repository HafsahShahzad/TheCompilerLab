	.build_version macos, 15, 0
	.section	__TEXT,__text,regular,pure_instructions
	.globl	_add                            ; -- Begin function add
	.p2align	2
_add:                                   ; @add
	.cfi_startproc
; %bb.0:
	add	w0, w0, w1
	ret
	.cfi_endproc
                                        ; -- End function
.subsections_via_symbols
