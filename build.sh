#!/bin/bash

# Install Rust and Cargo
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh -s -- -y

# Ensure Rust is available in the current shell
source $HOME/.cargo/env

# Proceed with the installation of Python dependencies
pip3.12 install --disable-pip-version-check --target . --upgrade -r /vercel/path0/requirements.txt
