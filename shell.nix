{ pkgs ? import <nixpkgs> {} }:

pkgs.mkShell {
  nativeBuildInputs = with pkgs; [
    python314
    python314Packages.pip
  ];

  buildInputs = with pkgs; [
    openssl
    zlib
  ];

  shellHook = ''
    if [ ! -d "venv" ]; then
      python -m venv venv
    fi

    export PATH="$PWD/venv/bin:$PATH"

    echo "environment loaded!"
  '';
}
