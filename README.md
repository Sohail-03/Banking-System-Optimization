# Banking System Optimization

## Overview

This project focuses on optimizing a digital banking platform by analyzing customer feedback and conducting competitive analysis. The aim is to improve features based on user sentiment and enhance user engagement.

### Features
- Sentiment analysis of customer feedback
- Feature ranking based on sentiment and frequency
- Competitive analysis against other digital banking platforms
- Visualization of recommended features for improvement

## Installation

To run this project, you'll need Python and the following libraries:

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/Banking-System-Optimization.git
    cd Banking-System-Optimization
    ```

2. Create a virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3. Install required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Place your `customer_feedback.csv` and `competitor_features.csv` datasets in the `data/` folder.

## Files
- `sentiment_analysis.py`: Performs sentiment analysis on customer feedback.
- `feature_ranking.py`: Ranks features based on customer sentiment and mentions.
- `competitive_analysis.py`: Compares features with competitors for optimization opportunities.

## Usage

Run the Python scripts in sequence to analyze and optimize the banking platform:

1. Analyze customer feedback:
    ```bash
    python sentiment_analysis.py
    ```

2. Rank features based on feedback:
    ```bash
    python feature_ranking.py
    ```

3. Run competitive analysis:
    ```bash
    python competitive_analysis.py
    ```
