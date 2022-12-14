{
  "Title": "Flexibly convert fmriprep confounds to censor files",
  "link_to_issue": "https://github.com/brainhackorg/global2022/issues/138",
  "issue_number": 138,
  "labels": [
    {
      "name": "washingtondc_usa",
      "description": "Washington DC event",
      "color": "d4c5f9"
    },
    {
      "name": "git_skills:0_none",
      "description": "",
      "color": "bfdadc"
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
      "name": "programming:Unix_command_line",
      "description": "",
      "color": "5319e7"
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
      "name": "project_type:data_management",
      "description": "involves programming",
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
      "name": "topic:MR_methodologies",
      "description": "",
      "color": "006b75"
    },
    {
      "name": "topic:reproducible_scientific_methods",
      "description": "",
      "color": "006b75"
    }
  ],
  "content": "### Title\n\nFmriprep to censor\n\n### Leaders\n\nDustin Moraczewski\n\n### Collaborators\n\n_No response_\n\n### Brainhack Global 2022 Event\n\nBrainhack Washington DC\n\n### Project Description\n\nFmriprep gives a smorgasbord of confounds to be used in later processing. While the program provides the option for generating censor files based on a few outlier criteria, I would like to expand on a tool I've written to take in fmriprep derivatives and write new censor files based on new outlier criteria. This tool can be of use to anyone who preprocesses their data with fmriprep and would like to have multiple censor files on hand.\r\n\r\nI have already written some basic code, but I'm quickly learning that it should be more flexible. \r\n\r\nKnowledge of censoring (aka scrubbing) in fmri is not essential, but for more info you can see this publication: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3849338/ \r\n\n\n### Link to project repository/sources\n\nhttps://github.com/dmoracze/HPC_helper_tools/blob/master/bin/fmriprep-to-censor.py\n\n### Goals for Brainhack Global\n\nExpand the functionality of the code I've already written to include any number of outlier criteria. \n\n### Good first issues\n\n1. issue one:\r\n\r\n2. issue two:\r\n\n\n### Communication channels\n\nfmriprep-censor channel on brainhack DC's slack workspace:\r\nhttps://brainhackdc.github.io/2022/index.html \n\n### Skills\n\nPython: beginner to intermediate to expand on the current code\r\nCommand line: basic, to help with testing the code and giving feedback about the user experience\r\n\r\n\n\n### Onboarding documentation\n\nhttps://www.ncbi.nlm.nih.gov/pmc/articles/PMC3849338/\r\n\r\nhttps://fmriprep.org/en/stable/outputs.html#confounds \n\n### What will participants learn?\n\nParticipants will learn about fmri censor files, fmriprep's confounds tables, and basic to intermediate python coding\n\n### Data to use\n\nI will provide some fmriprep derivatives from the open source ABIDE dataset\n\n### Number of collaborators\n\n2\n\n### Credit to collaborators\n\nContributors will be added as collaborators on the project's repo\n\n### Image\n\nLeave this text if you don't have an image yet.\n\n### Type\n\ndata_management, pipeline_development\n\n### Development status\n\n1_basic structure\n\n### Topic\n\nMR_methodologies, reproducible_scientific_methods\n\n### Tools\n\nBIDS, fMRIPrep\n\n### Programming language\n\nPython, unix_command_line\n\n### Modalities\n\nfMRI\n\n### Git skills\n\n0_no_git_skills, 1_commit_push\n\n### Anything else?\n\n_No response_\n\n### Things to do after the project is submitted and ready to review.\n\n- [X] Add a comment below the main post of your issue saying: `Hi @brainhackorg/project-monitors my project is ready!`\n- [X] Twitter-sized summary of your project pitch.",
  "project_url": "https://github.com/dmoracze/HPC_helper_tools/blob/master/bin/fmriprep-to-censor.py",
  "project_description": "\n\nFmriprep gives a smorgasbord of confounds to be used in later processing. While the program provides the option for generating censor files based on a few outlier criteria, I would like to expand on a tool I've written to take in fmriprep derivatives and write new censor files based on new outlier criteria. This tool can be of use to anyone who preprocesses their data with fmriprep and would like to have multiple censor files on hand.\r\n\r\nI have already written some basic code, but I'm quickly learning that it should be more flexible. \r\n\r\nKnowledge of censoring (aka scrubbing) in fmri is not essential, but for more info you can see this publication: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3849338/ \r\n\n\n"
}
