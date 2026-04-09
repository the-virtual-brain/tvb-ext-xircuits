# Parameter Space Exploration (PSE) Examples

## Overview

The PSE components enable automated parameter sweeps over TVB model parameters.

## Quick Start

    cd examples
    python parameter_space_exploration_demo.py

## Components

### Range Components
- PSELinspaceRange - Linear spacing
- PSEArangeRange - Arithmetic progression
- PSEValueList - Custom values

### Grid Component
- PSEParameterGrid - 2D Cartesian product

### Metric Components
- PSEResultCollector - Accumulates results
- PSEGlobalVariance - Computes variance
- PSEVarianceOfVariance - Variance of variance

## Files
- README_PSE.md - This file
- parameter_space_exploration_demo.py - Working demo
- outputs/ - Generated visualizations
