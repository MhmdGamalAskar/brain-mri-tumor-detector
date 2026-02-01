# 🧠 Brain MRI Tumor Detection

AI-powered web application for detecting brain tumors in MRI scans using Detectron2 and Faster R-CNN.

## 🌟 Features

- **Real-time Detection**: Upload MRI scans and get instant tumor detection results
- **Interactive Interface**: Adjust confidence threshold and view detailed results
- **High Accuracy**: 89.6% AP@50, 74.5% recall on test set
- **Downloadable Results**: Export annotated images and JSON reports
- **Professional UI**: Clean, medical-grade interface built with Streamlit

## 📊 Model Performance

| Metric | Score |
|--------|-------|
| AP@50 | 89.6% |
| AP@75 | 89.6% |
| Overall AP | 63.8% |
| Recall | 74.5% |
| Small Tumors AP | 73.3% |

## 🚀 Quick Start

### Local Installation

```bash
# Clone repository
git clone https://github.com/yourusername/brain-mri-tumor-detector.git
cd brain-mri-tumor-detector

# Install dependencies
pip install -r requirements.txt

# Run app
streamlit run app.py
```

### Docker (Recommended)

```bash
docker build -t brain-tumor-detector .
docker run -p 8501:8501 brain-tumor-detector
```

## 📁 Project Structure

```
brain-mri-tumor-detector/
├── app.py                 # Streamlit application
├── config.yaml           # Model configuration
├── requirements.txt      # Python dependencies
├── packages.txt         # System packages
├── runtime.txt          # Python version
├── model/
│   └── model_final.pth  # Trained weights (download separately)
├── README.md
└── .streamlit/
    └── config.toml      # Streamlit settings
```

## 📥 Download Model Weights

The trained model weights are too large for GitHub. Download from:
- [Google Drive Link](#) (Replace with your link)
- [Hugging Face Hub](#) (Replace with your link)

Place `model_final.pth` in the `model/` directory.

## 🛠️ Model Details

- **Architecture**: Faster R-CNN
- **Backbone**: ResNet-50-FPN (or X101-FPN if you used that)
- **Framework**: Detectron2 (PyTorch)
- **Training Dataset**: Brain MRI Tumor Dataset (518 training images)
- **Classes**: 1 (tumor)

## 🧪 Usage

1. **Upload Image**: Click "Upload Brain MRI Image" and select a scan
2. **Adjust Threshold**: Use the slider to set detection confidence (default: 0.5)
3. **View Results**: See detected tumors with bounding boxes
4. **Download**: Export annotated image or JSON report

## ⚙️ Configuration

### Confidence Threshold

- **Low (0.3-0.4)**: More detections, higher false positives
- **Medium (0.5-0.6)**: Balanced precision/recall
- **High (0.7+)**: Fewer detections, higher confidence

### Model Settings

Edit `config.yaml` to customize:
- Input image size
- Detection thresholds
- Batch size
- And more...

## 🌐 Deploy

### Streamlit Cloud

1. Push code to GitHub
2. Visit [streamlit.io/cloud](https://streamlit.io/cloud)
3. Connect repository
4. Deploy!

### Hugging Face Spaces

1. Create new Space at [huggingface.co/spaces](https://huggingface.co/spaces)
2. Select "Streamlit" SDK
3. Upload files
4. Done!

### Heroku

```bash
heroku create brain-tumor-detector
git push heroku main
```

## ⚠️ Disclaimer

**This tool is for research and educational purposes only.**

- NOT intended for clinical diagnosis
- Should NOT replace professional medical evaluation
- Always consult qualified healthcare professionals
- Results may contain false positives/negatives

## 📝 License

MIT License - See LICENSE file for details

## 🤝 Contributing

Contributions welcome! Please:
1. Fork the repository
2. Create feature branch
3. Commit changes
4. Push to branch
5. Open pull request

## 📧 Contact

For questions or feedback:
- GitHub Issues: [Report bugs or request features](#)
- Email: your.email@example.com

## 🙏 Acknowledgments

- [Detectron2](https://github.com/facebookresearch/detectron2) by Facebook AI Research
- [Streamlit](https://streamlit.io/) for the amazing framework
- Brain MRI dataset providers

## 📚 Citation

If you use this project in your research, please cite:

```bibtex
@misc{brain-tumor-detector,
  author = {Your Name},
  title = {Brain MRI Tumor Detection using Detectron2},
  year = {2026},
  publisher = {GitHub},
  url = {https://github.com/yourusername/brain-mri-tumor-detector}
}
```

---

Made with ❤️ and 🧠 using AI
