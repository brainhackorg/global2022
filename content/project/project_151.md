{
  "Title": "Scrubbing with clinical samples",
  "link_to_issue": "https://github.com/brainhackorg/global2022/issues/151",
  "issue_number": 151,
  "labels": [
    {
      "name": "toronto_can",
      "description": "Toronto event",
      "color": "d4c5f9"
    },
    {
      "name": "modality:MRI",
      "description": "",
      "color": "1d76db"
    },
    {
      "name": "modality:fMRI",
      "description": "",
      "color": "1d76db"
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
      "name": "tools:fMRIPrep",
      "description": "",
      "color": "0052cc"
    },
    {
      "name": "programming:shell_scripting",
      "description": "",
      "color": "5319e7"
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
      "name": "programming:R",
      "description": "",
      "color": "5319e7"
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
    }
  ],
  "content": "### Title\n\nScrubbing with clinical samples\n\n### Leaders\n\nJu-Chi Yu (Twitter: @juchiyu / Mattermost: @juchiyu) and Jerrold Jeyachandra (Mattermost: @jerdra)\n\n### Collaborators\n\n_No response_\n\n### Brainhack Global 2022 Event\n\nBrainHack Toronto\n\n### Project Description\n\n### Objectives:\r\nWe started this project because two data sets in our lab, SPINS (about schizophrenia) and SPASD (about autism), have strong motion effects that cannot be separated from group effects (SSD vs ASD vs Controls). This could be due to differences in the clinical populations given their symptoms. To alleviate the effect of motion in the analysis, Power et al. (2014) suggested ways to quality control for motion and introduced scrubbing as an additional step before cleaning the data. Scrubbing is a procedure that removes the TRs that have a big motion (as indicated by FD values that exceed a certain threshold) and the TRs between two motion spikes that are too close to each other (the TR section in between two spikes is called the island of which the length can be specified).\r\n\r\nWith SPINS and SPASD in mind, we would like to test if scrubbing is a possible solution to remove the motion effects that confound the group effects. However, schizophrenia and autism patients all tend to move more compared to healthy controls, so it might be worth checking different scrubbing arguments to leverage the quality of the data and the amount of usable data that go into the final analysis.\r\n\r\n### How to participate:\r\nWe have the scripts to 1) run scrubbing and cleaning and 2) plot the figures for quality control (QC). In this project, you can participate in three ways:\r\n\r\n1. Help us improve the documentation and join our discussion of deciding the best scrubbing parameters.\r\n2. Add other features to the procedure (e.g., add options to perform different scrubbing techniques)\r\n3. Bring your own data to perform scrubbing or to QC for motion effects\r\n\r\n### References:\r\n\r\n+ Power's Paper: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3849338/\r\n\r\n+ Lindquist Paper: https://onlinelibrary.wiley.com/doi/epdf/10.1002/hbm.24528\r\n\r\n+ Benchmark Paper: https://www.sciencedirect.com/science/article/pii/S1053811917302288\r\n\r\n+ PR w/Nilearn Code: nilearn/nilearn#3385\n\n### Link to project repository/sources\n\nhttps://github.com/TIGRLab/brainhack-2022-scrubbing\n\n### Goals for Brainhack Global\n\n- [ ] QC for motion and decide on the scrubbing parameters\r\n- [ ] Help improve documentation\n\n### Good first issues\n\n1. issue one: show the length of scans after scrubbing\r\n\r\n2. issue two: add options to scrub by removing a certain number of TRs after each motion spike\r\n\n\n### Communication channels\n\nJoin us on [Discord](https://discord.gg/HC7fumm79B)\n\n### Skills\n\n- Python: Basics\r\n- R: Basics\r\n- Bash: Basics\r\n_Note: These techniques will help if you want to code, but are not required to join the project for discussions._\n\n### Onboarding documentation\n\nhttps://github.com/TIGRLab/brainhack-2022-scrubbing#readme\n\n### What will participants learn?\n\n- What is scrubbing\r\n- The pros and cons of scrubbing for clinical samples\r\n- How to decide on better scrubbing parameters\r\n- Why fMRI is fun (and annoying)\n\n### Data to use\n\nThe project uses private data sets, but you can bring your own data too!\n\n### Number of collaborators\n\n2\n\n### Credit to collaborators\n\nProject contributors are listed on the README.md\n\n### Image\n\nLeave this text if you don't have an image yet.\n\n### Type\n\ndocumentation, pipeline_development, visualization\n\n### Development status\n\n1_basic structure\n\n### Topic\n\nother\n\n### Tools\n\nBIDS, fMRIPrep, Jupyter, other\n\n### Programming language\n\ndocumentation, Python, `R`, shell_scripting\n\n### Modalities\n\nfMRI\n\n### Git skills\n\n1_commit_push\n\n### Anything else?\n\nTopic: pipeline development\r\nTools: RStudio\r\n\n\n### Things to do after the project is submitted and ready to review.\n\n- [X] Add a comment below the main post of your issue saying: `Hi @brainhackorg/project-monitors my project is ready!`\n- [X] Twitter-sized summary of your project pitch.",
  "project_url": "https://github.com/TIGRLab/brainhack-2022-scrubbing",
  "project_description": "\n\n"
}
