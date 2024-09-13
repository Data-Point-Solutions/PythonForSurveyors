# SurveyMath and GIS Applications

Welcome to the **SurveyMath and GIS Applications** project! This is an ongoing
open-source collection of Python scripts aimed at solving common land surveying
and GIS (Geographic Information Systems) problems. Our goal is to provide
easy-to-use tools for land surveyors, GIS professionals, and anyone interested
in these fields.

## 🚀 Project Status

**This project is a work in progress.** New scripts and features will be
continuously added as the project evolves. Contributions are highly encouraged,
and collaborators are welcome to fork the repository, add new functionalities,
and help improve existing scripts.

## 📜 Overview

The repository currently includes Python scripts for various survey math
solutions, such as:

- Coordinate transformations
- Distance and bearing calculations
- Area and perimeter calculations
- Intersection point determinations
- Curve solutions
- Leveling calculations
- Traverse adjustments
- Vertical curve solutions

These scripts are designed to simplify complex calculations and provide
straightforward, reliable results for everyday use in land surveying and GIS
applications.

## 🛠 Features

- **User-Friendly:** Scripts include GUI options for ease of use without needing
  a command-line interface.
- **Extensible:** Designed for expansion, allowing for easy addition of new
  scripts and functionality.
- **Open Source:** Licensed under the MIT License, ensuring that the code can be
  freely used and modified.

## 📁 Project Structure

. |-- NOTES.md |-- README.md |-- TODO.md |-- assets |-- commitlint.config.js |--
docker | |-- Dockerfile |
`-- docker-compose.yml |-- docs |   |-- GIS |   |-- calculators |   |   |-- BearAz.md |   |   |-- Curve.md |   |   |-- DMS.md |   |   |-- LatDep.md |   |   |-- RecArea.md |   |`--
Traverse.md |
`-- overview.md |-- package.json |-- python |   |-- GIS |   |-- calculators |   |   |-- BearAz.py |   |   |-- Curve.py |   |   |-- DMS.py |   |   |-- LatDep.py |   |   |-- RecArea.py |   |`--
Traverse.py | `-- requirements.txt `-- yarn.lock

4 directories, 7 files

## 🐳 Running with Docker

To run the project using Docker, follow these steps:

1. **Ensure Docker is installed:** You need Docker installed on your machine.
   You can download it from
   [Docker's official site](https://www.docker.com/products/docker-desktop/).

2. **Clone the Repository:**

   ```bash
   git clone https://github.com/your-username/PythonForSurveyors.git
   cd PythonForSurveyors
   ```

3. **Navigate to the Docker Directory:**

   ```bash
   cd docker
   ```

4. **Build and Run with Docker Compose:**

   ```bash
   docker-compose up --build
   ```

   This command will:

   - Build the Docker image using the provided `Dockerfile`.
   - Start the container with the project mounted as a volume, allowing you to
     edit files on your host machine and run them in the container seamlessly.

5. **Access the Container:**

   - You can access the running container's shell using:

     ```bash
     docker exec -it <container_name> /bin/bash
     ```

   - Replace `<container_name>` with the actual name of the container, which you
     can find using:

     ```bash
     docker ps
     ```

## 💡 How to Contribute

We welcome contributions from the community! If you'd like to contribute, here's
how you can get started:

1. **Fork the Repository:** Click on the "Fork" button at the top right corner
   of this page.
2. **Clone Your Fork:** Clone your forked repository to your local machine.

   ```bash
   git clone https://github.com/your-username/SurveyMath-GIS-Applications.git
   ```

3. **Create a New Branch:** Create a branch for your feature or fix.

   ```bash
   git checkout -b feature/your-feature-name
   ```

4. **Make Changes:** Commit your changes to your branch, ensuring all commits
   are signed.
5. **Commit Changes:** Commit your changes with clear and concise commit
   messages.

   ```bash
   git commit -m "Add feature: description of the feature"
   ```

6. **Push Changes:** Push your changes to your fork.

   ```bash
   git push origin feature/your-feature-name
   ```

7. **Create a Pull Request:** Go to the original repository on GitHub and click
   "New Pull Request" targeting the `develop` branch of the main repository to
   submit your changes.

   - Ensure all checks pass and request a review.

8. **Review Process:** Await approval from a repository maintainer before
   merging.

## Branch Protection

- **No Direct Pushes to `main`:** All changes must go through pull requests.
- **Protected Branches:** Both `main` and `develop` are protected branches
  requiring pull request reviews and passing checks.
- **Signing Commits:** All commits must be signed using a GPG key.

Thank you for contributing!

## 📝 Requirements

To run the scripts without Docker, you'll need:

- Python 3.x
- Required Python libraries (specified in the `requirements.txt` file located in
  the `python` directory)

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file
for more information.

## 🤝 Acknowledgments

A big thank you to all contributors and the open-source community for their
ongoing support!

---

Feel free to reach out if you have any questions or suggestions. Let's build
something great together!
