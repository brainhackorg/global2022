{
  "Title": "containerize bidspm",
  "link_to_issue": "https://github.com/brainhackorg/global2022/issues/70",
  "issue_number": 70,
  "labels": [
    {
      "name": "donostia_esp",
      "description": "Donostia event",
      "color": "d4c5f9"
    },
    {
      "name": "modality:MRI",
      "description": "",
      "color": "1d76db"
    },
    {
      "name": "programming:Matlab",
      "description": "",
      "color": "5319e7"
    },
    {
      "name": "tools:BIDS",
      "description": "",
      "color": "0052cc"
    },
    {
      "name": "project",
      "description": "",
      "color": "f9bc70"
    },
    {
      "name": "tools:fMRIPrep",
      "description": "",
      "color": "0052cc"
    },
    {
      "name": "status:published",
      "description": "",
      "color": "0e8a16"
    },
    {
      "name": "tools:SPM",
      "description": "",
      "color": "0052cc"
    },
    {
      "name": "status:web_ready",
      "description": "",
      "color": "0e8a16"
    }
  ],
  "content": "## Project title:\r\ncontainerize bidspm\r\n\r\n## Project leader:\r\nRemi Gau\r\n\r\n## Email:\r\nremi.gau@gmail.com\r\n\r\n## Collaborators:\r\n\r\n\r\n## Brainhack Global 2022 Event:\r\nBrainHack Donostia\r\n\r\n## Topic:\r\nStatistical modelling\r\n\r\n## What is the purpose of the project:\r\nbidspm is an SPM centric automated pipeline to preprocess BIDS datasets and to run fmri statistical on them by relying on the BIDS stats model for model and contrast specification.Currently the pipeline can run on Matlab and Octave.The pupose of this project is to create containerized versions (Docker, Singularity) of the pipeline to help reusability and reproducibility.\r\n\r\n## Where can participants find key resources to work on this project:\r\nhttps://bidspm.readthedocs.io/en/latest/\r\n\r\n## What stage is the project on:\r\n4\r\n\r\n## Required programming skills for the project:\r\nAdvanced programming level\r\n\r\n## Background knowledge needed  on the topic:\r\nAdvanced\r\n\r\n## Data to use:\r\nThe demos of the pipeline should automatically download and bidsify example data from either OSF or from the SPM website.\r\n\r\n## Link to project repository:\r\nhttps://github.com/cpp-lln-lab/bidspm\r\n\r\n## Goals for Brainhack Donostia 2022:\r\n- improve the octave based docker container to make it run like a bids app\r\n- compile the pipeline matlab code to make it run without requiring a license\r\n\r\n## What will participants learn:\r\n- learn how to use matlab without having to pay for it- learn to use neurodocker to more easily build a docker / singularity recipe for your project\r\n\r\n## Number of collaborators:\r\n2\r\n\r\n## Credit to collaborators:\r\nWe use all contributors to keep track of people's contribution.\r\nContributing: https://github.com/cpp-lln-lab/.github/blob/main/CONTRIBUTING.md\r\n\r\n## Type of project:\r\nCoding methods, Data management, Pipeline development\r\n\r\n## Programming languages:\r\nMatlab, octave, docker\r\n\r\n## Necessary git skills level for the project:\r\nAdvanced (continuous integration)\r\n\r\n## Modality:\r\nfMRI\r\n\r\n## Software suites:\r\nBIDS, fMRIPrep, SPM"
}