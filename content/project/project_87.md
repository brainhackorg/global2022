{
  "Title": "Lightweight BIDS Layouts for all",
  "link_to_issue": "https://github.com/brainhackorg/global2022/issues/87",
  "issue_number": 87,
  "labels": [
    {
      "name": "git_skills:3_continuous_integration",
      "description": "",
      "color": "bfdadc"
    },
    {
      "name": "git_skills:2_branches_PRs",
      "description": "",
      "color": "bfdadc"
    },
    {
      "name": "git_skills:1_commit_push",
      "description": "",
      "color": "bfdadc"
    },
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
      "name": "project_type:coding_methods",
      "description": "",
      "color": "c5def5"
    },
    {
      "name": "tools:DIPY",
      "description": "",
      "color": "0052cc"
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
      "name": "project_development_status:2_releases_existing",
      "description": "",
      "color": "bfd4f2"
    },
    {
      "name": "status:web_ready",
      "description": "",
      "color": "0e8a16"
    },
    {
      "name": "topic:reproducible_scientific_methods",
      "description": "",
      "color": "006b75"
    },
    {
      "name": "bay_area_usa",
      "description": "Bay area event",
      "color": "d4c5f9"
    }
  ],
  "content": "### Title\n\nLightweight BIDS Layouts for all\n\n### Leaders\n\n| Name | GitHub |\r\n|---|---|\r\n| Chris Markiewicz | @effigies |\r\n| Alejandro de la Vega | @adelavega |\r\n\n\n### Collaborators\n\n| Name | GitHub |\r\n|---|---|\r\n| Your name here... | |\n\n### Brainhack Global 2022 Event\n\nBay Area Brainhack\n\n### Project Description\n\nPyBIDS' [`BIDSLayout`](https://bids-standard.github.io/pybids/generated/bids.layout.BIDSLayout.html#bids.layout.BIDSLayout) currently uses a generic database (sqlite) to represent a BIDS dataset. For large datasets of >100 subjects, this can be time-prohibitive to construct.\r\n\r\n[ancpBIDS](https://ancpbids.readthedocs.io/) has written a custom domain-specific model based at least partially on the [BIDS schema](https://github.com/bids-standard/bids-specification/tree/master/src/schema), which enables a [`BIDSLayout`](https://ancpbids.readthedocs.io/en/latest/api.html#ancpbids.BIDSLayout) that is orders of magnitude faster than PyBIDS'. \r\n\r\nDuring BrainHack Global, we will be working on porting PyBIDS to use ancpBIDS instead of sqlite to represent datasets in memory, and we would be glad to have your help.\n\n### Link to project repository/sources\n\n* PyBIDS: https://github.com/bids-standard/pybids\r\n* ancpBIDS: https://github.com/ANCPLabOldenburg/ancp-bids\n\n### Goals for Brainhack Global\n\n* ancpBIDS-backed BIDSLayout in PyBIDS with 100% backwards compatibility\r\n\r\nWe'll settle for not breaking any apps we test. So let's test some apps.\n\n### Good first issues\n\n1. https://github.com/bids-standard/pybids/issues/831\r\n\r\n2. We're aiming to do some additional prep and break this down into smaller issues\r\n\n\n### Communication channels\n\nhttps://mattermost.brainhack.org/brainhack/channels/pybids\n\n### Skills\n\nIf you want to work on the refactor:\r\n\r\n- Python: moderate\r\n  - Pandas: some experience\r\n  - Pytest: fixtures should be a known concept\r\n\r\nTesting:\r\n\r\n- git/GitHub: basic, able to commit changes and make pull requests against projects\r\n- Python: \n\n### Onboarding documentation\n\nPyBIDS doesn't have contribution guidelines currently. The DIPY developer guidelines are a pretty useful for general best practices: https://dipy.org/documentation/1.5.0/devel/ \r\n\r\nTo get up to speed on the problem, we have a couple PRs that are worth perusing:\r\n\r\n* https://github.com/bids-standard/pybids/pull/851\r\n* https://github.com/bids-standard/pybids/pull/863\n\n### What will participants learn?\n\nThis is going to be an exercise in refactoring and testing. You will learn:\r\n\r\n* To install multiple dependent projects in editable mode\r\n* To run unit tests and use the Python debug shell (pdb)\r\n* To delete hundreds of lines of code, even entire files, with no regrets\r\n\r\nWe will also need bug reports! Testing our proposal out on other projects will involve:\r\n\r\n* Installing the project that uses PyBIDS and patching in an unreleased version of PyBIDS\r\n   * For projects that distribute with Docker, patching packages into the Docker container may be easier than setting up a development environment\r\n* Writing detailed, actionable bug reports that can help others quickly reproduce the issue and identify its cause\n\n### Data to use\n\nIdeally we'll be working with a variety of BIDS datasets to ensure that we test as many components of BIDSLayout as possible, so feel free to bring your own data.\r\n\r\nAnother good source of datasets is https://openneuro.org\n\n### Number of collaborators\n\n3\n\n### Credit to collaborators\n\nPyBIDS contributors are credited in a [Zenodo file](https://github.com/bids-standard/pybids/blob/master/.zenodo.json) and listed as authors on Zenodo releases.\n\n### Image\n\nLeave this text if you don't have an image yet.\n\n### Type\n\ncoding_methods\n\n### Development status\n\n2_releases_existing\n\n### Topic\n\nreproducible_scientific_methods\n\n### Tools\n\nBIDS\n\n### Programming language\n\ncontainerization, documentation, Python\n\n### Modalities\n\nnot_applicable\n\n### Git skills\n\n1_commit_push, 2_branches_PRs, 3_continuous_integration\n\n### Anything else?\n\n_No response_\n\n### Things to do after the project is submitted and ready to review.\n\n- [ ] Add a comment below the main post of your issue saying: `Hi @brainhackorg/project-monitors my project is ready!`\n- [ ] Twitter-sized summary of your project pitch.",
  "project_url": "https://github.com/bids-standard/pybids",
  "project_description": "\n\nPyBIDS' [`BIDSLayout`](https://bids-standard.github.io/pybids/generated/bids.layout.BIDSLayout.html"
}
