# AnalyzeTEMPLATE

Analysis repository for XX.

[![Data](https://img.shields.io/badge/data-ConvertTEMPLATE-lightgrey)](https://github.com/HSUPipeline/ConvertTEMPLATE)
[![Template](https://img.shields.io/badge/template-HSUPipeline/AnalyzeTEMPLATE-yellow.svg)](https://github.com/HSUPipeline/AnalyzeTEMPLATE)

## TEMPLATE DESCRIPTION

This is a template repository for a standard layout for analyzing a single-unit project.

This template follows the general purpose
[ProjectTemplate](https://github.com/structuredscience/ProjectTemplate)
layout from
[StructuredScience](https://github.com/structuredscience/).

Note: if copying this template for use, this section can be removed.

## Overview

**Provide an overview of the analysis project here, for example:**

This repository analyses data from the XX task, which is XX.

## Requirements

**Fill in any extra requirements here.**

This repository requires Python >= 3.7.

As well as typical scientific Python packages, dependencies include:
- [pynwb](https://github.com/NeurodataWithoutBorders/pynwb)
- [convnwb](https://github.com/HSUPipeline/convnwb)
- [spiketools](https://github.com/spiketools/spiketools)

The full list of dependencies is listed in `requirements.txt`.

## Repository Layout

Add any details about repository layout here.

This repository is set up in the following way:
- `code/` contains custom code and utilities
- `notebooks/` contains notebooks for exploring analyses
- `scripts/` contains stand alone scripts

## Data

**Add any notes about the dataset here**

The datasets analyzed in this project are from human subjects with implanted microwires.

Data notes:
- Datasets for this project are organized into the [NWB](https://www.nwb.org/) format.
- Basic preprocessing and data conversion is done in the ConvertXX repository [ADD LINK].
- Spike sorting, to isolate putative single-neurons, has been performed on this data.
