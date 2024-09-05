{
  pkgs ? import <nixpkgs> { },
}:
pkgs.mkShell {
  name = "dev-environment";
  packages = [
    (pkgs.python3.withPackages (python-pkgs: [
      python-pkgs.flask
    ]))
  ];
}
