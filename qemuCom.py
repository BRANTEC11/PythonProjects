def qemu(s):
    print("aarch64-linux-gnu-as " + s + ".s -o " + s + ".o && aarch64-linux-gnu-ld " + s + ".o -lc && qemu-aarch64 -L /usr/aarch64-linux-gnu/ a.out")
