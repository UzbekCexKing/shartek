{ pkgs }: {
  deps = [
    pkgs.pyupgrade
    pkgs.gdb
    pkgs.nodejs-16_x
    pkgs.replitPackages.prybar-python3
  ];
}