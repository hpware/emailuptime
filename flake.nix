{
  description = "emailuptime";

  inputs = {
    nixpkgs.url = "github:nixos/nixpkgs/release-22.11";
    flake-utils.url = "github:numtide/flake-utils";
  };

  outputs = { self, nixpkgs, flake-utils }:
    flake-utils.lib.eachDefaultSystem (system:
      let
        pkgs = import nixpkgs { inherit system; };
        pythonEnv = pkgs.python3.withPackages (ps: with ps; [
          flask
          # Add other dependencies here, e.g. psycopg2, requests, etc.
        ]);
      in with pkgs; rec {
        # Development environment
        devShell = mkShell {
          name = "flask-example";
          nativeBuildInputs = [ pythonEnv ];
        };

        # Runtime package (if you want to build an app derivation)
        packages.app = pythonEnv;

        defaultPackage = packages.app;
      }
    );
}
