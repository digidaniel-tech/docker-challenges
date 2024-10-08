{
  pkgs ? import <nixpkgs> {},
}:
pkgs.mkShell {
  name = "dev-environment";
  packages = [
    (pkgs.nodejs_22)
    (pkgs.python3.withPackages (python-pkgs: [
      python-pkgs.flask
      python-pkgs.sqlalchemy
      python-pkgs.pg8000
      python-pkgs.flask-restful
    ]))
  ];
}
