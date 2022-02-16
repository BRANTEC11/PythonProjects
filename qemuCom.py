def qemu(s):
    print("aarch64-linux-gnu-as " + s + ".s -o " + s + ".o && aarch64-linux-gnu-ld " + s + ".o -lc && qemu-aarch64 -L /usr/aarch64-linux-gnu/ a.out")
#aarch64-linux-gnu-as lab6_2.s -o lab6_2.o && aarch64-linux-gnu-ld lab6_2.o -lc &&  qemu-aarch64 -L /usr/aarch64-linux-gnu/ a.out
#aarch64-linux-gnu-as lab6_1.s -o lab6_1.o && aarch64-linux-gnu-ld lab6_1.o -lc &&  qemu-aarch64 -L /usr/aarch64-linux-gnu/ a.out