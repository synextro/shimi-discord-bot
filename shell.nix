{ pkgs ? import <nixpkgs> {} }:

pkgs.mkShell {
  nativeBuildInputs = with pkgs; [
    python312
    python312Packages.pip
    ffmpeg_7
  ];

  buildInputs = with pkgs; [
    openssl
    zlib
    libopus
  ];

  shellHook = ''
    if [ ! -d "venv" ]; then
      python -m venv venv
    fi

    export PATH="$PWD/venv/bin:$PATH"

    echo "environment loaded!"
  '';
}
