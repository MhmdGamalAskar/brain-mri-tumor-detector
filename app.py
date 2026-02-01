import os
import json
import cv2
import numpy as np
import streamlit as st
from PIL import Image

import torch
from detectron2.config import get_cfg
from detectron2.engine import DefaultPredictor
from detectron2.data import MetadataCatalog
from detectron2.utils.visualizer import Visualizer, ColorMode

APP_DIR = os.path.dirname(__file__)
MODEL_PATH = os.path.join(APP_DIR, "model", "model_final.pth")
CFG_PATH   = os.path.join(APP_DIR, "config.yaml")

st.set_page_config(page_title="Brain Tumor Detector", layout="wide")

st.title("🧠 Brain MRI Tumor Detection")
st.caption("Upload an MRI image and the model will draw tumor bounding boxes.")

# ===== Sidebar settings =====
threshold = st.sidebar.slider("Confidence Threshold", 0.05, 0.95, 0.50, 0.05)
st.sidebar.write("Tip: lower threshold → more detections (more FP). Higher → fewer detections (more FN).")

@st.cache_resource
def load_predictor():
    if not os.path.exists(CFG_PATH):
        raise FileNotFoundError(f"Missing config.yaml at: {CFG_PATH}")
    if not os.path.exists(MODEL_PATH):
        raise FileNotFoundError(f"Missing model weights at: {MODEL_PATH}")

    cfg = get_cfg()
    cfg.merge_from_file(CFG_PATH)

    # Ensure correct settings
    cfg.MODEL.WEIGHTS = MODEL_PATH
    cfg.MODEL.DEVICE = "cuda" if torch.cuda.is_available() else "cpu"

    # We keep SCORE_THRESH_TEST = 0.0 and filter ourselves using slider
    cfg.MODEL.ROI_HEADS.SCORE_THRESH_TEST = 0.0
    cfg.MODEL.ROI_HEADS.NUM_CLASSES = 1

    predictor = DefaultPredictor(cfg)

    MetadataCatalog.get("brain_tumor_app").set(thing_classes=["tumor"])
    metadata = MetadataCatalog.get("brain_tumor_app")

    return predictor, metadata, cfg.MODEL.DEVICE

predictor, metadata, device = load_predictor()
st.sidebar.success(f"Model loaded on: {device}")

uploaded = st.file_uploader("Upload MRI image", type=["png", "jpg", "jpeg"])

if uploaded is None:
    st.info("Upload an image to start.")
    st.stop()

# Read image
img_pil = Image.open(uploaded).convert("RGB")
img_rgb = np.array(img_pil)
img_bgr = img_rgb[:, :, ::-1].copy()

# Predict
outputs = predictor(img_bgr)
inst = outputs["instances"].to("cpu")

# Apply threshold
keep = inst.scores >= float(threshold)
inst = inst[keep]

# Visualize
v = Visualizer(img_rgb, metadata=metadata, scale=1.1, instance_mode=ColorMode.IMAGE)
vis_rgb = v.draw_instance_predictions(inst).get_image()

# Layout
c1, c2 = st.columns(2)
with c1:
    st.subheader("Original")
    st.image(img_rgb, use_container_width=True)

with c2:
    st.subheader("Prediction")
    st.image(vis_rgb, use_container_width=True)

# Results
st.markdown("---")
st.subheader("Results")

result_dict = {
    "num_detections": int(len(inst)),
    "scores": inst.scores.tolist() if len(inst) > 0 else [],
    "boxes": inst.pred_boxes.tensor.tolist() if len(inst) > 0 else [],
}

st.write(f"Detections: **{result_dict['num_detections']}**")
st.json(result_dict)

# Optional download JSON
st.download_button(
    "Download JSON report",
    data=json.dumps(result_dict, indent=2),
    file_name="tumor_detection_report.json",
    mime="application/json"
)