# Wound-Healing-Analyzer-Model-using-Python

HealTrack: Automated Wound Healing Analyzer

HealTrack is a Python-based project that automates the analysis of wound healing using image processing techniques. The project focuses on quantifying the healing process by measuring the closure of wound areas over time using time-lapse images.

Project Overview

Wound healing is a complex biological process that requires effective monitoring to track recovery. HealTrack processes images from scratch assays to compute the wound area and visualize the healing process. It applies entropy-based filtering and Otsu's thresholding method to segment the wound area and calculate the healing rate. The output includes a time-series plot and linear regression analysis to assess healing trends.

Features

Image Preprocessing: Converts RGB images to grayscale and normalizes the pixel values.
Wound Area Calculation: Uses entropy-based filtering and Otsu’s thresholding for accurate wound segmentation.
Healing Progress Plot: Plots the wound area over time to visualize healing.
Linear Regression Analysis: Computes the slope, intercept, and R² value to quantify the healing rate.

Technologies Used

Programming Language: Python
Libraries: matplotlib, scikit-image, numpy, scipy, glob
