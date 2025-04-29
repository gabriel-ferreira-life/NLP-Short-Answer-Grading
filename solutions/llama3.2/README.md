## Evaluation Metrics

The model was evaluated on a test set containing 30,466 observations. The performance metrics for each class are as follows:

- **Correct:** 94.0% accuracy  
- **Partially Correct:** 35.3% accuracy  
- **Incorrect:** 96.5% accuracy  

### Classification Report

| **Label**           | **Precision** | **Recall** | **F1-Score** | **Support** |
|---------------------|---------------|------------|--------------|-------------|
| Correct             | 0.97          | 0.94       | 0.95         | 13,532      |
| Partially Correct   | 0.16          | 0.35       | 0.22         | 320         |
| Incorrect           | 0.97          | 0.97       | 0.97         | 16,614      |

- **Overall Accuracy:** 95.0%
- **Macro Average:** Precision = 0.70, Recall = 0.75, F1-Score = 0.71  
- **Weighted Average:** Precision = 0.96, Recall = 0.95, F1-Score = 0.95  

### 📊 Confusion Matrix

Each row represents the **true label**, and each column represents the **predicted label**.

|                        | Predicted: Correct | Predicted: Partially Correct | Predicted: Incorrect |
|------------------------|-------------------:|-----------------------------:|----------------------:|
| **Actual: Correct**            | 12,719              | 340                         | 473                   |
| **Actual: Partially Correct** | 99                  | 113                         | 108                   |
| **Actual: Incorrect**         | 317                 | 262                         | 16,035                |

**Interpretation:**
- **Diagonal values** indicate correct predictions per class.
- **Off-diagonal values** are misclassifications.

### Notes

- The model demonstrates strong performance for the **"Correct"** and **"Incorrect"** categories.
- The **"Partially Correct"** class, which has fewer samples, shows lower recall (35%) and F1-score (22%).
- These metrics highlight an area for potential improvement, such as:
  - Gathering more balanced training examples
  - Refining label definitions
  - Considering model-specific tuning or loss reweighting