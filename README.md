# MAIO

Course material for MAIO: a random forest model for ozone at Cabauw, and the literature on fast-response temperature measurement.

## Layout

```
literature/
  papers/        Original PDFs
                   vanasselt1991.pdf        van Asselt et al. (1991), A rigid fast-response thermometer for atmospheric research
                   schotanus1983.pdf        Schotanus et al. (1983), Temperature measurement with a sonic anemometer
                   nakamura_mahrt2005.pdf   Nakamura and Mahrt (2005), J. Atmos. Oceanic Technol. 22
  markdown/      Final Markdown versions of the papers
  conversion/    PDF-to-Markdown conversion output per paper (MinerU output, image crops, QA reports, fix notes)

random-forest/
  data/raw/      Hourly station data 2016-2019, one folder per station (Rural_*, Urban_*, Street_*)
  scripts/       Analysis and model scripts
  results/       Model output, statistics tables and figures
  report/        Extended abstract (abstract.tex, abstract.pdf) and the assignment (Handin_Random_Forest_2026.pdf)
  notes/         Project summary and oral exam preparation
```

## Running the scripts

Paths in `random-forest/scripts/` are relative to the script location, so the scripts run from any clone:

```
python random-forest/scripts/randomforest_o3_cabauw.py
```

Data is read from `random-forest/data/raw/` and output is written to `random-forest/results/`.

The notes in `random-forest/notes/` still refer to the old `D:\MAIO\` layout.
