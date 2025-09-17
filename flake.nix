{
  description = "Neuroject - Simple Python GUI for drawing geometry";

  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable";
    flake-utils.url = "github:numtide/flake-utils";
  };

  outputs = { self, nixpkgs, flake-utils }:
    flake-utils.lib.eachDefaultSystem (system:
      let
        pkgs = nixpkgs.legacyPackages.${system};
        
        python = pkgs.python3;
        
        # Simple script to run the GUI
        neuroject = pkgs.writeShellScriptBin "neuroject" ''
          cd ${./.}
          ${python}/bin/python main.py
        '';
      in
      {
        packages = {
          default = neuroject;
          neuroject = neuroject;
        };

        apps = {
          default = {
            type = "app";
            program = "${neuroject}/bin/neuroject";
          };
        };

        devShells.default = pkgs.mkShell {
          buildInputs = with pkgs; [
            python3
            python3Packages.tkinter
          ];
          
          shellHook = ''
            echo "Neuroject development environment"
            echo "Run 'python main.py' to start the GUI"
            echo "Or use 'nix run' to run the application"
          '';
        };
      });
}