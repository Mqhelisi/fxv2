
#!/usr/bin/env bash
sudo apt install build-essential wget -y
tar -xvf ta-lib-0.4.0-src.tar.gz
cd ta-lib/
./configure --prefix=/usr
make
sudo make install