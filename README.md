# COMPAS Introduction: MAS 2025/2026

[🎦 Slides](https://docs.google.com/presentation/d/1Sv9Yyys9Ud5o9Huc6GJtrD2rFueIHChBNAs1Dag9dQo/edit?usp=sharing)

## Installation

> **NOTE**: If you're on Windows, all commands below have to be executed in the *Anaconda Prompt* (NOT the *Command Prompt*)

We use `conda` to make sure we have clean, isolated environment for dependencies.

<details><summary>First time using <code>conda</code>?</summary>
<p>

Make sure you run this at least once:

    (base) conda config --add channels conda-forge

</p>
</details>


    (base) conda env create -f https://dfab.link/intro24.yml

### Add to Rhino

    (base)    conda activate intro24
    (intro24) python -m compas_rhino.install -v 7.0

### Get the workshop files

Clone the repository:

    (intro24) cd Documents
    (intro24) git clone https://github.com/gramaziokohler/compas_introduction_2024.git

### Verify installation

    (intro24) python -m compas

    Yay! COMPAS is installed correctly!

    COMPAS: 2.4.3
    Python: 3.10.15 (CPython)
    Extensions: ['compas']

### Update installation

To update your environment:

    (intro24) conda env update -f https://dfab.link/intro24.yml