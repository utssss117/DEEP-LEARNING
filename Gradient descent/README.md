**Gradient Descent — Notebook & Demo**

- **Description:** The `Gradient descent` folder contains a Jupyter notebook (`descent.ipynb`) that demonstrates training a small neural network on a toy/real dataset (`Social_Network_Ads.csv`) using TensorFlow/Keras. The notebook covers data loading, preprocessing (scaling), model definition, training with different batch sizes/epochs, and basic loss visualization.

- **Primary Files:**
  - `descent.ipynb` — The notebook implementing preprocessing, a Keras `Sequential` model, and training experiments.
  - `Social_Network_Ads.csv` — Dataset used by the notebook (expected in the same folder).

**Notebook highlights (what each section does)**
- Data import and selection of relevant columns (`Age`, `EstimatedSalary`, `Purchased`).
- Feature scaling using `sklearn.preprocessing.StandardScaler`.
- Construction of a small ANN with `keras.Sequential` and `Dense` layers.
- Model compilation and training with different `batch_size` and `epochs` settings.
- Plotting training loss (example: `plt.plot(history.history['loss'])`).

**Quick Start (Windows PowerShell)**
- Create and activate a virtual environment:

  ```powershell
  python -m venv .venv
  .\.venv\Scripts\Activate.ps1
  ```

- Install typical dependencies used by the notebook (adjust versions if needed):

  ```powershell
  pip install --upgrade pip
  pip install numpy pandas scikit-learn matplotlib tensorflow jupyter
  ```

- Launch Jupyter and open the notebook:

  ```powershell
  jupyter notebook
  # then open `descent.ipynb` in the browser
  ```

**Reproducibility & tips**
- Set random seeds for reproducible results (NumPy, TensorFlow, and scikit-learn). Example in Python:

  ```python
  import numpy as np
  import tensorflow as tf
  np.random.seed(42)
  tf.random.set_seed(42)
  ```

- If `history.history['loss']` is plotted and you want to compare training/validation, also plot `history.history['val_loss']`.
- Consider adding `model.save(...)` or callbacks (e.g., `EarlyStopping`, `ModelCheckpoint`) for longer experiments.

**Suggested improvements (optional)**
- Add a `requirements.txt` for exact package versions: `pip freeze > requirements.txt`.
- Add brief comments in notebook cells describing why specific batch sizes or epoch values are chosen.
- Export the notebook to a script for headless runs using `jupyter nbconvert --to script descent.ipynb`.

**Author / Contact**
- Created in this workspace. Reply if you want me to also add `requirements.txt`, add example saved model checkpoints, or convert the notebook to a runnable Python script.
