**Vanishing Gradient Problem — Notebook Demo**

- **Description:**
  This folder contains a Jupyter notebook (`vanish.ipynb`) that demonstrates the vanishing gradient problem in deep neural networks using synthetic data (moons dataset) and Keras/TensorFlow. The notebook explores how different activation functions and network depths affect gradient flow and weight updates.

- **Primary Files:**
  - `vanish.ipynb` — Main notebook with code to generate data, build models, train, and analyze gradients/weights.

**Notebook highlights**
- Imports and setup: NumPy, pandas, matplotlib, TensorFlow, Keras, scikit-learn.
- Data generation: Uses `make_moons` for a 2D classification task.
- Visualization: Plots the generated data for intuition.
- Model building: Demonstrates both shallow and deep networks with different activations (sigmoid, relu).
- Training: Shows how weights change before and after training, and how gradients/percent changes are computed.
- Analysis: Compares the effect of depth and activation on gradient magnitude and weight updates.

**Quick Start (Windows PowerShell)**
- Create and activate a virtual environment:

  ```powershell
  python -m venv .venv
  .\.venv\Scripts\Activate.ps1
  ```

- Install dependencies:

  ```powershell
  pip install --upgrade pip
  pip install numpy pandas matplotlib scikit-learn tensorflow keras jupyter
  ```

- Launch Jupyter and open the notebook:

  ```powershell
  jupyter notebook
  # then open `vanish.ipynb` in the browser
  ```

**Tips & suggestions**
- For reproducibility, set random seeds in NumPy and TensorFlow:

  ```python
  import numpy as np
  import tensorflow as tf
  np.random.seed(42)
  tf.random.set_seed(42)
  ```
- Try changing the number of layers and activation functions to see the vanishing gradient effect more clearly.
- Use the notebook's code to compare gradients and percent changes for shallow vs. deep networks.
- Add more visualizations (e.g., plot gradients layer-wise) for deeper analysis.

**Further improvements (optional)**
- Add a `requirements.txt` for exact package versions: `pip freeze > requirements.txt`.
- Add markdown explanations in the notebook for each experiment.
- Export the notebook to a script for automated runs: `jupyter nbconvert --to script vanish.ipynb`.

**Author / Contact**
- Created in this workspace. Reply if you want a `requirements.txt`, more visualizations, or a script version of the notebook.
