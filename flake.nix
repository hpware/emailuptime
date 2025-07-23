devShell = pkgs.mkShell {
  name = "emailuptime";
  nativeBuildInputs = [
    pythonEnv
    pkgs.glib
    pkgs.nspr
    pkgs.nss
    pkgs.dbus
    pkgs.atk
    pkgs.atk_bridge
    pkgs.cups
    pkgs.xorg.libxcb
    pkgs.xorg.libxkbcommon
    pkgs.atspi2
    pkgs.xorg.libX11
    pkgs.xorg.libXcomposite
    pkgs.xorg.libXdamage
    pkgs.xorg.libXext
    pkgs.xorg.libXfixes
    pkgs.xorg.libXrandr
    pkgs.gbm
    pkgs.cairo
    pkgs.pango
    pkgs.alsaLib
  ];
};
