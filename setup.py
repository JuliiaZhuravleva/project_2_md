from setuptools import setup, find_packages

setup(
    name="project_2_md",
    version="0.1",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "pathspec",
    ],
    entry_points={
        "console_scripts": [
            "project_2_md=main:main",
        ],
    },
    author="Your Name",
    author_email="your.email@example.com",
    description="A tool to extract project structure and code to Markdown",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/project_2_md",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)