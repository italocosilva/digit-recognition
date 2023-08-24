import os
import numpy as np
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "3"
import tensorflow as tf  # noqa: E402


def predict(img):
    # Get file dirname
    dirname = os.path.dirname(__file__)

    # Load model
    model = tf.keras.models.load_model(
        os.path.join(dirname, "..", "artifacts", "model.h5")
    )

    # Resize image before prediction
    img_resize = tf.image.resize(img, (28, 28), method="area").numpy()
    img_resize = tf.image.rgb_to_grayscale(img_resize).numpy()
    img_resize = np.expand_dims(img_resize, 0)

    # Predict
    pred = np.argmax(model.predict(img_resize))

    return pred
