<a id="readme-top"></a>

<!-- PROJECT SHIELDS -->
[![Python][python-shield]][python-url]
[![PyTorch][pytorch-shield]][pytorch-url]
[![FastAPI][fastapi-shield]][fastapi-url]
[![Docker][docker-shield]][docker-url]
[![AWS][aws-shield]][aws-url]
[![Unlicense License][license-shield]][license-url]


<!-- PROJECT LOGO -->
<br />
<div align="center">
  <h3 align="center">ML Eye Disease Detector</h3>

  <p align="center">
    An image-classification project that uses a fine-tuned PyTorch model to classify eye images.
    <br />
    <a href="https://eye.jasjeetsingh.me"><strong>Explore the live API »</strong></a>
    <br />
    <br />
    <a href="https://ey-dcdcbff7fd864d5da3e31fb52308fe29.ecs.us-east-2.on.aws/docs">View API documentation</a>
  </p>
</div>


<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#model-workflow">Model Workflow</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>


<!-- ABOUT THE PROJECT -->
## About The Project

ML Eye Disease Detector is a machine-learning project for classifying an eye image as one of three categories: Conjunctivitis, Normal, or Uveitis. The project was created to build practical experience with machine learning, transfer learning, API design, Docker, and AWS deployment while exploring a subject of personal interest.

The trained model is served through a FastAPI application. Users can upload an eye image to the API, and the service returns the predicted class and confidence score. The API is containerized with Docker and hosted on AWS using Amazon ECR and Amazon ECS.

This project is intended for learning and experimentation. It is not a medical diagnostic tool and should not be used as a substitute for professional medical advice.


### Built With

* [![Python][python-shield]][python-url]
* [![PyTorch][pytorch-shield]][pytorch-url]
* [![Torchvision][torchvision-shield]][torchvision-url]
* [![FastAPI][fastapi-shield]][fastapi-url]
* [![Docker][docker-shield]][docker-url]
* [![AWS][aws-shield]][aws-url]

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running, follow the steps below.

### Prerequisites

The project requires Python and Docker for local development and deployment.

* Python 3.11 or later
* pip
* Docker Desktop, if running the containerized API

### Installation

1. Clone the repository.

   ```sh
   git clone https://github.com/jasjeetsingh/MLEyeDiseaseDetector.git
   cd MLEyeDiseaseDetector
   ```

2. Install the Python dependencies.

   ```sh
   pip install -r requirements.txt
   ```

3. Start the API locally from the backend directory.

   ```sh
   cd backend
   uvicorn predictAPI:app --reload
   ```

4. Open the interactive API documentation at [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs).

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- USAGE EXAMPLES -->
## Usage

The API accepts an eye image as a multipart file upload at the `/eyes` endpoint.

```sh
curl -X POST http://127.0.0.1:8000/eyes \
  -F "eyePic=@/path/to/eye-image.jpg"
```

