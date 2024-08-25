# MotiveProcessor
MotiveProcessor is a project designed to process motion capture data using NMotive.
The project includes scripts for creating directories, extracting `.tak` files (for repeated recoding), 
and exporting them to `.csv` and `.trc` formats.

**Motive Version:** 2.0.0

## Author

- **Jaebeom Jo**
- **Email:** [jojaebeom@gm.gist.ac.kr](mailto:jojaebeom@gm.gist.ac.kr)

## Usage

### Setting Up Directories
To set up directories for a specific subject, you can use the `run_mk_dir.bat` script. 
This script will prompt you to enter a subject number and will create the necessary directories as configured in `config.json`.

```bash
run_mk_dir.bat
```

### Export .tak files to .csv and .trc
To export `.tak` files to `.csv` and `.trc` formats, you can use the `run_export.bat` script.
```bash
run_export.bat
```