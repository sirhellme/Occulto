# Occulto (Exoplanet Analysis Platform)

## Overview
Detects and characterizes exoplanet transit from raw satellite data (TESS/Kepler).

## Technical Motivation
Implements real astrophysical data processing; involves signal processing and statistical modelling.

## Difficulty
Research-level

## Duration
5 months

## Core Features
Light curve ingestion, detrending (Savitzy-Golay/GP), Box Least Squares (BLS) transit search.

## Advanced Features
Multi-planet system deblending, MCMC parameter estimation, habitable zone calculation.

## Architecture
Modular Python pipeline. Data ingestion -> Preprocessing -> Search -> Validation -> Reporting.

## Tech Stack
Python, NumPy, SciPy, Lightkurve, Astropy, Matplotlib, PyMC (for MCMC).

## Learning Objectives
Time-series analysis, Fourier transforms, Bayesian statistics, astrophysical transit models.

## Milestones
- M1: Data pipeline;
- M2: Detrending;
- M3: BLS implementation;
- M4: Validation;
- M5: Documentation/UI;

## Testing
Validate against known exoplanet database (NASA Exoplanet)

## GitHub
Data processing notebooks, core library, benchmark results, gallery of detected planets.

## Done
Pipeline reproduces parameters of 10+ confirmed planets within 5% error.
