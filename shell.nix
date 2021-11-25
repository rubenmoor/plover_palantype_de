# > nix-shell
# > virtualenv venv
# > source venv/bin/activate
# > python setup.py sdist bdist_wheel
# > twine upload dist/*

{ pkgs ? import <nixpkgs> {} }:
(pkgs.buildFHSUserEnv {
  name = "pipzone";
  targetPkgs = pkgs: (with pkgs; [
    python39
    python39Packages.pip
    python39Packages.virtualenv
  ]);
}).env
