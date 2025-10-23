from setuptools import setup, find_packages

# Read the contents of README file
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

# Read requirements
with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="neutts-air",
    version="0.1.0",
    author="Neuphonic",
    author_email="support@neuphonic.com",
    description="World's first super-realistic, on-device, TTS speech language model with instant voice cloning",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/neuphonic/neutts-air",
    project_urls={
        "Bug Tracker": "https://github.com/neuphonic/neutts-air/issues",
        "Documentation": "https://github.com/neuphonic/neutts-air/blob/main/README.md",
        "Source Code": "https://github.com/neuphonic/neutts-air",
        "HuggingFace Model": "https://huggingface.co/neuphonic/neutts-air",
    },
    packages=find_packages(exclude=["examples", "samples", "tests"]),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Multimedia :: Sound/Audio :: Speech",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.11",
    install_requires=requirements,
    extras_require={
        "gguf": ["llama-cpp-python"],
        "onnx": ["onnxruntime"],
        "dev": [
            "pytest",
            "black",
            "flake8",
        ],
    },
    include_package_data=True,
    package_data={
        "neuttsair": ["*.py"],
    },
    keywords=[
        "text-to-speech",
        "tts",
        "voice-cloning",
        "speech-synthesis",
        "audio",
        "deep-learning",
        "pytorch",
        "transformers",
        "on-device",
        "ai",
        "machine-learning",
    ],
)