The live service is available at [https://eye.jasjeetsingh.me](https://eye.jasjeetsingh.me), with interactive documentation at [https://eye.jasjeetsingh.me/docs](https://eye.jasjeetsingh.me/docs).

### Docker

Build and run the API locally with Docker:

```sh
docker build -t eye-disease-api -f dockerfile .
docker run --rm -p 8000:8000 eye-disease-api
```

The deployment uses CPU-only PyTorch dependencies so that the container does not include unnecessary CUDA libraries. Images intended for an AWS `linux/amd64` environment should be built for that platform:

```sh
docker buildx build \
  --platform linux/amd64 \
  -t eye-disease-api \
  --load \
  -f dockerfile .
```

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- MODEL WORKFLOW -->
## Model Workflow

The image dataset was sourced from [Kaggle's Eye Diseases Classification dataset](https://www.kaggle.com/datasets/orvile/eye-diseases-classification). It was organized into training and validation sets, with each set containing the Conjunctivitis, Normal, and Uveitis categories.

Training images were augmented with random rotation, horizontal flipping, and color jitter. These transformations are applied to the training set to improve generalization and reduce overfitting. Validation images are kept separate so the model can be evaluated on images it did not use during training.

The project uses transfer learning with ResNet34. ResNet18 initially achieved validation accuracy below 75% despite experimenting with different trainable layers. ResNet34 performed better, reaching approximately 82-84% validation accuracy when only the final layer was trained and approximately 89% after training the third, fourth, and final layers.

The saved model is selected from the point before validation performance begins to decline, helping avoid keeping a model that has started to overfit the training data.

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- ROADMAP -->
## Roadmap

- [x] Train an eye-disease classification model
- [x] Serve predictions through a FastAPI endpoint
- [x] Add image-upload testing
- [x] Containerize the API with Docker
- [x] Deploy the API to AWS
- [ ] Improve validation and test coverage
- [ ] Add model performance metrics and visualizations
- [ ] Improve error handling and API response consistency
- [ ] Add a client application for image uploads

See the [open issues](https://github.com/jasjeetsingh/MLEyeDiseaseDetector/issues) for proposed improvements and future work.

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- CONTRIBUTING -->
## Contributing

Contributions are welcome and appreciated. They are a useful way to improve the project while continuing to learn about machine learning and production API development.

1. Fork the project.
2. Create your feature branch (`git checkout -b feature/AmazingFeature`).
3. Commit your changes (`git commit -m 'Add an AmazingFeature'`).
4. Push to the branch (`git push origin feature/AmazingFeature`).
5. Open a pull request.

<p align="right">(<a href="#readme-top">back to top</a>)</p>




<!-- CONTACT -->
## Contact

Jasjeet Singh - [LinkedIn][linkedin-url]

Project Link: [https://github.com/jasjeetsingh/MLEyeDiseaseDetector](https://github.com/jasjeetsingh/MLEyeDiseaseDetector)

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

* [Kaggle Eye Diseases Classification Dataset](https://www.kaggle.com/datasets/orvile/eye-diseases-classification)
* [PyTorch](https://pytorch.org/)
* [Torchvision](https://pytorch.org/vision/stable/index.html)
* [FastAPI](https://fastapi.tiangolo.com/)
* [Docker](https://www.docker.com/)
* [Amazon ECS](https://aws.amazon.com/ecs/)
* [Amazon ECR](https://aws.amazon.com/ecr/)

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- MARKDOWN LINKS & IMAGES -->
[python-shield]: https://img.shields.io/badge/python-3.11%2B-3776AB.svg?style=for-the-badge&logo=python&logoColor=white
[python-url]: https://www.python.org/
[pytorch-shield]: https://img.shields.io/badge/PyTorch-EE4C2C.svg?style=for-the-badge&logo=pytorch&logoColor=white
[pytorch-url]: https://pytorch.org/
[torchvision-shield]: https://img.shields.io/badge/Torchvision-EE4C2C.svg?style=for-the-badge&logo=pytorch&logoColor=white
[torchvision-url]: https://pytorch.org/vision/stable/index.html
[fastapi-shield]: https://img.shields.io/badge/FastAPI-009688.svg?style=for-the-badge&logo=fastapi&logoColor=white
[fastapi-url]: https://fastapi.tiangolo.com/
[docker-shield]: https://img.shields.io/badge/Docker-2496ED.svg?style=for-the-badge&logo=docker&logoColor=white
[docker-url]: https://www.docker.com/
[aws-shield]: https://img.shields.io/badge/AWS-232F3E.svg?style=for-the-badge&logo=amazonaws&logoColor=white
[aws-url]: https://aws.amazon.com/
[license-shield]: https://img.shields.io/badge/license-Unlicense-blue.svg?style=for-the-badge
[license-url]: https://unlicense.org/
[linkedin-url]: https://www.linkedin.com/
