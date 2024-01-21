# molecule-kind

[![Unit Test](https://github.com/retr0h/molecule-kind/actions/workflows/unit.yml/badge.svg)](https://github.com/retr0h/molecule-kind/actions/workflows/unit.yml)
[![Lint](https://github.com/retr0h/molecule-kind/actions/workflows/lint.yml/badge.svg)](https://github.com/retr0h/molecule-kind/actions/workflows/lint.yml)

molecule-kind - Molecule Kind Driver allows Molecule users to test Ansible code using Kind.

## Dependencies

This project has been tested against the following matrix:

| Project  | Version |
| -------- | ------- |
| [Kind]   | 0.20    |
| Python   | 3.10    |
| Ansible  | 9.1.0   |
| Molecule | 6.0.3   |

## Installing

    $ pip install molecule-kind

## Usage

    $ molecule init scenario -d kind
    $ molecule test

## Testing

To execute unit tests.

    $ make dep
    $ make test

## License

The [MIT] License.

[Kind]: https://github.com/kubernetes-sigs/kind
[MIT]: LICENSE
