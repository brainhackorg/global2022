{
  "Title": "Continuous testing of neuroimaging results across pipelines and datasets",
  "link_to_issue": "https://github.com/brainhackorg/global2021/issues/172",
  "issue_number": 172,
  "labels": [
    {
      "name": "programming:containerization",
      "description": "Docker, Singularity",
      "color": "5319e7"
    },
    {
      "name": "programming:documentation",
      "description": "Markdown, Sphinx",
      "color": "5319e7"
    },
    {
      "name": "status:published",
      "description": "",
      "color": "0e8a16"
    },
    {
      "name": "project_development_status:1_basic structure",
      "description": "",
      "color": "bfd4f2"
    },
    {
      "name": "tools:Freesurfer",
      "description": "",
      "color": "0052cc"
    },
    {
      "name": "tools:ANTs",
      "description": "",
      "color": "0052cc"
    },
    {
      "name": "tools:SPM",
      "description": "",
      "color": "0052cc"
    },
    {
      "name": "project_tools_skills:familiar",
      "description": "",
      "color": "c2e0c6"
    },
    {
      "name": "project",
      "description": "",
      "color": "f9bc70"
    },
    {
      "name": "project_type:coding_methods",
      "description": "",
      "color": "c5def5"
    },
    {
      "name": "status:web_ready",
      "description": "",
      "color": "0e8a16"
    },
    {
      "name": "tools:FSL",
      "description": "",
      "color": "0052cc"
    },
    {
      "name": "topic:reproducible_scientific_methods",
      "description": "",
      "color": "006b75"
    },
    {
      "name": "tools:Datalad",
      "description": "",
      "color": "0052cc"
    },
    {
      "name": "programming:Python",
      "description": "",
      "color": "5319e7"
    },
    {
      "name": "tools:AFNI",
      "description": "",
      "color": "0052cc"
    },
    {
      "name": "project_type:documentation",
      "description": "",
      "color": "c5def5"
    },
    {
      "name": "git_skills:2_branches_PRs",
      "description": "",
      "color": "bfdadc"
    },
    {
      "name": "bhg:mtl_can_1",
      "description": "BHG 2021 Montreal event",
      "color": "d4c5f9"
    }
  ],
  "content": "### Title\r\n\r\nContinuous testing of neuroimaging results across pipelines and datasets\r\n\r\n### Leaders\r\n\r\nJacob Sanz-Robinson (Mattermost: @jacobsanz).\r\n\r\n### Collaborators\r\n\r\nJacob Sanz-Robinson  (Mattermost: @jacobsanz).\r\n\r\n### Brainhack Global 2021 Event\r\n\r\nBrainhack Montreal\r\n\r\n### Project Description\r\n\r\n- **What are you doing, for whom, and why?**\r\nNeuroimaging results are sensitive to variations in processing pipelines, contributing to scientific result reproducibility issues. In general, there is no ground truth and it is unclear which pipeline should be applied to data when they yield different results. This project is a software framework capable of helping neuroscientists test whether neuroimaging results are robust across pipelines and replicable across datasets.\r\n\r\n\r\n- **What makes your project special and exciting?**\r\nIt is, to the best of my knowledge, the first attempt at a generalized framework for performing distributed computations in a Continuous Integration setting. This will help scientists systematically evaluate result variability in their experiments. Users can pinpoint biases and discrepancies caused by processing methods and datasets, and quantify their impact on results. In areas where result reproducibility is a concern, the uptake of this novel tool could aid in consolidating knowledge and explaining the uncertainty in the field.\r\n\r\n- **How to get started?**\r\nHave a gander at the project repo!\r\nAny additional functionality is welcome in a Pull Request. If you are familiar with any neuroimaging pipelines, building Boutiques descriptors for them is extremely useful. Functions to visualize the data or retrieve/process summary statistics are also welcome!\r\n\r\n- **Where to find key resources?**\r\nThe project repo (readme) is a good place to start. Otherwise feel free to message me by e-mail, Mattermost, or homing pigeon (if it's clean).\r\n\r\n### Link to project repository/sources\r\n\r\n[https://github.com/jacobsanz97/NDR-CI](https://github.com/jacobsanz97/NDR-CI)\r\n\r\n### Goals for Brainhack Global\r\n\r\nMy personal efforts will be directed at a mechanism to repopulate the cache files by querying the CBRAIN distributed computation system in case they become corrupted or lost.\r\nIf there is additional time I will work on making prettier data visualizations and including statistical summaries.\r\nIf other people join, then hopefully we can containerize a pipeline or two, and make more progress on the visualizations.\r\n\r\n### Good first issues\r\n\r\n1. Issue one: Create a Boutiques descriptors for any neuroimaging pipeline of your choice!\r\n\r\n2. Issue two: Create visualizations that could help us compare results across pipelines and datasets.\r\n\r\n3. Issue three: Any additional functionality you may deem useful!\r\n\r\n4. Issue four: cache file repopulation/retrieval (this is what I will be working on).\r\n\r\n\r\n### Communication channels\r\n\r\n[https://mattermost.brainhack.org/brainhack/channels/neuro-repro-ci](https://mattermost.brainhack.org/brainhack/channels/neuro-repro-ci)\r\n\r\n### Skills\r\n\r\n- Python\r\n- Command line/bash\r\n- Any neuroimaging pipelines! (I have been dealing with FSL and FreeSurfer so far...If you are familiar with ANTs, MINC tools, CIVET, or SPM, you will be extremely useful!)\r\n- Containers/Boutiques.\r\n- Data visualization (You don't need to be advanced! Some basic experience in matplotlib/seaborn/plotly or the desire to learn these is more than enough!)\r\n\r\n### Onboarding documentation\r\n\r\nSee readme: [https://github.com/jacobsanz97/NDR-CI](https://github.com/jacobsanz97/NDR-CI)\r\n\r\n### What will participants learn?\r\n\r\nIf you wish to learn about containerization, running neuroimaging pipelines, or data visualization...This is a good project to pick up the basics of one or more of these :) .\r\n\r\n### Data to use\r\n\r\n_No response_\r\n\r\n### Number of collaborators\r\n\r\nmore\r\n\r\n### Credit to collaborators\r\n\r\nContributors will be listed in the project ReadMe.\r\n\r\n### Image\r\n\r\n![Copy of Copy of Diagram April2021 (4)](https://user-images.githubusercontent.com/47538991/144759835-b7ca7902-f4ee-4a88-b78c-817ab8754505.png)\r\n\r\n### Type\r\n\r\ncoding_methods\r\n\r\n### Development status\r\n\r\n1_basic structure\r\n\r\n### Topic\r\n\r\nreproducible_scientific_methods\r\n\r\n### Tools\r\n\r\nAFNI, ANTs, Datalad, Freesurfer, FSL, other\r\n\r\n### Programming language\r\n\r\nPython\r\n\r\n### Modalities\r\n\r\nother, not_applicable\r\n\r\n### Git skills\r\n\r\n2_branches_PRs\r\n\r\n### Anything else?\r\n\r\nFor Tools: Any and all tools and/or neuroimaging pipelines are useful to integrate into the project! At the same time, none are strictly necessary if you wish to focus your development efforts on another aspect of the framework.\r\n\r\n### Things to do after the project is submitted and ready to review.\r\n\r\n- [X] Add a comment below the main post of your issue saying: `Hi @brainhackorg/project-monitors my project is ready!`\r\n- [ ] Twitter-sized summary of your project pitch.",
  "project_url": "https://github.com/jacobsanz97/NDR-CI",
  "project_description": "\r\n\r\n- **What are you doing, for whom, and why?**\r\nNeuroimaging results are sensitive to variations in processing pipelines, contributing to scientific result reproducibility issues. In general, there is no ground truth and it is unclear which pipeline should be applied to data when they yield different results. This project is a software framework capable of helping neuroscientists test whether neuroimaging results are robust across pipelines and replicable across datasets.\r\n\r\n\r\n- **What makes your project special and exciting?**\r\nIt is, to the best of my knowledge, the first attempt at a generalized framework for performing distributed computations in a Continuous Integration setting. This will help scientists systematically evaluate result variability in their experiments. Users can pinpoint biases and discrepancies caused by processing methods and datasets, and quantify their impact on results. In areas where result reproducibility is a concern, the uptake of this novel tool could aid in consolidating knowledge and explaining the uncertainty in the field.\r\n\r\n- **How to get started?**\r\nHave a gander at the project repo!\r\nAny additional functionality is welcome in a Pull Request. If you are familiar with any neuroimaging pipelines, building Boutiques descriptors for them is extremely useful. Functions to visualize the data or retrieve/process summary statistics are also welcome!\r\n\r\n- **Where to find key resources?**\r\nThe project repo (readme) is a good place to start. Otherwise feel free to message me by e-mail, Mattermost, or homing pigeon (if it's clean).\r\n\r\n"
}