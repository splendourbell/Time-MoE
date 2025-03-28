from setuptools import setup, find_packages

setup(
    name="timemoe",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "pyyaml",
        "numpy",
        "pandas",
        "torch",
        "scikit-learn",
        "transformers==4.40.1",
        "datasets==2.18.0",
        "accelerate==0.28.0"
    ],
    author="Time-MoE",
    description="Time-MoE implementation",
    url="https://github.com/Time-MoE/Time-MoE",
    python_requires=">=3.6",
)
