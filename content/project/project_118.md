{
  "Title": "Neural encoding of acoustic features during speech and music perception: traduction of matlab code into python",
  "link_to_issue": "https://github.com/brainhackorg/global2022/issues/118",
  "issue_number": 118,
  "labels": [
    {
      "name": "marseille_fra",
      "description": "Marseille event",
      "color": "d4c5f9"
    },
    {
      "name": "programming:Matlab",
      "description": "",
      "color": "5319e7"
    },
    {
      "name": "modality:EEG",
      "description": "",
      "color": "1d76db"
    },
    {
      "name": "programming:documentation",
      "description": "Markdown, Sphinx",
      "color": "5319e7"
    },
    {
      "name": "project",
      "description": "",
      "color": "f9bc70"
    },
    {
      "name": "programming:Python",
      "description": "",
      "color": "5319e7"
    },
    {
      "name": "tools:MNE",
      "description": "",
      "color": "0052cc"
    },
    {
      "name": "project_development_status:1_basic structure",
      "description": "",
      "color": "bfd4f2"
    },
    {
      "name": "project_type:documentation",
      "description": "",
      "color": "c5def5"
    },
    {
      "name": "status:published",
      "description": "",
      "color": "0e8a16"
    },
    {
      "name": "project_type:pipeline_development",
      "description": "",
      "color": "c5def5"
    },
    {
      "name": "status:web_ready",
      "description": "",
      "color": "0e8a16"
    },
    {
      "name": "topic:neural_decoding",
      "description": "",
      "color": "006b75"
    }
  ],
  "content": "## Title\r\n\r\nNeural encoding of acoustic and semantic features during speech and music perception: Matlab to Python code translation\r\n\r\n## Leaders\r\n\r\nBruno Giordano (INT) :\r\nhttps://github.com/brungio/bhack_td\r\nhttps://twitter.com/brungio\r\nhttps://framateam.org/blgnatsou/messages/@bruno.giordano\r\n\r\nGiorgio Marinato (INT) :\r\nhttps://github.com/neurogima\r\nhttps://twitter.com/neurogima\r\nmattermost: @neurogima\r\n\r\n## Collaborators\r\n\r\nBenjamin Morillon (CR INS - https://github.com/DCP-INS)\r\nNad\u00e8ge Marin (IE, INS)\r\nArnaud Zalta (PhD student, INS)\r\n\r\n## Brainhack Global 2022 Event\r\n\r\nBrainhack Marseille\r\n\r\n## Project Description\r\n\r\nIn everyday life, humans are particularly attuned to listening to two particular types of sound: speech and music. We apply a novel analysis method to shed light on how the brain is almost effortlessly able to use acoustic features to assign meaning to sounds. To do so, we use an original cross-validated Representational Similarity Analyses (RSA) approach implemented in Matlab to estimate the similarity between acoustic or semantic features of an auditory stream (speech, music) and neural activity (here intracranial EEG recordings decomposed into frequency bands).\r\n\r\n## Link to project repository/sources\r\n\r\nhttps://github.com/brungio/bhack_td\r\n\r\n## Goals for Brainhack Global\r\n\r\nThe main goal of this project is to translate the Matlab code into Python:\r\n- translate the temporal folding on the neural signal in Python\r\n- identify the python libraries to calculate different distances metrics\r\n- translate the cross-validation method\r\n- implement native plotting using the Python libraries (e.g. Seaborn, matplotlib, etc)\r\n\r\n## Good first issues\r\n\r\n- identify python libraries that can speed up the code translation effort\r\n\r\n## Communication channels\r\n\r\nhttps://mattermost.brainhack.org/brainhack/channels/brainhack_marseille_2022_speech_music_representation\r\n\r\n## Skills\r\n\r\npython coding\r\nRepresentational Similarity Analyses (RSA)\r\nCross-validation (train-test-validate)\r\nintracranial EEG signal processing\r\nsharing data analyses ideas\r\n\r\n## Onboarding documentation\r\n\r\n## What will participants learn?\r\n\r\nto analyse intracranial EEG data\r\nto perform cross-validation procedures to estimate the neural encoding of different acoustic features\r\n\r\n## Data to use\r\n\r\nWe will provide a sample of a dataset of iEEG recordings.\r\n\r\n## Number of collaborators\r\n\r\nfrom 3 to 10\r\n\r\n## Credit to collaborators\r\n\r\nAcknowledgment in the code and in the Github repo.\r\n\r\n## Image\r\n\r\nLeave this text if you don't have an image yet.\r\n\r\n## Type\r\n\r\npipeline_development\r\n\r\n## Development status\r\n\r\n1_basic structure\r\n\r\n## Topic\r\n\r\nneural_decoding\r\n\r\n## Tools\r\n\r\nMNE, RSAtoolbox (github.com/rsagroup/rsatoolbox), Scikit Learn\r\n\r\n## Programming language\r\n\r\nPython, Matlab\r\n\r\n## Modalities\r\n\r\nintracranial EEG\r\n\r\n## Git skills\r\n\r\nBasic git workflow: fork, branches, commit and pull request"
}
