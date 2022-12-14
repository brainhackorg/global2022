{
  "Title": "Removing pink noise (1/f) in LFP across different electrophysiological recording systems",
  "link_to_issue": "https://github.com/brainhackorg/global2022/issues/125",
  "issue_number": 125,
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
      "name": "project_type:coding_methods",
      "description": "",
      "color": "c5def5"
    },
    {
      "name": "tools:MNE",
      "description": "",
      "color": "0052cc"
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
      "name": "project_type:pipeline_development",
      "description": "",
      "color": "c5def5"
    },
    {
      "name": "project_development_status:0_concept_no_content",
      "description": "",
      "color": "bfd4f2"
    },
    {
      "name": "status:web_ready",
      "description": "",
      "color": "0e8a16"
    },
    {
      "name": "topic:neural_encoding",
      "description": "",
      "color": "006b75"
    }
  ],
  "content": "### Title\r\n\r\nRemoving pink noise (1/f) in LFP across different electrophysiological recording systems\r\n\r\n### Leaders\r\n\r\nLaura L\u00d3PEZ GALDO, Shrabasti JANA, Camila LOSADA, Hasnae AGOURAM, Cl\u00e9o SCHOEFFEL, Nilanjana NANDI\r\n\r\n### Collaborators\r\n\r\n_No response_\r\n\r\n### Brainhack Global 2022 Event\r\n\r\nBrainhack Marseille\r\n\r\n### Project Description\r\n\r\n- What are you doing, for whom, and why?\r\n- What makes your project special and exciting?\r\n- How to get started?\r\n- Where to find key resources?\r\n\r\nWe will try to remove the aperiodic noise found in the spectrum of the LFP data using the _fooof_ module (https://github.com/fooof-tools/fooof). We will parametrize our signals, the aperiodic and periodic components and make some comparison across the different frequency bands. \r\n\r\nWe have data from EEG human recordings, LFP monkey utah array recordings and monkey laminar intracranial recordings across different areas. We want to see the effect of pink noise in each of the different setups and try to clean the signal.\r\n\r\nSome related literature can be found in the following links:\r\n\r\n- Parametrizing aperiodic component: https://doi.org/10.1038/s41593-020-00744-x\r\n- Gamma-Beta frequency interactions: www.pnas.org/cgi/doi/10.1073/pnas.1710323115 and 10.1162/jocn_a_01600\r\n\r\n### Link to project repository/sources\r\n\r\nhttps://github.com/lauralopezgaldo/Brainhack-Marseille-2022\r\n\r\n### Goals for Brainhack Global\r\n\r\n- Working together with different datasets\r\n- Compare the different results\r\n- Share the analysis code\r\n\r\n### Good first issues\r\n\r\n1. Get the spectrum from the raw data\r\n\r\n2. Parametrize the 1/f\r\n\r\n3. Frequency band comparison\r\n\r\n\r\n### Communication channels\r\n\r\nhttps://mattermost.brainhack.org/brainhack/channels/bhg22-marseille-pinknoise\r\n\r\n### Skills\r\n\r\n- python coding: 70%\r\n- sharing ideas: 60%\r\n- electrophysiological data: 100%\r\n- literature review: 30%\r\n\r\n### Onboarding documentation\r\n\r\n_No response_\r\n\r\n### What will participants learn?\r\n\r\nParticipants will learn to parametrize the spectrum of electrophysiological data and undertand the meaning of pink noise.\r\n\r\n### Data to use\r\n\r\n_No response_\r\n\r\n### Number of collaborators\r\n\r\nmore\r\n\r\n### Credit to collaborators\r\n\r\nEveryone will be able to use the data we have and we'll make the code open for everyone.\r\n\r\n### Image\r\n\r\n![image](https://user-images.githubusercontent.com/44520889/204252282-aea67e58-00c8-4dc3-85f0-0b15a0ef8e07.png)\r\n\r\n\r\n### Type\r\n\r\ncoding_methods, pipeline_development\r\n\r\n### Development status\r\n\r\n0_concept_no_content\r\n\r\n### Topic\r\n\r\nneural_encoding\r\n\r\n### Tools\r\n\r\nJupyter, MNE\r\n\r\n### Programming language\r\n\r\nPython\r\n\r\n### Modalities\r\n\r\nEEG, other\r\n\r\n### Git skills\r\n\r\n1_commit_push\r\n\r\n### Anything else?\r\n\r\n_No response_\r\n\r\n### Things to do after the project is submitted and ready to review.\r\n\r\n- [X] Add a comment below the main post of your issue saying: `Hi @brainhackorg/project-monitors my project is ready!`\r\n- [ ] Twitter-sized summary of your project pitch.",
  "project_url": "https://github.com/lauralopezgaldo/Brainhack-Marseille-2022",
  "project_description": "\r\n\r\n- What are you doing, for whom, and why?\r\n- What makes your project special and exciting?\r\n- How to get started?\r\n- Where to find key resources?\r\n\r\nWe will try to remove the aperiodic noise found in the spectrum of the LFP data using the _fooof_ module (https://github.com/fooof-tools/fooof). We will parametrize our signals, the aperiodic and periodic components and make some comparison across the different frequency bands. \r\n\r\nWe have data from EEG human recordings, LFP monkey utah array recordings and monkey laminar intracranial recordings across different areas. We want to see the effect of pink noise in each of the different setups and try to clean the signal.\r\n\r\nSome related literature can be found in the following links:\r\n\r\n- Parametrizing aperiodic component: https://doi.org/10.1038/s41593-020-00744-x\r\n- Gamma-Beta frequency interactions: www.pnas.org/cgi/doi/10.1073/pnas.1710323115 and 10.1162/jocn_a_01600\r\n\r\n"
}
