{
  "Title": "Automatic detection of spiking motifs in neurobiological data",
  "link_to_issue": "https://github.com/brainhackorg/global2022/issues/120",
  "issue_number": 120,
  "labels": [
    {
      "name": "marseille_fra",
      "description": "Marseille event",
      "color": "d4c5f9"
    },
    {
      "name": "git_skills:1_commit_push",
      "description": "",
      "color": "bfdadc"
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
      "name": "tools:Jupyter",
      "description": "",
      "color": "0052cc"
    },
    {
      "name": "status:published",
      "description": "",
      "color": "0e8a16"
    },
    {
      "name": "topic:deep_learning",
      "description": "",
      "color": "006b75"
    },
    {
      "name": "status:web_ready",
      "description": "",
      "color": "0e8a16"
    },
    {
      "name": "project_type:method_development",
      "description": "",
      "color": "c5def5"
    },
    {
      "name": "topic:machine_learning",
      "description": "",
      "color": "006b75"
    },
    {
      "name": "topic:neural_decoding",
      "description": "",
      "color": "006b75"
    },
    {
      "name": "topic:information_theory",
      "description": "",
      "color": "006b75"
    },
    {
      "name": "topic:neural_networks",
      "description": "",
      "color": "006b75"
    },
    {
      "name": "topic:physiology",
      "description": "",
      "color": "006b75"
    },
    {
      "name": "topic:statistical_modelling",
      "description": "",
      "color": "006b75"
    }
  ],
  "content": "### Title\r\n\r\nAutomatic detection of spiking motifs in neurobiological data\r\n\r\n### Leaders\r\n\r\n- [Matthieu Gilson](https://matthieugilson.eu) - https://github.com/MatthieuGilson\r\n- [Laurent Perrinet](https://laurentperrinet.github.io) - https://github.com/LaurentPerrinet\r\n\r\n### Collaborators\r\n\r\n* Hugo Ladret\r\n* George Abitbol\r\n\r\n### Brainhack Global 2022 Event\r\n\r\nBrainhack Marseille\r\n\r\n### Project Description\r\n\r\nThe study of spatio-temporal correlated activity patterns is very active in several fields related to neuroscience, like machine learning in vision [(Muller Nat Rev Neurosci 2018)](https://pubmed.ncbi.nlm.nih.gov/29563572/) and neuronal representations and processing [(Shahidi Nat Neurosci 2019)](https://pubmed.ncbi.nlm.nih.gov/31110324/). **This project aims to develop a method for the automated detection of repeating spiking motifs, possibly noisy, in ongoing activity.** A diversity of formalizations and detection methods have been proposed and we will focus on several example measures for event/spike trains, to be compared on both synthetic and real data. \r\n\r\nAn implementation could be based on autodifferentiable networks as implemented in Python libraries like pytorch. This framework allows for the tuning of parameters with specific architectures like convolutional layers that can capture various timescales in spike patterns (e.g. latencies) in an automated fashion. Another recent tool based on the estimation of firing probability for a range of latencies has been proposed [(Grimaldi ICIP 2022)](https://laurentperrinet.github.io/publication/grimaldi-22-bc/grimaldi-22-bc.pdf). This will be compared with existing approaches like Elephant\u2019s [SPADE](https://elephant.readthedocs.io/en/latest/reference/spade.html) or decoding techniques based on computed statistics computed on smoothed spike trains (adapted from time series processing, see [(Lawrie, biorxiv](https://doi.org/10.1101/2021.04.30.441789)).\r\n\r\nOne part concerns the generation of realistic synthetic data producing spike trains  which include spiking motifs with specific latencies or comodulation of firing rate. The goal is to test how these different structures, which rely on specific assumptions about e.g. stationarity or independent firing probability across time, can be captured by different detection methods. \r\n\r\n**Bring you real data to analyze them!** We will also provide data from electrophysiology.\r\n\r\n\r\n### Link to project repository/sources\r\n\r\n- [**Github repo**](https://github.com/SpikeAI/2022-11_brainhack_DetecSpikMotifs)\r\n\r\n- review on [Precise spiking motifs in neurobiological and neuromorphic data](https://laurentperrinet.github.io/publication/grimaldi-22-polychronies/grimaldi-22-polychronies.pdf)\r\n- [Grimaldi](https://laurentperrinet.github.io/author/antoine-grimaldi/), Besnainou,\u00a0Ladret, Perrinet\u00a0(2022).\u00a0[Learning heterogeneous delays of spiking neurons for motion detection](https://laurentperrinet.github.io/publication/grimaldi-22-icip/).\u00a0Proceedings of ICIP 2022. https://laurentperrinet.github.io/publication/grimaldi-22-bc/grimaldi-22-bc.pdf\r\n- [Polychronies](https://laurentperrinet.github.io/grant/polychronies/) grant\r\n\r\n### Goals for Brainhack Global\r\n\r\n- Code to generate various models of synthetic data (time series of spikes/events) with embedded patterns\r\n- Knowledge in signal processing & high-order statistics (correlation)\r\n- Tool for quantitative comparison of detection methods for correlated patterns \r\n\r\n\r\n### Good first issues\r\n\r\n1. issue one: generate synthetic model for raster plots\r\n\r\n2. issue two: design detection method knowing these motifs\r\n\r\n3. issue three: supervised learning\r\n\r\n4. issue four: unsupervised learning\r\n\r\n\r\n### Communication channels\r\n\r\nhttps://mattermost.brainhack.org/brainhack/channels/bhg22-marseille-detecspikmotifs\r\n\r\n### Skills\r\n\r\n- Interest in analyzing spiking activity: 100%\r\n- Programming Python (numpy, scikit-learn, pytorch): 70%\r\n- Data (spike trains, event time series): 50%\r\n- Sharing concepts and ideas (supervised/unsupervised learning, stochastic processes): 40%\r\n\r\n\r\n### Onboarding documentation\r\n\r\n_No response_\r\n\r\n### What will participants learn?\r\n\r\n- electro-physiology, spiking activity\r\n- correlation/synchrony measures\r\n- high-order statistics\r\n- supervised/unsupervised learning\r\n- stochastic processes\r\n\r\n### Data to use\r\n\r\n_No response_\r\n\r\n### Number of collaborators\r\n\r\n4\r\n\r\n### Credit to collaborators\r\n\r\nSee the README file on the project's github repo.\r\n\r\n### Image\r\n\r\n<img width=\"557\" alt=\"image\" src=\"https://user-images.githubusercontent.com/381808/202470026-cfb5ff2d-9310-4506-9350-fd61953a6e8d.png\">\r\n\r\n\r\n### Type\r\n\r\nmethod_development\r\n\r\n### Development status\r\n\r\n1_basic structure\r\n\r\n### Topic\r\n\r\nbayesian_approaches, deep_learning, information_theory, machine_learning, neural_decoding, neural_networks, statistical_modelling\r\n\r\n### Tools\r\n\r\nJupyter\r\n\r\n### Programming language\r\n\r\nPython\r\n\r\n### Modalities\r\n\r\nother\r\n\r\n### Git skills\r\n\r\n1_commit_push\r\n\r\n### Anything else?\r\n\r\nCome to us!\r\n\r\n### Things to do after the project is submitted and ready to review.\r\n\r\n- [x] Add a comment below the main post of your issue saying: `Hi @brainhackorg/project-monitors my project is ready!`\r\n- [x] Mastodon~~Twitter~~-sized summary of your project pitch.: \"This project aims to develop a method for the automated detection of repeating spiking motifs, possibly noisy, in ongoing activity.\"",
  "project_url": "https://github.com/SpikeAI/2022-11_brainhack_DetecSpikMotifs",
  "project_description": "\r\n\r\nThe study of spatio-temporal correlated activity patterns is very active in several fields related to neuroscience, like machine learning in vision [(Muller Nat Rev Neurosci 2018)](https://pubmed.ncbi.nlm.nih.gov/29563572/) and neuronal representations and processing [(Shahidi Nat Neurosci 2019)](https://pubmed.ncbi.nlm.nih.gov/31110324/). **This project aims to develop a method for the automated detection of repeating spiking motifs, possibly noisy, in ongoing activity.** A diversity of formalizations and detection methods have been proposed and we will focus on several example measures for event/spike trains, to be compared on both synthetic and real data. \r\n\r\nAn implementation could be based on autodifferentiable networks as implemented in Python libraries like pytorch. This framework allows for the tuning of parameters with specific architectures like convolutional layers that can capture various timescales in spike patterns (e.g. latencies) in an automated fashion. Another recent tool based on the estimation of firing probability for a range of latencies has been proposed [(Grimaldi ICIP 2022)](https://laurentperrinet.github.io/publication/grimaldi-22-bc/grimaldi-22-bc.pdf). This will be compared with existing approaches like Elephant\u2019s [SPADE](https://elephant.readthedocs.io/en/latest/reference/spade.html) or decoding techniques based on computed statistics computed on smoothed spike trains (adapted from time series processing, see [(Lawrie, biorxiv](https://doi.org/10.1101/2021.04.30.441789)).\r\n\r\nOne part concerns the generation of realistic synthetic data producing spike trains  which include spiking motifs with specific latencies or comodulation of firing rate. The goal is to test how these different structures, which rely on specific assumptions about e.g. stationarity or independent firing probability across time, can be captured by different detection methods. \r\n\r\n**Bring you real data to analyze them!** We will also provide data from electrophysiology.\r\n\r\n\r\n"
}
