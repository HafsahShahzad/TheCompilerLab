# from tvm.script import ir as I
# from tvm.script import tir as T
# from tvm.script import relax as R

@I.ir_module
class Module:
    @T.prim_func(private=True)
    def add(lv28: T.Buffer((T.int64(1), T.int64(256), T.int64(56), T.int64(56)), "float32"), lv29: T.Buffer((T.int64(1), T.int64(256), T.int64(56), T.int64(56)), "float32"), T_add: T.Buffer((T.int64(1), T.int64(256), T.int64(56), T.int64(56)), "float32")):
        T.func_attr({"tir.noalias": True})
        # with T.block("root"):
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(1), T.int64(256), T.int64(56), T.int64(56)):
            with T.block("T_add"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(lv28[v_ax0, v_ax1, v_ax2, v_ax3], lv29[v_ax0, v_ax1, v_ax2, v_ax3])
                T.writes(T_add[v_ax0, v_ax1, v_ax2, v_ax3])
                T_add[v_ax0, v_ax1, v_ax2, v_ax3] = lv28[v_ax0, v_ax1, v_ax2, v_ax3] + lv29[v_ax0, v_ax1, v_ax2, v_ax3]

    @T.prim_func(private=True)
    def add1(lv86: T.Buffer((T.int64(1), T.int64(512), T.int64(28), T.int64(28)), "float32"), lv87: T.Buffer((T.int64(1), T.int64(512), T.int64(28), T.int64(28)), "float32"), T_add: T.Buffer((T.int64(1), T.int64(512), T.int64(28), T.int64(28)), "float32")):
        T.func_attr({"tir.noalias": True})
        # with T.block("root"):
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(1), T.int64(512), T.int64(28), T.int64(28)):
            with T.block("T_add"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(lv86[v_ax0, v_ax1, v_ax2, v_ax3], lv87[v_ax0, v_ax1, v_ax2, v_ax3])
                T.writes(T_add[v_ax0, v_ax1, v_ax2, v_ax3])
                T_add[v_ax0, v_ax1, v_ax2, v_ax3] = lv86[v_ax0, v_ax1, v_ax2, v_ax3] + lv87[v_ax0, v_ax1, v_ax2, v_ax3]

    @T.prim_func(private=True)
    def add2(lv163: T.Buffer((T.int64(1), T.int64(1024), T.int64(14), T.int64(14)), "float32"), lv164: T.Buffer((T.int64(1), T.int64(1024), T.int64(14), T.int64(14)), "float32"), T_add: T.Buffer((T.int64(1), T.int64(1024), T.int64(14), T.int64(14)), "float32")):
        T.func_attr({"tir.noalias": True})
        # with T.block("root"):
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(1), T.int64(1024), T.int64(14), T.int64(14)):
            with T.block("T_add"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(lv163[v_ax0, v_ax1, v_ax2, v_ax3], lv164[v_ax0, v_ax1, v_ax2, v_ax3])
                T.writes(T_add[v_ax0, v_ax1, v_ax2, v_ax3])
                T_add[v_ax0, v_ax1, v_ax2, v_ax3] = lv163[v_ax0, v_ax1, v_ax2, v_ax3] + lv164[v_ax0, v_ax1, v_ax2, v_ax3]

    @T.prim_func(private=True)
    def add3(lv278: T.Buffer((T.int64(1), T.int64(2048), T.int64(7), T.int64(7)), "float32"), lv279: T.Buffer((T.int64(1), T.int64(2048), T.int64(7), T.int64(7)), "float32"), T_add: T.Buffer((T.int64(1), T.int64(2048), T.int64(7), T.int64(7)), "float32")):
        T.func_attr({"tir.noalias": True})
        # with T.block("root"):
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(1), T.int64(2048), T.int64(7), T.int64(7)):
            with T.block("T_add"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(lv278[v_ax0, v_ax1, v_ax2, v_ax3], lv279[v_ax0, v_ax1, v_ax2, v_ax3])
                T.writes(T_add[v_ax0, v_ax1, v_ax2, v_ax3])
                T_add[v_ax0, v_ax1, v_ax2, v_ax3] = lv278[v_ax0, v_ax1, v_ax2, v_ax3] + lv279[v_ax0, v_ax1, v_ax2, v_ax3]

    @T.prim_func(private=True)
    def add4(lv327: T.Buffer((T.int64(1), T.int64(1000)), "float32"), B: T.Buffer((T.int64(1000),), "float32"), T_add: T.Buffer((T.int64(1), T.int64(1000)), "float32")):
        T.func_attr({"tir.noalias": True})
        # with T.block("root"):
        for ax0, ax1 in T.grid(T.int64(1), T.int64(1000)):
            with T.block("T_add"):
                v_ax0, v_ax1 = T.axis.remap("SS", [ax0, ax1])
                T.reads(lv327[v_ax0, v_ax1], B[v_ax1])
                T.writes(T_add[v_ax0, v_ax1])
                T_add[v_ax0, v_ax1] = lv327[v_ax0, v_ax1] + B[v_ax1]

    @T.prim_func(private=True)
    def batch_norm(data: T.Buffer((T.int64(1), T.int64(3), T.int64(224), T.int64(224)), "float32"), B: T.Buffer((T.int64(3),), "float32"), C: T.Buffer((T.int64(3),), "float32"), D: T.Buffer((T.int64(3),), "float32"), E: T.Buffer((T.int64(3),), "float32"), T_add: T.Buffer((T.int64(1), T.int64(3), T.int64(224), T.int64(224)), "float32"), T_add_1: T.Buffer((T.int64(3),), "float32"), T_add_2: T.Buffer((T.int64(3),), "float32")):
        T.func_attr({"tir.noalias": True})
        # with T.block("root"):
        T_reshape = T.alloc_buffer((T.int64(1), T.int64(3), T.int64(1), T.int64(1)))
        T_subtract = T.alloc_buffer((T.int64(1), T.int64(3), T.int64(224), T.int64(224)))
        T_reshape_1 = T.alloc_buffer((T.int64(1), T.int64(3), T.int64(1), T.int64(1)))
        T_add_3 = T.alloc_buffer((T.int64(1), T.int64(3), T.int64(1), T.int64(1)))
        compute = T.alloc_buffer((T.int64(1), T.int64(3), T.int64(1), T.int64(1)))
        T_divide = T.alloc_buffer((T.int64(1), T.int64(3), T.int64(224), T.int64(224)))
        T_reshape_2 = T.alloc_buffer((T.int64(1), T.int64(3), T.int64(1), T.int64(1)))
        T_multiply = T.alloc_buffer((T.int64(1), T.int64(3), T.int64(224), T.int64(224)))
        T_reshape_3 = T.alloc_buffer((T.int64(1), T.int64(3), T.int64(1), T.int64(1)))
        T_multiply_1 = T.alloc_buffer((T.int64(3),))
        data_red = T.alloc_buffer((T.int64(3),))
        T_divide_1 = T.alloc_buffer((T.int64(3),))
        T_multiply_2 = T.alloc_buffer((T.int64(3),))
        T_multiply_3 = T.alloc_buffer((T.int64(3),))
        T_reshape_4 = T.alloc_buffer((T.int64(1), T.int64(3), T.int64(1), T.int64(1)))
        T_subtract_1 = T.alloc_buffer((T.int64(1), T.int64(3), T.int64(224), T.int64(224)))
        T_subtract_2 = T.alloc_buffer((T.int64(1), T.int64(3), T.int64(224), T.int64(224)))
        T_multiply_4 = T.alloc_buffer((T.int64(1), T.int64(3), T.int64(224), T.int64(224)))
        T_multiply_red = T.alloc_buffer((T.int64(3),))
        T_divide_2 = T.alloc_buffer((T.int64(3),))
        T_multiply_5 = T.alloc_buffer((T.int64(3),))
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(1), T.int64(3), T.int64(1), T.int64(1)):
            with T.block("T_reshape"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(D[(v_ax1 + v_ax2 + v_ax3) % T.int64(3)])
                T.writes(T_reshape[v_ax0, v_ax1, v_ax2, v_ax3])
                T_reshape[v_ax0, v_ax1, v_ax2, v_ax3] = D[(v_ax1 + v_ax2 + v_ax3) % T.int64(3)]
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(1), T.int64(3), T.int64(224), T.int64(224)):
            with T.block("T_subtract"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(data[v_ax0, v_ax1, v_ax2, v_ax3], T_reshape[v_ax0, v_ax1, T.int64(0), T.int64(0)])
                T.writes(T_subtract[v_ax0, v_ax1, v_ax2, v_ax3])
                T_subtract[v_ax0, v_ax1, v_ax2, v_ax3] = data[v_ax0, v_ax1, v_ax2, v_ax3] - T_reshape[v_ax0, v_ax1, T.int64(0), T.int64(0)]
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(1), T.int64(3), T.int64(1), T.int64(1)):
            with T.block("T_reshape_1"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(E[(v_ax1 + v_ax2 + v_ax3) % T.int64(3)])
                T.writes(T_reshape_1[v_ax0, v_ax1, v_ax2, v_ax3])
                T_reshape_1[v_ax0, v_ax1, v_ax2, v_ax3] = E[(v_ax1 + v_ax2 + v_ax3) % T.int64(3)]
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(1), T.int64(3), T.int64(1), T.int64(1)):
            with T.block("T_add"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(T_reshape_1[v_ax0, v_ax1, v_ax2, v_ax3])
                T.writes(T_add_3[v_ax0, v_ax1, v_ax2, v_ax3])
                T_add_3[v_ax0, v_ax1, v_ax2, v_ax3] = T_reshape_1[v_ax0, v_ax1, v_ax2, v_ax3] + T.float32(9.9999997473787516e-06)
        for i0, i1, i2, i3 in T.grid(T.int64(1), T.int64(3), T.int64(1), T.int64(1)):
            with T.block("compute"):
                v_i0, v_i1, v_i2, v_i3 = T.axis.remap("SSSS", [i0, i1, i2, i3])
                T.reads(T_add_3[v_i0, v_i1, v_i2, v_i3])
                T.writes(compute[v_i0, v_i1, v_i2, v_i3])
                compute[v_i0, v_i1, v_i2, v_i3] = T.sqrt(T_add_3[v_i0, v_i1, v_i2, v_i3])
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(1), T.int64(3), T.int64(224), T.int64(224)):
            with T.block("T_divide"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(T_subtract[v_ax0, v_ax1, v_ax2, v_ax3], compute[v_ax0, v_ax1, T.int64(0), T.int64(0)])
                T.writes(T_divide[v_ax0, v_ax1, v_ax2, v_ax3])
                T_divide[v_ax0, v_ax1, v_ax2, v_ax3] = T_subtract[v_ax0, v_ax1, v_ax2, v_ax3] / compute[v_ax0, v_ax1, T.int64(0), T.int64(0)]
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(1), T.int64(3), T.int64(1), T.int64(1)):
            with T.block("T_reshape_2"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(B[(v_ax1 + v_ax2 + v_ax3) % T.int64(3)])
                T.writes(T_reshape_2[v_ax0, v_ax1, v_ax2, v_ax3])
                T_reshape_2[v_ax0, v_ax1, v_ax2, v_ax3] = B[(v_ax1 + v_ax2 + v_ax3) % T.int64(3)]
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(1), T.int64(3), T.int64(224), T.int64(224)):
            with T.block("T_multiply"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(T_divide[v_ax0, v_ax1, v_ax2, v_ax3], T_reshape_2[v_ax0, v_ax1, T.int64(0), T.int64(0)])
                T.writes(T_multiply[v_ax0, v_ax1, v_ax2, v_ax3])
                T_multiply[v_ax0, v_ax1, v_ax2, v_ax3] = T_divide[v_ax0, v_ax1, v_ax2, v_ax3] * T_reshape_2[v_ax0, v_ax1, T.int64(0), T.int64(0)]
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(1), T.int64(3), T.int64(1), T.int64(1)):
            with T.block("T_reshape_3"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(C[(v_ax1 + v_ax2 + v_ax3) % T.int64(3)])
                T.writes(T_reshape_3[v_ax0, v_ax1, v_ax2, v_ax3])
                T_reshape_3[v_ax0, v_ax1, v_ax2, v_ax3] = C[(v_ax1 + v_ax2 + v_ax3) % T.int64(3)]
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(1), T.int64(3), T.int64(224), T.int64(224)):
            with T.block("T_add_1"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(T_multiply[v_ax0, v_ax1, v_ax2, v_ax3], T_reshape_3[v_ax0, v_ax1, T.int64(0), T.int64(0)])
                T.writes(T_add[v_ax0, v_ax1, v_ax2, v_ax3])
                T_add[v_ax0, v_ax1, v_ax2, v_ax3] = T_multiply[v_ax0, v_ax1, v_ax2, v_ax3] + T_reshape_3[v_ax0, v_ax1, T.int64(0), T.int64(0)]
        for ax0 in range(T.int64(3)):
            with T.block("T_multiply_1"):
                v_ax0 = T.axis.spatial(T.int64(3), ax0)
                T.reads(D[v_ax0])
                T.writes(T_multiply_1[v_ax0])
                T_multiply_1[v_ax0] = T.float32(0.90000000000000002) * D[v_ax0]
        for ax0, k0, k2, k3 in T.grid(T.int64(3), T.int64(1), T.int64(224), T.int64(224)):
            with T.block("data_red"):
                v_ax0, v_k0, v_k2, v_k3 = T.axis.remap("SRRR", [ax0, k0, k2, k3])
                T.reads(data[v_k0, v_ax0, v_k2, v_k3])
                T.writes(data_red[v_ax0])
                with T.init():
                    data_red[v_ax0] = T.float32(0.0)
                data_red[v_ax0] = data_red[v_ax0] + data[v_k0, v_ax0, v_k2, v_k3]
        for ax0 in range(T.int64(3)):
            with T.block("T_divide_1"):
                v_ax0 = T.axis.spatial(T.int64(3), ax0)
                T.reads(data_red[v_ax0])
                T.writes(T_divide_1[v_ax0])
                T_divide_1[v_ax0] = data_red[v_ax0] * T.float32(1.9929846938775509e-05)
        for ax0 in range(T.int64(3)):
            with T.block("T_multiply_2"):
                v_ax0 = T.axis.spatial(T.int64(3), ax0)
                T.reads(T_divide_1[v_ax0])
                T.writes(T_multiply_2[v_ax0])
                T_multiply_2[v_ax0] = T.float32(0.10000000000000001) * T_divide_1[v_ax0]
        for ax0 in range(T.int64(3)):
            with T.block("T_add_2"):
                v_ax0 = T.axis.spatial(T.int64(3), ax0)
                T.reads(T_multiply_1[v_ax0], T_multiply_2[v_ax0])
                T.writes(T_add_1[v_ax0])
                T_add_1[v_ax0] = T_multiply_1[v_ax0] + T_multiply_2[v_ax0]
        for ax0 in range(T.int64(3)):
            with T.block("T_multiply_3"):
                v_ax0 = T.axis.spatial(T.int64(3), ax0)
                T.reads(E[v_ax0])
                T.writes(T_multiply_3[v_ax0])
                T_multiply_3[v_ax0] = T.float32(0.90000000000000002) * E[v_ax0]
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(1), T.int64(3), T.int64(1), T.int64(1)):
            with T.block("T_reshape_4"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(T_divide_1[(v_ax1 + v_ax2 + v_ax3) % T.int64(3)])
                T.writes(T_reshape_4[v_ax0, v_ax1, v_ax2, v_ax3])
                T_reshape_4[v_ax0, v_ax1, v_ax2, v_ax3] = T_divide_1[(v_ax1 + v_ax2 + v_ax3) % T.int64(3)]
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(1), T.int64(3), T.int64(224), T.int64(224)):
            with T.block("T_subtract_1"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(data[v_ax0, v_ax1, v_ax2, v_ax3], T_reshape_4[v_ax0, v_ax1, T.int64(0), T.int64(0)])
                T.writes(T_subtract_1[v_ax0, v_ax1, v_ax2, v_ax3])
                T_subtract_1[v_ax0, v_ax1, v_ax2, v_ax3] = data[v_ax0, v_ax1, v_ax2, v_ax3] - T_reshape_4[v_ax0, v_ax1, T.int64(0), T.int64(0)]
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(1), T.int64(3), T.int64(224), T.int64(224)):
            with T.block("T_subtract_2"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(data[v_ax0, v_ax1, v_ax2, v_ax3], T_reshape_4[v_ax0, v_ax1, T.int64(0), T.int64(0)])
                T.writes(T_subtract_2[v_ax0, v_ax1, v_ax2, v_ax3])
                T_subtract_2[v_ax0, v_ax1, v_ax2, v_ax3] = data[v_ax0, v_ax1, v_ax2, v_ax3] - T_reshape_4[v_ax0, v_ax1, T.int64(0), T.int64(0)]
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(1), T.int64(3), T.int64(224), T.int64(224)):
            with T.block("T_multiply_4"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(T_subtract_1[v_ax0, v_ax1, v_ax2, v_ax3], T_subtract_2[v_ax0, v_ax1, v_ax2, v_ax3])
                T.writes(T_multiply_4[v_ax0, v_ax1, v_ax2, v_ax3])
                T_multiply_4[v_ax0, v_ax1, v_ax2, v_ax3] = T_subtract_1[v_ax0, v_ax1, v_ax2, v_ax3] * T_subtract_2[v_ax0, v_ax1, v_ax2, v_ax3]
        for ax0, k0, k2, k3 in T.grid(T.int64(3), T.int64(1), T.int64(224), T.int64(224)):
            with T.block("T_multiply_red"):
                v_ax0, v_k0, v_k2, v_k3 = T.axis.remap("SRRR", [ax0, k0, k2, k3])
                T.reads(T_multiply_4[v_k0, v_ax0, v_k2, v_k3])
                T.writes(T_multiply_red[v_ax0])
                with T.init():
                    T_multiply_red[v_ax0] = T.float32(0.0)
                T_multiply_red[v_ax0] = T_multiply_red[v_ax0] + T_multiply_4[v_k0, v_ax0, v_k2, v_k3]
        for ax0 in range(T.int64(3)):
            with T.block("T_divide_2"):
                v_ax0 = T.axis.spatial(T.int64(3), ax0)
                T.reads(T_multiply_red[v_ax0])
                T.writes(T_divide_2[v_ax0])
                T_divide_2[v_ax0] = T_multiply_red[v_ax0] * T.float32(1.9929846938775509e-05)
        for ax0 in range(T.int64(3)):
            with T.block("T_multiply_5"):
                v_ax0 = T.axis.spatial(T.int64(3), ax0)
                T.reads(T_divide_2[v_ax0])
                T.writes(T_multiply_5[v_ax0])
                T_multiply_5[v_ax0] = T.float32(0.10000000000000001) * T_divide_2[v_ax0]
        for ax0 in range(T.int64(3)):
            with T.block("T_add_3"):
                v_ax0 = T.axis.spatial(T.int64(3), ax0)
                T.reads(T_multiply_3[v_ax0], T_multiply_5[v_ax0])
                T.writes(T_add_2[v_ax0])
                T_add_2[v_ax0] = T_multiply_3[v_ax0] + T_multiply_5[v_ax0]

    @T.prim_func(private=True)
    def batch_norm1(lv4: T.Buffer((T.int64(1), T.int64(64), T.int64(112), T.int64(112)), "float32"), B: T.Buffer((T.int64(64),), "float32"), C: T.Buffer((T.int64(64),), "float32"), D: T.Buffer((T.int64(64),), "float32"), E: T.Buffer((T.int64(64),), "float32"), T_add: T.Buffer((T.int64(1), T.int64(64), T.int64(112), T.int64(112)), "float32"), T_add_1: T.Buffer((T.int64(64),), "float32"), T_add_2: T.Buffer((T.int64(64),), "float32")):
        T.func_attr({"tir.noalias": True})
        # with T.block("root"):
        T_reshape = T.alloc_buffer((T.int64(1), T.int64(64), T.int64(1), T.int64(1)))
        T_subtract = T.alloc_buffer((T.int64(1), T.int64(64), T.int64(112), T.int64(112)))
        T_reshape_1 = T.alloc_buffer((T.int64(1), T.int64(64), T.int64(1), T.int64(1)))
        T_add_3 = T.alloc_buffer((T.int64(1), T.int64(64), T.int64(1), T.int64(1)))
        compute = T.alloc_buffer((T.int64(1), T.int64(64), T.int64(1), T.int64(1)))
        T_divide = T.alloc_buffer((T.int64(1), T.int64(64), T.int64(112), T.int64(112)))
        T_reshape_2 = T.alloc_buffer((T.int64(1), T.int64(64), T.int64(1), T.int64(1)))
        T_multiply = T.alloc_buffer((T.int64(1), T.int64(64), T.int64(112), T.int64(112)))
        T_reshape_3 = T.alloc_buffer((T.int64(1), T.int64(64), T.int64(1), T.int64(1)))
        T_multiply_1 = T.alloc_buffer((T.int64(64),))
        lv4_red = T.alloc_buffer((T.int64(64),))
        T_divide_1 = T.alloc_buffer((T.int64(64),))
        T_multiply_2 = T.alloc_buffer((T.int64(64),))
        T_multiply_3 = T.alloc_buffer((T.int64(64),))
        T_reshape_4 = T.alloc_buffer((T.int64(1), T.int64(64), T.int64(1), T.int64(1)))
        T_subtract_1 = T.alloc_buffer((T.int64(1), T.int64(64), T.int64(112), T.int64(112)))
        T_subtract_2 = T.alloc_buffer((T.int64(1), T.int64(64), T.int64(112), T.int64(112)))
        T_multiply_4 = T.alloc_buffer((T.int64(1), T.int64(64), T.int64(112), T.int64(112)))
        T_multiply_red = T.alloc_buffer((T.int64(64),))
        T_divide_2 = T.alloc_buffer((T.int64(64),))
        T_multiply_5 = T.alloc_buffer((T.int64(64),))
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(1), T.int64(64), T.int64(1), T.int64(1)):
            with T.block("T_reshape"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(D[(v_ax1 + v_ax2 + v_ax3) % T.int64(64)])
                T.writes(T_reshape[v_ax0, v_ax1, v_ax2, v_ax3])
                T_reshape[v_ax0, v_ax1, v_ax2, v_ax3] = D[(v_ax1 + v_ax2 + v_ax3) % T.int64(64)]
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(1), T.int64(64), T.int64(112), T.int64(112)):
            with T.block("T_subtract"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(lv4[v_ax0, v_ax1, v_ax2, v_ax3], T_reshape[v_ax0, v_ax1, T.int64(0), T.int64(0)])
                T.writes(T_subtract[v_ax0, v_ax1, v_ax2, v_ax3])
                T_subtract[v_ax0, v_ax1, v_ax2, v_ax3] = lv4[v_ax0, v_ax1, v_ax2, v_ax3] - T_reshape[v_ax0, v_ax1, T.int64(0), T.int64(0)]
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(1), T.int64(64), T.int64(1), T.int64(1)):
            with T.block("T_reshape_1"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(E[(v_ax1 + v_ax2 + v_ax3) % T.int64(64)])
                T.writes(T_reshape_1[v_ax0, v_ax1, v_ax2, v_ax3])
                T_reshape_1[v_ax0, v_ax1, v_ax2, v_ax3] = E[(v_ax1 + v_ax2 + v_ax3) % T.int64(64)]
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(1), T.int64(64), T.int64(1), T.int64(1)):
            with T.block("T_add"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(T_reshape_1[v_ax0, v_ax1, v_ax2, v_ax3])
                T.writes(T_add_3[v_ax0, v_ax1, v_ax2, v_ax3])
                T_add_3[v_ax0, v_ax1, v_ax2, v_ax3] = T_reshape_1[v_ax0, v_ax1, v_ax2, v_ax3] + T.float32(9.9999997473787516e-06)
        for i0, i1, i2, i3 in T.grid(T.int64(1), T.int64(64), T.int64(1), T.int64(1)):
            with T.block("compute"):
                v_i0, v_i1, v_i2, v_i3 = T.axis.remap("SSSS", [i0, i1, i2, i3])
                T.reads(T_add_3[v_i0, v_i1, v_i2, v_i3])
                T.writes(compute[v_i0, v_i1, v_i2, v_i3])
                compute[v_i0, v_i1, v_i2, v_i3] = T.sqrt(T_add_3[v_i0, v_i1, v_i2, v_i3])
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(1), T.int64(64), T.int64(112), T.int64(112)):
            with T.block("T_divide"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(T_subtract[v_ax0, v_ax1, v_ax2, v_ax3], compute[v_ax0, v_ax1, T.int64(0), T.int64(0)])
                T.writes(T_divide[v_ax0, v_ax1, v_ax2, v_ax3])
                T_divide[v_ax0, v_ax1, v_ax2, v_ax3] = T_subtract[v_ax0, v_ax1, v_ax2, v_ax3] / compute[v_ax0, v_ax1, T.int64(0), T.int64(0)]
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(1), T.int64(64), T.int64(1), T.int64(1)):
            with T.block("T_reshape_2"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(B[(v_ax1 + v_ax2 + v_ax3) % T.int64(64)])
                T.writes(T_reshape_2[v_ax0, v_ax1, v_ax2, v_ax3])
                T_reshape_2[v_ax0, v_ax1, v_ax2, v_ax3] = B[(v_ax1 + v_ax2 + v_ax3) % T.int64(64)]
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(1), T.int64(64), T.int64(112), T.int64(112)):
            with T.block("T_multiply"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(T_divide[v_ax0, v_ax1, v_ax2, v_ax3], T_reshape_2[v_ax0, v_ax1, T.int64(0), T.int64(0)])
                T.writes(T_multiply[v_ax0, v_ax1, v_ax2, v_ax3])
                T_multiply[v_ax0, v_ax1, v_ax2, v_ax3] = T_divide[v_ax0, v_ax1, v_ax2, v_ax3] * T_reshape_2[v_ax0, v_ax1, T.int64(0), T.int64(0)]
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(1), T.int64(64), T.int64(1), T.int64(1)):
            with T.block("T_reshape_3"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(C[(v_ax1 + v_ax2 + v_ax3) % T.int64(64)])
                T.writes(T_reshape_3[v_ax0, v_ax1, v_ax2, v_ax3])
                T_reshape_3[v_ax0, v_ax1, v_ax2, v_ax3] = C[(v_ax1 + v_ax2 + v_ax3) % T.int64(64)]
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(1), T.int64(64), T.int64(112), T.int64(112)):
            with T.block("T_add_1"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(T_multiply[v_ax0, v_ax1, v_ax2, v_ax3], T_reshape_3[v_ax0, v_ax1, T.int64(0), T.int64(0)])
                T.writes(T_add[v_ax0, v_ax1, v_ax2, v_ax3])
                T_add[v_ax0, v_ax1, v_ax2, v_ax3] = T_multiply[v_ax0, v_ax1, v_ax2, v_ax3] + T_reshape_3[v_ax0, v_ax1, T.int64(0), T.int64(0)]
        for ax0 in range(T.int64(64)):
            with T.block("T_multiply_1"):
                v_ax0 = T.axis.spatial(T.int64(64), ax0)
                T.reads(D[v_ax0])
                T.writes(T_multiply_1[v_ax0])
                T_multiply_1[v_ax0] = T.float32(0.90000000000000002) * D[v_ax0]
        for ax0, k0, k2, k3 in T.grid(T.int64(64), T.int64(1), T.int64(112), T.int64(112)):
            with T.block("lv4_red"):
                v_ax0, v_k0, v_k2, v_k3 = T.axis.remap("SRRR", [ax0, k0, k2, k3])
                T.reads(lv4[v_k0, v_ax0, v_k2, v_k3])
                T.writes(lv4_red[v_ax0])
                with T.init():
                    lv4_red[v_ax0] = T.float32(0.0)
                lv4_red[v_ax0] = lv4_red[v_ax0] + lv4[v_k0, v_ax0, v_k2, v_k3]
        for ax0 in range(T.int64(64)):
            with T.block("T_divide_1"):
                v_ax0 = T.axis.spatial(T.int64(64), ax0)
                T.reads(lv4_red[v_ax0])
                T.writes(T_divide_1[v_ax0])
                T_divide_1[v_ax0] = lv4_red[v_ax0] * T.float32(7.9719387755102034e-05)
        for ax0 in range(T.int64(64)):
            with T.block("T_multiply_2"):
                v_ax0 = T.axis.spatial(T.int64(64), ax0)
                T.reads(T_divide_1[v_ax0])
                T.writes(T_multiply_2[v_ax0])
                T_multiply_2[v_ax0] = T.float32(0.10000000000000001) * T_divide_1[v_ax0]
        for ax0 in range(T.int64(64)):
            with T.block("T_add_2"):
                v_ax0 = T.axis.spatial(T.int64(64), ax0)
                T.reads(T_multiply_1[v_ax0], T_multiply_2[v_ax0])
                T.writes(T_add_1[v_ax0])
                T_add_1[v_ax0] = T_multiply_1[v_ax0] + T_multiply_2[v_ax0]
        for ax0 in range(T.int64(64)):
            with T.block("T_multiply_3"):
                v_ax0 = T.axis.spatial(T.int64(64), ax0)
                T.reads(E[v_ax0])
                T.writes(T_multiply_3[v_ax0])
                T_multiply_3[v_ax0] = T.float32(0.90000000000000002) * E[v_ax0]
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(1), T.int64(64), T.int64(1), T.int64(1)):
            with T.block("T_reshape_4"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(T_divide_1[(v_ax1 + v_ax2 + v_ax3) % T.int64(64)])
                T.writes(T_reshape_4[v_ax0, v_ax1, v_ax2, v_ax3])
                T_reshape_4[v_ax0, v_ax1, v_ax2, v_ax3] = T_divide_1[(v_ax1 + v_ax2 + v_ax3) % T.int64(64)]
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(1), T.int64(64), T.int64(112), T.int64(112)):
            with T.block("T_subtract_1"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(lv4[v_ax0, v_ax1, v_ax2, v_ax3], T_reshape_4[v_ax0, v_ax1, T.int64(0), T.int64(0)])
                T.writes(T_subtract_1[v_ax0, v_ax1, v_ax2, v_ax3])
                T_subtract_1[v_ax0, v_ax1, v_ax2, v_ax3] = lv4[v_ax0, v_ax1, v_ax2, v_ax3] - T_reshape_4[v_ax0, v_ax1, T.int64(0), T.int64(0)]
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(1), T.int64(64), T.int64(112), T.int64(112)):
            with T.block("T_subtract_2"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(lv4[v_ax0, v_ax1, v_ax2, v_ax3], T_reshape_4[v_ax0, v_ax1, T.int64(0), T.int64(0)])
                T.writes(T_subtract_2[v_ax0, v_ax1, v_ax2, v_ax3])
                T_subtract_2[v_ax0, v_ax1, v_ax2, v_ax3] = lv4[v_ax0, v_ax1, v_ax2, v_ax3] - T_reshape_4[v_ax0, v_ax1, T.int64(0), T.int64(0)]
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(1), T.int64(64), T.int64(112), T.int64(112)):
            with T.block("T_multiply_4"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(T_subtract_1[v_ax0, v_ax1, v_ax2, v_ax3], T_subtract_2[v_ax0, v_ax1, v_ax2, v_ax3])
                T.writes(T_multiply_4[v_ax0, v_ax1, v_ax2, v_ax3])
                T_multiply_4[v_ax0, v_ax1, v_ax2, v_ax3] = T_subtract_1[v_ax0, v_ax1, v_ax2, v_ax3] * T_subtract_2[v_ax0, v_ax1, v_ax2, v_ax3]
        for ax0, k0, k2, k3 in T.grid(T.int64(64), T.int64(1), T.int64(112), T.int64(112)):
            with T.block("T_multiply_red"):
                v_ax0, v_k0, v_k2, v_k3 = T.axis.remap("SRRR", [ax0, k0, k2, k3])
                T.reads(T_multiply_4[v_k0, v_ax0, v_k2, v_k3])
                T.writes(T_multiply_red[v_ax0])
                with T.init():
                    T_multiply_red[v_ax0] = T.float32(0.0)
                T_multiply_red[v_ax0] = T_multiply_red[v_ax0] + T_multiply_4[v_k0, v_ax0, v_k2, v_k3]
        for ax0 in range(T.int64(64)):
            with T.block("T_divide_2"):
                v_ax0 = T.axis.spatial(T.int64(64), ax0)
                T.reads(T_multiply_red[v_ax0])
                T.writes(T_divide_2[v_ax0])
                T_divide_2[v_ax0] = T_multiply_red[v_ax0] * T.float32(7.9719387755102034e-05)
        for ax0 in range(T.int64(64)):
            with T.block("T_multiply_5"):
                v_ax0 = T.axis.spatial(T.int64(64), ax0)
                T.reads(T_divide_2[v_ax0])
                T.writes(T_multiply_5[v_ax0])
                T_multiply_5[v_ax0] = T.float32(0.10000000000000001) * T_divide_2[v_ax0]
        for ax0 in range(T.int64(64)):
            with T.block("T_add_3"):
                v_ax0 = T.axis.spatial(T.int64(64), ax0)
                T.reads(T_multiply_3[v_ax0], T_multiply_5[v_ax0])
                T.writes(T_add_2[v_ax0])
                T_add_2[v_ax0] = T_multiply_3[v_ax0] + T_multiply_5[v_ax0]

    @T.prim_func(private=True)
    def batch_norm10(lv266: T.Buffer((T.int64(1), T.int64(512), T.int64(14), T.int64(14)), "float32"), B: T.Buffer((T.int64(512),), "float32"), C: T.Buffer((T.int64(512),), "float32"), D: T.Buffer((T.int64(512),), "float32"), E: T.Buffer((T.int64(512),), "float32"), T_add: T.Buffer((T.int64(1), T.int64(512), T.int64(14), T.int64(14)), "float32"), T_add_1: T.Buffer((T.int64(512),), "float32"), T_add_2: T.Buffer((T.int64(512),), "float32")):
        T.func_attr({"tir.noalias": True})
        # with T.block("root"):
        T_reshape = T.alloc_buffer((T.int64(1), T.int64(512), T.int64(1), T.int64(1)))
        T_subtract = T.alloc_buffer((T.int64(1), T.int64(512), T.int64(14), T.int64(14)))
        T_reshape_1 = T.alloc_buffer((T.int64(1), T.int64(512), T.int64(1), T.int64(1)))
        T_add_3 = T.alloc_buffer((T.int64(1), T.int64(512), T.int64(1), T.int64(1)))
        compute = T.alloc_buffer((T.int64(1), T.int64(512), T.int64(1), T.int64(1)))
        T_divide = T.alloc_buffer((T.int64(1), T.int64(512), T.int64(14), T.int64(14)))
        T_reshape_2 = T.alloc_buffer((T.int64(1), T.int64(512), T.int64(1), T.int64(1)))
        T_multiply = T.alloc_buffer((T.int64(1), T.int64(512), T.int64(14), T.int64(14)))
        T_reshape_3 = T.alloc_buffer((T.int64(1), T.int64(512), T.int64(1), T.int64(1)))
        T_multiply_1 = T.alloc_buffer((T.int64(512),))
        lv266_red = T.alloc_buffer((T.int64(512),))
        T_divide_1 = T.alloc_buffer((T.int64(512),))
        T_multiply_2 = T.alloc_buffer((T.int64(512),))
        T_multiply_3 = T.alloc_buffer((T.int64(512),))
        T_reshape_4 = T.alloc_buffer((T.int64(1), T.int64(512), T.int64(1), T.int64(1)))
        T_subtract_1 = T.alloc_buffer((T.int64(1), T.int64(512), T.int64(14), T.int64(14)))
        T_subtract_2 = T.alloc_buffer((T.int64(1), T.int64(512), T.int64(14), T.int64(14)))
        T_multiply_4 = T.alloc_buffer((T.int64(1), T.int64(512), T.int64(14), T.int64(14)))
        T_multiply_red = T.alloc_buffer((T.int64(512),))
        T_divide_2 = T.alloc_buffer((T.int64(512),))
        T_multiply_5 = T.alloc_buffer((T.int64(512),))
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(1), T.int64(512), T.int64(1), T.int64(1)):
            with T.block("T_reshape"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(D[(v_ax1 + v_ax2 + v_ax3) % T.int64(512)])
                T.writes(T_reshape[v_ax0, v_ax1, v_ax2, v_ax3])
                T_reshape[v_ax0, v_ax1, v_ax2, v_ax3] = D[(v_ax1 + v_ax2 + v_ax3) % T.int64(512)]
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(1), T.int64(512), T.int64(14), T.int64(14)):
            with T.block("T_subtract"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(lv266[v_ax0, v_ax1, v_ax2, v_ax3], T_reshape[v_ax0, v_ax1, T.int64(0), T.int64(0)])
                T.writes(T_subtract[v_ax0, v_ax1, v_ax2, v_ax3])
                T_subtract[v_ax0, v_ax1, v_ax2, v_ax3] = lv266[v_ax0, v_ax1, v_ax2, v_ax3] - T_reshape[v_ax0, v_ax1, T.int64(0), T.int64(0)]
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(1), T.int64(512), T.int64(1), T.int64(1)):
            with T.block("T_reshape_1"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(E[(v_ax1 + v_ax2 + v_ax3) % T.int64(512)])
                T.writes(T_reshape_1[v_ax0, v_ax1, v_ax2, v_ax3])
                T_reshape_1[v_ax0, v_ax1, v_ax2, v_ax3] = E[(v_ax1 + v_ax2 + v_ax3) % T.int64(512)]
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(1), T.int64(512), T.int64(1), T.int64(1)):
            with T.block("T_add"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(T_reshape_1[v_ax0, v_ax1, v_ax2, v_ax3])
                T.writes(T_add_3[v_ax0, v_ax1, v_ax2, v_ax3])
                T_add_3[v_ax0, v_ax1, v_ax2, v_ax3] = T_reshape_1[v_ax0, v_ax1, v_ax2, v_ax3] + T.float32(9.9999997473787516e-06)
        for i0, i1, i2, i3 in T.grid(T.int64(1), T.int64(512), T.int64(1), T.int64(1)):
            with T.block("compute"):
                v_i0, v_i1, v_i2, v_i3 = T.axis.remap("SSSS", [i0, i1, i2, i3])
                T.reads(T_add_3[v_i0, v_i1, v_i2, v_i3])
                T.writes(compute[v_i0, v_i1, v_i2, v_i3])
                compute[v_i0, v_i1, v_i2, v_i3] = T.sqrt(T_add_3[v_i0, v_i1, v_i2, v_i3])
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(1), T.int64(512), T.int64(14), T.int64(14)):
            with T.block("T_divide"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(T_subtract[v_ax0, v_ax1, v_ax2, v_ax3], compute[v_ax0, v_ax1, T.int64(0), T.int64(0)])
                T.writes(T_divide[v_ax0, v_ax1, v_ax2, v_ax3])
                T_divide[v_ax0, v_ax1, v_ax2, v_ax3] = T_subtract[v_ax0, v_ax1, v_ax2, v_ax3] / compute[v_ax0, v_ax1, T.int64(0), T.int64(0)]
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(1), T.int64(512), T.int64(1), T.int64(1)):
            with T.block("T_reshape_2"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(B[(v_ax1 + v_ax2 + v_ax3) % T.int64(512)])
                T.writes(T_reshape_2[v_ax0, v_ax1, v_ax2, v_ax3])
                T_reshape_2[v_ax0, v_ax1, v_ax2, v_ax3] = B[(v_ax1 + v_ax2 + v_ax3) % T.int64(512)]
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(1), T.int64(512), T.int64(14), T.int64(14)):
            with T.block("T_multiply"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(T_divide[v_ax0, v_ax1, v_ax2, v_ax3], T_reshape_2[v_ax0, v_ax1, T.int64(0), T.int64(0)])
                T.writes(T_multiply[v_ax0, v_ax1, v_ax2, v_ax3])
                T_multiply[v_ax0, v_ax1, v_ax2, v_ax3] = T_divide[v_ax0, v_ax1, v_ax2, v_ax3] * T_reshape_2[v_ax0, v_ax1, T.int64(0), T.int64(0)]
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(1), T.int64(512), T.int64(1), T.int64(1)):
            with T.block("T_reshape_3"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(C[(v_ax1 + v_ax2 + v_ax3) % T.int64(512)])
                T.writes(T_reshape_3[v_ax0, v_ax1, v_ax2, v_ax3])
                T_reshape_3[v_ax0, v_ax1, v_ax2, v_ax3] = C[(v_ax1 + v_ax2 + v_ax3) % T.int64(512)]
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(1), T.int64(512), T.int64(14), T.int64(14)):
            with T.block("T_add_1"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(T_multiply[v_ax0, v_ax1, v_ax2, v_ax3], T_reshape_3[v_ax0, v_ax1, T.int64(0), T.int64(0)])
                T.writes(T_add[v_ax0, v_ax1, v_ax2, v_ax3])
                T_add[v_ax0, v_ax1, v_ax2, v_ax3] = T_multiply[v_ax0, v_ax1, v_ax2, v_ax3] + T_reshape_3[v_ax0, v_ax1, T.int64(0), T.int64(0)]
        for ax0 in range(T.int64(512)):
            with T.block("T_multiply_1"):
                v_ax0 = T.axis.spatial(T.int64(512), ax0)
                T.reads(D[v_ax0])
                T.writes(T_multiply_1[v_ax0])
                T_multiply_1[v_ax0] = T.float32(0.90000000000000002) * D[v_ax0]
        for ax0, k0, k2, k3 in T.grid(T.int64(512), T.int64(1), T.int64(14), T.int64(14)):
            with T.block("lv266_red"):
                v_ax0, v_k0, v_k2, v_k3 = T.axis.remap("SRRR", [ax0, k0, k2, k3])
                T.reads(lv266[v_k0, v_ax0, v_k2, v_k3])
                T.writes(lv266_red[v_ax0])
                with T.init():
                    lv266_red[v_ax0] = T.float32(0.0)
                lv266_red[v_ax0] = lv266_red[v_ax0] + lv266[v_k0, v_ax0, v_k2, v_k3]
        for ax0 in range(T.int64(512)):
            with T.block("T_divide_1"):
                v_ax0 = T.axis.spatial(T.int64(512), ax0)
                T.reads(lv266_red[v_ax0])
                T.writes(T_divide_1[v_ax0])
                T_divide_1[v_ax0] = lv266_red[v_ax0] * T.float32(0.0051020408163265302)
        for ax0 in range(T.int64(512)):
            with T.block("T_multiply_2"):
                v_ax0 = T.axis.spatial(T.int64(512), ax0)
                T.reads(T_divide_1[v_ax0])
                T.writes(T_multiply_2[v_ax0])
                T_multiply_2[v_ax0] = T.float32(0.10000000000000001) * T_divide_1[v_ax0]
        for ax0 in range(T.int64(512)):
            with T.block("T_add_2"):
                v_ax0 = T.axis.spatial(T.int64(512), ax0)
                T.reads(T_multiply_1[v_ax0], T_multiply_2[v_ax0])
                T.writes(T_add_1[v_ax0])
                T_add_1[v_ax0] = T_multiply_1[v_ax0] + T_multiply_2[v_ax0]
        for ax0 in range(T.int64(512)):
            with T.block("T_multiply_3"):
                v_ax0 = T.axis.spatial(T.int64(512), ax0)
                T.reads(E[v_ax0])
                T.writes(T_multiply_3[v_ax0])
                T_multiply_3[v_ax0] = T.float32(0.90000000000000002) * E[v_ax0]
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(1), T.int64(512), T.int64(1), T.int64(1)):
            with T.block("T_reshape_4"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(T_divide_1[(v_ax1 + v_ax2 + v_ax3) % T.int64(512)])
                T.writes(T_reshape_4[v_ax0, v_ax1, v_ax2, v_ax3])
                T_reshape_4[v_ax0, v_ax1, v_ax2, v_ax3] = T_divide_1[(v_ax1 + v_ax2 + v_ax3) % T.int64(512)]
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(1), T.int64(512), T.int64(14), T.int64(14)):
            with T.block("T_subtract_1"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(lv266[v_ax0, v_ax1, v_ax2, v_ax3], T_reshape_4[v_ax0, v_ax1, T.int64(0), T.int64(0)])
                T.writes(T_subtract_1[v_ax0, v_ax1, v_ax2, v_ax3])
                T_subtract_1[v_ax0, v_ax1, v_ax2, v_ax3] = lv266[v_ax0, v_ax1, v_ax2, v_ax3] - T_reshape_4[v_ax0, v_ax1, T.int64(0), T.int64(0)]
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(1), T.int64(512), T.int64(14), T.int64(14)):
            with T.block("T_subtract_2"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(lv266[v_ax0, v_ax1, v_ax2, v_ax3], T_reshape_4[v_ax0, v_ax1, T.int64(0), T.int64(0)])
                T.writes(T_subtract_2[v_ax0, v_ax1, v_ax2, v_ax3])
                T_subtract_2[v_ax0, v_ax1, v_ax2, v_ax3] = lv266[v_ax0, v_ax1, v_ax2, v_ax3] - T_reshape_4[v_ax0, v_ax1, T.int64(0), T.int64(0)]
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(1), T.int64(512), T.int64(14), T.int64(14)):
            with T.block("T_multiply_4"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(T_subtract_1[v_ax0, v_ax1, v_ax2, v_ax3], T_subtract_2[v_ax0, v_ax1, v_ax2, v_ax3])
                T.writes(T_multiply_4[v_ax0, v_ax1, v_ax2, v_ax3])
                T_multiply_4[v_ax0, v_ax1, v_ax2, v_ax3] = T_subtract_1[v_ax0, v_ax1, v_ax2, v_ax3] * T_subtract_2[v_ax0, v_ax1, v_ax2, v_ax3]
        for ax0, k0, k2, k3 in T.grid(T.int64(512), T.int64(1), T.int64(14), T.int64(14)):
            with T.block("T_multiply_red"):
                v_ax0, v_k0, v_k2, v_k3 = T.axis.remap("SRRR", [ax0, k0, k2, k3])
                T.reads(T_multiply_4[v_k0, v_ax0, v_k2, v_k3])
                T.writes(T_multiply_red[v_ax0])
                with T.init():
                    T_multiply_red[v_ax0] = T.float32(0.0)
                T_multiply_red[v_ax0] = T_multiply_red[v_ax0] + T_multiply_4[v_k0, v_ax0, v_k2, v_k3]
        for ax0 in range(T.int64(512)):
            with T.block("T_divide_2"):
                v_ax0 = T.axis.spatial(T.int64(512), ax0)
                T.reads(T_multiply_red[v_ax0])
                T.writes(T_divide_2[v_ax0])
                T_divide_2[v_ax0] = T_multiply_red[v_ax0] * T.float32(0.0051020408163265302)
        for ax0 in range(T.int64(512)):
            with T.block("T_multiply_5"):
                v_ax0 = T.axis.spatial(T.int64(512), ax0)
                T.reads(T_divide_2[v_ax0])
                T.writes(T_multiply_5[v_ax0])
                T_multiply_5[v_ax0] = T.float32(0.10000000000000001) * T_divide_2[v_ax0]
        for ax0 in range(T.int64(512)):
            with T.block("T_add_3"):
                v_ax0 = T.axis.spatial(T.int64(512), ax0)
                T.reads(T_multiply_3[v_ax0], T_multiply_5[v_ax0])
                T.writes(T_add_2[v_ax0])
                T_add_2[v_ax0] = T_multiply_3[v_ax0] + T_multiply_5[v_ax0]

    @T.prim_func(private=True)
    def batch_norm11(lv272: T.Buffer((T.int64(1), T.int64(512), T.int64(7), T.int64(7)), "float32"), B: T.Buffer((T.int64(512),), "float32"), C: T.Buffer((T.int64(512),), "float32"), D: T.Buffer((T.int64(512),), "float32"), E: T.Buffer((T.int64(512),), "float32"), T_add: T.Buffer((T.int64(1), T.int64(512), T.int64(7), T.int64(7)), "float32"), T_add_1: T.Buffer((T.int64(512),), "float32"), T_add_2: T.Buffer((T.int64(512),), "float32")):
        T.func_attr({"tir.noalias": True})
        # with T.block("root"):
        T_reshape = T.alloc_buffer((T.int64(1), T.int64(512), T.int64(1), T.int64(1)))
        T_subtract = T.alloc_buffer((T.int64(1), T.int64(512), T.int64(7), T.int64(7)))
        T_reshape_1 = T.alloc_buffer((T.int64(1), T.int64(512), T.int64(1), T.int64(1)))
        T_add_3 = T.alloc_buffer((T.int64(1), T.int64(512), T.int64(1), T.int64(1)))
        compute = T.alloc_buffer((T.int64(1), T.int64(512), T.int64(1), T.int64(1)))
        T_divide = T.alloc_buffer((T.int64(1), T.int64(512), T.int64(7), T.int64(7)))
        T_reshape_2 = T.alloc_buffer((T.int64(1), T.int64(512), T.int64(1), T.int64(1)))
        T_multiply = T.alloc_buffer((T.int64(1), T.int64(512), T.int64(7), T.int64(7)))
        T_reshape_3 = T.alloc_buffer((T.int64(1), T.int64(512), T.int64(1), T.int64(1)))
        T_multiply_1 = T.alloc_buffer((T.int64(512),))
        lv272_red = T.alloc_buffer((T.int64(512),))
        T_divide_1 = T.alloc_buffer((T.int64(512),))
        T_multiply_2 = T.alloc_buffer((T.int64(512),))
        T_multiply_3 = T.alloc_buffer((T.int64(512),))
        T_reshape_4 = T.alloc_buffer((T.int64(1), T.int64(512), T.int64(1), T.int64(1)))
        T_subtract_1 = T.alloc_buffer((T.int64(1), T.int64(512), T.int64(7), T.int64(7)))
        T_subtract_2 = T.alloc_buffer((T.int64(1), T.int64(512), T.int64(7), T.int64(7)))
        T_multiply_4 = T.alloc_buffer((T.int64(1), T.int64(512), T.int64(7), T.int64(7)))
        T_multiply_red = T.alloc_buffer((T.int64(512),))
        T_divide_2 = T.alloc_buffer((T.int64(512),))
        T_multiply_5 = T.alloc_buffer((T.int64(512),))
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(1), T.int64(512), T.int64(1), T.int64(1)):
            with T.block("T_reshape"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(D[(v_ax1 + v_ax2 + v_ax3) % T.int64(512)])
                T.writes(T_reshape[v_ax0, v_ax1, v_ax2, v_ax3])
                T_reshape[v_ax0, v_ax1, v_ax2, v_ax3] = D[(v_ax1 + v_ax2 + v_ax3) % T.int64(512)]
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(1), T.int64(512), T.int64(7), T.int64(7)):
            with T.block("T_subtract"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(lv272[v_ax0, v_ax1, v_ax2, v_ax3], T_reshape[v_ax0, v_ax1, T.int64(0), T.int64(0)])
                T.writes(T_subtract[v_ax0, v_ax1, v_ax2, v_ax3])
                T_subtract[v_ax0, v_ax1, v_ax2, v_ax3] = lv272[v_ax0, v_ax1, v_ax2, v_ax3] - T_reshape[v_ax0, v_ax1, T.int64(0), T.int64(0)]
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(1), T.int64(512), T.int64(1), T.int64(1)):
            with T.block("T_reshape_1"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(E[(v_ax1 + v_ax2 + v_ax3) % T.int64(512)])
                T.writes(T_reshape_1[v_ax0, v_ax1, v_ax2, v_ax3])
                T_reshape_1[v_ax0, v_ax1, v_ax2, v_ax3] = E[(v_ax1 + v_ax2 + v_ax3) % T.int64(512)]
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(1), T.int64(512), T.int64(1), T.int64(1)):
            with T.block("T_add"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(T_reshape_1[v_ax0, v_ax1, v_ax2, v_ax3])
                T.writes(T_add_3[v_ax0, v_ax1, v_ax2, v_ax3])
                T_add_3[v_ax0, v_ax1, v_ax2, v_ax3] = T_reshape_1[v_ax0, v_ax1, v_ax2, v_ax3] + T.float32(9.9999997473787516e-06)
        for i0, i1, i2, i3 in T.grid(T.int64(1), T.int64(512), T.int64(1), T.int64(1)):
            with T.block("compute"):
                v_i0, v_i1, v_i2, v_i3 = T.axis.remap("SSSS", [i0, i1, i2, i3])
                T.reads(T_add_3[v_i0, v_i1, v_i2, v_i3])
                T.writes(compute[v_i0, v_i1, v_i2, v_i3])
                compute[v_i0, v_i1, v_i2, v_i3] = T.sqrt(T_add_3[v_i0, v_i1, v_i2, v_i3])
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(1), T.int64(512), T.int64(7), T.int64(7)):
            with T.block("T_divide"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(T_subtract[v_ax0, v_ax1, v_ax2, v_ax3], compute[v_ax0, v_ax1, T.int64(0), T.int64(0)])
                T.writes(T_divide[v_ax0, v_ax1, v_ax2, v_ax3])
                T_divide[v_ax0, v_ax1, v_ax2, v_ax3] = T_subtract[v_ax0, v_ax1, v_ax2, v_ax3] / compute[v_ax0, v_ax1, T.int64(0), T.int64(0)]
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(1), T.int64(512), T.int64(1), T.int64(1)):
            with T.block("T_reshape_2"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(B[(v_ax1 + v_ax2 + v_ax3) % T.int64(512)])
                T.writes(T_reshape_2[v_ax0, v_ax1, v_ax2, v_ax3])
                T_reshape_2[v_ax0, v_ax1, v_ax2, v_ax3] = B[(v_ax1 + v_ax2 + v_ax3) % T.int64(512)]
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(1), T.int64(512), T.int64(7), T.int64(7)):
            with T.block("T_multiply"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(T_divide[v_ax0, v_ax1, v_ax2, v_ax3], T_reshape_2[v_ax0, v_ax1, T.int64(0), T.int64(0)])
                T.writes(T_multiply[v_ax0, v_ax1, v_ax2, v_ax3])
                T_multiply[v_ax0, v_ax1, v_ax2, v_ax3] = T_divide[v_ax0, v_ax1, v_ax2, v_ax3] * T_reshape_2[v_ax0, v_ax1, T.int64(0), T.int64(0)]
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(1), T.int64(512), T.int64(1), T.int64(1)):
            with T.block("T_reshape_3"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(C[(v_ax1 + v_ax2 + v_ax3) % T.int64(512)])
                T.writes(T_reshape_3[v_ax0, v_ax1, v_ax2, v_ax3])
                T_reshape_3[v_ax0, v_ax1, v_ax2, v_ax3] = C[(v_ax1 + v_ax2 + v_ax3) % T.int64(512)]
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(1), T.int64(512), T.int64(7), T.int64(7)):
            with T.block("T_add_1"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(T_multiply[v_ax0, v_ax1, v_ax2, v_ax3], T_reshape_3[v_ax0, v_ax1, T.int64(0), T.int64(0)])
                T.writes(T_add[v_ax0, v_ax1, v_ax2, v_ax3])
                T_add[v_ax0, v_ax1, v_ax2, v_ax3] = T_multiply[v_ax0, v_ax1, v_ax2, v_ax3] + T_reshape_3[v_ax0, v_ax1, T.int64(0), T.int64(0)]
        for ax0 in range(T.int64(512)):
            with T.block("T_multiply_1"):
                v_ax0 = T.axis.spatial(T.int64(512), ax0)
                T.reads(D[v_ax0])
                T.writes(T_multiply_1[v_ax0])
                T_multiply_1[v_ax0] = T.float32(0.90000000000000002) * D[v_ax0]
        for ax0, k0, k2, k3 in T.grid(T.int64(512), T.int64(1), T.int64(7), T.int64(7)):
            with T.block("lv272_red"):
                v_ax0, v_k0, v_k2, v_k3 = T.axis.remap("SRRR", [ax0, k0, k2, k3])
                T.reads(lv272[v_k0, v_ax0, v_k2, v_k3])
                T.writes(lv272_red[v_ax0])
                with T.init():
                    lv272_red[v_ax0] = T.float32(0.0)
                lv272_red[v_ax0] = lv272_red[v_ax0] + lv272[v_k0, v_ax0, v_k2, v_k3]
        for ax0 in range(T.int64(512)):
            with T.block("T_divide_1"):
                v_ax0 = T.axis.spatial(T.int64(512), ax0)
                T.reads(lv272_red[v_ax0])
                T.writes(T_divide_1[v_ax0])
                T_divide_1[v_ax0] = lv272_red[v_ax0] * T.float32(0.020408163265306121)
        for ax0 in range(T.int64(512)):
            with T.block("T_multiply_2"):
                v_ax0 = T.axis.spatial(T.int64(512), ax0)
                T.reads(T_divide_1[v_ax0])
                T.writes(T_multiply_2[v_ax0])
                T_multiply_2[v_ax0] = T.float32(0.10000000000000001) * T_divide_1[v_ax0]
        for ax0 in range(T.int64(512)):
            with T.block("T_add_2"):
                v_ax0 = T.axis.spatial(T.int64(512), ax0)
                T.reads(T_multiply_1[v_ax0], T_multiply_2[v_ax0])
                T.writes(T_add_1[v_ax0])
                T_add_1[v_ax0] = T_multiply_1[v_ax0] + T_multiply_2[v_ax0]
        for ax0 in range(T.int64(512)):
            with T.block("T_multiply_3"):
                v_ax0 = T.axis.spatial(T.int64(512), ax0)
                T.reads(E[v_ax0])
                T.writes(T_multiply_3[v_ax0])
                T_multiply_3[v_ax0] = T.float32(0.90000000000000002) * E[v_ax0]
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(1), T.int64(512), T.int64(1), T.int64(1)):
            with T.block("T_reshape_4"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(T_divide_1[(v_ax1 + v_ax2 + v_ax3) % T.int64(512)])
                T.writes(T_reshape_4[v_ax0, v_ax1, v_ax2, v_ax3])
                T_reshape_4[v_ax0, v_ax1, v_ax2, v_ax3] = T_divide_1[(v_ax1 + v_ax2 + v_ax3) % T.int64(512)]
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(1), T.int64(512), T.int64(7), T.int64(7)):
            with T.block("T_subtract_1"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(lv272[v_ax0, v_ax1, v_ax2, v_ax3], T_reshape_4[v_ax0, v_ax1, T.int64(0), T.int64(0)])
                T.writes(T_subtract_1[v_ax0, v_ax1, v_ax2, v_ax3])
                T_subtract_1[v_ax0, v_ax1, v_ax2, v_ax3] = lv272[v_ax0, v_ax1, v_ax2, v_ax3] - T_reshape_4[v_ax0, v_ax1, T.int64(0), T.int64(0)]
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(1), T.int64(512), T.int64(7), T.int64(7)):
            with T.block("T_subtract_2"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(lv272[v_ax0, v_ax1, v_ax2, v_ax3], T_reshape_4[v_ax0, v_ax1, T.int64(0), T.int64(0)])
                T.writes(T_subtract_2[v_ax0, v_ax1, v_ax2, v_ax3])
                T_subtract_2[v_ax0, v_ax1, v_ax2, v_ax3] = lv272[v_ax0, v_ax1, v_ax2, v_ax3] - T_reshape_4[v_ax0, v_ax1, T.int64(0), T.int64(0)]
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(1), T.int64(512), T.int64(7), T.int64(7)):
            with T.block("T_multiply_4"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(T_subtract_1[v_ax0, v_ax1, v_ax2, v_ax3], T_subtract_2[v_ax0, v_ax1, v_ax2, v_ax3])
                T.writes(T_multiply_4[v_ax0, v_ax1, v_ax2, v_ax3])
                T_multiply_4[v_ax0, v_ax1, v_ax2, v_ax3] = T_subtract_1[v_ax0, v_ax1, v_ax2, v_ax3] * T_subtract_2[v_ax0, v_ax1, v_ax2, v_ax3]
        for ax0, k0, k2, k3 in T.grid(T.int64(512), T.int64(1), T.int64(7), T.int64(7)):
            with T.block("T_multiply_red"):
                v_ax0, v_k0, v_k2, v_k3 = T.axis.remap("SRRR", [ax0, k0, k2, k3])
                T.reads(T_multiply_4[v_k0, v_ax0, v_k2, v_k3])
                T.writes(T_multiply_red[v_ax0])
                with T.init():
                    T_multiply_red[v_ax0] = T.float32(0.0)
                T_multiply_red[v_ax0] = T_multiply_red[v_ax0] + T_multiply_4[v_k0, v_ax0, v_k2, v_k3]
        for ax0 in range(T.int64(512)):
            with T.block("T_divide_2"):
                v_ax0 = T.axis.spatial(T.int64(512), ax0)
                T.reads(T_multiply_red[v_ax0])
                T.writes(T_divide_2[v_ax0])
                T_divide_2[v_ax0] = T_multiply_red[v_ax0] * T.float32(0.020408163265306121)
        for ax0 in range(T.int64(512)):
            with T.block("T_multiply_5"):
                v_ax0 = T.axis.spatial(T.int64(512), ax0)
                T.reads(T_divide_2[v_ax0])
                T.writes(T_multiply_5[v_ax0])
                T_multiply_5[v_ax0] = T.float32(0.10000000000000001) * T_divide_2[v_ax0]
        for ax0 in range(T.int64(512)):
            with T.block("T_add_3"):
                v_ax0 = T.axis.spatial(T.int64(512), ax0)
                T.reads(T_multiply_3[v_ax0], T_multiply_5[v_ax0])
                T.writes(T_add_2[v_ax0])
                T_add_2[v_ax0] = T_multiply_3[v_ax0] + T_multiply_5[v_ax0]

    @T.prim_func(private=True)
    def batch_norm12(lv280: T.Buffer((T.int64(1), T.int64(2048), T.int64(7), T.int64(7)), "float32"), B: T.Buffer((T.int64(2048),), "float32"), C: T.Buffer((T.int64(2048),), "float32"), D: T.Buffer((T.int64(2048),), "float32"), E: T.Buffer((T.int64(2048),), "float32"), T_add: T.Buffer((T.int64(1), T.int64(2048), T.int64(7), T.int64(7)), "float32"), T_add_1: T.Buffer((T.int64(2048),), "float32"), T_add_2: T.Buffer((T.int64(2048),), "float32")):
        T.func_attr({"tir.noalias": True})
        # with T.block("root"):
        T_reshape = T.alloc_buffer((T.int64(1), T.int64(2048), T.int64(1), T.int64(1)))
        T_subtract = T.alloc_buffer((T.int64(1), T.int64(2048), T.int64(7), T.int64(7)))
        T_reshape_1 = T.alloc_buffer((T.int64(1), T.int64(2048), T.int64(1), T.int64(1)))
        T_add_3 = T.alloc_buffer((T.int64(1), T.int64(2048), T.int64(1), T.int64(1)))
        compute = T.alloc_buffer((T.int64(1), T.int64(2048), T.int64(1), T.int64(1)))
        T_divide = T.alloc_buffer((T.int64(1), T.int64(2048), T.int64(7), T.int64(7)))
        T_reshape_2 = T.alloc_buffer((T.int64(1), T.int64(2048), T.int64(1), T.int64(1)))
        T_multiply = T.alloc_buffer((T.int64(1), T.int64(2048), T.int64(7), T.int64(7)))
        T_reshape_3 = T.alloc_buffer((T.int64(1), T.int64(2048), T.int64(1), T.int64(1)))
        T_multiply_1 = T.alloc_buffer((T.int64(2048),))
        lv280_red = T.alloc_buffer((T.int64(2048),))
        T_divide_1 = T.alloc_buffer((T.int64(2048),))
        T_multiply_2 = T.alloc_buffer((T.int64(2048),))
        T_multiply_3 = T.alloc_buffer((T.int64(2048),))
        T_reshape_4 = T.alloc_buffer((T.int64(1), T.int64(2048), T.int64(1), T.int64(1)))
        T_subtract_1 = T.alloc_buffer((T.int64(1), T.int64(2048), T.int64(7), T.int64(7)))
        T_subtract_2 = T.alloc_buffer((T.int64(1), T.int64(2048), T.int64(7), T.int64(7)))
        T_multiply_4 = T.alloc_buffer((T.int64(1), T.int64(2048), T.int64(7), T.int64(7)))
        T_multiply_red = T.alloc_buffer((T.int64(2048),))
        T_divide_2 = T.alloc_buffer((T.int64(2048),))
        T_multiply_5 = T.alloc_buffer((T.int64(2048),))
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(1), T.int64(2048), T.int64(1), T.int64(1)):
            with T.block("T_reshape"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(D[(v_ax1 + v_ax2 + v_ax3) % T.int64(2048)])
                T.writes(T_reshape[v_ax0, v_ax1, v_ax2, v_ax3])
                T_reshape[v_ax0, v_ax1, v_ax2, v_ax3] = D[(v_ax1 + v_ax2 + v_ax3) % T.int64(2048)]
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(1), T.int64(2048), T.int64(7), T.int64(7)):
            with T.block("T_subtract"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(lv280[v_ax0, v_ax1, v_ax2, v_ax3], T_reshape[v_ax0, v_ax1, T.int64(0), T.int64(0)])
                T.writes(T_subtract[v_ax0, v_ax1, v_ax2, v_ax3])
                T_subtract[v_ax0, v_ax1, v_ax2, v_ax3] = lv280[v_ax0, v_ax1, v_ax2, v_ax3] - T_reshape[v_ax0, v_ax1, T.int64(0), T.int64(0)]
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(1), T.int64(2048), T.int64(1), T.int64(1)):
            with T.block("T_reshape_1"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(E[(v_ax1 + v_ax2 + v_ax3) % T.int64(2048)])
                T.writes(T_reshape_1[v_ax0, v_ax1, v_ax2, v_ax3])
                T_reshape_1[v_ax0, v_ax1, v_ax2, v_ax3] = E[(v_ax1 + v_ax2 + v_ax3) % T.int64(2048)]
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(1), T.int64(2048), T.int64(1), T.int64(1)):
            with T.block("T_add"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(T_reshape_1[v_ax0, v_ax1, v_ax2, v_ax3])
                T.writes(T_add_3[v_ax0, v_ax1, v_ax2, v_ax3])
                T_add_3[v_ax0, v_ax1, v_ax2, v_ax3] = T_reshape_1[v_ax0, v_ax1, v_ax2, v_ax3] + T.float32(9.9999997473787516e-06)
        for i0, i1, i2, i3 in T.grid(T.int64(1), T.int64(2048), T.int64(1), T.int64(1)):
            with T.block("compute"):
                v_i0, v_i1, v_i2, v_i3 = T.axis.remap("SSSS", [i0, i1, i2, i3])
                T.reads(T_add_3[v_i0, v_i1, v_i2, v_i3])
                T.writes(compute[v_i0, v_i1, v_i2, v_i3])
                compute[v_i0, v_i1, v_i2, v_i3] = T.sqrt(T_add_3[v_i0, v_i1, v_i2, v_i3])
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(1), T.int64(2048), T.int64(7), T.int64(7)):
            with T.block("T_divide"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(T_subtract[v_ax0, v_ax1, v_ax2, v_ax3], compute[v_ax0, v_ax1, T.int64(0), T.int64(0)])
                T.writes(T_divide[v_ax0, v_ax1, v_ax2, v_ax3])
                T_divide[v_ax0, v_ax1, v_ax2, v_ax3] = T_subtract[v_ax0, v_ax1, v_ax2, v_ax3] / compute[v_ax0, v_ax1, T.int64(0), T.int64(0)]
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(1), T.int64(2048), T.int64(1), T.int64(1)):
            with T.block("T_reshape_2"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(B[(v_ax1 + v_ax2 + v_ax3) % T.int64(2048)])
                T.writes(T_reshape_2[v_ax0, v_ax1, v_ax2, v_ax3])
                T_reshape_2[v_ax0, v_ax1, v_ax2, v_ax3] = B[(v_ax1 + v_ax2 + v_ax3) % T.int64(2048)]
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(1), T.int64(2048), T.int64(7), T.int64(7)):
            with T.block("T_multiply"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(T_divide[v_ax0, v_ax1, v_ax2, v_ax3], T_reshape_2[v_ax0, v_ax1, T.int64(0), T.int64(0)])
                T.writes(T_multiply[v_ax0, v_ax1, v_ax2, v_ax3])
                T_multiply[v_ax0, v_ax1, v_ax2, v_ax3] = T_divide[v_ax0, v_ax1, v_ax2, v_ax3] * T_reshape_2[v_ax0, v_ax1, T.int64(0), T.int64(0)]
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(1), T.int64(2048), T.int64(1), T.int64(1)):
            with T.block("T_reshape_3"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(C[(v_ax1 + v_ax2 + v_ax3) % T.int64(2048)])
                T.writes(T_reshape_3[v_ax0, v_ax1, v_ax2, v_ax3])
                T_reshape_3[v_ax0, v_ax1, v_ax2, v_ax3] = C[(v_ax1 + v_ax2 + v_ax3) % T.int64(2048)]
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(1), T.int64(2048), T.int64(7), T.int64(7)):
            with T.block("T_add_1"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(T_multiply[v_ax0, v_ax1, v_ax2, v_ax3], T_reshape_3[v_ax0, v_ax1, T.int64(0), T.int64(0)])
                T.writes(T_add[v_ax0, v_ax1, v_ax2, v_ax3])
                T_add[v_ax0, v_ax1, v_ax2, v_ax3] = T_multiply[v_ax0, v_ax1, v_ax2, v_ax3] + T_reshape_3[v_ax0, v_ax1, T.int64(0), T.int64(0)]
        for ax0 in range(T.int64(2048)):
            with T.block("T_multiply_1"):
                v_ax0 = T.axis.spatial(T.int64(2048), ax0)
                T.reads(D[v_ax0])
                T.writes(T_multiply_1[v_ax0])
                T_multiply_1[v_ax0] = T.float32(0.90000000000000002) * D[v_ax0]
        for ax0, k0, k2, k3 in T.grid(T.int64(2048), T.int64(1), T.int64(7), T.int64(7)):
            with T.block("lv280_red"):
                v_ax0, v_k0, v_k2, v_k3 = T.axis.remap("SRRR", [ax0, k0, k2, k3])
                T.reads(lv280[v_k0, v_ax0, v_k2, v_k3])
                T.writes(lv280_red[v_ax0])
                with T.init():
                    lv280_red[v_ax0] = T.float32(0.0)
                lv280_red[v_ax0] = lv280_red[v_ax0] + lv280[v_k0, v_ax0, v_k2, v_k3]
        for ax0 in range(T.int64(2048)):
            with T.block("T_divide_1"):
                v_ax0 = T.axis.spatial(T.int64(2048), ax0)
                T.reads(lv280_red[v_ax0])
                T.writes(T_divide_1[v_ax0])
                T_divide_1[v_ax0] = lv280_red[v_ax0] * T.float32(0.020408163265306121)
        for ax0 in range(T.int64(2048)):
            with T.block("T_multiply_2"):
                v_ax0 = T.axis.spatial(T.int64(2048), ax0)
                T.reads(T_divide_1[v_ax0])
                T.writes(T_multiply_2[v_ax0])
                T_multiply_2[v_ax0] = T.float32(0.10000000000000001) * T_divide_1[v_ax0]
        for ax0 in range(T.int64(2048)):
            with T.block("T_add_2"):
                v_ax0 = T.axis.spatial(T.int64(2048), ax0)
                T.reads(T_multiply_1[v_ax0], T_multiply_2[v_ax0])
                T.writes(T_add_1[v_ax0])
                T_add_1[v_ax0] = T_multiply_1[v_ax0] + T_multiply_2[v_ax0]
        for ax0 in range(T.int64(2048)):
            with T.block("T_multiply_3"):
                v_ax0 = T.axis.spatial(T.int64(2048), ax0)
                T.reads(E[v_ax0])
                T.writes(T_multiply_3[v_ax0])
                T_multiply_3[v_ax0] = T.float32(0.90000000000000002) * E[v_ax0]
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(1), T.int64(2048), T.int64(1), T.int64(1)):
            with T.block("T_reshape_4"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(T_divide_1[(v_ax1 + v_ax2 + v_ax3) % T.int64(2048)])
                T.writes(T_reshape_4[v_ax0, v_ax1, v_ax2, v_ax3])
                T_reshape_4[v_ax0, v_ax1, v_ax2, v_ax3] = T_divide_1[(v_ax1 + v_ax2 + v_ax3) % T.int64(2048)]
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(1), T.int64(2048), T.int64(7), T.int64(7)):
            with T.block("T_subtract_1"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(lv280[v_ax0, v_ax1, v_ax2, v_ax3], T_reshape_4[v_ax0, v_ax1, T.int64(0), T.int64(0)])
                T.writes(T_subtract_1[v_ax0, v_ax1, v_ax2, v_ax3])
                T_subtract_1[v_ax0, v_ax1, v_ax2, v_ax3] = lv280[v_ax0, v_ax1, v_ax2, v_ax3] - T_reshape_4[v_ax0, v_ax1, T.int64(0), T.int64(0)]
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(1), T.int64(2048), T.int64(7), T.int64(7)):
            with T.block("T_subtract_2"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(lv280[v_ax0, v_ax1, v_ax2, v_ax3], T_reshape_4[v_ax0, v_ax1, T.int64(0), T.int64(0)])
                T.writes(T_subtract_2[v_ax0, v_ax1, v_ax2, v_ax3])
                T_subtract_2[v_ax0, v_ax1, v_ax2, v_ax3] = lv280[v_ax0, v_ax1, v_ax2, v_ax3] - T_reshape_4[v_ax0, v_ax1, T.int64(0), T.int64(0)]
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(1), T.int64(2048), T.int64(7), T.int64(7)):
            with T.block("T_multiply_4"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(T_subtract_1[v_ax0, v_ax1, v_ax2, v_ax3], T_subtract_2[v_ax0, v_ax1, v_ax2, v_ax3])
                T.writes(T_multiply_4[v_ax0, v_ax1, v_ax2, v_ax3])
                T_multiply_4[v_ax0, v_ax1, v_ax2, v_ax3] = T_subtract_1[v_ax0, v_ax1, v_ax2, v_ax3] * T_subtract_2[v_ax0, v_ax1, v_ax2, v_ax3]
        for ax0, k0, k2, k3 in T.grid(T.int64(2048), T.int64(1), T.int64(7), T.int64(7)):
            with T.block("T_multiply_red"):
                v_ax0, v_k0, v_k2, v_k3 = T.axis.remap("SRRR", [ax0, k0, k2, k3])
                T.reads(T_multiply_4[v_k0, v_ax0, v_k2, v_k3])
                T.writes(T_multiply_red[v_ax0])
                with T.init():
                    T_multiply_red[v_ax0] = T.float32(0.0)
                T_multiply_red[v_ax0] = T_multiply_red[v_ax0] + T_multiply_4[v_k0, v_ax0, v_k2, v_k3]
        for ax0 in range(T.int64(2048)):
            with T.block("T_divide_2"):
                v_ax0 = T.axis.spatial(T.int64(2048), ax0)
                T.reads(T_multiply_red[v_ax0])
                T.writes(T_divide_2[v_ax0])
                T_divide_2[v_ax0] = T_multiply_red[v_ax0] * T.float32(0.020408163265306121)
        for ax0 in range(T.int64(2048)):
            with T.block("T_multiply_5"):
                v_ax0 = T.axis.spatial(T.int64(2048), ax0)
                T.reads(T_divide_2[v_ax0])
                T.writes(T_multiply_5[v_ax0])
                T_multiply_5[v_ax0] = T.float32(0.10000000000000001) * T_divide_2[v_ax0]
        for ax0 in range(T.int64(2048)):
            with T.block("T_add_3"):
                v_ax0 = T.axis.spatial(T.int64(2048), ax0)
                T.reads(T_multiply_3[v_ax0], T_multiply_5[v_ax0])
                T.writes(T_add_2[v_ax0])
                T_add_2[v_ax0] = T_multiply_3[v_ax0] + T_multiply_5[v_ax0]

    @T.prim_func(private=True)
    def batch_norm2(lv10: T.Buffer((T.int64(1), T.int64(64), T.int64(56), T.int64(56)), "float32"), B: T.Buffer((T.int64(64),), "float32"), C: T.Buffer((T.int64(64),), "float32"), D: T.Buffer((T.int64(64),), "float32"), E: T.Buffer((T.int64(64),), "float32"), T_add: T.Buffer((T.int64(1), T.int64(64), T.int64(56), T.int64(56)), "float32"), T_add_1: T.Buffer((T.int64(64),), "float32"), T_add_2: T.Buffer((T.int64(64),), "float32")):
        T.func_attr({"tir.noalias": True})
        # with T.block("root"):
        T_reshape = T.alloc_buffer((T.int64(1), T.int64(64), T.int64(1), T.int64(1)))
        T_subtract = T.alloc_buffer((T.int64(1), T.int64(64), T.int64(56), T.int64(56)))
        T_reshape_1 = T.alloc_buffer((T.int64(1), T.int64(64), T.int64(1), T.int64(1)))
        T_add_3 = T.alloc_buffer((T.int64(1), T.int64(64), T.int64(1), T.int64(1)))
        compute = T.alloc_buffer((T.int64(1), T.int64(64), T.int64(1), T.int64(1)))
        T_divide = T.alloc_buffer((T.int64(1), T.int64(64), T.int64(56), T.int64(56)))
        T_reshape_2 = T.alloc_buffer((T.int64(1), T.int64(64), T.int64(1), T.int64(1)))
        T_multiply = T.alloc_buffer((T.int64(1), T.int64(64), T.int64(56), T.int64(56)))
        T_reshape_3 = T.alloc_buffer((T.int64(1), T.int64(64), T.int64(1), T.int64(1)))
        T_multiply_1 = T.alloc_buffer((T.int64(64),))
        lv10_red = T.alloc_buffer((T.int64(64),))
        T_divide_1 = T.alloc_buffer((T.int64(64),))
        T_multiply_2 = T.alloc_buffer((T.int64(64),))
        T_multiply_3 = T.alloc_buffer((T.int64(64),))
        T_reshape_4 = T.alloc_buffer((T.int64(1), T.int64(64), T.int64(1), T.int64(1)))
        T_subtract_1 = T.alloc_buffer((T.int64(1), T.int64(64), T.int64(56), T.int64(56)))
        T_subtract_2 = T.alloc_buffer((T.int64(1), T.int64(64), T.int64(56), T.int64(56)))
        T_multiply_4 = T.alloc_buffer((T.int64(1), T.int64(64), T.int64(56), T.int64(56)))
        T_multiply_red = T.alloc_buffer((T.int64(64),))
        T_divide_2 = T.alloc_buffer((T.int64(64),))
        T_multiply_5 = T.alloc_buffer((T.int64(64),))
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(1), T.int64(64), T.int64(1), T.int64(1)):
            with T.block("T_reshape"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(D[(v_ax1 + v_ax2 + v_ax3) % T.int64(64)])
                T.writes(T_reshape[v_ax0, v_ax1, v_ax2, v_ax3])
                T_reshape[v_ax0, v_ax1, v_ax2, v_ax3] = D[(v_ax1 + v_ax2 + v_ax3) % T.int64(64)]
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(1), T.int64(64), T.int64(56), T.int64(56)):
            with T.block("T_subtract"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(lv10[v_ax0, v_ax1, v_ax2, v_ax3], T_reshape[v_ax0, v_ax1, T.int64(0), T.int64(0)])
                T.writes(T_subtract[v_ax0, v_ax1, v_ax2, v_ax3])
                T_subtract[v_ax0, v_ax1, v_ax2, v_ax3] = lv10[v_ax0, v_ax1, v_ax2, v_ax3] - T_reshape[v_ax0, v_ax1, T.int64(0), T.int64(0)]
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(1), T.int64(64), T.int64(1), T.int64(1)):
            with T.block("T_reshape_1"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(E[(v_ax1 + v_ax2 + v_ax3) % T.int64(64)])
                T.writes(T_reshape_1[v_ax0, v_ax1, v_ax2, v_ax3])
                T_reshape_1[v_ax0, v_ax1, v_ax2, v_ax3] = E[(v_ax1 + v_ax2 + v_ax3) % T.int64(64)]
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(1), T.int64(64), T.int64(1), T.int64(1)):
            with T.block("T_add"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(T_reshape_1[v_ax0, v_ax1, v_ax2, v_ax3])
                T.writes(T_add_3[v_ax0, v_ax1, v_ax2, v_ax3])
                T_add_3[v_ax0, v_ax1, v_ax2, v_ax3] = T_reshape_1[v_ax0, v_ax1, v_ax2, v_ax3] + T.float32(9.9999997473787516e-06)
        for i0, i1, i2, i3 in T.grid(T.int64(1), T.int64(64), T.int64(1), T.int64(1)):
            with T.block("compute"):
                v_i0, v_i1, v_i2, v_i3 = T.axis.remap("SSSS", [i0, i1, i2, i3])
                T.reads(T_add_3[v_i0, v_i1, v_i2, v_i3])
                T.writes(compute[v_i0, v_i1, v_i2, v_i3])
                compute[v_i0, v_i1, v_i2, v_i3] = T.sqrt(T_add_3[v_i0, v_i1, v_i2, v_i3])
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(1), T.int64(64), T.int64(56), T.int64(56)):
            with T.block("T_divide"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(T_subtract[v_ax0, v_ax1, v_ax2, v_ax3], compute[v_ax0, v_ax1, T.int64(0), T.int64(0)])
                T.writes(T_divide[v_ax0, v_ax1, v_ax2, v_ax3])
                T_divide[v_ax0, v_ax1, v_ax2, v_ax3] = T_subtract[v_ax0, v_ax1, v_ax2, v_ax3] / compute[v_ax0, v_ax1, T.int64(0), T.int64(0)]
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(1), T.int64(64), T.int64(1), T.int64(1)):
            with T.block("T_reshape_2"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(B[(v_ax1 + v_ax2 + v_ax3) % T.int64(64)])
                T.writes(T_reshape_2[v_ax0, v_ax1, v_ax2, v_ax3])
                T_reshape_2[v_ax0, v_ax1, v_ax2, v_ax3] = B[(v_ax1 + v_ax2 + v_ax3) % T.int64(64)]
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(1), T.int64(64), T.int64(56), T.int64(56)):
            with T.block("T_multiply"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(T_divide[v_ax0, v_ax1, v_ax2, v_ax3], T_reshape_2[v_ax0, v_ax1, T.int64(0), T.int64(0)])
                T.writes(T_multiply[v_ax0, v_ax1, v_ax2, v_ax3])
                T_multiply[v_ax0, v_ax1, v_ax2, v_ax3] = T_divide[v_ax0, v_ax1, v_ax2, v_ax3] * T_reshape_2[v_ax0, v_ax1, T.int64(0), T.int64(0)]
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(1), T.int64(64), T.int64(1), T.int64(1)):
            with T.block("T_reshape_3"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(C[(v_ax1 + v_ax2 + v_ax3) % T.int64(64)])
                T.writes(T_reshape_3[v_ax0, v_ax1, v_ax2, v_ax3])
                T_reshape_3[v_ax0, v_ax1, v_ax2, v_ax3] = C[(v_ax1 + v_ax2 + v_ax3) % T.int64(64)]
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(1), T.int64(64), T.int64(56), T.int64(56)):
            with T.block("T_add_1"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(T_multiply[v_ax0, v_ax1, v_ax2, v_ax3], T_reshape_3[v_ax0, v_ax1, T.int64(0), T.int64(0)])
                T.writes(T_add[v_ax0, v_ax1, v_ax2, v_ax3])
                T_add[v_ax0, v_ax1, v_ax2, v_ax3] = T_multiply[v_ax0, v_ax1, v_ax2, v_ax3] + T_reshape_3[v_ax0, v_ax1, T.int64(0), T.int64(0)]
        for ax0 in range(T.int64(64)):
            with T.block("T_multiply_1"):
                v_ax0 = T.axis.spatial(T.int64(64), ax0)
                T.reads(D[v_ax0])
                T.writes(T_multiply_1[v_ax0])
                T_multiply_1[v_ax0] = T.float32(0.90000000000000002) * D[v_ax0]
        for ax0, k0, k2, k3 in T.grid(T.int64(64), T.int64(1), T.int64(56), T.int64(56)):
            with T.block("lv10_red"):
                v_ax0, v_k0, v_k2, v_k3 = T.axis.remap("SRRR", [ax0, k0, k2, k3])
                T.reads(lv10[v_k0, v_ax0, v_k2, v_k3])
                T.writes(lv10_red[v_ax0])
                with T.init():
                    lv10_red[v_ax0] = T.float32(0.0)
                lv10_red[v_ax0] = lv10_red[v_ax0] + lv10[v_k0, v_ax0, v_k2, v_k3]
        for ax0 in range(T.int64(64)):
            with T.block("T_divide_1"):
                v_ax0 = T.axis.spatial(T.int64(64), ax0)
                T.reads(lv10_red[v_ax0])
                T.writes(T_divide_1[v_ax0])
                T_divide_1[v_ax0] = lv10_red[v_ax0] * T.float32(0.00031887755102040814)
        for ax0 in range(T.int64(64)):
            with T.block("T_multiply_2"):
                v_ax0 = T.axis.spatial(T.int64(64), ax0)
                T.reads(T_divide_1[v_ax0])
                T.writes(T_multiply_2[v_ax0])
                T_multiply_2[v_ax0] = T.float32(0.10000000000000001) * T_divide_1[v_ax0]
        for ax0 in range(T.int64(64)):
            with T.block("T_add_2"):
                v_ax0 = T.axis.spatial(T.int64(64), ax0)
                T.reads(T_multiply_1[v_ax0], T_multiply_2[v_ax0])
                T.writes(T_add_1[v_ax0])
                T_add_1[v_ax0] = T_multiply_1[v_ax0] + T_multiply_2[v_ax0]
        for ax0 in range(T.int64(64)):
            with T.block("T_multiply_3"):
                v_ax0 = T.axis.spatial(T.int64(64), ax0)
                T.reads(E[v_ax0])
                T.writes(T_multiply_3[v_ax0])
                T_multiply_3[v_ax0] = T.float32(0.90000000000000002) * E[v_ax0]
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(1), T.int64(64), T.int64(1), T.int64(1)):
            with T.block("T_reshape_4"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(T_divide_1[(v_ax1 + v_ax2 + v_ax3) % T.int64(64)])
                T.writes(T_reshape_4[v_ax0, v_ax1, v_ax2, v_ax3])
                T_reshape_4[v_ax0, v_ax1, v_ax2, v_ax3] = T_divide_1[(v_ax1 + v_ax2 + v_ax3) % T.int64(64)]
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(1), T.int64(64), T.int64(56), T.int64(56)):
            with T.block("T_subtract_1"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(lv10[v_ax0, v_ax1, v_ax2, v_ax3], T_reshape_4[v_ax0, v_ax1, T.int64(0), T.int64(0)])
                T.writes(T_subtract_1[v_ax0, v_ax1, v_ax2, v_ax3])
                T_subtract_1[v_ax0, v_ax1, v_ax2, v_ax3] = lv10[v_ax0, v_ax1, v_ax2, v_ax3] - T_reshape_4[v_ax0, v_ax1, T.int64(0), T.int64(0)]
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(1), T.int64(64), T.int64(56), T.int64(56)):
            with T.block("T_subtract_2"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(lv10[v_ax0, v_ax1, v_ax2, v_ax3], T_reshape_4[v_ax0, v_ax1, T.int64(0), T.int64(0)])
                T.writes(T_subtract_2[v_ax0, v_ax1, v_ax2, v_ax3])
                T_subtract_2[v_ax0, v_ax1, v_ax2, v_ax3] = lv10[v_ax0, v_ax1, v_ax2, v_ax3] - T_reshape_4[v_ax0, v_ax1, T.int64(0), T.int64(0)]
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(1), T.int64(64), T.int64(56), T.int64(56)):
            with T.block("T_multiply_4"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(T_subtract_1[v_ax0, v_ax1, v_ax2, v_ax3], T_subtract_2[v_ax0, v_ax1, v_ax2, v_ax3])
                T.writes(T_multiply_4[v_ax0, v_ax1, v_ax2, v_ax3])
                T_multiply_4[v_ax0, v_ax1, v_ax2, v_ax3] = T_subtract_1[v_ax0, v_ax1, v_ax2, v_ax3] * T_subtract_2[v_ax0, v_ax1, v_ax2, v_ax3]
        for ax0, k0, k2, k3 in T.grid(T.int64(64), T.int64(1), T.int64(56), T.int64(56)):
            with T.block("T_multiply_red"):
                v_ax0, v_k0, v_k2, v_k3 = T.axis.remap("SRRR", [ax0, k0, k2, k3])
                T.reads(T_multiply_4[v_k0, v_ax0, v_k2, v_k3])
                T.writes(T_multiply_red[v_ax0])
                with T.init():
                    T_multiply_red[v_ax0] = T.float32(0.0)
                T_multiply_red[v_ax0] = T_multiply_red[v_ax0] + T_multiply_4[v_k0, v_ax0, v_k2, v_k3]
        for ax0 in range(T.int64(64)):
            with T.block("T_divide_2"):
                v_ax0 = T.axis.spatial(T.int64(64), ax0)
                T.reads(T_multiply_red[v_ax0])
                T.writes(T_divide_2[v_ax0])
                T_divide_2[v_ax0] = T_multiply_red[v_ax0] * T.float32(0.00031887755102040814)
        for ax0 in range(T.int64(64)):
            with T.block("T_multiply_5"):
                v_ax0 = T.axis.spatial(T.int64(64), ax0)
                T.reads(T_divide_2[v_ax0])
                T.writes(T_multiply_5[v_ax0])
                T_multiply_5[v_ax0] = T.float32(0.10000000000000001) * T_divide_2[v_ax0]
        for ax0 in range(T.int64(64)):
            with T.block("T_add_3"):
                v_ax0 = T.axis.spatial(T.int64(64), ax0)
                T.reads(T_multiply_3[v_ax0], T_multiply_5[v_ax0])
                T.writes(T_add_2[v_ax0])
                T_add_2[v_ax0] = T_multiply_3[v_ax0] + T_multiply_5[v_ax0]

    @T.prim_func(private=True)
    def batch_norm3(lv30: T.Buffer((T.int64(1), T.int64(256), T.int64(56), T.int64(56)), "float32"), B: T.Buffer((T.int64(256),), "float32"), C: T.Buffer((T.int64(256),), "float32"), D: T.Buffer((T.int64(256),), "float32"), E: T.Buffer((T.int64(256),), "float32"), T_add: T.Buffer((T.int64(1), T.int64(256), T.int64(56), T.int64(56)), "float32"), T_add_1: T.Buffer((T.int64(256),), "float32"), T_add_2: T.Buffer((T.int64(256),), "float32")):
        T.func_attr({"tir.noalias": True})
        # with T.block("root"):
        T_reshape = T.alloc_buffer((T.int64(1), T.int64(256), T.int64(1), T.int64(1)))
        T_subtract = T.alloc_buffer((T.int64(1), T.int64(256), T.int64(56), T.int64(56)))
        T_reshape_1 = T.alloc_buffer((T.int64(1), T.int64(256), T.int64(1), T.int64(1)))
        T_add_3 = T.alloc_buffer((T.int64(1), T.int64(256), T.int64(1), T.int64(1)))
        compute = T.alloc_buffer((T.int64(1), T.int64(256), T.int64(1), T.int64(1)))
        T_divide = T.alloc_buffer((T.int64(1), T.int64(256), T.int64(56), T.int64(56)))
        T_reshape_2 = T.alloc_buffer((T.int64(1), T.int64(256), T.int64(1), T.int64(1)))
        T_multiply = T.alloc_buffer((T.int64(1), T.int64(256), T.int64(56), T.int64(56)))
        T_reshape_3 = T.alloc_buffer((T.int64(1), T.int64(256), T.int64(1), T.int64(1)))
        T_multiply_1 = T.alloc_buffer((T.int64(256),))
        lv30_red = T.alloc_buffer((T.int64(256),))
        T_divide_1 = T.alloc_buffer((T.int64(256),))
        T_multiply_2 = T.alloc_buffer((T.int64(256),))
        T_multiply_3 = T.alloc_buffer((T.int64(256),))
        T_reshape_4 = T.alloc_buffer((T.int64(1), T.int64(256), T.int64(1), T.int64(1)))
        T_subtract_1 = T.alloc_buffer((T.int64(1), T.int64(256), T.int64(56), T.int64(56)))
        T_subtract_2 = T.alloc_buffer((T.int64(1), T.int64(256), T.int64(56), T.int64(56)))
        T_multiply_4 = T.alloc_buffer((T.int64(1), T.int64(256), T.int64(56), T.int64(56)))
        T_multiply_red = T.alloc_buffer((T.int64(256),))
        T_divide_2 = T.alloc_buffer((T.int64(256),))
        T_multiply_5 = T.alloc_buffer((T.int64(256),))
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(1), T.int64(256), T.int64(1), T.int64(1)):
            with T.block("T_reshape"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(D[(v_ax1 + v_ax2 + v_ax3) % T.int64(256)])
                T.writes(T_reshape[v_ax0, v_ax1, v_ax2, v_ax3])
                T_reshape[v_ax0, v_ax1, v_ax2, v_ax3] = D[(v_ax1 + v_ax2 + v_ax3) % T.int64(256)]
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(1), T.int64(256), T.int64(56), T.int64(56)):
            with T.block("T_subtract"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(lv30[v_ax0, v_ax1, v_ax2, v_ax3], T_reshape[v_ax0, v_ax1, T.int64(0), T.int64(0)])
                T.writes(T_subtract[v_ax0, v_ax1, v_ax2, v_ax3])
                T_subtract[v_ax0, v_ax1, v_ax2, v_ax3] = lv30[v_ax0, v_ax1, v_ax2, v_ax3] - T_reshape[v_ax0, v_ax1, T.int64(0), T.int64(0)]
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(1), T.int64(256), T.int64(1), T.int64(1)):
            with T.block("T_reshape_1"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(E[(v_ax1 + v_ax2 + v_ax3) % T.int64(256)])
                T.writes(T_reshape_1[v_ax0, v_ax1, v_ax2, v_ax3])
                T_reshape_1[v_ax0, v_ax1, v_ax2, v_ax3] = E[(v_ax1 + v_ax2 + v_ax3) % T.int64(256)]
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(1), T.int64(256), T.int64(1), T.int64(1)):
            with T.block("T_add"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(T_reshape_1[v_ax0, v_ax1, v_ax2, v_ax3])
                T.writes(T_add_3[v_ax0, v_ax1, v_ax2, v_ax3])
                T_add_3[v_ax0, v_ax1, v_ax2, v_ax3] = T_reshape_1[v_ax0, v_ax1, v_ax2, v_ax3] + T.float32(9.9999997473787516e-06)
        for i0, i1, i2, i3 in T.grid(T.int64(1), T.int64(256), T.int64(1), T.int64(1)):
            with T.block("compute"):
                v_i0, v_i1, v_i2, v_i3 = T.axis.remap("SSSS", [i0, i1, i2, i3])
                T.reads(T_add_3[v_i0, v_i1, v_i2, v_i3])
                T.writes(compute[v_i0, v_i1, v_i2, v_i3])
                compute[v_i0, v_i1, v_i2, v_i3] = T.sqrt(T_add_3[v_i0, v_i1, v_i2, v_i3])
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(1), T.int64(256), T.int64(56), T.int64(56)):
            with T.block("T_divide"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(T_subtract[v_ax0, v_ax1, v_ax2, v_ax3], compute[v_ax0, v_ax1, T.int64(0), T.int64(0)])
                T.writes(T_divide[v_ax0, v_ax1, v_ax2, v_ax3])
                T_divide[v_ax0, v_ax1, v_ax2, v_ax3] = T_subtract[v_ax0, v_ax1, v_ax2, v_ax3] / compute[v_ax0, v_ax1, T.int64(0), T.int64(0)]
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(1), T.int64(256), T.int64(1), T.int64(1)):
            with T.block("T_reshape_2"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(B[(v_ax1 + v_ax2 + v_ax3) % T.int64(256)])
                T.writes(T_reshape_2[v_ax0, v_ax1, v_ax2, v_ax3])
                T_reshape_2[v_ax0, v_ax1, v_ax2, v_ax3] = B[(v_ax1 + v_ax2 + v_ax3) % T.int64(256)]
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(1), T.int64(256), T.int64(56), T.int64(56)):
            with T.block("T_multiply"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(T_divide[v_ax0, v_ax1, v_ax2, v_ax3], T_reshape_2[v_ax0, v_ax1, T.int64(0), T.int64(0)])
                T.writes(T_multiply[v_ax0, v_ax1, v_ax2, v_ax3])
                T_multiply[v_ax0, v_ax1, v_ax2, v_ax3] = T_divide[v_ax0, v_ax1, v_ax2, v_ax3] * T_reshape_2[v_ax0, v_ax1, T.int64(0), T.int64(0)]
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(1), T.int64(256), T.int64(1), T.int64(1)):
            with T.block("T_reshape_3"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(C[(v_ax1 + v_ax2 + v_ax3) % T.int64(256)])
                T.writes(T_reshape_3[v_ax0, v_ax1, v_ax2, v_ax3])
                T_reshape_3[v_ax0, v_ax1, v_ax2, v_ax3] = C[(v_ax1 + v_ax2 + v_ax3) % T.int64(256)]
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(1), T.int64(256), T.int64(56), T.int64(56)):
            with T.block("T_add_1"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(T_multiply[v_ax0, v_ax1, v_ax2, v_ax3], T_reshape_3[v_ax0, v_ax1, T.int64(0), T.int64(0)])
                T.writes(T_add[v_ax0, v_ax1, v_ax2, v_ax3])
                T_add[v_ax0, v_ax1, v_ax2, v_ax3] = T_multiply[v_ax0, v_ax1, v_ax2, v_ax3] + T_reshape_3[v_ax0, v_ax1, T.int64(0), T.int64(0)]
        for ax0 in range(T.int64(256)):
            with T.block("T_multiply_1"):
                v_ax0 = T.axis.spatial(T.int64(256), ax0)
                T.reads(D[v_ax0])
                T.writes(T_multiply_1[v_ax0])
                T_multiply_1[v_ax0] = T.float32(0.90000000000000002) * D[v_ax0]
        for ax0, k0, k2, k3 in T.grid(T.int64(256), T.int64(1), T.int64(56), T.int64(56)):
            with T.block("lv30_red"):
                v_ax0, v_k0, v_k2, v_k3 = T.axis.remap("SRRR", [ax0, k0, k2, k3])
                T.reads(lv30[v_k0, v_ax0, v_k2, v_k3])
                T.writes(lv30_red[v_ax0])
                with T.init():
                    lv30_red[v_ax0] = T.float32(0.0)
                lv30_red[v_ax0] = lv30_red[v_ax0] + lv30[v_k0, v_ax0, v_k2, v_k3]
        for ax0 in range(T.int64(256)):
            with T.block("T_divide_1"):
                v_ax0 = T.axis.spatial(T.int64(256), ax0)
                T.reads(lv30_red[v_ax0])
                T.writes(T_divide_1[v_ax0])
                T_divide_1[v_ax0] = lv30_red[v_ax0] * T.float32(0.00031887755102040814)
        for ax0 in range(T.int64(256)):
            with T.block("T_multiply_2"):
                v_ax0 = T.axis.spatial(T.int64(256), ax0)
                T.reads(T_divide_1[v_ax0])
                T.writes(T_multiply_2[v_ax0])
                T_multiply_2[v_ax0] = T.float32(0.10000000000000001) * T_divide_1[v_ax0]
        for ax0 in range(T.int64(256)):
            with T.block("T_add_2"):
                v_ax0 = T.axis.spatial(T.int64(256), ax0)
                T.reads(T_multiply_1[v_ax0], T_multiply_2[v_ax0])
                T.writes(T_add_1[v_ax0])
                T_add_1[v_ax0] = T_multiply_1[v_ax0] + T_multiply_2[v_ax0]
        for ax0 in range(T.int64(256)):
            with T.block("T_multiply_3"):
                v_ax0 = T.axis.spatial(T.int64(256), ax0)
                T.reads(E[v_ax0])
                T.writes(T_multiply_3[v_ax0])
                T_multiply_3[v_ax0] = T.float32(0.90000000000000002) * E[v_ax0]
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(1), T.int64(256), T.int64(1), T.int64(1)):
            with T.block("T_reshape_4"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(T_divide_1[(v_ax1 + v_ax2 + v_ax3) % T.int64(256)])
                T.writes(T_reshape_4[v_ax0, v_ax1, v_ax2, v_ax3])
                T_reshape_4[v_ax0, v_ax1, v_ax2, v_ax3] = T_divide_1[(v_ax1 + v_ax2 + v_ax3) % T.int64(256)]
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(1), T.int64(256), T.int64(56), T.int64(56)):
            with T.block("T_subtract_1"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(lv30[v_ax0, v_ax1, v_ax2, v_ax3], T_reshape_4[v_ax0, v_ax1, T.int64(0), T.int64(0)])
                T.writes(T_subtract_1[v_ax0, v_ax1, v_ax2, v_ax3])
                T_subtract_1[v_ax0, v_ax1, v_ax2, v_ax3] = lv30[v_ax0, v_ax1, v_ax2, v_ax3] - T_reshape_4[v_ax0, v_ax1, T.int64(0), T.int64(0)]
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(1), T.int64(256), T.int64(56), T.int64(56)):
            with T.block("T_subtract_2"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(lv30[v_ax0, v_ax1, v_ax2, v_ax3], T_reshape_4[v_ax0, v_ax1, T.int64(0), T.int64(0)])
                T.writes(T_subtract_2[v_ax0, v_ax1, v_ax2, v_ax3])
                T_subtract_2[v_ax0, v_ax1, v_ax2, v_ax3] = lv30[v_ax0, v_ax1, v_ax2, v_ax3] - T_reshape_4[v_ax0, v_ax1, T.int64(0), T.int64(0)]
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(1), T.int64(256), T.int64(56), T.int64(56)):
            with T.block("T_multiply_4"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(T_subtract_1[v_ax0, v_ax1, v_ax2, v_ax3], T_subtract_2[v_ax0, v_ax1, v_ax2, v_ax3])
                T.writes(T_multiply_4[v_ax0, v_ax1, v_ax2, v_ax3])
                T_multiply_4[v_ax0, v_ax1, v_ax2, v_ax3] = T_subtract_1[v_ax0, v_ax1, v_ax2, v_ax3] * T_subtract_2[v_ax0, v_ax1, v_ax2, v_ax3]
        for ax0, k0, k2, k3 in T.grid(T.int64(256), T.int64(1), T.int64(56), T.int64(56)):
            with T.block("T_multiply_red"):
                v_ax0, v_k0, v_k2, v_k3 = T.axis.remap("SRRR", [ax0, k0, k2, k3])
                T.reads(T_multiply_4[v_k0, v_ax0, v_k2, v_k3])
                T.writes(T_multiply_red[v_ax0])
                with T.init():
                    T_multiply_red[v_ax0] = T.float32(0.0)
                T_multiply_red[v_ax0] = T_multiply_red[v_ax0] + T_multiply_4[v_k0, v_ax0, v_k2, v_k3]
        for ax0 in range(T.int64(256)):
            with T.block("T_divide_2"):
                v_ax0 = T.axis.spatial(T.int64(256), ax0)
                T.reads(T_multiply_red[v_ax0])
                T.writes(T_divide_2[v_ax0])
                T_divide_2[v_ax0] = T_multiply_red[v_ax0] * T.float32(0.00031887755102040814)
        for ax0 in range(T.int64(256)):
            with T.block("T_multiply_5"):
                v_ax0 = T.axis.spatial(T.int64(256), ax0)
                T.reads(T_divide_2[v_ax0])
                T.writes(T_multiply_5[v_ax0])
                T_multiply_5[v_ax0] = T.float32(0.10000000000000001) * T_divide_2[v_ax0]
        for ax0 in range(T.int64(256)):
            with T.block("T_add_3"):
                v_ax0 = T.axis.spatial(T.int64(256), ax0)
                T.reads(T_multiply_3[v_ax0], T_multiply_5[v_ax0])
                T.writes(T_add_2[v_ax0])
                T_add_2[v_ax0] = T_multiply_3[v_ax0] + T_multiply_5[v_ax0]

    @T.prim_func(private=True)
    def batch_norm4(lv74: T.Buffer((T.int64(1), T.int64(128), T.int64(56), T.int64(56)), "float32"), B: T.Buffer((T.int64(128),), "float32"), C: T.Buffer((T.int64(128),), "float32"), D: T.Buffer((T.int64(128),), "float32"), E: T.Buffer((T.int64(128),), "float32"), T_add: T.Buffer((T.int64(1), T.int64(128), T.int64(56), T.int64(56)), "float32"), T_add_1: T.Buffer((T.int64(128),), "float32"), T_add_2: T.Buffer((T.int64(128),), "float32")):
        T.func_attr({"tir.noalias": True})
        # with T.block("root"):
        T_reshape = T.alloc_buffer((T.int64(1), T.int64(128), T.int64(1), T.int64(1)))
        T_subtract = T.alloc_buffer((T.int64(1), T.int64(128), T.int64(56), T.int64(56)))
        T_reshape_1 = T.alloc_buffer((T.int64(1), T.int64(128), T.int64(1), T.int64(1)))
        T_add_3 = T.alloc_buffer((T.int64(1), T.int64(128), T.int64(1), T.int64(1)))
        compute = T.alloc_buffer((T.int64(1), T.int64(128), T.int64(1), T.int64(1)))
        T_divide = T.alloc_buffer((T.int64(1), T.int64(128), T.int64(56), T.int64(56)))
        T_reshape_2 = T.alloc_buffer((T.int64(1), T.int64(128), T.int64(1), T.int64(1)))
        T_multiply = T.alloc_buffer((T.int64(1), T.int64(128), T.int64(56), T.int64(56)))
        T_reshape_3 = T.alloc_buffer((T.int64(1), T.int64(128), T.int64(1), T.int64(1)))
        T_multiply_1 = T.alloc_buffer((T.int64(128),))
        lv74_red = T.alloc_buffer((T.int64(128),))
        T_divide_1 = T.alloc_buffer((T.int64(128),))
        T_multiply_2 = T.alloc_buffer((T.int64(128),))
        T_multiply_3 = T.alloc_buffer((T.int64(128),))
        T_reshape_4 = T.alloc_buffer((T.int64(1), T.int64(128), T.int64(1), T.int64(1)))
        T_subtract_1 = T.alloc_buffer((T.int64(1), T.int64(128), T.int64(56), T.int64(56)))
        T_subtract_2 = T.alloc_buffer((T.int64(1), T.int64(128), T.int64(56), T.int64(56)))
        T_multiply_4 = T.alloc_buffer((T.int64(1), T.int64(128), T.int64(56), T.int64(56)))
        T_multiply_red = T.alloc_buffer((T.int64(128),))
        T_divide_2 = T.alloc_buffer((T.int64(128),))
        T_multiply_5 = T.alloc_buffer((T.int64(128),))
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(1), T.int64(128), T.int64(1), T.int64(1)):
            with T.block("T_reshape"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(D[(v_ax1 + v_ax2 + v_ax3) % T.int64(128)])
                T.writes(T_reshape[v_ax0, v_ax1, v_ax2, v_ax3])
                T_reshape[v_ax0, v_ax1, v_ax2, v_ax3] = D[(v_ax1 + v_ax2 + v_ax3) % T.int64(128)]
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(1), T.int64(128), T.int64(56), T.int64(56)):
            with T.block("T_subtract"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(lv74[v_ax0, v_ax1, v_ax2, v_ax3], T_reshape[v_ax0, v_ax1, T.int64(0), T.int64(0)])
                T.writes(T_subtract[v_ax0, v_ax1, v_ax2, v_ax3])
                T_subtract[v_ax0, v_ax1, v_ax2, v_ax3] = lv74[v_ax0, v_ax1, v_ax2, v_ax3] - T_reshape[v_ax0, v_ax1, T.int64(0), T.int64(0)]
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(1), T.int64(128), T.int64(1), T.int64(1)):
            with T.block("T_reshape_1"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(E[(v_ax1 + v_ax2 + v_ax3) % T.int64(128)])
                T.writes(T_reshape_1[v_ax0, v_ax1, v_ax2, v_ax3])
                T_reshape_1[v_ax0, v_ax1, v_ax2, v_ax3] = E[(v_ax1 + v_ax2 + v_ax3) % T.int64(128)]
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(1), T.int64(128), T.int64(1), T.int64(1)):
            with T.block("T_add"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(T_reshape_1[v_ax0, v_ax1, v_ax2, v_ax3])
                T.writes(T_add_3[v_ax0, v_ax1, v_ax2, v_ax3])
                T_add_3[v_ax0, v_ax1, v_ax2, v_ax3] = T_reshape_1[v_ax0, v_ax1, v_ax2, v_ax3] + T.float32(9.9999997473787516e-06)
        for i0, i1, i2, i3 in T.grid(T.int64(1), T.int64(128), T.int64(1), T.int64(1)):
            with T.block("compute"):
                v_i0, v_i1, v_i2, v_i3 = T.axis.remap("SSSS", [i0, i1, i2, i3])
                T.reads(T_add_3[v_i0, v_i1, v_i2, v_i3])
                T.writes(compute[v_i0, v_i1, v_i2, v_i3])
                compute[v_i0, v_i1, v_i2, v_i3] = T.sqrt(T_add_3[v_i0, v_i1, v_i2, v_i3])
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(1), T.int64(128), T.int64(56), T.int64(56)):
            with T.block("T_divide"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(T_subtract[v_ax0, v_ax1, v_ax2, v_ax3], compute[v_ax0, v_ax1, T.int64(0), T.int64(0)])
                T.writes(T_divide[v_ax0, v_ax1, v_ax2, v_ax3])
                T_divide[v_ax0, v_ax1, v_ax2, v_ax3] = T_subtract[v_ax0, v_ax1, v_ax2, v_ax3] / compute[v_ax0, v_ax1, T.int64(0), T.int64(0)]
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(1), T.int64(128), T.int64(1), T.int64(1)):
            with T.block("T_reshape_2"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(B[(v_ax1 + v_ax2 + v_ax3) % T.int64(128)])
                T.writes(T_reshape_2[v_ax0, v_ax1, v_ax2, v_ax3])
                T_reshape_2[v_ax0, v_ax1, v_ax2, v_ax3] = B[(v_ax1 + v_ax2 + v_ax3) % T.int64(128)]
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(1), T.int64(128), T.int64(56), T.int64(56)):
            with T.block("T_multiply"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(T_divide[v_ax0, v_ax1, v_ax2, v_ax3], T_reshape_2[v_ax0, v_ax1, T.int64(0), T.int64(0)])
                T.writes(T_multiply[v_ax0, v_ax1, v_ax2, v_ax3])
                T_multiply[v_ax0, v_ax1, v_ax2, v_ax3] = T_divide[v_ax0, v_ax1, v_ax2, v_ax3] * T_reshape_2[v_ax0, v_ax1, T.int64(0), T.int64(0)]
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(1), T.int64(128), T.int64(1), T.int64(1)):
            with T.block("T_reshape_3"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(C[(v_ax1 + v_ax2 + v_ax3) % T.int64(128)])
                T.writes(T_reshape_3[v_ax0, v_ax1, v_ax2, v_ax3])
                T_reshape_3[v_ax0, v_ax1, v_ax2, v_ax3] = C[(v_ax1 + v_ax2 + v_ax3) % T.int64(128)]
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(1), T.int64(128), T.int64(56), T.int64(56)):
            with T.block("T_add_1"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(T_multiply[v_ax0, v_ax1, v_ax2, v_ax3], T_reshape_3[v_ax0, v_ax1, T.int64(0), T.int64(0)])
                T.writes(T_add[v_ax0, v_ax1, v_ax2, v_ax3])
                T_add[v_ax0, v_ax1, v_ax2, v_ax3] = T_multiply[v_ax0, v_ax1, v_ax2, v_ax3] + T_reshape_3[v_ax0, v_ax1, T.int64(0), T.int64(0)]
        for ax0 in range(T.int64(128)):
            with T.block("T_multiply_1"):
                v_ax0 = T.axis.spatial(T.int64(128), ax0)
                T.reads(D[v_ax0])
                T.writes(T_multiply_1[v_ax0])
                T_multiply_1[v_ax0] = T.float32(0.90000000000000002) * D[v_ax0]
        for ax0, k0, k2, k3 in T.grid(T.int64(128), T.int64(1), T.int64(56), T.int64(56)):
            with T.block("lv74_red"):
                v_ax0, v_k0, v_k2, v_k3 = T.axis.remap("SRRR", [ax0, k0, k2, k3])
                T.reads(lv74[v_k0, v_ax0, v_k2, v_k3])
                T.writes(lv74_red[v_ax0])
                with T.init():
                    lv74_red[v_ax0] = T.float32(0.0)
                lv74_red[v_ax0] = lv74_red[v_ax0] + lv74[v_k0, v_ax0, v_k2, v_k3]
        for ax0 in range(T.int64(128)):
            with T.block("T_divide_1"):
                v_ax0 = T.axis.spatial(T.int64(128), ax0)
                T.reads(lv74_red[v_ax0])
                T.writes(T_divide_1[v_ax0])
                T_divide_1[v_ax0] = lv74_red[v_ax0] * T.float32(0.00031887755102040814)
        for ax0 in range(T.int64(128)):
            with T.block("T_multiply_2"):
                v_ax0 = T.axis.spatial(T.int64(128), ax0)
                T.reads(T_divide_1[v_ax0])
                T.writes(T_multiply_2[v_ax0])
                T_multiply_2[v_ax0] = T.float32(0.10000000000000001) * T_divide_1[v_ax0]
        for ax0 in range(T.int64(128)):
            with T.block("T_add_2"):
                v_ax0 = T.axis.spatial(T.int64(128), ax0)
                T.reads(T_multiply_1[v_ax0], T_multiply_2[v_ax0])
                T.writes(T_add_1[v_ax0])
                T_add_1[v_ax0] = T_multiply_1[v_ax0] + T_multiply_2[v_ax0]
        for ax0 in range(T.int64(128)):
            with T.block("T_multiply_3"):
                v_ax0 = T.axis.spatial(T.int64(128), ax0)
                T.reads(E[v_ax0])
                T.writes(T_multiply_3[v_ax0])
                T_multiply_3[v_ax0] = T.float32(0.90000000000000002) * E[v_ax0]
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(1), T.int64(128), T.int64(1), T.int64(1)):
            with T.block("T_reshape_4"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(T_divide_1[(v_ax1 + v_ax2 + v_ax3) % T.int64(128)])
                T.writes(T_reshape_4[v_ax0, v_ax1, v_ax2, v_ax3])
                T_reshape_4[v_ax0, v_ax1, v_ax2, v_ax3] = T_divide_1[(v_ax1 + v_ax2 + v_ax3) % T.int64(128)]
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(1), T.int64(128), T.int64(56), T.int64(56)):
            with T.block("T_subtract_1"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(lv74[v_ax0, v_ax1, v_ax2, v_ax3], T_reshape_4[v_ax0, v_ax1, T.int64(0), T.int64(0)])
                T.writes(T_subtract_1[v_ax0, v_ax1, v_ax2, v_ax3])
                T_subtract_1[v_ax0, v_ax1, v_ax2, v_ax3] = lv74[v_ax0, v_ax1, v_ax2, v_ax3] - T_reshape_4[v_ax0, v_ax1, T.int64(0), T.int64(0)]
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(1), T.int64(128), T.int64(56), T.int64(56)):
            with T.block("T_subtract_2"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(lv74[v_ax0, v_ax1, v_ax2, v_ax3], T_reshape_4[v_ax0, v_ax1, T.int64(0), T.int64(0)])
                T.writes(T_subtract_2[v_ax0, v_ax1, v_ax2, v_ax3])
                T_subtract_2[v_ax0, v_ax1, v_ax2, v_ax3] = lv74[v_ax0, v_ax1, v_ax2, v_ax3] - T_reshape_4[v_ax0, v_ax1, T.int64(0), T.int64(0)]
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(1), T.int64(128), T.int64(56), T.int64(56)):
            with T.block("T_multiply_4"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(T_subtract_1[v_ax0, v_ax1, v_ax2, v_ax3], T_subtract_2[v_ax0, v_ax1, v_ax2, v_ax3])
                T.writes(T_multiply_4[v_ax0, v_ax1, v_ax2, v_ax3])
                T_multiply_4[v_ax0, v_ax1, v_ax2, v_ax3] = T_subtract_1[v_ax0, v_ax1, v_ax2, v_ax3] * T_subtract_2[v_ax0, v_ax1, v_ax2, v_ax3]
        for ax0, k0, k2, k3 in T.grid(T.int64(128), T.int64(1), T.int64(56), T.int64(56)):
            with T.block("T_multiply_red"):
                v_ax0, v_k0, v_k2, v_k3 = T.axis.remap("SRRR", [ax0, k0, k2, k3])
                T.reads(T_multiply_4[v_k0, v_ax0, v_k2, v_k3])
                T.writes(T_multiply_red[v_ax0])
                with T.init():
                    T_multiply_red[v_ax0] = T.float32(0.0)
                T_multiply_red[v_ax0] = T_multiply_red[v_ax0] + T_multiply_4[v_k0, v_ax0, v_k2, v_k3]
        for ax0 in range(T.int64(128)):
            with T.block("T_divide_2"):
                v_ax0 = T.axis.spatial(T.int64(128), ax0)
                T.reads(T_multiply_red[v_ax0])
                T.writes(T_divide_2[v_ax0])
                T_divide_2[v_ax0] = T_multiply_red[v_ax0] * T.float32(0.00031887755102040814)
        for ax0 in range(T.int64(128)):
            with T.block("T_multiply_5"):
                v_ax0 = T.axis.spatial(T.int64(128), ax0)
                T.reads(T_divide_2[v_ax0])
                T.writes(T_multiply_5[v_ax0])
                T_multiply_5[v_ax0] = T.float32(0.10000000000000001) * T_divide_2[v_ax0]
        for ax0 in range(T.int64(128)):
            with T.block("T_add_3"):
                v_ax0 = T.axis.spatial(T.int64(128), ax0)
                T.reads(T_multiply_3[v_ax0], T_multiply_5[v_ax0])
                T.writes(T_add_2[v_ax0])
                T_add_2[v_ax0] = T_multiply_3[v_ax0] + T_multiply_5[v_ax0]

    @T.prim_func(private=True)
    def batch_norm5(lv80: T.Buffer((T.int64(1), T.int64(128), T.int64(28), T.int64(28)), "float32"), B: T.Buffer((T.int64(128),), "float32"), C: T.Buffer((T.int64(128),), "float32"), D: T.Buffer((T.int64(128),), "float32"), E: T.Buffer((T.int64(128),), "float32"), T_add: T.Buffer((T.int64(1), T.int64(128), T.int64(28), T.int64(28)), "float32"), T_add_1: T.Buffer((T.int64(128),), "float32"), T_add_2: T.Buffer((T.int64(128),), "float32")):
        T.func_attr({"tir.noalias": True})
        # with T.block("root"):
        T_reshape = T.alloc_buffer((T.int64(1), T.int64(128), T.int64(1), T.int64(1)))
        T_subtract = T.alloc_buffer((T.int64(1), T.int64(128), T.int64(28), T.int64(28)))
        T_reshape_1 = T.alloc_buffer((T.int64(1), T.int64(128), T.int64(1), T.int64(1)))
        T_add_3 = T.alloc_buffer((T.int64(1), T.int64(128), T.int64(1), T.int64(1)))
        compute = T.alloc_buffer((T.int64(1), T.int64(128), T.int64(1), T.int64(1)))
        T_divide = T.alloc_buffer((T.int64(1), T.int64(128), T.int64(28), T.int64(28)))
        T_reshape_2 = T.alloc_buffer((T.int64(1), T.int64(128), T.int64(1), T.int64(1)))
        T_multiply = T.alloc_buffer((T.int64(1), T.int64(128), T.int64(28), T.int64(28)))
        T_reshape_3 = T.alloc_buffer((T.int64(1), T.int64(128), T.int64(1), T.int64(1)))
        T_multiply_1 = T.alloc_buffer((T.int64(128),))
        lv80_red = T.alloc_buffer((T.int64(128),))
        T_divide_1 = T.alloc_buffer((T.int64(128),))
        T_multiply_2 = T.alloc_buffer((T.int64(128),))
        T_multiply_3 = T.alloc_buffer((T.int64(128),))
        T_reshape_4 = T.alloc_buffer((T.int64(1), T.int64(128), T.int64(1), T.int64(1)))
        T_subtract_1 = T.alloc_buffer((T.int64(1), T.int64(128), T.int64(28), T.int64(28)))
        T_subtract_2 = T.alloc_buffer((T.int64(1), T.int64(128), T.int64(28), T.int64(28)))
        T_multiply_4 = T.alloc_buffer((T.int64(1), T.int64(128), T.int64(28), T.int64(28)))
        T_multiply_red = T.alloc_buffer((T.int64(128),))
        T_divide_2 = T.alloc_buffer((T.int64(128),))
        T_multiply_5 = T.alloc_buffer((T.int64(128),))
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(1), T.int64(128), T.int64(1), T.int64(1)):
            with T.block("T_reshape"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(D[(v_ax1 + v_ax2 + v_ax3) % T.int64(128)])
                T.writes(T_reshape[v_ax0, v_ax1, v_ax2, v_ax3])
                T_reshape[v_ax0, v_ax1, v_ax2, v_ax3] = D[(v_ax1 + v_ax2 + v_ax3) % T.int64(128)]
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(1), T.int64(128), T.int64(28), T.int64(28)):
            with T.block("T_subtract"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(lv80[v_ax0, v_ax1, v_ax2, v_ax3], T_reshape[v_ax0, v_ax1, T.int64(0), T.int64(0)])
                T.writes(T_subtract[v_ax0, v_ax1, v_ax2, v_ax3])
                T_subtract[v_ax0, v_ax1, v_ax2, v_ax3] = lv80[v_ax0, v_ax1, v_ax2, v_ax3] - T_reshape[v_ax0, v_ax1, T.int64(0), T.int64(0)]
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(1), T.int64(128), T.int64(1), T.int64(1)):
            with T.block("T_reshape_1"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(E[(v_ax1 + v_ax2 + v_ax3) % T.int64(128)])
                T.writes(T_reshape_1[v_ax0, v_ax1, v_ax2, v_ax3])
                T_reshape_1[v_ax0, v_ax1, v_ax2, v_ax3] = E[(v_ax1 + v_ax2 + v_ax3) % T.int64(128)]
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(1), T.int64(128), T.int64(1), T.int64(1)):
            with T.block("T_add"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(T_reshape_1[v_ax0, v_ax1, v_ax2, v_ax3])
                T.writes(T_add_3[v_ax0, v_ax1, v_ax2, v_ax3])
                T_add_3[v_ax0, v_ax1, v_ax2, v_ax3] = T_reshape_1[v_ax0, v_ax1, v_ax2, v_ax3] + T.float32(9.9999997473787516e-06)
        for i0, i1, i2, i3 in T.grid(T.int64(1), T.int64(128), T.int64(1), T.int64(1)):
            with T.block("compute"):
                v_i0, v_i1, v_i2, v_i3 = T.axis.remap("SSSS", [i0, i1, i2, i3])
                T.reads(T_add_3[v_i0, v_i1, v_i2, v_i3])
                T.writes(compute[v_i0, v_i1, v_i2, v_i3])
                compute[v_i0, v_i1, v_i2, v_i3] = T.sqrt(T_add_3[v_i0, v_i1, v_i2, v_i3])
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(1), T.int64(128), T.int64(28), T.int64(28)):
            with T.block("T_divide"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(T_subtract[v_ax0, v_ax1, v_ax2, v_ax3], compute[v_ax0, v_ax1, T.int64(0), T.int64(0)])
                T.writes(T_divide[v_ax0, v_ax1, v_ax2, v_ax3])
                T_divide[v_ax0, v_ax1, v_ax2, v_ax3] = T_subtract[v_ax0, v_ax1, v_ax2, v_ax3] / compute[v_ax0, v_ax1, T.int64(0), T.int64(0)]
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(1), T.int64(128), T.int64(1), T.int64(1)):
            with T.block("T_reshape_2"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(B[(v_ax1 + v_ax2 + v_ax3) % T.int64(128)])
                T.writes(T_reshape_2[v_ax0, v_ax1, v_ax2, v_ax3])
                T_reshape_2[v_ax0, v_ax1, v_ax2, v_ax3] = B[(v_ax1 + v_ax2 + v_ax3) % T.int64(128)]
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(1), T.int64(128), T.int64(28), T.int64(28)):
            with T.block("T_multiply"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(T_divide[v_ax0, v_ax1, v_ax2, v_ax3], T_reshape_2[v_ax0, v_ax1, T.int64(0), T.int64(0)])
                T.writes(T_multiply[v_ax0, v_ax1, v_ax2, v_ax3])
                T_multiply[v_ax0, v_ax1, v_ax2, v_ax3] = T_divide[v_ax0, v_ax1, v_ax2, v_ax3] * T_reshape_2[v_ax0, v_ax1, T.int64(0), T.int64(0)]
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(1), T.int64(128), T.int64(1), T.int64(1)):
            with T.block("T_reshape_3"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(C[(v_ax1 + v_ax2 + v_ax3) % T.int64(128)])
                T.writes(T_reshape_3[v_ax0, v_ax1, v_ax2, v_ax3])
                T_reshape_3[v_ax0, v_ax1, v_ax2, v_ax3] = C[(v_ax1 + v_ax2 + v_ax3) % T.int64(128)]
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(1), T.int64(128), T.int64(28), T.int64(28)):
            with T.block("T_add_1"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(T_multiply[v_ax0, v_ax1, v_ax2, v_ax3], T_reshape_3[v_ax0, v_ax1, T.int64(0), T.int64(0)])
                T.writes(T_add[v_ax0, v_ax1, v_ax2, v_ax3])
                T_add[v_ax0, v_ax1, v_ax2, v_ax3] = T_multiply[v_ax0, v_ax1, v_ax2, v_ax3] + T_reshape_3[v_ax0, v_ax1, T.int64(0), T.int64(0)]
        for ax0 in range(T.int64(128)):
            with T.block("T_multiply_1"):
                v_ax0 = T.axis.spatial(T.int64(128), ax0)
                T.reads(D[v_ax0])
                T.writes(T_multiply_1[v_ax0])
                T_multiply_1[v_ax0] = T.float32(0.90000000000000002) * D[v_ax0]
        for ax0, k0, k2, k3 in T.grid(T.int64(128), T.int64(1), T.int64(28), T.int64(28)):
            with T.block("lv80_red"):
                v_ax0, v_k0, v_k2, v_k3 = T.axis.remap("SRRR", [ax0, k0, k2, k3])
                T.reads(lv80[v_k0, v_ax0, v_k2, v_k3])
                T.writes(lv80_red[v_ax0])
                with T.init():
                    lv80_red[v_ax0] = T.float32(0.0)
                lv80_red[v_ax0] = lv80_red[v_ax0] + lv80[v_k0, v_ax0, v_k2, v_k3]
        for ax0 in range(T.int64(128)):
            with T.block("T_divide_1"):
                v_ax0 = T.axis.spatial(T.int64(128), ax0)
                T.reads(lv80_red[v_ax0])
                T.writes(T_divide_1[v_ax0])
                T_divide_1[v_ax0] = lv80_red[v_ax0] * T.float32(0.0012755102040816326)
        for ax0 in range(T.int64(128)):
            with T.block("T_multiply_2"):
                v_ax0 = T.axis.spatial(T.int64(128), ax0)
                T.reads(T_divide_1[v_ax0])
                T.writes(T_multiply_2[v_ax0])
                T_multiply_2[v_ax0] = T.float32(0.10000000000000001) * T_divide_1[v_ax0]
        for ax0 in range(T.int64(128)):
            with T.block("T_add_2"):
                v_ax0 = T.axis.spatial(T.int64(128), ax0)
                T.reads(T_multiply_1[v_ax0], T_multiply_2[v_ax0])
                T.writes(T_add_1[v_ax0])
                T_add_1[v_ax0] = T_multiply_1[v_ax0] + T_multiply_2[v_ax0]
        for ax0 in range(T.int64(128)):
            with T.block("T_multiply_3"):
                v_ax0 = T.axis.spatial(T.int64(128), ax0)
                T.reads(E[v_ax0])
                T.writes(T_multiply_3[v_ax0])
                T_multiply_3[v_ax0] = T.float32(0.90000000000000002) * E[v_ax0]
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(1), T.int64(128), T.int64(1), T.int64(1)):
            with T.block("T_reshape_4"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(T_divide_1[(v_ax1 + v_ax2 + v_ax3) % T.int64(128)])
                T.writes(T_reshape_4[v_ax0, v_ax1, v_ax2, v_ax3])
                T_reshape_4[v_ax0, v_ax1, v_ax2, v_ax3] = T_divide_1[(v_ax1 + v_ax2 + v_ax3) % T.int64(128)]
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(1), T.int64(128), T.int64(28), T.int64(28)):
            with T.block("T_subtract_1"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(lv80[v_ax0, v_ax1, v_ax2, v_ax3], T_reshape_4[v_ax0, v_ax1, T.int64(0), T.int64(0)])
                T.writes(T_subtract_1[v_ax0, v_ax1, v_ax2, v_ax3])
                T_subtract_1[v_ax0, v_ax1, v_ax2, v_ax3] = lv80[v_ax0, v_ax1, v_ax2, v_ax3] - T_reshape_4[v_ax0, v_ax1, T.int64(0), T.int64(0)]
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(1), T.int64(128), T.int64(28), T.int64(28)):
            with T.block("T_subtract_2"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(lv80[v_ax0, v_ax1, v_ax2, v_ax3], T_reshape_4[v_ax0, v_ax1, T.int64(0), T.int64(0)])
                T.writes(T_subtract_2[v_ax0, v_ax1, v_ax2, v_ax3])
                T_subtract_2[v_ax0, v_ax1, v_ax2, v_ax3] = lv80[v_ax0, v_ax1, v_ax2, v_ax3] - T_reshape_4[v_ax0, v_ax1, T.int64(0), T.int64(0)]
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(1), T.int64(128), T.int64(28), T.int64(28)):
            with T.block("T_multiply_4"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(T_subtract_1[v_ax0, v_ax1, v_ax2, v_ax3], T_subtract_2[v_ax0, v_ax1, v_ax2, v_ax3])
                T.writes(T_multiply_4[v_ax0, v_ax1, v_ax2, v_ax3])
                T_multiply_4[v_ax0, v_ax1, v_ax2, v_ax3] = T_subtract_1[v_ax0, v_ax1, v_ax2, v_ax3] * T_subtract_2[v_ax0, v_ax1, v_ax2, v_ax3]
        for ax0, k0, k2, k3 in T.grid(T.int64(128), T.int64(1), T.int64(28), T.int64(28)):
            with T.block("T_multiply_red"):
                v_ax0, v_k0, v_k2, v_k3 = T.axis.remap("SRRR", [ax0, k0, k2, k3])
                T.reads(T_multiply_4[v_k0, v_ax0, v_k2, v_k3])
                T.writes(T_multiply_red[v_ax0])
                with T.init():
                    T_multiply_red[v_ax0] = T.float32(0.0)
                T_multiply_red[v_ax0] = T_multiply_red[v_ax0] + T_multiply_4[v_k0, v_ax0, v_k2, v_k3]
        for ax0 in range(T.int64(128)):
            with T.block("T_divide_2"):
                v_ax0 = T.axis.spatial(T.int64(128), ax0)
                T.reads(T_multiply_red[v_ax0])
                T.writes(T_divide_2[v_ax0])
                T_divide_2[v_ax0] = T_multiply_red[v_ax0] * T.float32(0.0012755102040816326)
        for ax0 in range(T.int64(128)):
            with T.block("T_multiply_5"):
                v_ax0 = T.axis.spatial(T.int64(128), ax0)
                T.reads(T_divide_2[v_ax0])
                T.writes(T_multiply_5[v_ax0])
                T_multiply_5[v_ax0] = T.float32(0.10000000000000001) * T_divide_2[v_ax0]
        for ax0 in range(T.int64(128)):
            with T.block("T_add_3"):
                v_ax0 = T.axis.spatial(T.int64(128), ax0)
                T.reads(T_multiply_3[v_ax0], T_multiply_5[v_ax0])
                T.writes(T_add_2[v_ax0])
                T_add_2[v_ax0] = T_multiply_3[v_ax0] + T_multiply_5[v_ax0]

    @T.prim_func(private=True)
    def batch_norm6(lv88: T.Buffer((T.int64(1), T.int64(512), T.int64(28), T.int64(28)), "float32"), B: T.Buffer((T.int64(512),), "float32"), C: T.Buffer((T.int64(512),), "float32"), D: T.Buffer((T.int64(512),), "float32"), E: T.Buffer((T.int64(512),), "float32"), T_add: T.Buffer((T.int64(1), T.int64(512), T.int64(28), T.int64(28)), "float32"), T_add_1: T.Buffer((T.int64(512),), "float32"), T_add_2: T.Buffer((T.int64(512),), "float32")):
        T.func_attr({"tir.noalias": True})
        # with T.block("root"):
        T_reshape = T.alloc_buffer((T.int64(1), T.int64(512), T.int64(1), T.int64(1)))
        T_subtract = T.alloc_buffer((T.int64(1), T.int64(512), T.int64(28), T.int64(28)))
        T_reshape_1 = T.alloc_buffer((T.int64(1), T.int64(512), T.int64(1), T.int64(1)))
        T_add_3 = T.alloc_buffer((T.int64(1), T.int64(512), T.int64(1), T.int64(1)))
        compute = T.alloc_buffer((T.int64(1), T.int64(512), T.int64(1), T.int64(1)))
        T_divide = T.alloc_buffer((T.int64(1), T.int64(512), T.int64(28), T.int64(28)))
        T_reshape_2 = T.alloc_buffer((T.int64(1), T.int64(512), T.int64(1), T.int64(1)))
        T_multiply = T.alloc_buffer((T.int64(1), T.int64(512), T.int64(28), T.int64(28)))
        T_reshape_3 = T.alloc_buffer((T.int64(1), T.int64(512), T.int64(1), T.int64(1)))
        T_multiply_1 = T.alloc_buffer((T.int64(512),))
        lv88_red = T.alloc_buffer((T.int64(512),))
        T_divide_1 = T.alloc_buffer((T.int64(512),))
        T_multiply_2 = T.alloc_buffer((T.int64(512),))
        T_multiply_3 = T.alloc_buffer((T.int64(512),))
        T_reshape_4 = T.alloc_buffer((T.int64(1), T.int64(512), T.int64(1), T.int64(1)))
        T_subtract_1 = T.alloc_buffer((T.int64(1), T.int64(512), T.int64(28), T.int64(28)))
        T_subtract_2 = T.alloc_buffer((T.int64(1), T.int64(512), T.int64(28), T.int64(28)))
        T_multiply_4 = T.alloc_buffer((T.int64(1), T.int64(512), T.int64(28), T.int64(28)))
        T_multiply_red = T.alloc_buffer((T.int64(512),))
        T_divide_2 = T.alloc_buffer((T.int64(512),))
        T_multiply_5 = T.alloc_buffer((T.int64(512),))
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(1), T.int64(512), T.int64(1), T.int64(1)):
            with T.block("T_reshape"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(D[(v_ax1 + v_ax2 + v_ax3) % T.int64(512)])
                T.writes(T_reshape[v_ax0, v_ax1, v_ax2, v_ax3])
                T_reshape[v_ax0, v_ax1, v_ax2, v_ax3] = D[(v_ax1 + v_ax2 + v_ax3) % T.int64(512)]
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(1), T.int64(512), T.int64(28), T.int64(28)):
            with T.block("T_subtract"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(lv88[v_ax0, v_ax1, v_ax2, v_ax3], T_reshape[v_ax0, v_ax1, T.int64(0), T.int64(0)])
                T.writes(T_subtract[v_ax0, v_ax1, v_ax2, v_ax3])
                T_subtract[v_ax0, v_ax1, v_ax2, v_ax3] = lv88[v_ax0, v_ax1, v_ax2, v_ax3] - T_reshape[v_ax0, v_ax1, T.int64(0), T.int64(0)]
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(1), T.int64(512), T.int64(1), T.int64(1)):
            with T.block("T_reshape_1"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(E[(v_ax1 + v_ax2 + v_ax3) % T.int64(512)])
                T.writes(T_reshape_1[v_ax0, v_ax1, v_ax2, v_ax3])
                T_reshape_1[v_ax0, v_ax1, v_ax2, v_ax3] = E[(v_ax1 + v_ax2 + v_ax3) % T.int64(512)]
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(1), T.int64(512), T.int64(1), T.int64(1)):
            with T.block("T_add"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(T_reshape_1[v_ax0, v_ax1, v_ax2, v_ax3])
                T.writes(T_add_3[v_ax0, v_ax1, v_ax2, v_ax3])
                T_add_3[v_ax0, v_ax1, v_ax2, v_ax3] = T_reshape_1[v_ax0, v_ax1, v_ax2, v_ax3] + T.float32(9.9999997473787516e-06)
        for i0, i1, i2, i3 in T.grid(T.int64(1), T.int64(512), T.int64(1), T.int64(1)):
            with T.block("compute"):
                v_i0, v_i1, v_i2, v_i3 = T.axis.remap("SSSS", [i0, i1, i2, i3])
                T.reads(T_add_3[v_i0, v_i1, v_i2, v_i3])
                T.writes(compute[v_i0, v_i1, v_i2, v_i3])
                compute[v_i0, v_i1, v_i2, v_i3] = T.sqrt(T_add_3[v_i0, v_i1, v_i2, v_i3])
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(1), T.int64(512), T.int64(28), T.int64(28)):
            with T.block("T_divide"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(T_subtract[v_ax0, v_ax1, v_ax2, v_ax3], compute[v_ax0, v_ax1, T.int64(0), T.int64(0)])
                T.writes(T_divide[v_ax0, v_ax1, v_ax2, v_ax3])
                T_divide[v_ax0, v_ax1, v_ax2, v_ax3] = T_subtract[v_ax0, v_ax1, v_ax2, v_ax3] / compute[v_ax0, v_ax1, T.int64(0), T.int64(0)]
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(1), T.int64(512), T.int64(1), T.int64(1)):
            with T.block("T_reshape_2"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(B[(v_ax1 + v_ax2 + v_ax3) % T.int64(512)])
                T.writes(T_reshape_2[v_ax0, v_ax1, v_ax2, v_ax3])
                T_reshape_2[v_ax0, v_ax1, v_ax2, v_ax3] = B[(v_ax1 + v_ax2 + v_ax3) % T.int64(512)]
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(1), T.int64(512), T.int64(28), T.int64(28)):
            with T.block("T_multiply"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(T_divide[v_ax0, v_ax1, v_ax2, v_ax3], T_reshape_2[v_ax0, v_ax1, T.int64(0), T.int64(0)])
                T.writes(T_multiply[v_ax0, v_ax1, v_ax2, v_ax3])
                T_multiply[v_ax0, v_ax1, v_ax2, v_ax3] = T_divide[v_ax0, v_ax1, v_ax2, v_ax3] * T_reshape_2[v_ax0, v_ax1, T.int64(0), T.int64(0)]
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(1), T.int64(512), T.int64(1), T.int64(1)):
            with T.block("T_reshape_3"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(C[(v_ax1 + v_ax2 + v_ax3) % T.int64(512)])
                T.writes(T_reshape_3[v_ax0, v_ax1, v_ax2, v_ax3])
                T_reshape_3[v_ax0, v_ax1, v_ax2, v_ax3] = C[(v_ax1 + v_ax2 + v_ax3) % T.int64(512)]
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(1), T.int64(512), T.int64(28), T.int64(28)):
            with T.block("T_add_1"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(T_multiply[v_ax0, v_ax1, v_ax2, v_ax3], T_reshape_3[v_ax0, v_ax1, T.int64(0), T.int64(0)])
                T.writes(T_add[v_ax0, v_ax1, v_ax2, v_ax3])
                T_add[v_ax0, v_ax1, v_ax2, v_ax3] = T_multiply[v_ax0, v_ax1, v_ax2, v_ax3] + T_reshape_3[v_ax0, v_ax1, T.int64(0), T.int64(0)]
        for ax0 in range(T.int64(512)):
            with T.block("T_multiply_1"):
                v_ax0 = T.axis.spatial(T.int64(512), ax0)
                T.reads(D[v_ax0])
                T.writes(T_multiply_1[v_ax0])
                T_multiply_1[v_ax0] = T.float32(0.90000000000000002) * D[v_ax0]
        for ax0, k0, k2, k3 in T.grid(T.int64(512), T.int64(1), T.int64(28), T.int64(28)):
            with T.block("lv88_red"):
                v_ax0, v_k0, v_k2, v_k3 = T.axis.remap("SRRR", [ax0, k0, k2, k3])
                T.reads(lv88[v_k0, v_ax0, v_k2, v_k3])
                T.writes(lv88_red[v_ax0])
                with T.init():
                    lv88_red[v_ax0] = T.float32(0.0)
                lv88_red[v_ax0] = lv88_red[v_ax0] + lv88[v_k0, v_ax0, v_k2, v_k3]
        for ax0 in range(T.int64(512)):
            with T.block("T_divide_1"):
                v_ax0 = T.axis.spatial(T.int64(512), ax0)
                T.reads(lv88_red[v_ax0])
                T.writes(T_divide_1[v_ax0])
                T_divide_1[v_ax0] = lv88_red[v_ax0] * T.float32(0.0012755102040816326)
        for ax0 in range(T.int64(512)):
            with T.block("T_multiply_2"):
                v_ax0 = T.axis.spatial(T.int64(512), ax0)
                T.reads(T_divide_1[v_ax0])
                T.writes(T_multiply_2[v_ax0])
                T_multiply_2[v_ax0] = T.float32(0.10000000000000001) * T_divide_1[v_ax0]
        for ax0 in range(T.int64(512)):
            with T.block("T_add_2"):
                v_ax0 = T.axis.spatial(T.int64(512), ax0)
                T.reads(T_multiply_1[v_ax0], T_multiply_2[v_ax0])
                T.writes(T_add_1[v_ax0])
                T_add_1[v_ax0] = T_multiply_1[v_ax0] + T_multiply_2[v_ax0]
        for ax0 in range(T.int64(512)):
            with T.block("T_multiply_3"):
                v_ax0 = T.axis.spatial(T.int64(512), ax0)
                T.reads(E[v_ax0])
                T.writes(T_multiply_3[v_ax0])
                T_multiply_3[v_ax0] = T.float32(0.90000000000000002) * E[v_ax0]
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(1), T.int64(512), T.int64(1), T.int64(1)):
            with T.block("T_reshape_4"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(T_divide_1[(v_ax1 + v_ax2 + v_ax3) % T.int64(512)])
                T.writes(T_reshape_4[v_ax0, v_ax1, v_ax2, v_ax3])
                T_reshape_4[v_ax0, v_ax1, v_ax2, v_ax3] = T_divide_1[(v_ax1 + v_ax2 + v_ax3) % T.int64(512)]
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(1), T.int64(512), T.int64(28), T.int64(28)):
            with T.block("T_subtract_1"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(lv88[v_ax0, v_ax1, v_ax2, v_ax3], T_reshape_4[v_ax0, v_ax1, T.int64(0), T.int64(0)])
                T.writes(T_subtract_1[v_ax0, v_ax1, v_ax2, v_ax3])
                T_subtract_1[v_ax0, v_ax1, v_ax2, v_ax3] = lv88[v_ax0, v_ax1, v_ax2, v_ax3] - T_reshape_4[v_ax0, v_ax1, T.int64(0), T.int64(0)]
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(1), T.int64(512), T.int64(28), T.int64(28)):
            with T.block("T_subtract_2"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(lv88[v_ax0, v_ax1, v_ax2, v_ax3], T_reshape_4[v_ax0, v_ax1, T.int64(0), T.int64(0)])
                T.writes(T_subtract_2[v_ax0, v_ax1, v_ax2, v_ax3])
                T_subtract_2[v_ax0, v_ax1, v_ax2, v_ax3] = lv88[v_ax0, v_ax1, v_ax2, v_ax3] - T_reshape_4[v_ax0, v_ax1, T.int64(0), T.int64(0)]
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(1), T.int64(512), T.int64(28), T.int64(28)):
            with T.block("T_multiply_4"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(T_subtract_1[v_ax0, v_ax1, v_ax2, v_ax3], T_subtract_2[v_ax0, v_ax1, v_ax2, v_ax3])
                T.writes(T_multiply_4[v_ax0, v_ax1, v_ax2, v_ax3])
                T_multiply_4[v_ax0, v_ax1, v_ax2, v_ax3] = T_subtract_1[v_ax0, v_ax1, v_ax2, v_ax3] * T_subtract_2[v_ax0, v_ax1, v_ax2, v_ax3]
        for ax0, k0, k2, k3 in T.grid(T.int64(512), T.int64(1), T.int64(28), T.int64(28)):
            with T.block("T_multiply_red"):
                v_ax0, v_k0, v_k2, v_k3 = T.axis.remap("SRRR", [ax0, k0, k2, k3])
                T.reads(T_multiply_4[v_k0, v_ax0, v_k2, v_k3])
                T.writes(T_multiply_red[v_ax0])
                with T.init():
                    T_multiply_red[v_ax0] = T.float32(0.0)
                T_multiply_red[v_ax0] = T_multiply_red[v_ax0] + T_multiply_4[v_k0, v_ax0, v_k2, v_k3]
        for ax0 in range(T.int64(512)):
            with T.block("T_divide_2"):
                v_ax0 = T.axis.spatial(T.int64(512), ax0)
                T.reads(T_multiply_red[v_ax0])
                T.writes(T_divide_2[v_ax0])
                T_divide_2[v_ax0] = T_multiply_red[v_ax0] * T.float32(0.0012755102040816326)
        for ax0 in range(T.int64(512)):
            with T.block("T_multiply_5"):
                v_ax0 = T.axis.spatial(T.int64(512), ax0)
                T.reads(T_divide_2[v_ax0])
                T.writes(T_multiply_5[v_ax0])
                T_multiply_5[v_ax0] = T.float32(0.10000000000000001) * T_divide_2[v_ax0]
        for ax0 in range(T.int64(512)):
            with T.block("T_add_3"):
                v_ax0 = T.axis.spatial(T.int64(512), ax0)
                T.reads(T_multiply_3[v_ax0], T_multiply_5[v_ax0])
                T.writes(T_add_2[v_ax0])
                T_add_2[v_ax0] = T_multiply_3[v_ax0] + T_multiply_5[v_ax0]

    @T.prim_func(private=True)
    def batch_norm7(lv151: T.Buffer((T.int64(1), T.int64(256), T.int64(28), T.int64(28)), "float32"), B: T.Buffer((T.int64(256),), "float32"), C: T.Buffer((T.int64(256),), "float32"), D: T.Buffer((T.int64(256),), "float32"), E: T.Buffer((T.int64(256),), "float32"), T_add: T.Buffer((T.int64(1), T.int64(256), T.int64(28), T.int64(28)), "float32"), T_add_1: T.Buffer((T.int64(256),), "float32"), T_add_2: T.Buffer((T.int64(256),), "float32")):
        T.func_attr({"tir.noalias": True})
        # with T.block("root"):
        T_reshape = T.alloc_buffer((T.int64(1), T.int64(256), T.int64(1), T.int64(1)))
        T_subtract = T.alloc_buffer((T.int64(1), T.int64(256), T.int64(28), T.int64(28)))
        T_reshape_1 = T.alloc_buffer((T.int64(1), T.int64(256), T.int64(1), T.int64(1)))
        T_add_3 = T.alloc_buffer((T.int64(1), T.int64(256), T.int64(1), T.int64(1)))
        compute = T.alloc_buffer((T.int64(1), T.int64(256), T.int64(1), T.int64(1)))
        T_divide = T.alloc_buffer((T.int64(1), T.int64(256), T.int64(28), T.int64(28)))
        T_reshape_2 = T.alloc_buffer((T.int64(1), T.int64(256), T.int64(1), T.int64(1)))
        T_multiply = T.alloc_buffer((T.int64(1), T.int64(256), T.int64(28), T.int64(28)))
        T_reshape_3 = T.alloc_buffer((T.int64(1), T.int64(256), T.int64(1), T.int64(1)))
        T_multiply_1 = T.alloc_buffer((T.int64(256),))
        lv151_red = T.alloc_buffer((T.int64(256),))
        T_divide_1 = T.alloc_buffer((T.int64(256),))
        T_multiply_2 = T.alloc_buffer((T.int64(256),))
        T_multiply_3 = T.alloc_buffer((T.int64(256),))
        T_reshape_4 = T.alloc_buffer((T.int64(1), T.int64(256), T.int64(1), T.int64(1)))
        T_subtract_1 = T.alloc_buffer((T.int64(1), T.int64(256), T.int64(28), T.int64(28)))
        T_subtract_2 = T.alloc_buffer((T.int64(1), T.int64(256), T.int64(28), T.int64(28)))
        T_multiply_4 = T.alloc_buffer((T.int64(1), T.int64(256), T.int64(28), T.int64(28)))
        T_multiply_red = T.alloc_buffer((T.int64(256),))
        T_divide_2 = T.alloc_buffer((T.int64(256),))
        T_multiply_5 = T.alloc_buffer((T.int64(256),))
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(1), T.int64(256), T.int64(1), T.int64(1)):
            with T.block("T_reshape"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(D[(v_ax1 + v_ax2 + v_ax3) % T.int64(256)])
                T.writes(T_reshape[v_ax0, v_ax1, v_ax2, v_ax3])
                T_reshape[v_ax0, v_ax1, v_ax2, v_ax3] = D[(v_ax1 + v_ax2 + v_ax3) % T.int64(256)]
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(1), T.int64(256), T.int64(28), T.int64(28)):
            with T.block("T_subtract"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(lv151[v_ax0, v_ax1, v_ax2, v_ax3], T_reshape[v_ax0, v_ax1, T.int64(0), T.int64(0)])
                T.writes(T_subtract[v_ax0, v_ax1, v_ax2, v_ax3])
                T_subtract[v_ax0, v_ax1, v_ax2, v_ax3] = lv151[v_ax0, v_ax1, v_ax2, v_ax3] - T_reshape[v_ax0, v_ax1, T.int64(0), T.int64(0)]
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(1), T.int64(256), T.int64(1), T.int64(1)):
            with T.block("T_reshape_1"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(E[(v_ax1 + v_ax2 + v_ax3) % T.int64(256)])
                T.writes(T_reshape_1[v_ax0, v_ax1, v_ax2, v_ax3])
                T_reshape_1[v_ax0, v_ax1, v_ax2, v_ax3] = E[(v_ax1 + v_ax2 + v_ax3) % T.int64(256)]
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(1), T.int64(256), T.int64(1), T.int64(1)):
            with T.block("T_add"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(T_reshape_1[v_ax0, v_ax1, v_ax2, v_ax3])
                T.writes(T_add_3[v_ax0, v_ax1, v_ax2, v_ax3])
                T_add_3[v_ax0, v_ax1, v_ax2, v_ax3] = T_reshape_1[v_ax0, v_ax1, v_ax2, v_ax3] + T.float32(9.9999997473787516e-06)
        for i0, i1, i2, i3 in T.grid(T.int64(1), T.int64(256), T.int64(1), T.int64(1)):
            with T.block("compute"):
                v_i0, v_i1, v_i2, v_i3 = T.axis.remap("SSSS", [i0, i1, i2, i3])
                T.reads(T_add_3[v_i0, v_i1, v_i2, v_i3])
                T.writes(compute[v_i0, v_i1, v_i2, v_i3])
                compute[v_i0, v_i1, v_i2, v_i3] = T.sqrt(T_add_3[v_i0, v_i1, v_i2, v_i3])
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(1), T.int64(256), T.int64(28), T.int64(28)):
            with T.block("T_divide"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(T_subtract[v_ax0, v_ax1, v_ax2, v_ax3], compute[v_ax0, v_ax1, T.int64(0), T.int64(0)])
                T.writes(T_divide[v_ax0, v_ax1, v_ax2, v_ax3])
                T_divide[v_ax0, v_ax1, v_ax2, v_ax3] = T_subtract[v_ax0, v_ax1, v_ax2, v_ax3] / compute[v_ax0, v_ax1, T.int64(0), T.int64(0)]
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(1), T.int64(256), T.int64(1), T.int64(1)):
            with T.block("T_reshape_2"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(B[(v_ax1 + v_ax2 + v_ax3) % T.int64(256)])
                T.writes(T_reshape_2[v_ax0, v_ax1, v_ax2, v_ax3])
                T_reshape_2[v_ax0, v_ax1, v_ax2, v_ax3] = B[(v_ax1 + v_ax2 + v_ax3) % T.int64(256)]
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(1), T.int64(256), T.int64(28), T.int64(28)):
            with T.block("T_multiply"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(T_divide[v_ax0, v_ax1, v_ax2, v_ax3], T_reshape_2[v_ax0, v_ax1, T.int64(0), T.int64(0)])
                T.writes(T_multiply[v_ax0, v_ax1, v_ax2, v_ax3])
                T_multiply[v_ax0, v_ax1, v_ax2, v_ax3] = T_divide[v_ax0, v_ax1, v_ax2, v_ax3] * T_reshape_2[v_ax0, v_ax1, T.int64(0), T.int64(0)]
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(1), T.int64(256), T.int64(1), T.int64(1)):
            with T.block("T_reshape_3"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(C[(v_ax1 + v_ax2 + v_ax3) % T.int64(256)])
                T.writes(T_reshape_3[v_ax0, v_ax1, v_ax2, v_ax3])
                T_reshape_3[v_ax0, v_ax1, v_ax2, v_ax3] = C[(v_ax1 + v_ax2 + v_ax3) % T.int64(256)]
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(1), T.int64(256), T.int64(28), T.int64(28)):
            with T.block("T_add_1"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(T_multiply[v_ax0, v_ax1, v_ax2, v_ax3], T_reshape_3[v_ax0, v_ax1, T.int64(0), T.int64(0)])
                T.writes(T_add[v_ax0, v_ax1, v_ax2, v_ax3])
                T_add[v_ax0, v_ax1, v_ax2, v_ax3] = T_multiply[v_ax0, v_ax1, v_ax2, v_ax3] + T_reshape_3[v_ax0, v_ax1, T.int64(0), T.int64(0)]
        for ax0 in range(T.int64(256)):
            with T.block("T_multiply_1"):
                v_ax0 = T.axis.spatial(T.int64(256), ax0)
                T.reads(D[v_ax0])
                T.writes(T_multiply_1[v_ax0])
                T_multiply_1[v_ax0] = T.float32(0.90000000000000002) * D[v_ax0]
        for ax0, k0, k2, k3 in T.grid(T.int64(256), T.int64(1), T.int64(28), T.int64(28)):
            with T.block("lv151_red"):
                v_ax0, v_k0, v_k2, v_k3 = T.axis.remap("SRRR", [ax0, k0, k2, k3])
                T.reads(lv151[v_k0, v_ax0, v_k2, v_k3])
                T.writes(lv151_red[v_ax0])
                with T.init():
                    lv151_red[v_ax0] = T.float32(0.0)
                lv151_red[v_ax0] = lv151_red[v_ax0] + lv151[v_k0, v_ax0, v_k2, v_k3]
        for ax0 in range(T.int64(256)):
            with T.block("T_divide_1"):
                v_ax0 = T.axis.spatial(T.int64(256), ax0)
                T.reads(lv151_red[v_ax0])
                T.writes(T_divide_1[v_ax0])
                T_divide_1[v_ax0] = lv151_red[v_ax0] * T.float32(0.0012755102040816326)
        for ax0 in range(T.int64(256)):
            with T.block("T_multiply_2"):
                v_ax0 = T.axis.spatial(T.int64(256), ax0)
                T.reads(T_divide_1[v_ax0])
                T.writes(T_multiply_2[v_ax0])
                T_multiply_2[v_ax0] = T.float32(0.10000000000000001) * T_divide_1[v_ax0]
        for ax0 in range(T.int64(256)):
            with T.block("T_add_2"):
                v_ax0 = T.axis.spatial(T.int64(256), ax0)
                T.reads(T_multiply_1[v_ax0], T_multiply_2[v_ax0])
                T.writes(T_add_1[v_ax0])
                T_add_1[v_ax0] = T_multiply_1[v_ax0] + T_multiply_2[v_ax0]
        for ax0 in range(T.int64(256)):
            with T.block("T_multiply_3"):
                v_ax0 = T.axis.spatial(T.int64(256), ax0)
                T.reads(E[v_ax0])
                T.writes(T_multiply_3[v_ax0])
                T_multiply_3[v_ax0] = T.float32(0.90000000000000002) * E[v_ax0]
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(1), T.int64(256), T.int64(1), T.int64(1)):
            with T.block("T_reshape_4"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(T_divide_1[(v_ax1 + v_ax2 + v_ax3) % T.int64(256)])
                T.writes(T_reshape_4[v_ax0, v_ax1, v_ax2, v_ax3])
                T_reshape_4[v_ax0, v_ax1, v_ax2, v_ax3] = T_divide_1[(v_ax1 + v_ax2 + v_ax3) % T.int64(256)]
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(1), T.int64(256), T.int64(28), T.int64(28)):
            with T.block("T_subtract_1"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(lv151[v_ax0, v_ax1, v_ax2, v_ax3], T_reshape_4[v_ax0, v_ax1, T.int64(0), T.int64(0)])
                T.writes(T_subtract_1[v_ax0, v_ax1, v_ax2, v_ax3])
                T_subtract_1[v_ax0, v_ax1, v_ax2, v_ax3] = lv151[v_ax0, v_ax1, v_ax2, v_ax3] - T_reshape_4[v_ax0, v_ax1, T.int64(0), T.int64(0)]
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(1), T.int64(256), T.int64(28), T.int64(28)):
            with T.block("T_subtract_2"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(lv151[v_ax0, v_ax1, v_ax2, v_ax3], T_reshape_4[v_ax0, v_ax1, T.int64(0), T.int64(0)])
                T.writes(T_subtract_2[v_ax0, v_ax1, v_ax2, v_ax3])
                T_subtract_2[v_ax0, v_ax1, v_ax2, v_ax3] = lv151[v_ax0, v_ax1, v_ax2, v_ax3] - T_reshape_4[v_ax0, v_ax1, T.int64(0), T.int64(0)]
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(1), T.int64(256), T.int64(28), T.int64(28)):
            with T.block("T_multiply_4"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(T_subtract_1[v_ax0, v_ax1, v_ax2, v_ax3], T_subtract_2[v_ax0, v_ax1, v_ax2, v_ax3])
                T.writes(T_multiply_4[v_ax0, v_ax1, v_ax2, v_ax3])
                T_multiply_4[v_ax0, v_ax1, v_ax2, v_ax3] = T_subtract_1[v_ax0, v_ax1, v_ax2, v_ax3] * T_subtract_2[v_ax0, v_ax1, v_ax2, v_ax3]
        for ax0, k0, k2, k3 in T.grid(T.int64(256), T.int64(1), T.int64(28), T.int64(28)):
            with T.block("T_multiply_red"):
                v_ax0, v_k0, v_k2, v_k3 = T.axis.remap("SRRR", [ax0, k0, k2, k3])
                T.reads(T_multiply_4[v_k0, v_ax0, v_k2, v_k3])
                T.writes(T_multiply_red[v_ax0])
                with T.init():
                    T_multiply_red[v_ax0] = T.float32(0.0)
                T_multiply_red[v_ax0] = T_multiply_red[v_ax0] + T_multiply_4[v_k0, v_ax0, v_k2, v_k3]
        for ax0 in range(T.int64(256)):
            with T.block("T_divide_2"):
                v_ax0 = T.axis.spatial(T.int64(256), ax0)
                T.reads(T_multiply_red[v_ax0])
                T.writes(T_divide_2[v_ax0])
                T_divide_2[v_ax0] = T_multiply_red[v_ax0] * T.float32(0.0012755102040816326)
        for ax0 in range(T.int64(256)):
            with T.block("T_multiply_5"):
                v_ax0 = T.axis.spatial(T.int64(256), ax0)
                T.reads(T_divide_2[v_ax0])
                T.writes(T_multiply_5[v_ax0])
                T_multiply_5[v_ax0] = T.float32(0.10000000000000001) * T_divide_2[v_ax0]
        for ax0 in range(T.int64(256)):
            with T.block("T_add_3"):
                v_ax0 = T.axis.spatial(T.int64(256), ax0)
                T.reads(T_multiply_3[v_ax0], T_multiply_5[v_ax0])
                T.writes(T_add_2[v_ax0])
                T_add_2[v_ax0] = T_multiply_3[v_ax0] + T_multiply_5[v_ax0]

    @T.prim_func(private=True)
    def batch_norm8(lv157: T.Buffer((T.int64(1), T.int64(256), T.int64(14), T.int64(14)), "float32"), B: T.Buffer((T.int64(256),), "float32"), C: T.Buffer((T.int64(256),), "float32"), D: T.Buffer((T.int64(256),), "float32"), E: T.Buffer((T.int64(256),), "float32"), T_add: T.Buffer((T.int64(1), T.int64(256), T.int64(14), T.int64(14)), "float32"), T_add_1: T.Buffer((T.int64(256),), "float32"), T_add_2: T.Buffer((T.int64(256),), "float32")):
        T.func_attr({"tir.noalias": True})
        # with T.block("root"):
        T_reshape = T.alloc_buffer((T.int64(1), T.int64(256), T.int64(1), T.int64(1)))
        T_subtract = T.alloc_buffer((T.int64(1), T.int64(256), T.int64(14), T.int64(14)))
        T_reshape_1 = T.alloc_buffer((T.int64(1), T.int64(256), T.int64(1), T.int64(1)))
        T_add_3 = T.alloc_buffer((T.int64(1), T.int64(256), T.int64(1), T.int64(1)))
        compute = T.alloc_buffer((T.int64(1), T.int64(256), T.int64(1), T.int64(1)))
        T_divide = T.alloc_buffer((T.int64(1), T.int64(256), T.int64(14), T.int64(14)))
        T_reshape_2 = T.alloc_buffer((T.int64(1), T.int64(256), T.int64(1), T.int64(1)))
        T_multiply = T.alloc_buffer((T.int64(1), T.int64(256), T.int64(14), T.int64(14)))
        T_reshape_3 = T.alloc_buffer((T.int64(1), T.int64(256), T.int64(1), T.int64(1)))
        T_multiply_1 = T.alloc_buffer((T.int64(256),))
        lv157_red = T.alloc_buffer((T.int64(256),))
        T_divide_1 = T.alloc_buffer((T.int64(256),))
        T_multiply_2 = T.alloc_buffer((T.int64(256),))
        T_multiply_3 = T.alloc_buffer((T.int64(256),))
        T_reshape_4 = T.alloc_buffer((T.int64(1), T.int64(256), T.int64(1), T.int64(1)))
        T_subtract_1 = T.alloc_buffer((T.int64(1), T.int64(256), T.int64(14), T.int64(14)))
        T_subtract_2 = T.alloc_buffer((T.int64(1), T.int64(256), T.int64(14), T.int64(14)))
        T_multiply_4 = T.alloc_buffer((T.int64(1), T.int64(256), T.int64(14), T.int64(14)))
        T_multiply_red = T.alloc_buffer((T.int64(256),))
        T_divide_2 = T.alloc_buffer((T.int64(256),))
        T_multiply_5 = T.alloc_buffer((T.int64(256),))
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(1), T.int64(256), T.int64(1), T.int64(1)):
            with T.block("T_reshape"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(D[(v_ax1 + v_ax2 + v_ax3) % T.int64(256)])
                T.writes(T_reshape[v_ax0, v_ax1, v_ax2, v_ax3])
                T_reshape[v_ax0, v_ax1, v_ax2, v_ax3] = D[(v_ax1 + v_ax2 + v_ax3) % T.int64(256)]
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(1), T.int64(256), T.int64(14), T.int64(14)):
            with T.block("T_subtract"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(lv157[v_ax0, v_ax1, v_ax2, v_ax3], T_reshape[v_ax0, v_ax1, T.int64(0), T.int64(0)])
                T.writes(T_subtract[v_ax0, v_ax1, v_ax2, v_ax3])
                T_subtract[v_ax0, v_ax1, v_ax2, v_ax3] = lv157[v_ax0, v_ax1, v_ax2, v_ax3] - T_reshape[v_ax0, v_ax1, T.int64(0), T.int64(0)]
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(1), T.int64(256), T.int64(1), T.int64(1)):
            with T.block("T_reshape_1"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(E[(v_ax1 + v_ax2 + v_ax3) % T.int64(256)])
                T.writes(T_reshape_1[v_ax0, v_ax1, v_ax2, v_ax3])
                T_reshape_1[v_ax0, v_ax1, v_ax2, v_ax3] = E[(v_ax1 + v_ax2 + v_ax3) % T.int64(256)]
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(1), T.int64(256), T.int64(1), T.int64(1)):
            with T.block("T_add"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(T_reshape_1[v_ax0, v_ax1, v_ax2, v_ax3])
                T.writes(T_add_3[v_ax0, v_ax1, v_ax2, v_ax3])
                T_add_3[v_ax0, v_ax1, v_ax2, v_ax3] = T_reshape_1[v_ax0, v_ax1, v_ax2, v_ax3] + T.float32(9.9999997473787516e-06)
        for i0, i1, i2, i3 in T.grid(T.int64(1), T.int64(256), T.int64(1), T.int64(1)):
            with T.block("compute"):
                v_i0, v_i1, v_i2, v_i3 = T.axis.remap("SSSS", [i0, i1, i2, i3])
                T.reads(T_add_3[v_i0, v_i1, v_i2, v_i3])
                T.writes(compute[v_i0, v_i1, v_i2, v_i3])
                compute[v_i0, v_i1, v_i2, v_i3] = T.sqrt(T_add_3[v_i0, v_i1, v_i2, v_i3])
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(1), T.int64(256), T.int64(14), T.int64(14)):
            with T.block("T_divide"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(T_subtract[v_ax0, v_ax1, v_ax2, v_ax3], compute[v_ax0, v_ax1, T.int64(0), T.int64(0)])
                T.writes(T_divide[v_ax0, v_ax1, v_ax2, v_ax3])
                T_divide[v_ax0, v_ax1, v_ax2, v_ax3] = T_subtract[v_ax0, v_ax1, v_ax2, v_ax3] / compute[v_ax0, v_ax1, T.int64(0), T.int64(0)]
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(1), T.int64(256), T.int64(1), T.int64(1)):
            with T.block("T_reshape_2"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(B[(v_ax1 + v_ax2 + v_ax3) % T.int64(256)])
                T.writes(T_reshape_2[v_ax0, v_ax1, v_ax2, v_ax3])
                T_reshape_2[v_ax0, v_ax1, v_ax2, v_ax3] = B[(v_ax1 + v_ax2 + v_ax3) % T.int64(256)]
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(1), T.int64(256), T.int64(14), T.int64(14)):
            with T.block("T_multiply"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(T_divide[v_ax0, v_ax1, v_ax2, v_ax3], T_reshape_2[v_ax0, v_ax1, T.int64(0), T.int64(0)])
                T.writes(T_multiply[v_ax0, v_ax1, v_ax2, v_ax3])
                T_multiply[v_ax0, v_ax1, v_ax2, v_ax3] = T_divide[v_ax0, v_ax1, v_ax2, v_ax3] * T_reshape_2[v_ax0, v_ax1, T.int64(0), T.int64(0)]
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(1), T.int64(256), T.int64(1), T.int64(1)):
            with T.block("T_reshape_3"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(C[(v_ax1 + v_ax2 + v_ax3) % T.int64(256)])
                T.writes(T_reshape_3[v_ax0, v_ax1, v_ax2, v_ax3])
                T_reshape_3[v_ax0, v_ax1, v_ax2, v_ax3] = C[(v_ax1 + v_ax2 + v_ax3) % T.int64(256)]
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(1), T.int64(256), T.int64(14), T.int64(14)):
            with T.block("T_add_1"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(T_multiply[v_ax0, v_ax1, v_ax2, v_ax3], T_reshape_3[v_ax0, v_ax1, T.int64(0), T.int64(0)])
                T.writes(T_add[v_ax0, v_ax1, v_ax2, v_ax3])
                T_add[v_ax0, v_ax1, v_ax2, v_ax3] = T_multiply[v_ax0, v_ax1, v_ax2, v_ax3] + T_reshape_3[v_ax0, v_ax1, T.int64(0), T.int64(0)]
        for ax0 in range(T.int64(256)):
            with T.block("T_multiply_1"):
                v_ax0 = T.axis.spatial(T.int64(256), ax0)
                T.reads(D[v_ax0])
                T.writes(T_multiply_1[v_ax0])
                T_multiply_1[v_ax0] = T.float32(0.90000000000000002) * D[v_ax0]
        for ax0, k0, k2, k3 in T.grid(T.int64(256), T.int64(1), T.int64(14), T.int64(14)):
            with T.block("lv157_red"):
                v_ax0, v_k0, v_k2, v_k3 = T.axis.remap("SRRR", [ax0, k0, k2, k3])
                T.reads(lv157[v_k0, v_ax0, v_k2, v_k3])
                T.writes(lv157_red[v_ax0])
                with T.init():
                    lv157_red[v_ax0] = T.float32(0.0)
                lv157_red[v_ax0] = lv157_red[v_ax0] + lv157[v_k0, v_ax0, v_k2, v_k3]
        for ax0 in range(T.int64(256)):
            with T.block("T_divide_1"):
                v_ax0 = T.axis.spatial(T.int64(256), ax0)
                T.reads(lv157_red[v_ax0])
                T.writes(T_divide_1[v_ax0])
                T_divide_1[v_ax0] = lv157_red[v_ax0] * T.float32(0.0051020408163265302)
        for ax0 in range(T.int64(256)):
            with T.block("T_multiply_2"):
                v_ax0 = T.axis.spatial(T.int64(256), ax0)
                T.reads(T_divide_1[v_ax0])
                T.writes(T_multiply_2[v_ax0])
                T_multiply_2[v_ax0] = T.float32(0.10000000000000001) * T_divide_1[v_ax0]
        for ax0 in range(T.int64(256)):
            with T.block("T_add_2"):
                v_ax0 = T.axis.spatial(T.int64(256), ax0)
                T.reads(T_multiply_1[v_ax0], T_multiply_2[v_ax0])
                T.writes(T_add_1[v_ax0])
                T_add_1[v_ax0] = T_multiply_1[v_ax0] + T_multiply_2[v_ax0]
        for ax0 in range(T.int64(256)):
            with T.block("T_multiply_3"):
                v_ax0 = T.axis.spatial(T.int64(256), ax0)
                T.reads(E[v_ax0])
                T.writes(T_multiply_3[v_ax0])
                T_multiply_3[v_ax0] = T.float32(0.90000000000000002) * E[v_ax0]
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(1), T.int64(256), T.int64(1), T.int64(1)):
            with T.block("T_reshape_4"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(T_divide_1[(v_ax1 + v_ax2 + v_ax3) % T.int64(256)])
                T.writes(T_reshape_4[v_ax0, v_ax1, v_ax2, v_ax3])
                T_reshape_4[v_ax0, v_ax1, v_ax2, v_ax3] = T_divide_1[(v_ax1 + v_ax2 + v_ax3) % T.int64(256)]
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(1), T.int64(256), T.int64(14), T.int64(14)):
            with T.block("T_subtract_1"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(lv157[v_ax0, v_ax1, v_ax2, v_ax3], T_reshape_4[v_ax0, v_ax1, T.int64(0), T.int64(0)])
                T.writes(T_subtract_1[v_ax0, v_ax1, v_ax2, v_ax3])
                T_subtract_1[v_ax0, v_ax1, v_ax2, v_ax3] = lv157[v_ax0, v_ax1, v_ax2, v_ax3] - T_reshape_4[v_ax0, v_ax1, T.int64(0), T.int64(0)]
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(1), T.int64(256), T.int64(14), T.int64(14)):
            with T.block("T_subtract_2"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(lv157[v_ax0, v_ax1, v_ax2, v_ax3], T_reshape_4[v_ax0, v_ax1, T.int64(0), T.int64(0)])
                T.writes(T_subtract_2[v_ax0, v_ax1, v_ax2, v_ax3])
                T_subtract_2[v_ax0, v_ax1, v_ax2, v_ax3] = lv157[v_ax0, v_ax1, v_ax2, v_ax3] - T_reshape_4[v_ax0, v_ax1, T.int64(0), T.int64(0)]
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(1), T.int64(256), T.int64(14), T.int64(14)):
            with T.block("T_multiply_4"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(T_subtract_1[v_ax0, v_ax1, v_ax2, v_ax3], T_subtract_2[v_ax0, v_ax1, v_ax2, v_ax3])
                T.writes(T_multiply_4[v_ax0, v_ax1, v_ax2, v_ax3])
                T_multiply_4[v_ax0, v_ax1, v_ax2, v_ax3] = T_subtract_1[v_ax0, v_ax1, v_ax2, v_ax3] * T_subtract_2[v_ax0, v_ax1, v_ax2, v_ax3]
        for ax0, k0, k2, k3 in T.grid(T.int64(256), T.int64(1), T.int64(14), T.int64(14)):
            with T.block("T_multiply_red"):
                v_ax0, v_k0, v_k2, v_k3 = T.axis.remap("SRRR", [ax0, k0, k2, k3])
                T.reads(T_multiply_4[v_k0, v_ax0, v_k2, v_k3])
                T.writes(T_multiply_red[v_ax0])
                with T.init():
                    T_multiply_red[v_ax0] = T.float32(0.0)
                T_multiply_red[v_ax0] = T_multiply_red[v_ax0] + T_multiply_4[v_k0, v_ax0, v_k2, v_k3]
        for ax0 in range(T.int64(256)):
            with T.block("T_divide_2"):
                v_ax0 = T.axis.spatial(T.int64(256), ax0)
                T.reads(T_multiply_red[v_ax0])
                T.writes(T_divide_2[v_ax0])
                T_divide_2[v_ax0] = T_multiply_red[v_ax0] * T.float32(0.0051020408163265302)
        for ax0 in range(T.int64(256)):
            with T.block("T_multiply_5"):
                v_ax0 = T.axis.spatial(T.int64(256), ax0)
                T.reads(T_divide_2[v_ax0])
                T.writes(T_multiply_5[v_ax0])
                T_multiply_5[v_ax0] = T.float32(0.10000000000000001) * T_divide_2[v_ax0]
        for ax0 in range(T.int64(256)):
            with T.block("T_add_3"):
                v_ax0 = T.axis.spatial(T.int64(256), ax0)
                T.reads(T_multiply_3[v_ax0], T_multiply_5[v_ax0])
                T.writes(T_add_2[v_ax0])
                T_add_2[v_ax0] = T_multiply_3[v_ax0] + T_multiply_5[v_ax0]

    @T.prim_func(private=True)
    def batch_norm9(lv165: T.Buffer((T.int64(1), T.int64(1024), T.int64(14), T.int64(14)), "float32"), B: T.Buffer((T.int64(1024),), "float32"), C: T.Buffer((T.int64(1024),), "float32"), D: T.Buffer((T.int64(1024),), "float32"), E: T.Buffer((T.int64(1024),), "float32"), T_add: T.Buffer((T.int64(1), T.int64(1024), T.int64(14), T.int64(14)), "float32"), T_add_1: T.Buffer((T.int64(1024),), "float32"), T_add_2: T.Buffer((T.int64(1024),), "float32")):
        T.func_attr({"tir.noalias": True})
        # with T.block("root"):
        T_reshape = T.alloc_buffer((T.int64(1), T.int64(1024), T.int64(1), T.int64(1)))
        T_subtract = T.alloc_buffer((T.int64(1), T.int64(1024), T.int64(14), T.int64(14)))
        T_reshape_1 = T.alloc_buffer((T.int64(1), T.int64(1024), T.int64(1), T.int64(1)))
        T_add_3 = T.alloc_buffer((T.int64(1), T.int64(1024), T.int64(1), T.int64(1)))
        compute = T.alloc_buffer((T.int64(1), T.int64(1024), T.int64(1), T.int64(1)))
        T_divide = T.alloc_buffer((T.int64(1), T.int64(1024), T.int64(14), T.int64(14)))
        T_reshape_2 = T.alloc_buffer((T.int64(1), T.int64(1024), T.int64(1), T.int64(1)))
        T_multiply = T.alloc_buffer((T.int64(1), T.int64(1024), T.int64(14), T.int64(14)))
        T_reshape_3 = T.alloc_buffer((T.int64(1), T.int64(1024), T.int64(1), T.int64(1)))
        T_multiply_1 = T.alloc_buffer((T.int64(1024),))
        lv165_red = T.alloc_buffer((T.int64(1024),))
        T_divide_1 = T.alloc_buffer((T.int64(1024),))
        T_multiply_2 = T.alloc_buffer((T.int64(1024),))
        T_multiply_3 = T.alloc_buffer((T.int64(1024),))
        T_reshape_4 = T.alloc_buffer((T.int64(1), T.int64(1024), T.int64(1), T.int64(1)))
        T_subtract_1 = T.alloc_buffer((T.int64(1), T.int64(1024), T.int64(14), T.int64(14)))
        T_subtract_2 = T.alloc_buffer((T.int64(1), T.int64(1024), T.int64(14), T.int64(14)))
        T_multiply_4 = T.alloc_buffer((T.int64(1), T.int64(1024), T.int64(14), T.int64(14)))
        T_multiply_red = T.alloc_buffer((T.int64(1024),))
        T_divide_2 = T.alloc_buffer((T.int64(1024),))
        T_multiply_5 = T.alloc_buffer((T.int64(1024),))
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(1), T.int64(1024), T.int64(1), T.int64(1)):
            with T.block("T_reshape"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(D[(v_ax1 + v_ax2 + v_ax3) % T.int64(1024)])
                T.writes(T_reshape[v_ax0, v_ax1, v_ax2, v_ax3])
                T_reshape[v_ax0, v_ax1, v_ax2, v_ax3] = D[(v_ax1 + v_ax2 + v_ax3) % T.int64(1024)]
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(1), T.int64(1024), T.int64(14), T.int64(14)):
            with T.block("T_subtract"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(lv165[v_ax0, v_ax1, v_ax2, v_ax3], T_reshape[v_ax0, v_ax1, T.int64(0), T.int64(0)])
                T.writes(T_subtract[v_ax0, v_ax1, v_ax2, v_ax3])
                T_subtract[v_ax0, v_ax1, v_ax2, v_ax3] = lv165[v_ax0, v_ax1, v_ax2, v_ax3] - T_reshape[v_ax0, v_ax1, T.int64(0), T.int64(0)]
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(1), T.int64(1024), T.int64(1), T.int64(1)):
            with T.block("T_reshape_1"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(E[(v_ax1 + v_ax2 + v_ax3) % T.int64(1024)])
                T.writes(T_reshape_1[v_ax0, v_ax1, v_ax2, v_ax3])
                T_reshape_1[v_ax0, v_ax1, v_ax2, v_ax3] = E[(v_ax1 + v_ax2 + v_ax3) % T.int64(1024)]
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(1), T.int64(1024), T.int64(1), T.int64(1)):
            with T.block("T_add"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(T_reshape_1[v_ax0, v_ax1, v_ax2, v_ax3])
                T.writes(T_add_3[v_ax0, v_ax1, v_ax2, v_ax3])
                T_add_3[v_ax0, v_ax1, v_ax2, v_ax3] = T_reshape_1[v_ax0, v_ax1, v_ax2, v_ax3] + T.float32(9.9999997473787516e-06)
        for i0, i1, i2, i3 in T.grid(T.int64(1), T.int64(1024), T.int64(1), T.int64(1)):
            with T.block("compute"):
                v_i0, v_i1, v_i2, v_i3 = T.axis.remap("SSSS", [i0, i1, i2, i3])
                T.reads(T_add_3[v_i0, v_i1, v_i2, v_i3])
                T.writes(compute[v_i0, v_i1, v_i2, v_i3])
                compute[v_i0, v_i1, v_i2, v_i3] = T.sqrt(T_add_3[v_i0, v_i1, v_i2, v_i3])
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(1), T.int64(1024), T.int64(14), T.int64(14)):
            with T.block("T_divide"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(T_subtract[v_ax0, v_ax1, v_ax2, v_ax3], compute[v_ax0, v_ax1, T.int64(0), T.int64(0)])
                T.writes(T_divide[v_ax0, v_ax1, v_ax2, v_ax3])
                T_divide[v_ax0, v_ax1, v_ax2, v_ax3] = T_subtract[v_ax0, v_ax1, v_ax2, v_ax3] / compute[v_ax0, v_ax1, T.int64(0), T.int64(0)]
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(1), T.int64(1024), T.int64(1), T.int64(1)):
            with T.block("T_reshape_2"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(B[(v_ax1 + v_ax2 + v_ax3) % T.int64(1024)])
                T.writes(T_reshape_2[v_ax0, v_ax1, v_ax2, v_ax3])
                T_reshape_2[v_ax0, v_ax1, v_ax2, v_ax3] = B[(v_ax1 + v_ax2 + v_ax3) % T.int64(1024)]
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(1), T.int64(1024), T.int64(14), T.int64(14)):
            with T.block("T_multiply"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(T_divide[v_ax0, v_ax1, v_ax2, v_ax3], T_reshape_2[v_ax0, v_ax1, T.int64(0), T.int64(0)])
                T.writes(T_multiply[v_ax0, v_ax1, v_ax2, v_ax3])
                T_multiply[v_ax0, v_ax1, v_ax2, v_ax3] = T_divide[v_ax0, v_ax1, v_ax2, v_ax3] * T_reshape_2[v_ax0, v_ax1, T.int64(0), T.int64(0)]
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(1), T.int64(1024), T.int64(1), T.int64(1)):
            with T.block("T_reshape_3"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(C[(v_ax1 + v_ax2 + v_ax3) % T.int64(1024)])
                T.writes(T_reshape_3[v_ax0, v_ax1, v_ax2, v_ax3])
                T_reshape_3[v_ax0, v_ax1, v_ax2, v_ax3] = C[(v_ax1 + v_ax2 + v_ax3) % T.int64(1024)]
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(1), T.int64(1024), T.int64(14), T.int64(14)):
            with T.block("T_add_1"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(T_multiply[v_ax0, v_ax1, v_ax2, v_ax3], T_reshape_3[v_ax0, v_ax1, T.int64(0), T.int64(0)])
                T.writes(T_add[v_ax0, v_ax1, v_ax2, v_ax3])
                T_add[v_ax0, v_ax1, v_ax2, v_ax3] = T_multiply[v_ax0, v_ax1, v_ax2, v_ax3] + T_reshape_3[v_ax0, v_ax1, T.int64(0), T.int64(0)]
        for ax0 in range(T.int64(1024)):
            with T.block("T_multiply_1"):
                v_ax0 = T.axis.spatial(T.int64(1024), ax0)
                T.reads(D[v_ax0])
                T.writes(T_multiply_1[v_ax0])
                T_multiply_1[v_ax0] = T.float32(0.90000000000000002) * D[v_ax0]
        for ax0, k0, k2, k3 in T.grid(T.int64(1024), T.int64(1), T.int64(14), T.int64(14)):
            with T.block("lv165_red"):
                v_ax0, v_k0, v_k2, v_k3 = T.axis.remap("SRRR", [ax0, k0, k2, k3])
                T.reads(lv165[v_k0, v_ax0, v_k2, v_k3])
                T.writes(lv165_red[v_ax0])
                with T.init():
                    lv165_red[v_ax0] = T.float32(0.0)
                lv165_red[v_ax0] = lv165_red[v_ax0] + lv165[v_k0, v_ax0, v_k2, v_k3]
        for ax0 in range(T.int64(1024)):
            with T.block("T_divide_1"):
                v_ax0 = T.axis.spatial(T.int64(1024), ax0)
                T.reads(lv165_red[v_ax0])
                T.writes(T_divide_1[v_ax0])
                T_divide_1[v_ax0] = lv165_red[v_ax0] * T.float32(0.0051020408163265302)
        for ax0 in range(T.int64(1024)):
            with T.block("T_multiply_2"):
                v_ax0 = T.axis.spatial(T.int64(1024), ax0)
                T.reads(T_divide_1[v_ax0])
                T.writes(T_multiply_2[v_ax0])
                T_multiply_2[v_ax0] = T.float32(0.10000000000000001) * T_divide_1[v_ax0]
        for ax0 in range(T.int64(1024)):
            with T.block("T_add_2"):
                v_ax0 = T.axis.spatial(T.int64(1024), ax0)
                T.reads(T_multiply_1[v_ax0], T_multiply_2[v_ax0])
                T.writes(T_add_1[v_ax0])
                T_add_1[v_ax0] = T_multiply_1[v_ax0] + T_multiply_2[v_ax0]
        for ax0 in range(T.int64(1024)):
            with T.block("T_multiply_3"):
                v_ax0 = T.axis.spatial(T.int64(1024), ax0)
                T.reads(E[v_ax0])
                T.writes(T_multiply_3[v_ax0])
                T_multiply_3[v_ax0] = T.float32(0.90000000000000002) * E[v_ax0]
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(1), T.int64(1024), T.int64(1), T.int64(1)):
            with T.block("T_reshape_4"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(T_divide_1[(v_ax1 + v_ax2 + v_ax3) % T.int64(1024)])
                T.writes(T_reshape_4[v_ax0, v_ax1, v_ax2, v_ax3])
                T_reshape_4[v_ax0, v_ax1, v_ax2, v_ax3] = T_divide_1[(v_ax1 + v_ax2 + v_ax3) % T.int64(1024)]
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(1), T.int64(1024), T.int64(14), T.int64(14)):
            with T.block("T_subtract_1"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(lv165[v_ax0, v_ax1, v_ax2, v_ax3], T_reshape_4[v_ax0, v_ax1, T.int64(0), T.int64(0)])
                T.writes(T_subtract_1[v_ax0, v_ax1, v_ax2, v_ax3])
                T_subtract_1[v_ax0, v_ax1, v_ax2, v_ax3] = lv165[v_ax0, v_ax1, v_ax2, v_ax3] - T_reshape_4[v_ax0, v_ax1, T.int64(0), T.int64(0)]
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(1), T.int64(1024), T.int64(14), T.int64(14)):
            with T.block("T_subtract_2"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(lv165[v_ax0, v_ax1, v_ax2, v_ax3], T_reshape_4[v_ax0, v_ax1, T.int64(0), T.int64(0)])
                T.writes(T_subtract_2[v_ax0, v_ax1, v_ax2, v_ax3])
                T_subtract_2[v_ax0, v_ax1, v_ax2, v_ax3] = lv165[v_ax0, v_ax1, v_ax2, v_ax3] - T_reshape_4[v_ax0, v_ax1, T.int64(0), T.int64(0)]
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(1), T.int64(1024), T.int64(14), T.int64(14)):
            with T.block("T_multiply_4"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(T_subtract_1[v_ax0, v_ax1, v_ax2, v_ax3], T_subtract_2[v_ax0, v_ax1, v_ax2, v_ax3])
                T.writes(T_multiply_4[v_ax0, v_ax1, v_ax2, v_ax3])
                T_multiply_4[v_ax0, v_ax1, v_ax2, v_ax3] = T_subtract_1[v_ax0, v_ax1, v_ax2, v_ax3] * T_subtract_2[v_ax0, v_ax1, v_ax2, v_ax3]
        for ax0, k0, k2, k3 in T.grid(T.int64(1024), T.int64(1), T.int64(14), T.int64(14)):
            with T.block("T_multiply_red"):
                v_ax0, v_k0, v_k2, v_k3 = T.axis.remap("SRRR", [ax0, k0, k2, k3])
                T.reads(T_multiply_4[v_k0, v_ax0, v_k2, v_k3])
                T.writes(T_multiply_red[v_ax0])
                with T.init():
                    T_multiply_red[v_ax0] = T.float32(0.0)
                T_multiply_red[v_ax0] = T_multiply_red[v_ax0] + T_multiply_4[v_k0, v_ax0, v_k2, v_k3]
        for ax0 in range(T.int64(1024)):
            with T.block("T_divide_2"):
                v_ax0 = T.axis.spatial(T.int64(1024), ax0)
                T.reads(T_multiply_red[v_ax0])
                T.writes(T_divide_2[v_ax0])
                T_divide_2[v_ax0] = T_multiply_red[v_ax0] * T.float32(0.0051020408163265302)
        for ax0 in range(T.int64(1024)):
            with T.block("T_multiply_5"):
                v_ax0 = T.axis.spatial(T.int64(1024), ax0)
                T.reads(T_divide_2[v_ax0])
                T.writes(T_multiply_5[v_ax0])
                T_multiply_5[v_ax0] = T.float32(0.10000000000000001) * T_divide_2[v_ax0]
        for ax0 in range(T.int64(1024)):
            with T.block("T_add_3"):
                v_ax0 = T.axis.spatial(T.int64(1024), ax0)
                T.reads(T_multiply_3[v_ax0], T_multiply_5[v_ax0])
                T.writes(T_add_2[v_ax0])
                T_add_2[v_ax0] = T_multiply_3[v_ax0] + T_multiply_5[v_ax0]

    @T.prim_func(private=True)
    def conv2d(lv1: T.Buffer((T.int64(1), T.int64(3), T.int64(224), T.int64(224)), "float32"), B: T.Buffer((T.int64(64), T.int64(3), T.int64(7), T.int64(7)), "float32"), conv2d_nchw: T.Buffer((T.int64(1), T.int64(64), T.int64(112), T.int64(112)), "float32")):
        T.func_attr({"tir.noalias": True})
        # with T.block("root"):
        pad_temp = T.alloc_buffer((T.int64(1), T.int64(3), T.int64(230), T.int64(230)))
        for i0, i1, i2, i3 in T.grid(T.int64(1), T.int64(3), T.int64(230), T.int64(230)):
            with T.block("pad_temp"):
                v_i0, v_i1, v_i2, v_i3 = T.axis.remap("SSSS", [i0, i1, i2, i3])
                T.reads(lv1[v_i0, v_i1, v_i2 - T.int64(3), v_i3 - T.int64(3)])
                T.writes(pad_temp[v_i0, v_i1, v_i2, v_i3])
                pad_temp[v_i0, v_i1, v_i2, v_i3] = T.if_then_else(T.int64(3) <= v_i2 and v_i2 < T.int64(227) and T.int64(3) <= v_i3 and v_i3 < T.int64(227), lv1[v_i0, v_i1, v_i2 - T.int64(3), v_i3 - T.int64(3)], T.float32(0.0))
        for nn, ff, yy, xx, rc, ry, rx in T.grid(T.int64(1), T.int64(64), T.int64(112), T.int64(112), T.int64(3), T.int64(7), T.int64(7)):
            with T.block("conv2d_nchw"):
                v_nn, v_ff, v_yy, v_xx, v_rc, v_ry, v_rx = T.axis.remap("SSSSRRR", [nn, ff, yy, xx, rc, ry, rx])
                T.reads(pad_temp[v_nn, v_rc, v_yy * T.int64(2) + v_ry, v_xx * T.int64(2) + v_rx], B[v_ff, v_rc, v_ry, v_rx])
                T.writes(conv2d_nchw[v_nn, v_ff, v_yy, v_xx])
                with T.init():
                    conv2d_nchw[v_nn, v_ff, v_yy, v_xx] = T.float32(0.0)
                conv2d_nchw[v_nn, v_ff, v_yy, v_xx] = conv2d_nchw[v_nn, v_ff, v_yy, v_xx] + pad_temp[v_nn, v_rc, v_yy * T.int64(2) + v_ry, v_xx * T.int64(2) + v_rx] * B[v_ff, v_rc, v_ry, v_rx]

    @T.prim_func(private=True)
    def conv2d1(lv15: T.Buffer((T.int64(1), T.int64(64), T.int64(56), T.int64(56)), "float32"), B: T.Buffer((T.int64(64), T.int64(64), T.int64(1), T.int64(1)), "float32"), conv2d_nchw: T.Buffer((T.int64(1), T.int64(64), T.int64(56), T.int64(56)), "float32")):
        T.func_attr({"tir.noalias": True})
        # with T.block("root"):
        pad_temp = T.alloc_buffer((T.int64(1), T.int64(64), T.int64(56), T.int64(56)))
        for i0, i1, i2, i3 in T.grid(T.int64(1), T.int64(64), T.int64(56), T.int64(56)):
            with T.block("pad_temp"):
                v_i0, v_i1, v_i2, v_i3 = T.axis.remap("SSSS", [i0, i1, i2, i3])
                T.reads(lv15[v_i0, v_i1, v_i2, v_i3])
                T.writes(pad_temp[v_i0, v_i1, v_i2, v_i3])
                pad_temp[v_i0, v_i1, v_i2, v_i3] = lv15[v_i0, v_i1, v_i2, v_i3]
        for nn, ff, yy, xx, rc, ry, rx in T.grid(T.int64(1), T.int64(64), T.int64(56), T.int64(56), T.int64(64), T.int64(1), T.int64(1)):
            with T.block("conv2d_nchw"):
                v_nn, v_ff, v_yy, v_xx, v_rc, v_ry, v_rx = T.axis.remap("SSSSRRR", [nn, ff, yy, xx, rc, ry, rx])
                T.reads(pad_temp[v_nn, v_rc, v_yy + v_ry, v_xx + v_rx], B[v_ff, v_rc, v_ry, v_rx])
                T.writes(conv2d_nchw[v_nn, v_ff, v_yy, v_xx])
                with T.init():
                    conv2d_nchw[v_nn, v_ff, v_yy, v_xx] = T.float32(0.0)
                conv2d_nchw[v_nn, v_ff, v_yy, v_xx] = conv2d_nchw[v_nn, v_ff, v_yy, v_xx] + pad_temp[v_nn, v_rc, v_yy + v_ry, v_xx + v_rx] * B[v_ff, v_rc, v_ry, v_rx]

    @T.prim_func(private=True)
    def conv2d10(lv99: T.Buffer((T.int64(1), T.int64(128), T.int64(28), T.int64(28)), "float32"), B: T.Buffer((T.int64(128), T.int64(128), T.int64(3), T.int64(3)), "float32"), conv2d_nchw: T.Buffer((T.int64(1), T.int64(128), T.int64(28), T.int64(28)), "float32")):
        T.func_attr({"tir.noalias": True})
        # with T.block("root"):
        pad_temp = T.alloc_buffer((T.int64(1), T.int64(128), T.int64(30), T.int64(30)))
        for i0, i1, i2, i3 in T.grid(T.int64(1), T.int64(128), T.int64(30), T.int64(30)):
            with T.block("pad_temp"):
                v_i0, v_i1, v_i2, v_i3 = T.axis.remap("SSSS", [i0, i1, i2, i3])
                T.reads(lv99[v_i0, v_i1, v_i2 - T.int64(1), v_i3 - T.int64(1)])
                T.writes(pad_temp[v_i0, v_i1, v_i2, v_i3])
                pad_temp[v_i0, v_i1, v_i2, v_i3] = T.if_then_else(T.int64(1) <= v_i2 and v_i2 < T.int64(29) and T.int64(1) <= v_i3 and v_i3 < T.int64(29), lv99[v_i0, v_i1, v_i2 - T.int64(1), v_i3 - T.int64(1)], T.float32(0.0))
        for nn, ff, yy, xx, rc, ry, rx in T.grid(T.int64(1), T.int64(128), T.int64(28), T.int64(28), T.int64(128), T.int64(3), T.int64(3)):
            with T.block("conv2d_nchw"):
                v_nn, v_ff, v_yy, v_xx, v_rc, v_ry, v_rx = T.axis.remap("SSSSRRR", [nn, ff, yy, xx, rc, ry, rx])
                T.reads(pad_temp[v_nn, v_rc, v_yy + v_ry, v_xx + v_rx], B[v_ff, v_rc, v_ry, v_rx])
                T.writes(conv2d_nchw[v_nn, v_ff, v_yy, v_xx])
                with T.init():
                    conv2d_nchw[v_nn, v_ff, v_yy, v_xx] = T.float32(0.0)
                conv2d_nchw[v_nn, v_ff, v_yy, v_xx] = conv2d_nchw[v_nn, v_ff, v_yy, v_xx] + pad_temp[v_nn, v_rc, v_yy + v_ry, v_xx + v_rx] * B[v_ff, v_rc, v_ry, v_rx]

    @T.prim_func(private=True)
    def conv2d11(lv150: T.Buffer((T.int64(1), T.int64(512), T.int64(28), T.int64(28)), "float32"), B: T.Buffer((T.int64(256), T.int64(512), T.int64(1), T.int64(1)), "float32"), conv2d_nchw: T.Buffer((T.int64(1), T.int64(256), T.int64(28), T.int64(28)), "float32")):
        T.func_attr({"tir.noalias": True})
        # with T.block("root"):
        pad_temp = T.alloc_buffer((T.int64(1), T.int64(512), T.int64(28), T.int64(28)))
        for i0, i1, i2, i3 in T.grid(T.int64(1), T.int64(512), T.int64(28), T.int64(28)):
            with T.block("pad_temp"):
                v_i0, v_i1, v_i2, v_i3 = T.axis.remap("SSSS", [i0, i1, i2, i3])
                T.reads(lv150[v_i0, v_i1, v_i2, v_i3])
                T.writes(pad_temp[v_i0, v_i1, v_i2, v_i3])
                pad_temp[v_i0, v_i1, v_i2, v_i3] = lv150[v_i0, v_i1, v_i2, v_i3]
        for nn, ff, yy, xx, rc, ry, rx in T.grid(T.int64(1), T.int64(256), T.int64(28), T.int64(28), T.int64(512), T.int64(1), T.int64(1)):
            with T.block("conv2d_nchw"):
                v_nn, v_ff, v_yy, v_xx, v_rc, v_ry, v_rx = T.axis.remap("SSSSRRR", [nn, ff, yy, xx, rc, ry, rx])
                T.reads(pad_temp[v_nn, v_rc, v_yy + v_ry, v_xx + v_rx], B[v_ff, v_rc, v_ry, v_rx])
                T.writes(conv2d_nchw[v_nn, v_ff, v_yy, v_xx])
                with T.init():
                    conv2d_nchw[v_nn, v_ff, v_yy, v_xx] = T.float32(0.0)
                conv2d_nchw[v_nn, v_ff, v_yy, v_xx] = conv2d_nchw[v_nn, v_ff, v_yy, v_xx] + pad_temp[v_nn, v_rc, v_yy + v_ry, v_xx + v_rx] * B[v_ff, v_rc, v_ry, v_rx]

    @T.prim_func(private=True)
    def conv2d12(lv156: T.Buffer((T.int64(1), T.int64(256), T.int64(28), T.int64(28)), "float32"), B: T.Buffer((T.int64(256), T.int64(256), T.int64(3), T.int64(3)), "float32"), conv2d_nchw: T.Buffer((T.int64(1), T.int64(256), T.int64(14), T.int64(14)), "float32")):
        T.func_attr({"tir.noalias": True})
        # with T.block("root"):
        pad_temp = T.alloc_buffer((T.int64(1), T.int64(256), T.int64(30), T.int64(30)))
        for i0, i1, i2, i3 in T.grid(T.int64(1), T.int64(256), T.int64(30), T.int64(30)):
            with T.block("pad_temp"):
                v_i0, v_i1, v_i2, v_i3 = T.axis.remap("SSSS", [i0, i1, i2, i3])
                T.reads(lv156[v_i0, v_i1, v_i2 - T.int64(1), v_i3 - T.int64(1)])
                T.writes(pad_temp[v_i0, v_i1, v_i2, v_i3])
                pad_temp[v_i0, v_i1, v_i2, v_i3] = T.if_then_else(T.int64(1) <= v_i2 and v_i2 < T.int64(29) and T.int64(1) <= v_i3 and v_i3 < T.int64(29), lv156[v_i0, v_i1, v_i2 - T.int64(1), v_i3 - T.int64(1)], T.float32(0.0))
        for nn, ff, yy, xx, rc, ry, rx in T.grid(T.int64(1), T.int64(256), T.int64(14), T.int64(14), T.int64(256), T.int64(3), T.int64(3)):
            with T.block("conv2d_nchw"):
                v_nn, v_ff, v_yy, v_xx, v_rc, v_ry, v_rx = T.axis.remap("SSSSRRR", [nn, ff, yy, xx, rc, ry, rx])
                T.reads(pad_temp[v_nn, v_rc, v_yy * T.int64(2) + v_ry, v_xx * T.int64(2) + v_rx], B[v_ff, v_rc, v_ry, v_rx])
                T.writes(conv2d_nchw[v_nn, v_ff, v_yy, v_xx])
                with T.init():
                    conv2d_nchw[v_nn, v_ff, v_yy, v_xx] = T.float32(0.0)
                conv2d_nchw[v_nn, v_ff, v_yy, v_xx] = conv2d_nchw[v_nn, v_ff, v_yy, v_xx] + pad_temp[v_nn, v_rc, v_yy * T.int64(2) + v_ry, v_xx * T.int64(2) + v_rx] * B[v_ff, v_rc, v_ry, v_rx]

    @T.prim_func(private=True)
    def conv2d13(lv162: T.Buffer((T.int64(1), T.int64(256), T.int64(14), T.int64(14)), "float32"), B: T.Buffer((T.int64(1024), T.int64(256), T.int64(1), T.int64(1)), "float32"), conv2d_nchw: T.Buffer((T.int64(1), T.int64(1024), T.int64(14), T.int64(14)), "float32")):
        T.func_attr({"tir.noalias": True})
        # with T.block("root"):
        pad_temp = T.alloc_buffer((T.int64(1), T.int64(256), T.int64(14), T.int64(14)))
        for i0, i1, i2, i3 in T.grid(T.int64(1), T.int64(256), T.int64(14), T.int64(14)):
            with T.block("pad_temp"):
                v_i0, v_i1, v_i2, v_i3 = T.axis.remap("SSSS", [i0, i1, i2, i3])
                T.reads(lv162[v_i0, v_i1, v_i2, v_i3])
                T.writes(pad_temp[v_i0, v_i1, v_i2, v_i3])
                pad_temp[v_i0, v_i1, v_i2, v_i3] = lv162[v_i0, v_i1, v_i2, v_i3]
        for nn, ff, yy, xx, rc, ry, rx in T.grid(T.int64(1), T.int64(1024), T.int64(14), T.int64(14), T.int64(256), T.int64(1), T.int64(1)):
            with T.block("conv2d_nchw"):
                v_nn, v_ff, v_yy, v_xx, v_rc, v_ry, v_rx = T.axis.remap("SSSSRRR", [nn, ff, yy, xx, rc, ry, rx])
                T.reads(pad_temp[v_nn, v_rc, v_yy + v_ry, v_xx + v_rx], B[v_ff, v_rc, v_ry, v_rx])
                T.writes(conv2d_nchw[v_nn, v_ff, v_yy, v_xx])
                with T.init():
                    conv2d_nchw[v_nn, v_ff, v_yy, v_xx] = T.float32(0.0)
                conv2d_nchw[v_nn, v_ff, v_yy, v_xx] = conv2d_nchw[v_nn, v_ff, v_yy, v_xx] + pad_temp[v_nn, v_rc, v_yy + v_ry, v_xx + v_rx] * B[v_ff, v_rc, v_ry, v_rx]

    @T.prim_func(private=True)
    def conv2d14(lv150: T.Buffer((T.int64(1), T.int64(512), T.int64(28), T.int64(28)), "float32"), B: T.Buffer((T.int64(1024), T.int64(512), T.int64(1), T.int64(1)), "float32"), conv2d_nchw: T.Buffer((T.int64(1), T.int64(1024), T.int64(14), T.int64(14)), "float32")):
        T.func_attr({"tir.noalias": True})
        # with T.block("root"):
        pad_temp = T.alloc_buffer((T.int64(1), T.int64(512), T.int64(28), T.int64(28)))
        for i0, i1, i2, i3 in T.grid(T.int64(1), T.int64(512), T.int64(28), T.int64(28)):
            with T.block("pad_temp"):
                v_i0, v_i1, v_i2, v_i3 = T.axis.remap("SSSS", [i0, i1, i2, i3])
                T.reads(lv150[v_i0, v_i1, v_i2, v_i3])
                T.writes(pad_temp[v_i0, v_i1, v_i2, v_i3])
                pad_temp[v_i0, v_i1, v_i2, v_i3] = lv150[v_i0, v_i1, v_i2, v_i3]
        for nn, ff, yy, xx, rc, ry, rx in T.grid(T.int64(1), T.int64(1024), T.int64(14), T.int64(14), T.int64(512), T.int64(1), T.int64(1)):
            with T.block("conv2d_nchw"):
                v_nn, v_ff, v_yy, v_xx, v_rc, v_ry, v_rx = T.axis.remap("SSSSRRR", [nn, ff, yy, xx, rc, ry, rx])
                T.reads(pad_temp[v_nn, v_rc, v_yy * T.int64(2) + v_ry, v_xx * T.int64(2) + v_rx], B[v_ff, v_rc, v_ry, v_rx])
                T.writes(conv2d_nchw[v_nn, v_ff, v_yy, v_xx])
                with T.init():
                    conv2d_nchw[v_nn, v_ff, v_yy, v_xx] = T.float32(0.0)
                conv2d_nchw[v_nn, v_ff, v_yy, v_xx] = conv2d_nchw[v_nn, v_ff, v_yy, v_xx] + pad_temp[v_nn, v_rc, v_yy * T.int64(2) + v_ry, v_xx * T.int64(2) + v_rx] * B[v_ff, v_rc, v_ry, v_rx]

    @T.prim_func(private=True)
    def conv2d15(lv170: T.Buffer((T.int64(1), T.int64(1024), T.int64(14), T.int64(14)), "float32"), B: T.Buffer((T.int64(256), T.int64(1024), T.int64(1), T.int64(1)), "float32"), conv2d_nchw: T.Buffer((T.int64(1), T.int64(256), T.int64(14), T.int64(14)), "float32")):
        T.func_attr({"tir.noalias": True})
        # with T.block("root"):
        pad_temp = T.alloc_buffer((T.int64(1), T.int64(1024), T.int64(14), T.int64(14)))
        for i0, i1, i2, i3 in T.grid(T.int64(1), T.int64(1024), T.int64(14), T.int64(14)):
            with T.block("pad_temp"):
                v_i0, v_i1, v_i2, v_i3 = T.axis.remap("SSSS", [i0, i1, i2, i3])
                T.reads(lv170[v_i0, v_i1, v_i2, v_i3])
                T.writes(pad_temp[v_i0, v_i1, v_i2, v_i3])
                pad_temp[v_i0, v_i1, v_i2, v_i3] = lv170[v_i0, v_i1, v_i2, v_i3]
        for nn, ff, yy, xx, rc, ry, rx in T.grid(T.int64(1), T.int64(256), T.int64(14), T.int64(14), T.int64(1024), T.int64(1), T.int64(1)):
            with T.block("conv2d_nchw"):
                v_nn, v_ff, v_yy, v_xx, v_rc, v_ry, v_rx = T.axis.remap("SSSSRRR", [nn, ff, yy, xx, rc, ry, rx])
                T.reads(pad_temp[v_nn, v_rc, v_yy + v_ry, v_xx + v_rx], B[v_ff, v_rc, v_ry, v_rx])
                T.writes(conv2d_nchw[v_nn, v_ff, v_yy, v_xx])
                with T.init():
                    conv2d_nchw[v_nn, v_ff, v_yy, v_xx] = T.float32(0.0)
                conv2d_nchw[v_nn, v_ff, v_yy, v_xx] = conv2d_nchw[v_nn, v_ff, v_yy, v_xx] + pad_temp[v_nn, v_rc, v_yy + v_ry, v_xx + v_rx] * B[v_ff, v_rc, v_ry, v_rx]

    @T.prim_func(private=True)
    def conv2d16(lv176: T.Buffer((T.int64(1), T.int64(256), T.int64(14), T.int64(14)), "float32"), B: T.Buffer((T.int64(256), T.int64(256), T.int64(3), T.int64(3)), "float32"), conv2d_nchw: T.Buffer((T.int64(1), T.int64(256), T.int64(14), T.int64(14)), "float32")):
        T.func_attr({"tir.noalias": True})
        # with T.block("root"):
        pad_temp = T.alloc_buffer((T.int64(1), T.int64(256), T.int64(16), T.int64(16)))
        for i0, i1, i2, i3 in T.grid(T.int64(1), T.int64(256), T.int64(16), T.int64(16)):
            with T.block("pad_temp"):
                v_i0, v_i1, v_i2, v_i3 = T.axis.remap("SSSS", [i0, i1, i2, i3])
                T.reads(lv176[v_i0, v_i1, v_i2 - T.int64(1), v_i3 - T.int64(1)])
                T.writes(pad_temp[v_i0, v_i1, v_i2, v_i3])
                pad_temp[v_i0, v_i1, v_i2, v_i3] = T.if_then_else(T.int64(1) <= v_i2 and v_i2 < T.int64(15) and T.int64(1) <= v_i3 and v_i3 < T.int64(15), lv176[v_i0, v_i1, v_i2 - T.int64(1), v_i3 - T.int64(1)], T.float32(0.0))
        for nn, ff, yy, xx, rc, ry, rx in T.grid(T.int64(1), T.int64(256), T.int64(14), T.int64(14), T.int64(256), T.int64(3), T.int64(3)):
            with T.block("conv2d_nchw"):
                v_nn, v_ff, v_yy, v_xx, v_rc, v_ry, v_rx = T.axis.remap("SSSSRRR", [nn, ff, yy, xx, rc, ry, rx])
                T.reads(pad_temp[v_nn, v_rc, v_yy + v_ry, v_xx + v_rx], B[v_ff, v_rc, v_ry, v_rx])
                T.writes(conv2d_nchw[v_nn, v_ff, v_yy, v_xx])
                with T.init():
                    conv2d_nchw[v_nn, v_ff, v_yy, v_xx] = T.float32(0.0)
                conv2d_nchw[v_nn, v_ff, v_yy, v_xx] = conv2d_nchw[v_nn, v_ff, v_yy, v_xx] + pad_temp[v_nn, v_rc, v_yy + v_ry, v_xx + v_rx] * B[v_ff, v_rc, v_ry, v_rx]

    @T.prim_func(private=True)
    def conv2d17(lv265: T.Buffer((T.int64(1), T.int64(1024), T.int64(14), T.int64(14)), "float32"), B: T.Buffer((T.int64(512), T.int64(1024), T.int64(1), T.int64(1)), "float32"), conv2d_nchw: T.Buffer((T.int64(1), T.int64(512), T.int64(14), T.int64(14)), "float32")):
        T.func_attr({"tir.noalias": True})
        # with T.block("root"):
        pad_temp = T.alloc_buffer((T.int64(1), T.int64(1024), T.int64(14), T.int64(14)))
        for i0, i1, i2, i3 in T.grid(T.int64(1), T.int64(1024), T.int64(14), T.int64(14)):
            with T.block("pad_temp"):
                v_i0, v_i1, v_i2, v_i3 = T.axis.remap("SSSS", [i0, i1, i2, i3])
                T.reads(lv265[v_i0, v_i1, v_i2, v_i3])
                T.writes(pad_temp[v_i0, v_i1, v_i2, v_i3])
                pad_temp[v_i0, v_i1, v_i2, v_i3] = lv265[v_i0, v_i1, v_i2, v_i3]
        for nn, ff, yy, xx, rc, ry, rx in T.grid(T.int64(1), T.int64(512), T.int64(14), T.int64(14), T.int64(1024), T.int64(1), T.int64(1)):
            with T.block("conv2d_nchw"):
                v_nn, v_ff, v_yy, v_xx, v_rc, v_ry, v_rx = T.axis.remap("SSSSRRR", [nn, ff, yy, xx, rc, ry, rx])
                T.reads(pad_temp[v_nn, v_rc, v_yy + v_ry, v_xx + v_rx], B[v_ff, v_rc, v_ry, v_rx])
                T.writes(conv2d_nchw[v_nn, v_ff, v_yy, v_xx])
                with T.init():
                    conv2d_nchw[v_nn, v_ff, v_yy, v_xx] = T.float32(0.0)
                conv2d_nchw[v_nn, v_ff, v_yy, v_xx] = conv2d_nchw[v_nn, v_ff, v_yy, v_xx] + pad_temp[v_nn, v_rc, v_yy + v_ry, v_xx + v_rx] * B[v_ff, v_rc, v_ry, v_rx]

    @T.prim_func(private=True)
    def conv2d18(lv271: T.Buffer((T.int64(1), T.int64(512), T.int64(14), T.int64(14)), "float32"), B: T.Buffer((T.int64(512), T.int64(512), T.int64(3), T.int64(3)), "float32"), conv2d_nchw: T.Buffer((T.int64(1), T.int64(512), T.int64(7), T.int64(7)), "float32")):
        T.func_attr({"tir.noalias": True})
        # with T.block("root"):
        pad_temp = T.alloc_buffer((T.int64(1), T.int64(512), T.int64(16), T.int64(16)))
        for i0, i1, i2, i3 in T.grid(T.int64(1), T.int64(512), T.int64(16), T.int64(16)):
            with T.block("pad_temp"):
                v_i0, v_i1, v_i2, v_i3 = T.axis.remap("SSSS", [i0, i1, i2, i3])
                T.reads(lv271[v_i0, v_i1, v_i2 - T.int64(1), v_i3 - T.int64(1)])
                T.writes(pad_temp[v_i0, v_i1, v_i2, v_i3])
                pad_temp[v_i0, v_i1, v_i2, v_i3] = T.if_then_else(T.int64(1) <= v_i2 and v_i2 < T.int64(15) and T.int64(1) <= v_i3 and v_i3 < T.int64(15), lv271[v_i0, v_i1, v_i2 - T.int64(1), v_i3 - T.int64(1)], T.float32(0.0))
        for nn, ff, yy, xx, rc, ry, rx in T.grid(T.int64(1), T.int64(512), T.int64(7), T.int64(7), T.int64(512), T.int64(3), T.int64(3)):
            with T.block("conv2d_nchw"):
                v_nn, v_ff, v_yy, v_xx, v_rc, v_ry, v_rx = T.axis.remap("SSSSRRR", [nn, ff, yy, xx, rc, ry, rx])
                T.reads(pad_temp[v_nn, v_rc, v_yy * T.int64(2) + v_ry, v_xx * T.int64(2) + v_rx], B[v_ff, v_rc, v_ry, v_rx])
                T.writes(conv2d_nchw[v_nn, v_ff, v_yy, v_xx])
                with T.init():
                    conv2d_nchw[v_nn, v_ff, v_yy, v_xx] = T.float32(0.0)
                conv2d_nchw[v_nn, v_ff, v_yy, v_xx] = conv2d_nchw[v_nn, v_ff, v_yy, v_xx] + pad_temp[v_nn, v_rc, v_yy * T.int64(2) + v_ry, v_xx * T.int64(2) + v_rx] * B[v_ff, v_rc, v_ry, v_rx]

    @T.prim_func(private=True)
    def conv2d19(lv277: T.Buffer((T.int64(1), T.int64(512), T.int64(7), T.int64(7)), "float32"), B: T.Buffer((T.int64(2048), T.int64(512), T.int64(1), T.int64(1)), "float32"), conv2d_nchw: T.Buffer((T.int64(1), T.int64(2048), T.int64(7), T.int64(7)), "float32")):
        T.func_attr({"tir.noalias": True})
        # with T.block("root"):
        pad_temp = T.alloc_buffer((T.int64(1), T.int64(512), T.int64(7), T.int64(7)))
        for i0, i1, i2, i3 in T.grid(T.int64(1), T.int64(512), T.int64(7), T.int64(7)):
            with T.block("pad_temp"):
                v_i0, v_i1, v_i2, v_i3 = T.axis.remap("SSSS", [i0, i1, i2, i3])
                T.reads(lv277[v_i0, v_i1, v_i2, v_i3])
                T.writes(pad_temp[v_i0, v_i1, v_i2, v_i3])
                pad_temp[v_i0, v_i1, v_i2, v_i3] = lv277[v_i0, v_i1, v_i2, v_i3]
        for nn, ff, yy, xx, rc, ry, rx in T.grid(T.int64(1), T.int64(2048), T.int64(7), T.int64(7), T.int64(512), T.int64(1), T.int64(1)):
            with T.block("conv2d_nchw"):
                v_nn, v_ff, v_yy, v_xx, v_rc, v_ry, v_rx = T.axis.remap("SSSSRRR", [nn, ff, yy, xx, rc, ry, rx])
                T.reads(pad_temp[v_nn, v_rc, v_yy + v_ry, v_xx + v_rx], B[v_ff, v_rc, v_ry, v_rx])
                T.writes(conv2d_nchw[v_nn, v_ff, v_yy, v_xx])
                with T.init():
                    conv2d_nchw[v_nn, v_ff, v_yy, v_xx] = T.float32(0.0)
                conv2d_nchw[v_nn, v_ff, v_yy, v_xx] = conv2d_nchw[v_nn, v_ff, v_yy, v_xx] + pad_temp[v_nn, v_rc, v_yy + v_ry, v_xx + v_rx] * B[v_ff, v_rc, v_ry, v_rx]

    @T.prim_func(private=True)
    def conv2d2(lv21: T.Buffer((T.int64(1), T.int64(64), T.int64(56), T.int64(56)), "float32"), B: T.Buffer((T.int64(64), T.int64(64), T.int64(3), T.int64(3)), "float32"), conv2d_nchw: T.Buffer((T.int64(1), T.int64(64), T.int64(56), T.int64(56)), "float32")):
        T.func_attr({"tir.noalias": True})
        # with T.block("root"):
        pad_temp = T.alloc_buffer((T.int64(1), T.int64(64), T.int64(58), T.int64(58)))
        for i0, i1, i2, i3 in T.grid(T.int64(1), T.int64(64), T.int64(58), T.int64(58)):
            with T.block("pad_temp"):
                v_i0, v_i1, v_i2, v_i3 = T.axis.remap("SSSS", [i0, i1, i2, i3])
                T.reads(lv21[v_i0, v_i1, v_i2 - T.int64(1), v_i3 - T.int64(1)])
                T.writes(pad_temp[v_i0, v_i1, v_i2, v_i3])
                pad_temp[v_i0, v_i1, v_i2, v_i3] = T.if_then_else(T.int64(1) <= v_i2 and v_i2 < T.int64(57) and T.int64(1) <= v_i3 and v_i3 < T.int64(57), lv21[v_i0, v_i1, v_i2 - T.int64(1), v_i3 - T.int64(1)], T.float32(0.0))
        for nn, ff, yy, xx, rc, ry, rx in T.grid(T.int64(1), T.int64(64), T.int64(56), T.int64(56), T.int64(64), T.int64(3), T.int64(3)):
            with T.block("conv2d_nchw"):
                v_nn, v_ff, v_yy, v_xx, v_rc, v_ry, v_rx = T.axis.remap("SSSSRRR", [nn, ff, yy, xx, rc, ry, rx])
                T.reads(pad_temp[v_nn, v_rc, v_yy + v_ry, v_xx + v_rx], B[v_ff, v_rc, v_ry, v_rx])
                T.writes(conv2d_nchw[v_nn, v_ff, v_yy, v_xx])
                with T.init():
                    conv2d_nchw[v_nn, v_ff, v_yy, v_xx] = T.float32(0.0)
                conv2d_nchw[v_nn, v_ff, v_yy, v_xx] = conv2d_nchw[v_nn, v_ff, v_yy, v_xx] + pad_temp[v_nn, v_rc, v_yy + v_ry, v_xx + v_rx] * B[v_ff, v_rc, v_ry, v_rx]

    @T.prim_func(private=True)
    def conv2d20(lv265: T.Buffer((T.int64(1), T.int64(1024), T.int64(14), T.int64(14)), "float32"), B: T.Buffer((T.int64(2048), T.int64(1024), T.int64(1), T.int64(1)), "float32"), conv2d_nchw: T.Buffer((T.int64(1), T.int64(2048), T.int64(7), T.int64(7)), "float32")):
        T.func_attr({"tir.noalias": True})
        # with T.block("root"):
        pad_temp = T.alloc_buffer((T.int64(1), T.int64(1024), T.int64(14), T.int64(14)))
        for i0, i1, i2, i3 in T.grid(T.int64(1), T.int64(1024), T.int64(14), T.int64(14)):
            with T.block("pad_temp"):
                v_i0, v_i1, v_i2, v_i3 = T.axis.remap("SSSS", [i0, i1, i2, i3])
                T.reads(lv265[v_i0, v_i1, v_i2, v_i3])
                T.writes(pad_temp[v_i0, v_i1, v_i2, v_i3])
                pad_temp[v_i0, v_i1, v_i2, v_i3] = lv265[v_i0, v_i1, v_i2, v_i3]
        for nn, ff, yy, xx, rc, ry, rx in T.grid(T.int64(1), T.int64(2048), T.int64(7), T.int64(7), T.int64(1024), T.int64(1), T.int64(1)):
            with T.block("conv2d_nchw"):
                v_nn, v_ff, v_yy, v_xx, v_rc, v_ry, v_rx = T.axis.remap("SSSSRRR", [nn, ff, yy, xx, rc, ry, rx])
                T.reads(pad_temp[v_nn, v_rc, v_yy * T.int64(2) + v_ry, v_xx * T.int64(2) + v_rx], B[v_ff, v_rc, v_ry, v_rx])
                T.writes(conv2d_nchw[v_nn, v_ff, v_yy, v_xx])
                with T.init():
                    conv2d_nchw[v_nn, v_ff, v_yy, v_xx] = T.float32(0.0)
                conv2d_nchw[v_nn, v_ff, v_yy, v_xx] = conv2d_nchw[v_nn, v_ff, v_yy, v_xx] + pad_temp[v_nn, v_rc, v_yy * T.int64(2) + v_ry, v_xx * T.int64(2) + v_rx] * B[v_ff, v_rc, v_ry, v_rx]

    @T.prim_func(private=True)
    def conv2d21(lv285: T.Buffer((T.int64(1), T.int64(2048), T.int64(7), T.int64(7)), "float32"), B: T.Buffer((T.int64(512), T.int64(2048), T.int64(1), T.int64(1)), "float32"), conv2d_nchw: T.Buffer((T.int64(1), T.int64(512), T.int64(7), T.int64(7)), "float32")):
        T.func_attr({"tir.noalias": True})
        # with T.block("root"):
        pad_temp = T.alloc_buffer((T.int64(1), T.int64(2048), T.int64(7), T.int64(7)))
        for i0, i1, i2, i3 in T.grid(T.int64(1), T.int64(2048), T.int64(7), T.int64(7)):
            with T.block("pad_temp"):
                v_i0, v_i1, v_i2, v_i3 = T.axis.remap("SSSS", [i0, i1, i2, i3])
                T.reads(lv285[v_i0, v_i1, v_i2, v_i3])
                T.writes(pad_temp[v_i0, v_i1, v_i2, v_i3])
                pad_temp[v_i0, v_i1, v_i2, v_i3] = lv285[v_i0, v_i1, v_i2, v_i3]
        for nn, ff, yy, xx, rc, ry, rx in T.grid(T.int64(1), T.int64(512), T.int64(7), T.int64(7), T.int64(2048), T.int64(1), T.int64(1)):
            with T.block("conv2d_nchw"):
                v_nn, v_ff, v_yy, v_xx, v_rc, v_ry, v_rx = T.axis.remap("SSSSRRR", [nn, ff, yy, xx, rc, ry, rx])
                T.reads(pad_temp[v_nn, v_rc, v_yy + v_ry, v_xx + v_rx], B[v_ff, v_rc, v_ry, v_rx])
                T.writes(conv2d_nchw[v_nn, v_ff, v_yy, v_xx])
                with T.init():
                    conv2d_nchw[v_nn, v_ff, v_yy, v_xx] = T.float32(0.0)
                conv2d_nchw[v_nn, v_ff, v_yy, v_xx] = conv2d_nchw[v_nn, v_ff, v_yy, v_xx] + pad_temp[v_nn, v_rc, v_yy + v_ry, v_xx + v_rx] * B[v_ff, v_rc, v_ry, v_rx]

    @T.prim_func(private=True)
    def conv2d22(lv291: T.Buffer((T.int64(1), T.int64(512), T.int64(7), T.int64(7)), "float32"), B: T.Buffer((T.int64(512), T.int64(512), T.int64(3), T.int64(3)), "float32"), conv2d_nchw: T.Buffer((T.int64(1), T.int64(512), T.int64(7), T.int64(7)), "float32")):
        T.func_attr({"tir.noalias": True})
        # with T.block("root"):
        pad_temp = T.alloc_buffer((T.int64(1), T.int64(512), T.int64(9), T.int64(9)))
        for i0, i1, i2, i3 in T.grid(T.int64(1), T.int64(512), T.int64(9), T.int64(9)):
            with T.block("pad_temp"):
                v_i0, v_i1, v_i2, v_i3 = T.axis.remap("SSSS", [i0, i1, i2, i3])
                T.reads(lv291[v_i0, v_i1, v_i2 - T.int64(1), v_i3 - T.int64(1)])
                T.writes(pad_temp[v_i0, v_i1, v_i2, v_i3])
                pad_temp[v_i0, v_i1, v_i2, v_i3] = T.if_then_else(T.int64(1) <= v_i2 and v_i2 < T.int64(8) and T.int64(1) <= v_i3 and v_i3 < T.int64(8), lv291[v_i0, v_i1, v_i2 - T.int64(1), v_i3 - T.int64(1)], T.float32(0.0))
        for nn, ff, yy, xx, rc, ry, rx in T.grid(T.int64(1), T.int64(512), T.int64(7), T.int64(7), T.int64(512), T.int64(3), T.int64(3)):
            with T.block("conv2d_nchw"):
                v_nn, v_ff, v_yy, v_xx, v_rc, v_ry, v_rx = T.axis.remap("SSSSRRR", [nn, ff, yy, xx, rc, ry, rx])
                T.reads(pad_temp[v_nn, v_rc, v_yy + v_ry, v_xx + v_rx], B[v_ff, v_rc, v_ry, v_rx])
                T.writes(conv2d_nchw[v_nn, v_ff, v_yy, v_xx])
                with T.init():
                    conv2d_nchw[v_nn, v_ff, v_yy, v_xx] = T.float32(0.0)
                conv2d_nchw[v_nn, v_ff, v_yy, v_xx] = conv2d_nchw[v_nn, v_ff, v_yy, v_xx] + pad_temp[v_nn, v_rc, v_yy + v_ry, v_xx + v_rx] * B[v_ff, v_rc, v_ry, v_rx]

    @T.prim_func(private=True)
    def conv2d3(lv27: T.Buffer((T.int64(1), T.int64(64), T.int64(56), T.int64(56)), "float32"), B: T.Buffer((T.int64(256), T.int64(64), T.int64(1), T.int64(1)), "float32"), conv2d_nchw: T.Buffer((T.int64(1), T.int64(256), T.int64(56), T.int64(56)), "float32")):
        T.func_attr({"tir.noalias": True})
        # with T.block("root"):
        pad_temp = T.alloc_buffer((T.int64(1), T.int64(64), T.int64(56), T.int64(56)))
        for i0, i1, i2, i3 in T.grid(T.int64(1), T.int64(64), T.int64(56), T.int64(56)):
            with T.block("pad_temp"):
                v_i0, v_i1, v_i2, v_i3 = T.axis.remap("SSSS", [i0, i1, i2, i3])
                T.reads(lv27[v_i0, v_i1, v_i2, v_i3])
                T.writes(pad_temp[v_i0, v_i1, v_i2, v_i3])
                pad_temp[v_i0, v_i1, v_i2, v_i3] = lv27[v_i0, v_i1, v_i2, v_i3]
        for nn, ff, yy, xx, rc, ry, rx in T.grid(T.int64(1), T.int64(256), T.int64(56), T.int64(56), T.int64(64), T.int64(1), T.int64(1)):
            with T.block("conv2d_nchw"):
                v_nn, v_ff, v_yy, v_xx, v_rc, v_ry, v_rx = T.axis.remap("SSSSRRR", [nn, ff, yy, xx, rc, ry, rx])
                T.reads(pad_temp[v_nn, v_rc, v_yy + v_ry, v_xx + v_rx], B[v_ff, v_rc, v_ry, v_rx])
                T.writes(conv2d_nchw[v_nn, v_ff, v_yy, v_xx])
                with T.init():
                    conv2d_nchw[v_nn, v_ff, v_yy, v_xx] = T.float32(0.0)
                conv2d_nchw[v_nn, v_ff, v_yy, v_xx] = conv2d_nchw[v_nn, v_ff, v_yy, v_xx] + pad_temp[v_nn, v_rc, v_yy + v_ry, v_xx + v_rx] * B[v_ff, v_rc, v_ry, v_rx]

    @T.prim_func(private=True)
    def conv2d4(lv35: T.Buffer((T.int64(1), T.int64(256), T.int64(56), T.int64(56)), "float32"), B: T.Buffer((T.int64(64), T.int64(256), T.int64(1), T.int64(1)), "float32"), conv2d_nchw: T.Buffer((T.int64(1), T.int64(64), T.int64(56), T.int64(56)), "float32")):
        T.func_attr({"tir.noalias": True})
        # with T.block("root"):
        pad_temp = T.alloc_buffer((T.int64(1), T.int64(256), T.int64(56), T.int64(56)))
        for i0, i1, i2, i3 in T.grid(T.int64(1), T.int64(256), T.int64(56), T.int64(56)):
            with T.block("pad_temp"):
                v_i0, v_i1, v_i2, v_i3 = T.axis.remap("SSSS", [i0, i1, i2, i3])
                T.reads(lv35[v_i0, v_i1, v_i2, v_i3])
                T.writes(pad_temp[v_i0, v_i1, v_i2, v_i3])
                pad_temp[v_i0, v_i1, v_i2, v_i3] = lv35[v_i0, v_i1, v_i2, v_i3]
        for nn, ff, yy, xx, rc, ry, rx in T.grid(T.int64(1), T.int64(64), T.int64(56), T.int64(56), T.int64(256), T.int64(1), T.int64(1)):
            with T.block("conv2d_nchw"):
                v_nn, v_ff, v_yy, v_xx, v_rc, v_ry, v_rx = T.axis.remap("SSSSRRR", [nn, ff, yy, xx, rc, ry, rx])
                T.reads(pad_temp[v_nn, v_rc, v_yy + v_ry, v_xx + v_rx], B[v_ff, v_rc, v_ry, v_rx])
                T.writes(conv2d_nchw[v_nn, v_ff, v_yy, v_xx])
                with T.init():
                    conv2d_nchw[v_nn, v_ff, v_yy, v_xx] = T.float32(0.0)
                conv2d_nchw[v_nn, v_ff, v_yy, v_xx] = conv2d_nchw[v_nn, v_ff, v_yy, v_xx] + pad_temp[v_nn, v_rc, v_yy + v_ry, v_xx + v_rx] * B[v_ff, v_rc, v_ry, v_rx]

    @T.prim_func(private=True)
    def conv2d5(lv73: T.Buffer((T.int64(1), T.int64(256), T.int64(56), T.int64(56)), "float32"), B: T.Buffer((T.int64(128), T.int64(256), T.int64(1), T.int64(1)), "float32"), conv2d_nchw: T.Buffer((T.int64(1), T.int64(128), T.int64(56), T.int64(56)), "float32")):
        T.func_attr({"tir.noalias": True})
        # with T.block("root"):
        pad_temp = T.alloc_buffer((T.int64(1), T.int64(256), T.int64(56), T.int64(56)))
        for i0, i1, i2, i3 in T.grid(T.int64(1), T.int64(256), T.int64(56), T.int64(56)):
            with T.block("pad_temp"):
                v_i0, v_i1, v_i2, v_i3 = T.axis.remap("SSSS", [i0, i1, i2, i3])
                T.reads(lv73[v_i0, v_i1, v_i2, v_i3])
                T.writes(pad_temp[v_i0, v_i1, v_i2, v_i3])
                pad_temp[v_i0, v_i1, v_i2, v_i3] = lv73[v_i0, v_i1, v_i2, v_i3]
        for nn, ff, yy, xx, rc, ry, rx in T.grid(T.int64(1), T.int64(128), T.int64(56), T.int64(56), T.int64(256), T.int64(1), T.int64(1)):
            with T.block("conv2d_nchw"):
                v_nn, v_ff, v_yy, v_xx, v_rc, v_ry, v_rx = T.axis.remap("SSSSRRR", [nn, ff, yy, xx, rc, ry, rx])
                T.reads(pad_temp[v_nn, v_rc, v_yy + v_ry, v_xx + v_rx], B[v_ff, v_rc, v_ry, v_rx])
                T.writes(conv2d_nchw[v_nn, v_ff, v_yy, v_xx])
                with T.init():
                    conv2d_nchw[v_nn, v_ff, v_yy, v_xx] = T.float32(0.0)
                conv2d_nchw[v_nn, v_ff, v_yy, v_xx] = conv2d_nchw[v_nn, v_ff, v_yy, v_xx] + pad_temp[v_nn, v_rc, v_yy + v_ry, v_xx + v_rx] * B[v_ff, v_rc, v_ry, v_rx]

    @T.prim_func(private=True)
    def conv2d6(lv79: T.Buffer((T.int64(1), T.int64(128), T.int64(56), T.int64(56)), "float32"), B: T.Buffer((T.int64(128), T.int64(128), T.int64(3), T.int64(3)), "float32"), conv2d_nchw: T.Buffer((T.int64(1), T.int64(128), T.int64(28), T.int64(28)), "float32")):
        T.func_attr({"tir.noalias": True})
        # with T.block("root"):
        pad_temp = T.alloc_buffer((T.int64(1), T.int64(128), T.int64(58), T.int64(58)))
        for i0, i1, i2, i3 in T.grid(T.int64(1), T.int64(128), T.int64(58), T.int64(58)):
            with T.block("pad_temp"):
                v_i0, v_i1, v_i2, v_i3 = T.axis.remap("SSSS", [i0, i1, i2, i3])
                T.reads(lv79[v_i0, v_i1, v_i2 - T.int64(1), v_i3 - T.int64(1)])
                T.writes(pad_temp[v_i0, v_i1, v_i2, v_i3])
                pad_temp[v_i0, v_i1, v_i2, v_i3] = T.if_then_else(T.int64(1) <= v_i2 and v_i2 < T.int64(57) and T.int64(1) <= v_i3 and v_i3 < T.int64(57), lv79[v_i0, v_i1, v_i2 - T.int64(1), v_i3 - T.int64(1)], T.float32(0.0))
        for nn, ff, yy, xx, rc, ry, rx in T.grid(T.int64(1), T.int64(128), T.int64(28), T.int64(28), T.int64(128), T.int64(3), T.int64(3)):
            with T.block("conv2d_nchw"):
                v_nn, v_ff, v_yy, v_xx, v_rc, v_ry, v_rx = T.axis.remap("SSSSRRR", [nn, ff, yy, xx, rc, ry, rx])
                T.reads(pad_temp[v_nn, v_rc, v_yy * T.int64(2) + v_ry, v_xx * T.int64(2) + v_rx], B[v_ff, v_rc, v_ry, v_rx])
                T.writes(conv2d_nchw[v_nn, v_ff, v_yy, v_xx])
                with T.init():
                    conv2d_nchw[v_nn, v_ff, v_yy, v_xx] = T.float32(0.0)
                conv2d_nchw[v_nn, v_ff, v_yy, v_xx] = conv2d_nchw[v_nn, v_ff, v_yy, v_xx] + pad_temp[v_nn, v_rc, v_yy * T.int64(2) + v_ry, v_xx * T.int64(2) + v_rx] * B[v_ff, v_rc, v_ry, v_rx]

    @T.prim_func(private=True)
    def conv2d7(lv85: T.Buffer((T.int64(1), T.int64(128), T.int64(28), T.int64(28)), "float32"), B: T.Buffer((T.int64(512), T.int64(128), T.int64(1), T.int64(1)), "float32"), conv2d_nchw: T.Buffer((T.int64(1), T.int64(512), T.int64(28), T.int64(28)), "float32")):
        T.func_attr({"tir.noalias": True})
        # with T.block("root"):
        pad_temp = T.alloc_buffer((T.int64(1), T.int64(128), T.int64(28), T.int64(28)))
        for i0, i1, i2, i3 in T.grid(T.int64(1), T.int64(128), T.int64(28), T.int64(28)):
            with T.block("pad_temp"):
                v_i0, v_i1, v_i2, v_i3 = T.axis.remap("SSSS", [i0, i1, i2, i3])
                T.reads(lv85[v_i0, v_i1, v_i2, v_i3])
                T.writes(pad_temp[v_i0, v_i1, v_i2, v_i3])
                pad_temp[v_i0, v_i1, v_i2, v_i3] = lv85[v_i0, v_i1, v_i2, v_i3]
        for nn, ff, yy, xx, rc, ry, rx in T.grid(T.int64(1), T.int64(512), T.int64(28), T.int64(28), T.int64(128), T.int64(1), T.int64(1)):
            with T.block("conv2d_nchw"):
                v_nn, v_ff, v_yy, v_xx, v_rc, v_ry, v_rx = T.axis.remap("SSSSRRR", [nn, ff, yy, xx, rc, ry, rx])
                T.reads(pad_temp[v_nn, v_rc, v_yy + v_ry, v_xx + v_rx], B[v_ff, v_rc, v_ry, v_rx])
                T.writes(conv2d_nchw[v_nn, v_ff, v_yy, v_xx])
                with T.init():
                    conv2d_nchw[v_nn, v_ff, v_yy, v_xx] = T.float32(0.0)
                conv2d_nchw[v_nn, v_ff, v_yy, v_xx] = conv2d_nchw[v_nn, v_ff, v_yy, v_xx] + pad_temp[v_nn, v_rc, v_yy + v_ry, v_xx + v_rx] * B[v_ff, v_rc, v_ry, v_rx]

    @T.prim_func(private=True)
    def conv2d8(lv73: T.Buffer((T.int64(1), T.int64(256), T.int64(56), T.int64(56)), "float32"), B: T.Buffer((T.int64(512), T.int64(256), T.int64(1), T.int64(1)), "float32"), conv2d_nchw: T.Buffer((T.int64(1), T.int64(512), T.int64(28), T.int64(28)), "float32")):
        T.func_attr({"tir.noalias": True})
        # with T.block("root"):
        pad_temp = T.alloc_buffer((T.int64(1), T.int64(256), T.int64(56), T.int64(56)))
        for i0, i1, i2, i3 in T.grid(T.int64(1), T.int64(256), T.int64(56), T.int64(56)):
            with T.block("pad_temp"):
                v_i0, v_i1, v_i2, v_i3 = T.axis.remap("SSSS", [i0, i1, i2, i3])
                T.reads(lv73[v_i0, v_i1, v_i2, v_i3])
                T.writes(pad_temp[v_i0, v_i1, v_i2, v_i3])
                pad_temp[v_i0, v_i1, v_i2, v_i3] = lv73[v_i0, v_i1, v_i2, v_i3]
        for nn, ff, yy, xx, rc, ry, rx in T.grid(T.int64(1), T.int64(512), T.int64(28), T.int64(28), T.int64(256), T.int64(1), T.int64(1)):
            with T.block("conv2d_nchw"):
                v_nn, v_ff, v_yy, v_xx, v_rc, v_ry, v_rx = T.axis.remap("SSSSRRR", [nn, ff, yy, xx, rc, ry, rx])
                T.reads(pad_temp[v_nn, v_rc, v_yy * T.int64(2) + v_ry, v_xx * T.int64(2) + v_rx], B[v_ff, v_rc, v_ry, v_rx])
                T.writes(conv2d_nchw[v_nn, v_ff, v_yy, v_xx])
                with T.init():
                    conv2d_nchw[v_nn, v_ff, v_yy, v_xx] = T.float32(0.0)
                conv2d_nchw[v_nn, v_ff, v_yy, v_xx] = conv2d_nchw[v_nn, v_ff, v_yy, v_xx] + pad_temp[v_nn, v_rc, v_yy * T.int64(2) + v_ry, v_xx * T.int64(2) + v_rx] * B[v_ff, v_rc, v_ry, v_rx]

    @T.prim_func(private=True)
    def conv2d9(lv93: T.Buffer((T.int64(1), T.int64(512), T.int64(28), T.int64(28)), "float32"), B: T.Buffer((T.int64(128), T.int64(512), T.int64(1), T.int64(1)), "float32"), conv2d_nchw: T.Buffer((T.int64(1), T.int64(128), T.int64(28), T.int64(28)), "float32")):
        T.func_attr({"tir.noalias": True})
        # with T.block("root"):
        pad_temp = T.alloc_buffer((T.int64(1), T.int64(512), T.int64(28), T.int64(28)))
        for i0, i1, i2, i3 in T.grid(T.int64(1), T.int64(512), T.int64(28), T.int64(28)):
            with T.block("pad_temp"):
                v_i0, v_i1, v_i2, v_i3 = T.axis.remap("SSSS", [i0, i1, i2, i3])
                T.reads(lv93[v_i0, v_i1, v_i2, v_i3])
                T.writes(pad_temp[v_i0, v_i1, v_i2, v_i3])
                pad_temp[v_i0, v_i1, v_i2, v_i3] = lv93[v_i0, v_i1, v_i2, v_i3]
        for nn, ff, yy, xx, rc, ry, rx in T.grid(T.int64(1), T.int64(128), T.int64(28), T.int64(28), T.int64(512), T.int64(1), T.int64(1)):
            with T.block("conv2d_nchw"):
                v_nn, v_ff, v_yy, v_xx, v_rc, v_ry, v_rx = T.axis.remap("SSSSRRR", [nn, ff, yy, xx, rc, ry, rx])
                T.reads(pad_temp[v_nn, v_rc, v_yy + v_ry, v_xx + v_rx], B[v_ff, v_rc, v_ry, v_rx])
                T.writes(conv2d_nchw[v_nn, v_ff, v_yy, v_xx])
                with T.init():
                    conv2d_nchw[v_nn, v_ff, v_yy, v_xx] = T.float32(0.0)
                conv2d_nchw[v_nn, v_ff, v_yy, v_xx] = conv2d_nchw[v_nn, v_ff, v_yy, v_xx] + pad_temp[v_nn, v_rc, v_yy + v_ry, v_xx + v_rx] * B[v_ff, v_rc, v_ry, v_rx]

    @T.prim_func(private=True)
    def matmul(lv325: T.Buffer((T.int64(1), T.int64(2048)), "float32"), lv326: T.Buffer((T.int64(2048), T.int64(1000)), "float32"), matmul: T.Buffer((T.int64(1), T.int64(1000)), "float32")):
        T.func_attr({"tir.noalias": True})
        # with T.block("root"):
        for i0, i1, k in T.grid(T.int64(1), T.int64(1000), T.int64(2048)):
            with T.block("matmul"):
                v_i0, v_i1, v_k = T.axis.remap("SSR", [i0, i1, k])
                T.reads(lv325[v_i0, v_k], lv326[v_k, v_i1])
                T.writes(matmul[v_i0, v_i1])
                with T.init():
                    matmul[v_i0, v_i1] = T.float32(0.0)
                matmul[v_i0, v_i1] = matmul[v_i0, v_i1] + lv325[v_i0, v_k] * lv326[v_k, v_i1]

    @T.prim_func(private=True)
    def max_pool2d(lv9: T.Buffer((T.int64(1), T.int64(64), T.int64(112), T.int64(112)), "float32"), pool_max: T.Buffer((T.int64(1), T.int64(64), T.int64(56), T.int64(56)), "float32")):
        T.func_attr({"tir.noalias": True})
        # with T.block("root"):
        pad_temp = T.alloc_buffer((T.int64(1), T.int64(64), T.int64(114), T.int64(114)))
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(1), T.int64(64), T.int64(114), T.int64(114)):
            with T.block("pad_temp"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(lv9[v_ax0, v_ax1, v_ax2 - T.int64(1), v_ax3 - T.int64(1)])
                T.writes(pad_temp[v_ax0, v_ax1, v_ax2, v_ax3])
                pad_temp[v_ax0, v_ax1, v_ax2, v_ax3] = T.if_then_else(T.int64(1) <= v_ax2 and v_ax2 < T.int64(113) and T.int64(1) <= v_ax3 and v_ax3 < T.int64(113), lv9[v_ax0, v_ax1, v_ax2 - T.int64(1), v_ax3 - T.int64(1)], T.float32(-340282346638528859811704183484516925440.0))
        for ax0, ax1, ax2, ax3, rv0, rv1 in T.grid(T.int64(1), T.int64(64), T.int64(56), T.int64(56), T.int64(3), T.int64(3)):
            with T.block("pool_max"):
                v_ax0, v_ax1, v_ax2, v_ax3, v_rv0, v_rv1 = T.axis.remap("SSSSRR", [ax0, ax1, ax2, ax3, rv0, rv1])
                T.reads(pad_temp[v_ax0, v_ax1, v_ax2 * T.int64(2) + v_rv0, v_ax3 * T.int64(2) + v_rv1])
                T.writes(pool_max[v_ax0, v_ax1, v_ax2, v_ax3])
                T.block_attr({"schedule_rule": "meta_schedule.pool_max"})
                with T.init():
                    pool_max[v_ax0, v_ax1, v_ax2, v_ax3] = T.float32(-340282346638528859811704183484516925440.0)
                pool_max[v_ax0, v_ax1, v_ax2, v_ax3] = T.max(pool_max[v_ax0, v_ax1, v_ax2, v_ax3], pad_temp[v_ax0, v_ax1, v_ax2 * T.int64(2) + v_rv0, v_ax3 * T.int64(2) + v_rv1])

    @T.prim_func(private=True)
    def mean(lv323: T.Buffer((T.int64(1), T.int64(2048), T.int64(7), T.int64(7)), "float32"), T_divide: T.Buffer((T.int64(1), T.int64(2048), T.int64(1), T.int64(1)), "float32")):
        T.func_attr({"tir.noalias": True})
        # with T.block("root"):
        lv323_red = T.alloc_buffer((T.int64(1), T.int64(2048), T.int64(1), T.int64(1)))
        for ax0, ax1, ax2, ax3, k2, k3 in T.grid(T.int64(1), T.int64(2048), T.int64(1), T.int64(1), T.int64(7), T.int64(7)):
            with T.block("lv323_red"):
                v_ax0, v_ax1, v_ax2, v_ax3, v_k2, v_k3 = T.axis.remap("SSSSRR", [ax0, ax1, ax2, ax3, k2, k3])
                T.reads(lv323[v_ax0, v_ax1, v_k2, v_k3])
                T.writes(lv323_red[v_ax0, v_ax1, v_ax2, v_ax3])
                with T.init():
                    lv323_red[v_ax0, v_ax1, v_ax2, v_ax3] = T.float32(0.0)
                lv323_red[v_ax0, v_ax1, v_ax2, v_ax3] = lv323_red[v_ax0, v_ax1, v_ax2, v_ax3] + lv323[v_ax0, v_ax1, v_k2, v_k3]
        for ax0, ax1, ax2, ax3 in T.grid(T.int64(1), T.int64(2048), T.int64(1), T.int64(1)):
            with T.block("T_divide"):
                v_ax0, v_ax1, v_ax2, v_ax3 = T.axis.remap("SSSS", [ax0, ax1, ax2, ax3])
                T.reads(lv323_red[v_ax0, v_ax1, v_ax2, v_ax3])
                T.writes(T_divide[v_ax0, v_ax1, v_ax2, v_ax3])
                T_divide[v_ax0, v_ax1, v_ax2, v_ax3] = lv323_red[v_ax0, v_ax1, v_ax2, v_ax3] * T.float32(0.020408163265306121)

    @T.prim_func(private=True)
    def relu(lv6: T.Buffer((T.int64(1), T.int64(64), T.int64(112), T.int64(112)), "float32"), compute: T.Buffer((T.int64(1), T.int64(64), T.int64(112), T.int64(112)), "float32")):
        T.func_attr({"tir.noalias": True})
        # with T.block("root"):
        for i0, i1, i2, i3 in T.grid(T.int64(1), T.int64(64), T.int64(112), T.int64(112)):
            with T.block("compute"):
                v_i0, v_i1, v_i2, v_i3 = T.axis.remap("SSSS", [i0, i1, i2, i3])
                T.reads(lv6[v_i0, v_i1, v_i2, v_i3])
                T.writes(compute[v_i0, v_i1, v_i2, v_i3])
                compute[v_i0, v_i1, v_i2, v_i3] = T.max(lv6[v_i0, v_i1, v_i2, v_i3], T.float32(0.0))

    @T.prim_func(private=True)
    def relu1(lv12: T.Buffer((T.int64(1), T.int64(64), T.int64(56), T.int64(56)), "float32"), compute: T.Buffer((T.int64(1), T.int64(64), T.int64(56), T.int64(56)), "float32")):
        T.func_attr({"tir.noalias": True})
        # with T.block("root"):
        for i0, i1, i2, i3 in T.grid(T.int64(1), T.int64(64), T.int64(56), T.int64(56)):
            with T.block("compute"):
                v_i0, v_i1, v_i2, v_i3 = T.axis.remap("SSSS", [i0, i1, i2, i3])
                T.reads(lv12[v_i0, v_i1, v_i2, v_i3])
                T.writes(compute[v_i0, v_i1, v_i2, v_i3])
                compute[v_i0, v_i1, v_i2, v_i3] = T.max(lv12[v_i0, v_i1, v_i2, v_i3], T.float32(0.0))

    @T.prim_func(private=True)
    def relu10(lv274: T.Buffer((T.int64(1), T.int64(512), T.int64(7), T.int64(7)), "float32"), compute: T.Buffer((T.int64(1), T.int64(512), T.int64(7), T.int64(7)), "float32")):
        T.func_attr({"tir.noalias": True})
        # with T.block("root"):
        for i0, i1, i2, i3 in T.grid(T.int64(1), T.int64(512), T.int64(7), T.int64(7)):
            with T.block("compute"):
                v_i0, v_i1, v_i2, v_i3 = T.axis.remap("SSSS", [i0, i1, i2, i3])
                T.reads(lv274[v_i0, v_i1, v_i2, v_i3])
                T.writes(compute[v_i0, v_i1, v_i2, v_i3])
                compute[v_i0, v_i1, v_i2, v_i3] = T.max(lv274[v_i0, v_i1, v_i2, v_i3], T.float32(0.0))

    @T.prim_func(private=True)
    def relu11(lv282: T.Buffer((T.int64(1), T.int64(2048), T.int64(7), T.int64(7)), "float32"), compute: T.Buffer((T.int64(1), T.int64(2048), T.int64(7), T.int64(7)), "float32")):
        T.func_attr({"tir.noalias": True})
        # with T.block("root"):
        for i0, i1, i2, i3 in T.grid(T.int64(1), T.int64(2048), T.int64(7), T.int64(7)):
            with T.block("compute"):
                v_i0, v_i1, v_i2, v_i3 = T.axis.remap("SSSS", [i0, i1, i2, i3])
                T.reads(lv282[v_i0, v_i1, v_i2, v_i3])
                T.writes(compute[v_i0, v_i1, v_i2, v_i3])
                compute[v_i0, v_i1, v_i2, v_i3] = T.max(lv282[v_i0, v_i1, v_i2, v_i3], T.float32(0.0))

    @T.prim_func(private=True)
    def relu2(lv32: T.Buffer((T.int64(1), T.int64(256), T.int64(56), T.int64(56)), "float32"), compute: T.Buffer((T.int64(1), T.int64(256), T.int64(56), T.int64(56)), "float32")):
        T.func_attr({"tir.noalias": True})
        # with T.block("root"):
        for i0, i1, i2, i3 in T.grid(T.int64(1), T.int64(256), T.int64(56), T.int64(56)):
            with T.block("compute"):
                v_i0, v_i1, v_i2, v_i3 = T.axis.remap("SSSS", [i0, i1, i2, i3])
                T.reads(lv32[v_i0, v_i1, v_i2, v_i3])
                T.writes(compute[v_i0, v_i1, v_i2, v_i3])
                compute[v_i0, v_i1, v_i2, v_i3] = T.max(lv32[v_i0, v_i1, v_i2, v_i3], T.float32(0.0))

    @T.prim_func(private=True)
    def relu3(lv76: T.Buffer((T.int64(1), T.int64(128), T.int64(56), T.int64(56)), "float32"), compute: T.Buffer((T.int64(1), T.int64(128), T.int64(56), T.int64(56)), "float32")):
        T.func_attr({"tir.noalias": True})
        # with T.block("root"):
        for i0, i1, i2, i3 in T.grid(T.int64(1), T.int64(128), T.int64(56), T.int64(56)):
            with T.block("compute"):
                v_i0, v_i1, v_i2, v_i3 = T.axis.remap("SSSS", [i0, i1, i2, i3])
                T.reads(lv76[v_i0, v_i1, v_i2, v_i3])
                T.writes(compute[v_i0, v_i1, v_i2, v_i3])
                compute[v_i0, v_i1, v_i2, v_i3] = T.max(lv76[v_i0, v_i1, v_i2, v_i3], T.float32(0.0))

    @T.prim_func(private=True)
    def relu4(lv82: T.Buffer((T.int64(1), T.int64(128), T.int64(28), T.int64(28)), "float32"), compute: T.Buffer((T.int64(1), T.int64(128), T.int64(28), T.int64(28)), "float32")):
        T.func_attr({"tir.noalias": True})
        # with T.block("root"):
        for i0, i1, i2, i3 in T.grid(T.int64(1), T.int64(128), T.int64(28), T.int64(28)):
            with T.block("compute"):
                v_i0, v_i1, v_i2, v_i3 = T.axis.remap("SSSS", [i0, i1, i2, i3])
                T.reads(lv82[v_i0, v_i1, v_i2, v_i3])
                T.writes(compute[v_i0, v_i1, v_i2, v_i3])
                compute[v_i0, v_i1, v_i2, v_i3] = T.max(lv82[v_i0, v_i1, v_i2, v_i3], T.float32(0.0))

    @T.prim_func(private=True)
    def relu5(lv90: T.Buffer((T.int64(1), T.int64(512), T.int64(28), T.int64(28)), "float32"), compute: T.Buffer((T.int64(1), T.int64(512), T.int64(28), T.int64(28)), "float32")):
        T.func_attr({"tir.noalias": True})
        # with T.block("root"):
        for i0, i1, i2, i3 in T.grid(T.int64(1), T.int64(512), T.int64(28), T.int64(28)):
            with T.block("compute"):
                v_i0, v_i1, v_i2, v_i3 = T.axis.remap("SSSS", [i0, i1, i2, i3])
                T.reads(lv90[v_i0, v_i1, v_i2, v_i3])
                T.writes(compute[v_i0, v_i1, v_i2, v_i3])
                compute[v_i0, v_i1, v_i2, v_i3] = T.max(lv90[v_i0, v_i1, v_i2, v_i3], T.float32(0.0))

    @T.prim_func(private=True)
    def relu6(lv153: T.Buffer((T.int64(1), T.int64(256), T.int64(28), T.int64(28)), "float32"), compute: T.Buffer((T.int64(1), T.int64(256), T.int64(28), T.int64(28)), "float32")):
        T.func_attr({"tir.noalias": True})
        # with T.block("root"):
        for i0, i1, i2, i3 in T.grid(T.int64(1), T.int64(256), T.int64(28), T.int64(28)):
            with T.block("compute"):
                v_i0, v_i1, v_i2, v_i3 = T.axis.remap("SSSS", [i0, i1, i2, i3])
                T.reads(lv153[v_i0, v_i1, v_i2, v_i3])
                T.writes(compute[v_i0, v_i1, v_i2, v_i3])
                compute[v_i0, v_i1, v_i2, v_i3] = T.max(lv153[v_i0, v_i1, v_i2, v_i3], T.float32(0.0))

    @T.prim_func(private=True)
    def relu7(lv159: T.Buffer((T.int64(1), T.int64(256), T.int64(14), T.int64(14)), "float32"), compute: T.Buffer((T.int64(1), T.int64(256), T.int64(14), T.int64(14)), "float32")):
        T.func_attr({"tir.noalias": True})
        # with T.block("root"):
        for i0, i1, i2, i3 in T.grid(T.int64(1), T.int64(256), T.int64(14), T.int64(14)):
            with T.block("compute"):
                v_i0, v_i1, v_i2, v_i3 = T.axis.remap("SSSS", [i0, i1, i2, i3])
                T.reads(lv159[v_i0, v_i1, v_i2, v_i3])
                T.writes(compute[v_i0, v_i1, v_i2, v_i3])
                compute[v_i0, v_i1, v_i2, v_i3] = T.max(lv159[v_i0, v_i1, v_i2, v_i3], T.float32(0.0))

    @T.prim_func(private=True)
    def relu8(lv167: T.Buffer((T.int64(1), T.int64(1024), T.int64(14), T.int64(14)), "float32"), compute: T.Buffer((T.int64(1), T.int64(1024), T.int64(14), T.int64(14)), "float32")):
        T.func_attr({"tir.noalias": True})
        # with T.block("root"):
        for i0, i1, i2, i3 in T.grid(T.int64(1), T.int64(1024), T.int64(14), T.int64(14)):
            with T.block("compute"):
                v_i0, v_i1, v_i2, v_i3 = T.axis.remap("SSSS", [i0, i1, i2, i3])
                T.reads(lv167[v_i0, v_i1, v_i2, v_i3])
                T.writes(compute[v_i0, v_i1, v_i2, v_i3])
                compute[v_i0, v_i1, v_i2, v_i3] = T.max(lv167[v_i0, v_i1, v_i2, v_i3], T.float32(0.0))

    @T.prim_func(private=True)
    def relu9(lv268: T.Buffer((T.int64(1), T.int64(512), T.int64(14), T.int64(14)), "float32"), compute: T.Buffer((T.int64(1), T.int64(512), T.int64(14), T.int64(14)), "float32")):
        T.func_attr({"tir.noalias": True})
        # with T.block("root"):
        for i0, i1, i2, i3 in T.grid(T.int64(1), T.int64(512), T.int64(14), T.int64(14)):
            with T.block("compute"):
                v_i0, v_i1, v_i2, v_i3 = T.axis.remap("SSSS", [i0, i1, i2, i3])
                T.reads(lv268[v_i0, v_i1, v_i2, v_i3])
                T.writes(compute[v_i0, v_i1, v_i2, v_i3])
                compute[v_i0, v_i1, v_i2, v_i3] = T.max(lv268[v_i0, v_i1, v_i2, v_i3], T.float32(0.0))

    @T.prim_func(private=True)
    def reshape(lv324: T.Buffer((T.int64(1), T.int64(2048), T.int64(1), T.int64(1)), "float32"), T_reshape: T.Buffer((T.int64(1), T.int64(2048)), "float32")):
        T.func_attr({"tir.noalias": True})
        # with T.block("root"):
        for ax0, ax1 in T.grid(T.int64(1), T.int64(2048)):
            with T.block("T_reshape"):
                v_ax0, v_ax1 = T.axis.remap("SS", [ax0, ax1])
                T.reads(lv324[T.int64(0), v_ax1 % T.int64(2048), T.int64(0), T.int64(0)])
                T.writes(T_reshape[v_ax0, v_ax1])
                T_reshape[v_ax0, v_ax1] = lv324[T.int64(0), v_ax1 % T.int64(2048), T.int64(0), T.int64(0)]

    @T.prim_func(private=True)
    def transpose(A: T.Buffer((T.int64(1000), T.int64(2048)), "float32"), T_transpose: T.Buffer((T.int64(2048), T.int64(1000)), "float32")):
        T.func_attr({"tir.noalias": True})
        # with T.block("root"):
        for ax0, ax1 in T.grid(T.int64(2048), T.int64(1000)):
            with T.block("T_transpose"):
                v_ax0, v_ax1 = T.axis.remap("SS", [ax0, ax1])
                T.reads(A[v_ax1, v_ax0])
                T.writes(T_transpose[v_ax0, v_ax1])
                T_transpose[v_ax0, v_ax1] = A[v_ax1, v_ax0]

    @R.function
    def main(data: R.Tensor((1, 3, 224, 224), dtype="float32")) -> R.Tensor((1, 1000), dtype="float32"):
        R.func_attr({"num_input": 1})
        cls = Module
        with R.dataflow():
            lv = R.call_tir(cls.batch_norm, (data, metadata["relax.expr.Constant"][0], metadata["relax.expr.Constant"][1], metadata["relax.expr.Constant"][2], metadata["relax.expr.Constant"][3]), out_sinfo=[R.Tensor((1, 3, 224, 224), dtype="float32"), R.Tensor((3,), dtype="float32"), R.Tensor((3,), dtype="float32")])
            lv1: R.Tensor((1, 3, 224, 224), dtype="float32") = lv[0]
            lv4 = R.call_tir(cls.conv2d, (lv1, metadata["relax.expr.Constant"][4]), out_sinfo=R.Tensor((1, 64, 112, 112), dtype="float32"))
            lv5 = R.call_tir(cls.batch_norm1, (lv4, metadata["relax.expr.Constant"][5], metadata["relax.expr.Constant"][6], metadata["relax.expr.Constant"][7], metadata["relax.expr.Constant"][8]), out_sinfo=[R.Tensor((1, 64, 112, 112), dtype="float32"), R.Tensor((64,), dtype="float32"), R.Tensor((64,), dtype="float32")])
            lv6: R.Tensor((1, 64, 112, 112), dtype="float32") = lv5[0]
            lv9 = R.call_tir(cls.relu, (lv6,), out_sinfo=R.Tensor((1, 64, 112, 112), dtype="float32"))
            lv10 = R.call_tir(cls.max_pool2d, (lv9,), out_sinfo=R.Tensor((1, 64, 56, 56), dtype="float32"))
            lv11 = R.call_tir(cls.batch_norm2, (lv10, metadata["relax.expr.Constant"][9], metadata["relax.expr.Constant"][10], metadata["relax.expr.Constant"][11], metadata["relax.expr.Constant"][12]), out_sinfo=[R.Tensor((1, 64, 56, 56), dtype="float32"), R.Tensor((64,), dtype="float32"), R.Tensor((64,), dtype="float32")])
            lv12: R.Tensor((1, 64, 56, 56), dtype="float32") = lv11[0]
            lv15 = R.call_tir(cls.relu1, (lv12,), out_sinfo=R.Tensor((1, 64, 56, 56), dtype="float32"))
            lv16 = R.call_tir(cls.conv2d1, (lv15, metadata["relax.expr.Constant"][13]), out_sinfo=R.Tensor((1, 64, 56, 56), dtype="float32"))
            lv17 = R.call_tir(cls.batch_norm2, (lv16, metadata["relax.expr.Constant"][14], metadata["relax.expr.Constant"][15], metadata["relax.expr.Constant"][16], metadata["relax.expr.Constant"][17]), out_sinfo=[R.Tensor((1, 64, 56, 56), dtype="float32"), R.Tensor((64,), dtype="float32"), R.Tensor((64,), dtype="float32")])
            lv18: R.Tensor((1, 64, 56, 56), dtype="float32") = lv17[0]
            lv21 = R.call_tir(cls.relu1, (lv18,), out_sinfo=R.Tensor((1, 64, 56, 56), dtype="float32"))
            lv22 = R.call_tir(cls.conv2d2, (lv21, metadata["relax.expr.Constant"][18]), out_sinfo=R.Tensor((1, 64, 56, 56), dtype="float32"))
            lv23 = R.call_tir(cls.batch_norm2, (lv22, metadata["relax.expr.Constant"][19], metadata["relax.expr.Constant"][20], metadata["relax.expr.Constant"][21], metadata["relax.expr.Constant"][22]), out_sinfo=[R.Tensor((1, 64, 56, 56), dtype="float32"), R.Tensor((64,), dtype="float32"), R.Tensor((64,), dtype="float32")])
            lv24: R.Tensor((1, 64, 56, 56), dtype="float32") = lv23[0]
            lv27 = R.call_tir(cls.relu1, (lv24,), out_sinfo=R.Tensor((1, 64, 56, 56), dtype="float32"))
            lv28 = R.call_tir(cls.conv2d3, (lv27, metadata["relax.expr.Constant"][23]), out_sinfo=R.Tensor((1, 256, 56, 56), dtype="float32"))
            lv29 = R.call_tir(cls.conv2d3, (lv15, metadata["relax.expr.Constant"][24]), out_sinfo=R.Tensor((1, 256, 56, 56), dtype="float32"))
            lv30 = R.call_tir(cls.add, (lv28, lv29), out_sinfo=R.Tensor((1, 256, 56, 56), dtype="float32"))
            lv31 = R.call_tir(cls.batch_norm3, (lv30, metadata["relax.expr.Constant"][25], metadata["relax.expr.Constant"][26], metadata["relax.expr.Constant"][27], metadata["relax.expr.Constant"][28]), out_sinfo=[R.Tensor((1, 256, 56, 56), dtype="float32"), R.Tensor((256,), dtype="float32"), R.Tensor((256,), dtype="float32")])
            lv32: R.Tensor((1, 256, 56, 56), dtype="float32") = lv31[0]
            lv35 = R.call_tir(cls.relu2, (lv32,), out_sinfo=R.Tensor((1, 256, 56, 56), dtype="float32"))
            lv36 = R.call_tir(cls.conv2d4, (lv35, metadata["relax.expr.Constant"][29]), out_sinfo=R.Tensor((1, 64, 56, 56), dtype="float32"))
            lv37 = R.call_tir(cls.batch_norm2, (lv36, metadata["relax.expr.Constant"][30], metadata["relax.expr.Constant"][31], metadata["relax.expr.Constant"][32], metadata["relax.expr.Constant"][33]), out_sinfo=[R.Tensor((1, 64, 56, 56), dtype="float32"), R.Tensor((64,), dtype="float32"), R.Tensor((64,), dtype="float32")])
            lv38: R.Tensor((1, 64, 56, 56), dtype="float32") = lv37[0]
            lv41 = R.call_tir(cls.relu1, (lv38,), out_sinfo=R.Tensor((1, 64, 56, 56), dtype="float32"))
            lv42 = R.call_tir(cls.conv2d2, (lv41, metadata["relax.expr.Constant"][34]), out_sinfo=R.Tensor((1, 64, 56, 56), dtype="float32"))
            lv43 = R.call_tir(cls.batch_norm2, (lv42, metadata["relax.expr.Constant"][35], metadata["relax.expr.Constant"][36], metadata["relax.expr.Constant"][37], metadata["relax.expr.Constant"][38]), out_sinfo=[R.Tensor((1, 64, 56, 56), dtype="float32"), R.Tensor((64,), dtype="float32"), R.Tensor((64,), dtype="float32")])
            lv44: R.Tensor((1, 64, 56, 56), dtype="float32") = lv43[0]
            lv47 = R.call_tir(cls.relu1, (lv44,), out_sinfo=R.Tensor((1, 64, 56, 56), dtype="float32"))
            lv48 = R.call_tir(cls.conv2d3, (lv47, metadata["relax.expr.Constant"][39]), out_sinfo=R.Tensor((1, 256, 56, 56), dtype="float32"))
            lv49 = R.call_tir(cls.add, (lv48, lv30), out_sinfo=R.Tensor((1, 256, 56, 56), dtype="float32"))
            lv50 = R.call_tir(cls.batch_norm3, (lv49, metadata["relax.expr.Constant"][40], metadata["relax.expr.Constant"][41], metadata["relax.expr.Constant"][42], metadata["relax.expr.Constant"][43]), out_sinfo=[R.Tensor((1, 256, 56, 56), dtype="float32"), R.Tensor((256,), dtype="float32"), R.Tensor((256,), dtype="float32")])
            lv51: R.Tensor((1, 256, 56, 56), dtype="float32") = lv50[0]
            lv54 = R.call_tir(cls.relu2, (lv51,), out_sinfo=R.Tensor((1, 256, 56, 56), dtype="float32"))
            lv55 = R.call_tir(cls.conv2d4, (lv54, metadata["relax.expr.Constant"][44]), out_sinfo=R.Tensor((1, 64, 56, 56), dtype="float32"))
            lv56 = R.call_tir(cls.batch_norm2, (lv55, metadata["relax.expr.Constant"][45], metadata["relax.expr.Constant"][46], metadata["relax.expr.Constant"][47], metadata["relax.expr.Constant"][48]), out_sinfo=[R.Tensor((1, 64, 56, 56), dtype="float32"), R.Tensor((64,), dtype="float32"), R.Tensor((64,), dtype="float32")])
            lv57: R.Tensor((1, 64, 56, 56), dtype="float32") = lv56[0]
            lv60 = R.call_tir(cls.relu1, (lv57,), out_sinfo=R.Tensor((1, 64, 56, 56), dtype="float32"))
            lv61 = R.call_tir(cls.conv2d2, (lv60, metadata["relax.expr.Constant"][49]), out_sinfo=R.Tensor((1, 64, 56, 56), dtype="float32"))
            lv62 = R.call_tir(cls.batch_norm2, (lv61, metadata["relax.expr.Constant"][50], metadata["relax.expr.Constant"][51], metadata["relax.expr.Constant"][52], metadata["relax.expr.Constant"][53]), out_sinfo=[R.Tensor((1, 64, 56, 56), dtype="float32"), R.Tensor((64,), dtype="float32"), R.Tensor((64,), dtype="float32")])
            lv63: R.Tensor((1, 64, 56, 56), dtype="float32") = lv62[0]
            lv66 = R.call_tir(cls.relu1, (lv63,), out_sinfo=R.Tensor((1, 64, 56, 56), dtype="float32"))
            lv67 = R.call_tir(cls.conv2d3, (lv66, metadata["relax.expr.Constant"][54]), out_sinfo=R.Tensor((1, 256, 56, 56), dtype="float32"))
            lv68 = R.call_tir(cls.add, (lv67, lv49), out_sinfo=R.Tensor((1, 256, 56, 56), dtype="float32"))
            lv69 = R.call_tir(cls.batch_norm3, (lv68, metadata["relax.expr.Constant"][55], metadata["relax.expr.Constant"][56], metadata["relax.expr.Constant"][57], metadata["relax.expr.Constant"][58]), out_sinfo=[R.Tensor((1, 256, 56, 56), dtype="float32"), R.Tensor((256,), dtype="float32"), R.Tensor((256,), dtype="float32")])
            lv70: R.Tensor((1, 256, 56, 56), dtype="float32") = lv69[0]
            lv73 = R.call_tir(cls.relu2, (lv70,), out_sinfo=R.Tensor((1, 256, 56, 56), dtype="float32"))
            lv74 = R.call_tir(cls.conv2d5, (lv73, metadata["relax.expr.Constant"][59]), out_sinfo=R.Tensor((1, 128, 56, 56), dtype="float32"))
            lv75 = R.call_tir(cls.batch_norm4, (lv74, metadata["relax.expr.Constant"][60], metadata["relax.expr.Constant"][61], metadata["relax.expr.Constant"][62], metadata["relax.expr.Constant"][63]), out_sinfo=[R.Tensor((1, 128, 56, 56), dtype="float32"), R.Tensor((128,), dtype="float32"), R.Tensor((128,), dtype="float32")])
            lv76: R.Tensor((1, 128, 56, 56), dtype="float32") = lv75[0]
            lv79 = R.call_tir(cls.relu3, (lv76,), out_sinfo=R.Tensor((1, 128, 56, 56), dtype="float32"))
            lv80 = R.call_tir(cls.conv2d6, (lv79, metadata["relax.expr.Constant"][64]), out_sinfo=R.Tensor((1, 128, 28, 28), dtype="float32"))
            lv81 = R.call_tir(cls.batch_norm5, (lv80, metadata["relax.expr.Constant"][65], metadata["relax.expr.Constant"][66], metadata["relax.expr.Constant"][67], metadata["relax.expr.Constant"][68]), out_sinfo=[R.Tensor((1, 128, 28, 28), dtype="float32"), R.Tensor((128,), dtype="float32"), R.Tensor((128,), dtype="float32")])
            lv82: R.Tensor((1, 128, 28, 28), dtype="float32") = lv81[0]
            lv85 = R.call_tir(cls.relu4, (lv82,), out_sinfo=R.Tensor((1, 128, 28, 28), dtype="float32"))
            lv86 = R.call_tir(cls.conv2d7, (lv85, metadata["relax.expr.Constant"][69]), out_sinfo=R.Tensor((1, 512, 28, 28), dtype="float32"))
            lv87 = R.call_tir(cls.conv2d8, (lv73, metadata["relax.expr.Constant"][70]), out_sinfo=R.Tensor((1, 512, 28, 28), dtype="float32"))
            lv88 = R.call_tir(cls.add1, (lv86, lv87), out_sinfo=R.Tensor((1, 512, 28, 28), dtype="float32"))
            lv89 = R.call_tir(cls.batch_norm6, (lv88, metadata["relax.expr.Constant"][71], metadata["relax.expr.Constant"][72], metadata["relax.expr.Constant"][73], metadata["relax.expr.Constant"][74]), out_sinfo=[R.Tensor((1, 512, 28, 28), dtype="float32"), R.Tensor((512,), dtype="float32"), R.Tensor((512,), dtype="float32")])
            lv90: R.Tensor((1, 512, 28, 28), dtype="float32") = lv89[0]
            lv93 = R.call_tir(cls.relu5, (lv90,), out_sinfo=R.Tensor((1, 512, 28, 28), dtype="float32"))
            lv94 = R.call_tir(cls.conv2d9, (lv93, metadata["relax.expr.Constant"][75]), out_sinfo=R.Tensor((1, 128, 28, 28), dtype="float32"))
            lv95 = R.call_tir(cls.batch_norm5, (lv94, metadata["relax.expr.Constant"][76], metadata["relax.expr.Constant"][77], metadata["relax.expr.Constant"][78], metadata["relax.expr.Constant"][79]), out_sinfo=[R.Tensor((1, 128, 28, 28), dtype="float32"), R.Tensor((128,), dtype="float32"), R.Tensor((128,), dtype="float32")])
            lv96: R.Tensor((1, 128, 28, 28), dtype="float32") = lv95[0]
            lv99 = R.call_tir(cls.relu4, (lv96,), out_sinfo=R.Tensor((1, 128, 28, 28), dtype="float32"))
            lv100 = R.call_tir(cls.conv2d10, (lv99, metadata["relax.expr.Constant"][80]), out_sinfo=R.Tensor((1, 128, 28, 28), dtype="float32"))
            lv101 = R.call_tir(cls.batch_norm5, (lv100, metadata["relax.expr.Constant"][81], metadata["relax.expr.Constant"][82], metadata["relax.expr.Constant"][83], metadata["relax.expr.Constant"][84]), out_sinfo=[R.Tensor((1, 128, 28, 28), dtype="float32"), R.Tensor((128,), dtype="float32"), R.Tensor((128,), dtype="float32")])
            lv102: R.Tensor((1, 128, 28, 28), dtype="float32") = lv101[0]
            lv105 = R.call_tir(cls.relu4, (lv102,), out_sinfo=R.Tensor((1, 128, 28, 28), dtype="float32"))
            lv106 = R.call_tir(cls.conv2d7, (lv105, metadata["relax.expr.Constant"][85]), out_sinfo=R.Tensor((1, 512, 28, 28), dtype="float32"))
            lv107 = R.call_tir(cls.add1, (lv106, lv88), out_sinfo=R.Tensor((1, 512, 28, 28), dtype="float32"))
            lv108 = R.call_tir(cls.batch_norm6, (lv107, metadata["relax.expr.Constant"][86], metadata["relax.expr.Constant"][87], metadata["relax.expr.Constant"][88], metadata["relax.expr.Constant"][89]), out_sinfo=[R.Tensor((1, 512, 28, 28), dtype="float32"), R.Tensor((512,), dtype="float32"), R.Tensor((512,), dtype="float32")])
            lv109: R.Tensor((1, 512, 28, 28), dtype="float32") = lv108[0]
            lv112 = R.call_tir(cls.relu5, (lv109,), out_sinfo=R.Tensor((1, 512, 28, 28), dtype="float32"))
            lv113 = R.call_tir(cls.conv2d9, (lv112, metadata["relax.expr.Constant"][90]), out_sinfo=R.Tensor((1, 128, 28, 28), dtype="float32"))
            lv114 = R.call_tir(cls.batch_norm5, (lv113, metadata["relax.expr.Constant"][91], metadata["relax.expr.Constant"][92], metadata["relax.expr.Constant"][93], metadata["relax.expr.Constant"][94]), out_sinfo=[R.Tensor((1, 128, 28, 28), dtype="float32"), R.Tensor((128,), dtype="float32"), R.Tensor((128,), dtype="float32")])
            lv115: R.Tensor((1, 128, 28, 28), dtype="float32") = lv114[0]
            lv118 = R.call_tir(cls.relu4, (lv115,), out_sinfo=R.Tensor((1, 128, 28, 28), dtype="float32"))
            lv119 = R.call_tir(cls.conv2d10, (lv118, metadata["relax.expr.Constant"][95]), out_sinfo=R.Tensor((1, 128, 28, 28), dtype="float32"))
            lv120 = R.call_tir(cls.batch_norm5, (lv119, metadata["relax.expr.Constant"][96], metadata["relax.expr.Constant"][97], metadata["relax.expr.Constant"][98], metadata["relax.expr.Constant"][99]), out_sinfo=[R.Tensor((1, 128, 28, 28), dtype="float32"), R.Tensor((128,), dtype="float32"), R.Tensor((128,), dtype="float32")])
            lv121: R.Tensor((1, 128, 28, 28), dtype="float32") = lv120[0]
            lv124 = R.call_tir(cls.relu4, (lv121,), out_sinfo=R.Tensor((1, 128, 28, 28), dtype="float32"))
            lv125 = R.call_tir(cls.conv2d7, (lv124, metadata["relax.expr.Constant"][100]), out_sinfo=R.Tensor((1, 512, 28, 28), dtype="float32"))
            lv126 = R.call_tir(cls.add1, (lv125, lv107), out_sinfo=R.Tensor((1, 512, 28, 28), dtype="float32"))
            lv127 = R.call_tir(cls.batch_norm6, (lv126, metadata["relax.expr.Constant"][101], metadata["relax.expr.Constant"][102], metadata["relax.expr.Constant"][103], metadata["relax.expr.Constant"][104]), out_sinfo=[R.Tensor((1, 512, 28, 28), dtype="float32"), R.Tensor((512,), dtype="float32"), R.Tensor((512,), dtype="float32")])
            lv128: R.Tensor((1, 512, 28, 28), dtype="float32") = lv127[0]
            lv131 = R.call_tir(cls.relu5, (lv128,), out_sinfo=R.Tensor((1, 512, 28, 28), dtype="float32"))
            lv132 = R.call_tir(cls.conv2d9, (lv131, metadata["relax.expr.Constant"][105]), out_sinfo=R.Tensor((1, 128, 28, 28), dtype="float32"))
            lv133 = R.call_tir(cls.batch_norm5, (lv132, metadata["relax.expr.Constant"][106], metadata["relax.expr.Constant"][107], metadata["relax.expr.Constant"][108], metadata["relax.expr.Constant"][109]), out_sinfo=[R.Tensor((1, 128, 28, 28), dtype="float32"), R.Tensor((128,), dtype="float32"), R.Tensor((128,), dtype="float32")])
            lv134: R.Tensor((1, 128, 28, 28), dtype="float32") = lv133[0]
            lv137 = R.call_tir(cls.relu4, (lv134,), out_sinfo=R.Tensor((1, 128, 28, 28), dtype="float32"))
            lv138 = R.call_tir(cls.conv2d10, (lv137, metadata["relax.expr.Constant"][110]), out_sinfo=R.Tensor((1, 128, 28, 28), dtype="float32"))
            lv139 = R.call_tir(cls.batch_norm5, (lv138, metadata["relax.expr.Constant"][111], metadata["relax.expr.Constant"][112], metadata["relax.expr.Constant"][113], metadata["relax.expr.Constant"][114]), out_sinfo=[R.Tensor((1, 128, 28, 28), dtype="float32"), R.Tensor((128,), dtype="float32"), R.Tensor((128,), dtype="float32")])
            lv140: R.Tensor((1, 128, 28, 28), dtype="float32") = lv139[0]
            lv143 = R.call_tir(cls.relu4, (lv140,), out_sinfo=R.Tensor((1, 128, 28, 28), dtype="float32"))
            lv144 = R.call_tir(cls.conv2d7, (lv143, metadata["relax.expr.Constant"][115]), out_sinfo=R.Tensor((1, 512, 28, 28), dtype="float32"))
            lv145 = R.call_tir(cls.add1, (lv144, lv126), out_sinfo=R.Tensor((1, 512, 28, 28), dtype="float32"))
            lv146 = R.call_tir(cls.batch_norm6, (lv145, metadata["relax.expr.Constant"][116], metadata["relax.expr.Constant"][117], metadata["relax.expr.Constant"][118], metadata["relax.expr.Constant"][119]), out_sinfo=[R.Tensor((1, 512, 28, 28), dtype="float32"), R.Tensor((512,), dtype="float32"), R.Tensor((512,), dtype="float32")])
            lv147: R.Tensor((1, 512, 28, 28), dtype="float32") = lv146[0]
            lv150 = R.call_tir(cls.relu5, (lv147,), out_sinfo=R.Tensor((1, 512, 28, 28), dtype="float32"))
            lv151 = R.call_tir(cls.conv2d11, (lv150, metadata["relax.expr.Constant"][120]), out_sinfo=R.Tensor((1, 256, 28, 28), dtype="float32"))
            lv152 = R.call_tir(cls.batch_norm7, (lv151, metadata["relax.expr.Constant"][121], metadata["relax.expr.Constant"][122], metadata["relax.expr.Constant"][123], metadata["relax.expr.Constant"][124]), out_sinfo=[R.Tensor((1, 256, 28, 28), dtype="float32"), R.Tensor((256,), dtype="float32"), R.Tensor((256,), dtype="float32")])
            lv153: R.Tensor((1, 256, 28, 28), dtype="float32") = lv152[0]
            lv156 = R.call_tir(cls.relu6, (lv153,), out_sinfo=R.Tensor((1, 256, 28, 28), dtype="float32"))
            lv157 = R.call_tir(cls.conv2d12, (lv156, metadata["relax.expr.Constant"][125]), out_sinfo=R.Tensor((1, 256, 14, 14), dtype="float32"))
            lv158 = R.call_tir(cls.batch_norm8, (lv157, metadata["relax.expr.Constant"][126], metadata["relax.expr.Constant"][127], metadata["relax.expr.Constant"][128], metadata["relax.expr.Constant"][129]), out_sinfo=[R.Tensor((1, 256, 14, 14), dtype="float32"), R.Tensor((256,), dtype="float32"), R.Tensor((256,), dtype="float32")])
            lv159: R.Tensor((1, 256, 14, 14), dtype="float32") = lv158[0]
            lv162 = R.call_tir(cls.relu7, (lv159,), out_sinfo=R.Tensor((1, 256, 14, 14), dtype="float32"))
            lv163 = R.call_tir(cls.conv2d13, (lv162, metadata["relax.expr.Constant"][130]), out_sinfo=R.Tensor((1, 1024, 14, 14), dtype="float32"))
            lv164 = R.call_tir(cls.conv2d14, (lv150, metadata["relax.expr.Constant"][131]), out_sinfo=R.Tensor((1, 1024, 14, 14), dtype="float32"))
            lv165 = R.call_tir(cls.add2, (lv163, lv164), out_sinfo=R.Tensor((1, 1024, 14, 14), dtype="float32"))
            lv166 = R.call_tir(cls.batch_norm9, (lv165, metadata["relax.expr.Constant"][132], metadata["relax.expr.Constant"][133], metadata["relax.expr.Constant"][134], metadata["relax.expr.Constant"][135]), out_sinfo=[R.Tensor((1, 1024, 14, 14), dtype="float32"), R.Tensor((1024,), dtype="float32"), R.Tensor((1024,), dtype="float32")])
            lv167: R.Tensor((1, 1024, 14, 14), dtype="float32") = lv166[0]
            lv170 = R.call_tir(cls.relu8, (lv167,), out_sinfo=R.Tensor((1, 1024, 14, 14), dtype="float32"))
            lv171 = R.call_tir(cls.conv2d15, (lv170, metadata["relax.expr.Constant"][136]), out_sinfo=R.Tensor((1, 256, 14, 14), dtype="float32"))
            lv172 = R.call_tir(cls.batch_norm8, (lv171, metadata["relax.expr.Constant"][137], metadata["relax.expr.Constant"][138], metadata["relax.expr.Constant"][139], metadata["relax.expr.Constant"][140]), out_sinfo=[R.Tensor((1, 256, 14, 14), dtype="float32"), R.Tensor((256,), dtype="float32"), R.Tensor((256,), dtype="float32")])
            lv173: R.Tensor((1, 256, 14, 14), dtype="float32") = lv172[0]
            lv176 = R.call_tir(cls.relu7, (lv173,), out_sinfo=R.Tensor((1, 256, 14, 14), dtype="float32"))
            lv177 = R.call_tir(cls.conv2d16, (lv176, metadata["relax.expr.Constant"][141]), out_sinfo=R.Tensor((1, 256, 14, 14), dtype="float32"))
            lv178 = R.call_tir(cls.batch_norm8, (lv177, metadata["relax.expr.Constant"][142], metadata["relax.expr.Constant"][143], metadata["relax.expr.Constant"][144], metadata["relax.expr.Constant"][145]), out_sinfo=[R.Tensor((1, 256, 14, 14), dtype="float32"), R.Tensor((256,), dtype="float32"), R.Tensor((256,), dtype="float32")])
            lv179: R.Tensor((1, 256, 14, 14), dtype="float32") = lv178[0]
            lv182 = R.call_tir(cls.relu7, (lv179,), out_sinfo=R.Tensor((1, 256, 14, 14), dtype="float32"))
            lv183 = R.call_tir(cls.conv2d13, (lv182, metadata["relax.expr.Constant"][146]), out_sinfo=R.Tensor((1, 1024, 14, 14), dtype="float32"))
            lv184 = R.call_tir(cls.add2, (lv183, lv165), out_sinfo=R.Tensor((1, 1024, 14, 14), dtype="float32"))
            lv185 = R.call_tir(cls.batch_norm9, (lv184, metadata["relax.expr.Constant"][147], metadata["relax.expr.Constant"][148], metadata["relax.expr.Constant"][149], metadata["relax.expr.Constant"][150]), out_sinfo=[R.Tensor((1, 1024, 14, 14), dtype="float32"), R.Tensor((1024,), dtype="float32"), R.Tensor((1024,), dtype="float32")])
            lv186: R.Tensor((1, 1024, 14, 14), dtype="float32") = lv185[0]
            lv189 = R.call_tir(cls.relu8, (lv186,), out_sinfo=R.Tensor((1, 1024, 14, 14), dtype="float32"))
            lv190 = R.call_tir(cls.conv2d15, (lv189, metadata["relax.expr.Constant"][151]), out_sinfo=R.Tensor((1, 256, 14, 14), dtype="float32"))
            lv191 = R.call_tir(cls.batch_norm8, (lv190, metadata["relax.expr.Constant"][152], metadata["relax.expr.Constant"][153], metadata["relax.expr.Constant"][154], metadata["relax.expr.Constant"][155]), out_sinfo=[R.Tensor((1, 256, 14, 14), dtype="float32"), R.Tensor((256,), dtype="float32"), R.Tensor((256,), dtype="float32")])
            lv192: R.Tensor((1, 256, 14, 14), dtype="float32") = lv191[0]
            lv195 = R.call_tir(cls.relu7, (lv192,), out_sinfo=R.Tensor((1, 256, 14, 14), dtype="float32"))
            lv196 = R.call_tir(cls.conv2d16, (lv195, metadata["relax.expr.Constant"][156]), out_sinfo=R.Tensor((1, 256, 14, 14), dtype="float32"))
            lv197 = R.call_tir(cls.batch_norm8, (lv196, metadata["relax.expr.Constant"][157], metadata["relax.expr.Constant"][158], metadata["relax.expr.Constant"][159], metadata["relax.expr.Constant"][160]), out_sinfo=[R.Tensor((1, 256, 14, 14), dtype="float32"), R.Tensor((256,), dtype="float32"), R.Tensor((256,), dtype="float32")])
            lv198: R.Tensor((1, 256, 14, 14), dtype="float32") = lv197[0]
            lv201 = R.call_tir(cls.relu7, (lv198,), out_sinfo=R.Tensor((1, 256, 14, 14), dtype="float32"))
            lv202 = R.call_tir(cls.conv2d13, (lv201, metadata["relax.expr.Constant"][161]), out_sinfo=R.Tensor((1, 1024, 14, 14), dtype="float32"))
            lv203 = R.call_tir(cls.add2, (lv202, lv184), out_sinfo=R.Tensor((1, 1024, 14, 14), dtype="float32"))
            lv204 = R.call_tir(cls.batch_norm9, (lv203, metadata["relax.expr.Constant"][162], metadata["relax.expr.Constant"][163], metadata["relax.expr.Constant"][164], metadata["relax.expr.Constant"][165]), out_sinfo=[R.Tensor((1, 1024, 14, 14), dtype="float32"), R.Tensor((1024,), dtype="float32"), R.Tensor((1024,), dtype="float32")])
            lv205: R.Tensor((1, 1024, 14, 14), dtype="float32") = lv204[0]
            lv208 = R.call_tir(cls.relu8, (lv205,), out_sinfo=R.Tensor((1, 1024, 14, 14), dtype="float32"))
            lv209 = R.call_tir(cls.conv2d15, (lv208, metadata["relax.expr.Constant"][166]), out_sinfo=R.Tensor((1, 256, 14, 14), dtype="float32"))
            lv210 = R.call_tir(cls.batch_norm8, (lv209, metadata["relax.expr.Constant"][167], metadata["relax.expr.Constant"][168], metadata["relax.expr.Constant"][169], metadata["relax.expr.Constant"][170]), out_sinfo=[R.Tensor((1, 256, 14, 14), dtype="float32"), R.Tensor((256,), dtype="float32"), R.Tensor((256,), dtype="float32")])
            lv211: R.Tensor((1, 256, 14, 14), dtype="float32") = lv210[0]
            lv214 = R.call_tir(cls.relu7, (lv211,), out_sinfo=R.Tensor((1, 256, 14, 14), dtype="float32"))
            lv215 = R.call_tir(cls.conv2d16, (lv214, metadata["relax.expr.Constant"][171]), out_sinfo=R.Tensor((1, 256, 14, 14), dtype="float32"))
            lv216 = R.call_tir(cls.batch_norm8, (lv215, metadata["relax.expr.Constant"][172], metadata["relax.expr.Constant"][173], metadata["relax.expr.Constant"][174], metadata["relax.expr.Constant"][175]), out_sinfo=[R.Tensor((1, 256, 14, 14), dtype="float32"), R.Tensor((256,), dtype="float32"), R.Tensor((256,), dtype="float32")])
            lv217: R.Tensor((1, 256, 14, 14), dtype="float32") = lv216[0]
            lv220 = R.call_tir(cls.relu7, (lv217,), out_sinfo=R.Tensor((1, 256, 14, 14), dtype="float32"))
            lv221 = R.call_tir(cls.conv2d13, (lv220, metadata["relax.expr.Constant"][176]), out_sinfo=R.Tensor((1, 1024, 14, 14), dtype="float32"))
            lv222 = R.call_tir(cls.add2, (lv221, lv203), out_sinfo=R.Tensor((1, 1024, 14, 14), dtype="float32"))
            lv223 = R.call_tir(cls.batch_norm9, (lv222, metadata["relax.expr.Constant"][177], metadata["relax.expr.Constant"][178], metadata["relax.expr.Constant"][179], metadata["relax.expr.Constant"][180]), out_sinfo=[R.Tensor((1, 1024, 14, 14), dtype="float32"), R.Tensor((1024,), dtype="float32"), R.Tensor((1024,), dtype="float32")])
            lv224: R.Tensor((1, 1024, 14, 14), dtype="float32") = lv223[0]
            lv227 = R.call_tir(cls.relu8, (lv224,), out_sinfo=R.Tensor((1, 1024, 14, 14), dtype="float32"))
            lv228 = R.call_tir(cls.conv2d15, (lv227, metadata["relax.expr.Constant"][181]), out_sinfo=R.Tensor((1, 256, 14, 14), dtype="float32"))
            lv229 = R.call_tir(cls.batch_norm8, (lv228, metadata["relax.expr.Constant"][182], metadata["relax.expr.Constant"][183], metadata["relax.expr.Constant"][184], metadata["relax.expr.Constant"][185]), out_sinfo=[R.Tensor((1, 256, 14, 14), dtype="float32"), R.Tensor((256,), dtype="float32"), R.Tensor((256,), dtype="float32")])
            lv230: R.Tensor((1, 256, 14, 14), dtype="float32") = lv229[0]
            lv233 = R.call_tir(cls.relu7, (lv230,), out_sinfo=R.Tensor((1, 256, 14, 14), dtype="float32"))
            lv234 = R.call_tir(cls.conv2d16, (lv233, metadata["relax.expr.Constant"][186]), out_sinfo=R.Tensor((1, 256, 14, 14), dtype="float32"))
            lv235 = R.call_tir(cls.batch_norm8, (lv234, metadata["relax.expr.Constant"][187], metadata["relax.expr.Constant"][188], metadata["relax.expr.Constant"][189], metadata["relax.expr.Constant"][190]), out_sinfo=[R.Tensor((1, 256, 14, 14), dtype="float32"), R.Tensor((256,), dtype="float32"), R.Tensor((256,), dtype="float32")])
            lv236: R.Tensor((1, 256, 14, 14), dtype="float32") = lv235[0]
            lv239 = R.call_tir(cls.relu7, (lv236,), out_sinfo=R.Tensor((1, 256, 14, 14), dtype="float32"))
            lv240 = R.call_tir(cls.conv2d13, (lv239, metadata["relax.expr.Constant"][191]), out_sinfo=R.Tensor((1, 1024, 14, 14), dtype="float32"))
            lv241 = R.call_tir(cls.add2, (lv240, lv222), out_sinfo=R.Tensor((1, 1024, 14, 14), dtype="float32"))
            lv242 = R.call_tir(cls.batch_norm9, (lv241, metadata["relax.expr.Constant"][192], metadata["relax.expr.Constant"][193], metadata["relax.expr.Constant"][194], metadata["relax.expr.Constant"][195]), out_sinfo=[R.Tensor((1, 1024, 14, 14), dtype="float32"), R.Tensor((1024,), dtype="float32"), R.Tensor((1024,), dtype="float32")])
            lv243: R.Tensor((1, 1024, 14, 14), dtype="float32") = lv242[0]
            lv246 = R.call_tir(cls.relu8, (lv243,), out_sinfo=R.Tensor((1, 1024, 14, 14), dtype="float32"))
            lv247 = R.call_tir(cls.conv2d15, (lv246, metadata["relax.expr.Constant"][196]), out_sinfo=R.Tensor((1, 256, 14, 14), dtype="float32"))
            lv248 = R.call_tir(cls.batch_norm8, (lv247, metadata["relax.expr.Constant"][197], metadata["relax.expr.Constant"][198], metadata["relax.expr.Constant"][199], metadata["relax.expr.Constant"][200]), out_sinfo=[R.Tensor((1, 256, 14, 14), dtype="float32"), R.Tensor((256,), dtype="float32"), R.Tensor((256,), dtype="float32")])
            lv249: R.Tensor((1, 256, 14, 14), dtype="float32") = lv248[0]
            lv252 = R.call_tir(cls.relu7, (lv249,), out_sinfo=R.Tensor((1, 256, 14, 14), dtype="float32"))
            lv253 = R.call_tir(cls.conv2d16, (lv252, metadata["relax.expr.Constant"][201]), out_sinfo=R.Tensor((1, 256, 14, 14), dtype="float32"))
            lv254 = R.call_tir(cls.batch_norm8, (lv253, metadata["relax.expr.Constant"][202], metadata["relax.expr.Constant"][203], metadata["relax.expr.Constant"][204], metadata["relax.expr.Constant"][205]), out_sinfo=[R.Tensor((1, 256, 14, 14), dtype="float32"), R.Tensor((256,), dtype="float32"), R.Tensor((256,), dtype="float32")])
            lv255: R.Tensor((1, 256, 14, 14), dtype="float32") = lv254[0]
            lv258 = R.call_tir(cls.relu7, (lv255,), out_sinfo=R.Tensor((1, 256, 14, 14), dtype="float32"))
            lv259 = R.call_tir(cls.conv2d13, (lv258, metadata["relax.expr.Constant"][206]), out_sinfo=R.Tensor((1, 1024, 14, 14), dtype="float32"))
            lv260 = R.call_tir(cls.add2, (lv259, lv241), out_sinfo=R.Tensor((1, 1024, 14, 14), dtype="float32"))
            lv261 = R.call_tir(cls.batch_norm9, (lv260, metadata["relax.expr.Constant"][207], metadata["relax.expr.Constant"][208], metadata["relax.expr.Constant"][209], metadata["relax.expr.Constant"][210]), out_sinfo=[R.Tensor((1, 1024, 14, 14), dtype="float32"), R.Tensor((1024,), dtype="float32"), R.Tensor((1024,), dtype="float32")])
            lv262: R.Tensor((1, 1024, 14, 14), dtype="float32") = lv261[0]
            lv265 = R.call_tir(cls.relu8, (lv262,), out_sinfo=R.Tensor((1, 1024, 14, 14), dtype="float32"))
            lv266 = R.call_tir(cls.conv2d17, (lv265, metadata["relax.expr.Constant"][211]), out_sinfo=R.Tensor((1, 512, 14, 14), dtype="float32"))
            lv267 = R.call_tir(cls.batch_norm10, (lv266, metadata["relax.expr.Constant"][212], metadata["relax.expr.Constant"][213], metadata["relax.expr.Constant"][214], metadata["relax.expr.Constant"][215]), out_sinfo=[R.Tensor((1, 512, 14, 14), dtype="float32"), R.Tensor((512,), dtype="float32"), R.Tensor((512,), dtype="float32")])
            lv268: R.Tensor((1, 512, 14, 14), dtype="float32") = lv267[0]
            lv271 = R.call_tir(cls.relu9, (lv268,), out_sinfo=R.Tensor((1, 512, 14, 14), dtype="float32"))
            lv272 = R.call_tir(cls.conv2d18, (lv271, metadata["relax.expr.Constant"][216]), out_sinfo=R.Tensor((1, 512, 7, 7), dtype="float32"))
            lv273 = R.call_tir(cls.batch_norm11, (lv272, metadata["relax.expr.Constant"][217], metadata["relax.expr.Constant"][218], metadata["relax.expr.Constant"][219], metadata["relax.expr.Constant"][220]), out_sinfo=[R.Tensor((1, 512, 7, 7), dtype="float32"), R.Tensor((512,), dtype="float32"), R.Tensor((512,), dtype="float32")])
            lv274: R.Tensor((1, 512, 7, 7), dtype="float32") = lv273[0]
            lv277 = R.call_tir(cls.relu10, (lv274,), out_sinfo=R.Tensor((1, 512, 7, 7), dtype="float32"))
            lv278 = R.call_tir(cls.conv2d19, (lv277, metadata["relax.expr.Constant"][221]), out_sinfo=R.Tensor((1, 2048, 7, 7), dtype="float32"))
            lv279 = R.call_tir(cls.conv2d20, (lv265, metadata["relax.expr.Constant"][222]), out_sinfo=R.Tensor((1, 2048, 7, 7), dtype="float32"))
            lv280 = R.call_tir(cls.add3, (lv278, lv279), out_sinfo=R.Tensor((1, 2048, 7, 7), dtype="float32"))
            lv281 = R.call_tir(cls.batch_norm12, (lv280, metadata["relax.expr.Constant"][223], metadata["relax.expr.Constant"][224], metadata["relax.expr.Constant"][225], metadata["relax.expr.Constant"][226]), out_sinfo=[R.Tensor((1, 2048, 7, 7), dtype="float32"), R.Tensor((2048,), dtype="float32"), R.Tensor((2048,), dtype="float32")])
            lv282: R.Tensor((1, 2048, 7, 7), dtype="float32") = lv281[0]
            lv285 = R.call_tir(cls.relu11, (lv282,), out_sinfo=R.Tensor((1, 2048, 7, 7), dtype="float32"))
            lv286 = R.call_tir(cls.conv2d21, (lv285, metadata["relax.expr.Constant"][227]), out_sinfo=R.Tensor((1, 512, 7, 7), dtype="float32"))
            lv287 = R.call_tir(cls.batch_norm11, (lv286, metadata["relax.expr.Constant"][228], metadata["relax.expr.Constant"][229], metadata["relax.expr.Constant"][230], metadata["relax.expr.Constant"][231]), out_sinfo=[R.Tensor((1, 512, 7, 7), dtype="float32"), R.Tensor((512,), dtype="float32"), R.Tensor((512,), dtype="float32")])
            lv288: R.Tensor((1, 512, 7, 7), dtype="float32") = lv287[0]
            lv291 = R.call_tir(cls.relu10, (lv288,), out_sinfo=R.Tensor((1, 512, 7, 7), dtype="float32"))
            lv292 = R.call_tir(cls.conv2d22, (lv291, metadata["relax.expr.Constant"][232]), out_sinfo=R.Tensor((1, 512, 7, 7), dtype="float32"))
            lv293 = R.call_tir(cls.batch_norm11, (lv292, metadata["relax.expr.Constant"][233], metadata["relax.expr.Constant"][234], metadata["relax.expr.Constant"][235], metadata["relax.expr.Constant"][236]), out_sinfo=[R.Tensor((1, 512, 7, 7), dtype="float32"), R.Tensor((512,), dtype="float32"), R.Tensor((512,), dtype="float32")])
            lv294: R.Tensor((1, 512, 7, 7), dtype="float32") = lv293[0]
            lv297 = R.call_tir(cls.relu10, (lv294,), out_sinfo=R.Tensor((1, 512, 7, 7), dtype="float32"))
            lv298 = R.call_tir(cls.conv2d19, (lv297, metadata["relax.expr.Constant"][237]), out_sinfo=R.Tensor((1, 2048, 7, 7), dtype="float32"))
            lv299 = R.call_tir(cls.add3, (lv298, lv280), out_sinfo=R.Tensor((1, 2048, 7, 7), dtype="float32"))
            lv300 = R.call_tir(cls.batch_norm12, (lv299, metadata["relax.expr.Constant"][238], metadata["relax.expr.Constant"][239], metadata["relax.expr.Constant"][240], metadata["relax.expr.Constant"][241]), out_sinfo=[R.Tensor((1, 2048, 7, 7), dtype="float32"), R.Tensor((2048,), dtype="float32"), R.Tensor((2048,), dtype="float32")])
            lv301: R.Tensor((1, 2048, 7, 7), dtype="float32") = lv300[0]
            lv304 = R.call_tir(cls.relu11, (lv301,), out_sinfo=R.Tensor((1, 2048, 7, 7), dtype="float32"))
            lv305 = R.call_tir(cls.conv2d21, (lv304, metadata["relax.expr.Constant"][242]), out_sinfo=R.Tensor((1, 512, 7, 7), dtype="float32"))
            lv306 = R.call_tir(cls.batch_norm11, (lv305, metadata["relax.expr.Constant"][243], metadata["relax.expr.Constant"][244], metadata["relax.expr.Constant"][245], metadata["relax.expr.Constant"][246]), out_sinfo=[R.Tensor((1, 512, 7, 7), dtype="float32"), R.Tensor((512,), dtype="float32"), R.Tensor((512,), dtype="float32")])
            lv307: R.Tensor((1, 512, 7, 7), dtype="float32") = lv306[0]
            lv310 = R.call_tir(cls.relu10, (lv307,), out_sinfo=R.Tensor((1, 512, 7, 7), dtype="float32"))
            lv311 = R.call_tir(cls.conv2d22, (lv310, metadata["relax.expr.Constant"][247]), out_sinfo=R.Tensor((1, 512, 7, 7), dtype="float32"))
            lv312 = R.call_tir(cls.batch_norm11, (lv311, metadata["relax.expr.Constant"][248], metadata["relax.expr.Constant"][249], metadata["relax.expr.Constant"][250], metadata["relax.expr.Constant"][251]), out_sinfo=[R.Tensor((1, 512, 7, 7), dtype="float32"), R.Tensor((512,), dtype="float32"), R.Tensor((512,), dtype="float32")])
            lv313: R.Tensor((1, 512, 7, 7), dtype="float32") = lv312[0]
            lv316 = R.call_tir(cls.relu10, (lv313,), out_sinfo=R.Tensor((1, 512, 7, 7), dtype="float32"))
            lv317 = R.call_tir(cls.conv2d19, (lv316, metadata["relax.expr.Constant"][252]), out_sinfo=R.Tensor((1, 2048, 7, 7), dtype="float32"))
            lv318 = R.call_tir(cls.add3, (lv317, lv299), out_sinfo=R.Tensor((1, 2048, 7, 7), dtype="float32"))
            lv319 = R.call_tir(cls.batch_norm12, (lv318, metadata["relax.expr.Constant"][253], metadata["relax.expr.Constant"][254], metadata["relax.expr.Constant"][255], metadata["relax.expr.Constant"][256]), out_sinfo=[R.Tensor((1, 2048, 7, 7), dtype="float32"), R.Tensor((2048,), dtype="float32"), R.Tensor((2048,), dtype="float32")])
            lv320: R.Tensor((1, 2048, 7, 7), dtype="float32") = lv319[0]
            lv323 = R.call_tir(cls.relu11, (lv320,), out_sinfo=R.Tensor((1, 2048, 7, 7), dtype="float32"))
            lv324 = R.call_tir(cls.mean, (lv323,), out_sinfo=R.Tensor((1, 2048, 1, 1), dtype="float32"))
            lv325 = R.call_tir(cls.reshape, (lv324,), out_sinfo=R.Tensor((1, 2048), dtype="float32"))
            lv326 = R.call_tir(cls.transpose, (metadata["relax.expr.Constant"][257],), out_sinfo=R.Tensor((2048, 1000), dtype="float32"))
            lv327 = R.call_tir(cls.matmul, (lv325, lv326), out_sinfo=R.Tensor((1, 1000), dtype="float32"))
            gv = R.call_tir(cls.add4, (lv327, metadata["relax.expr.Constant"][258]), out_sinfo=R.Tensor((1, 1000), dtype="float32"))
            R.output(gv)
        return gv

# Metadata omitted. Use show_meta=True in script() method to show it.