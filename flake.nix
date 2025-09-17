{
  description = "Neuroject - A simple Python GUI for drawing geometry";

  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable";
    flake-utils.url = "github:numtide/flake-utils";
  };

  outputs = { self, nixpkgs, flake-utils }:
    flake-utils.lib.eachDefaultSystem (system:
      let
        pkgs = nixpkgs.legacyPackages.${system};
        
        python-with-packages = pkgs.python3.withPackages (p: with p; [
          tkinter
          matplotlib
          numpy
        ]);

        neuroject = pkgs.writeShellScriptBin "neuroject" ''
          ${python-with-packages}/bin/python ${./src/main.py}
        '';

      in
      {
        packages.default = neuroject;
        packages.neuroject = neuroject;

        devShells.default = pkgs.mkShell {
          buildInputs = with pkgs; [
            python-with-packages
            # Development tools
            python3Packages.black
            python3Packages.flake8
          ];

          shellHook = ''
            echo "Welcome to Neuroject development environment!"
            echo "Python GUI for drawing simple geometry"
            echo ""
            echo "Available commands:"
            echo "  python src/main.py  - Run the application directly"
            echo "  nix run            - Run the packaged application"
            echo ""
            echo "Dependencies available:"
            echo "  - Python ${python-with-packages.version}"
            echo "  - tkinter (GUI framework)"
            echo "  - matplotlib (plotting)"
            echo "  - numpy (numerical operations)"
          '';
        };

        apps.default = {
          type = "app";
          program = "${neuroject}/bin/neuroject";
        };
      });
}