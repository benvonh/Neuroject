{
  description = "Neuroject - Python GUI for drawing simple geometry";

  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable";
    flake-utils.url = "github:numtide/flake-utils";
  };

  outputs = { self, nixpkgs, flake-utils }:
    flake-utils.lib.eachDefaultSystem (system:
      let
        pkgs = nixpkgs.legacyPackages.${system};
        
        python = pkgs.python3;
        pythonPackages = python.pkgs;
        
        neuroject = pythonPackages.buildPythonApplication {
          pname = "neuroject";
          version = "0.1.0";
          
          src = ./.;
          
          propagatedBuildInputs = with pythonPackages; [
            tkinter
          ];
          
          meta = with pkgs.lib; {
            description = "Simple GUI for drawing geometry";
            license = licenses.mit;
            maintainers = [ ];
          };
        };
      in
      {
        packages = {
          default = neuroject;
          neuroject = neuroject;
        };

        devShells.default = pkgs.mkShell {
          buildInputs = with pkgs; [
            python3
            python3Packages.tkinter
            python3Packages.pip
            python3Packages.setuptools
          ];
          
          shellHook = ''
            echo "Neuroject development environment"
            echo "Run 'python -m neuroject' to start the GUI"
          '';
        };
      });
}