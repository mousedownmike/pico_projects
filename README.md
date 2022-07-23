# pico_projects

This repository contains my random Raspberry Pi Pico projects.

# Project Setup

## Poetry

Projects use [Poetry] for package management.

## Create New Projects

```shell
mkdir project_name
cd project_name
poetry init
```

# PyCharm Set Up

- Use MicroPython plugin
- Add user to `dialout` on Ubuntu
 - `sudo usermod -a -G dialout mike` 
 - Reboot