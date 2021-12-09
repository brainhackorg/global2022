{
  "Title": "Niviz: Configurable quality control image generation and rating",
  "link_to_issue": "https://github.com/brainhackorg/global2021/issues/181",
  "issue_number": 181,
  "labels": [
    {
      "name": "programming:Java",
      "description": "Java",
      "color": "5319e7"
    },
    {
      "name": "programming:documentation",
      "description": "Markdown, Sphinx",
      "color": "5319e7"
    },
    {
      "name": "project_development_status:1_basic structure",
      "description": "",
      "color": "bfd4f2"
    },
    {
      "name": "topic:data_visualisation",
      "description": "",
      "color": "006b75"
    },
    {
      "name": "project",
      "description": "",
      "color": "f9bc70"
    },
    {
      "name": "tools:BIDS",
      "description": "",
      "color": "0052cc"
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
      "name": "modality:DWI",
      "description": "",
      "color": "1d76db"
    },
    {
      "name": "tools:fMRIPrep",
      "description": "",
      "color": "0052cc"
    },
    {
      "name": "programming:Python",
      "description": "",
      "color": "5319e7"
    },
    {
      "name": "git_skills:1_commit_push",
      "description": "",
      "color": "bfdadc"
    },
    {
      "name": "project_type:documentation",
      "description": "",
      "color": "c5def5"
    },
    {
      "name": "tools:Nipype",
      "description": "",
      "color": "0052cc"
    },
    {
      "name": "modality:MRI",
      "description": "",
      "color": "1d76db"
    },
    {
      "name": "git_skills:2_branches_PRs",
      "description": "",
      "color": "bfdadc"
    },
    {
      "name": "modality:fMRI",
      "description": "",
      "color": "1d76db"
    },
    {
      "name": "project_type:visualisation",
      "description": "",
      "color": "c5def5"
    },
    {
      "name": "bhg:toronto_can_1",
      "description": "BHG 2021 Toronto event",
      "color": "d4c5f9"
    },
    {
      "name": "programming:html_css",
      "description": "",
      "color": "5319e7"
    },
    {
      "name": "programming:Javascript",
      "description": "Javascript",
      "color": "5319E7"
    }
  ],
  "content": "### Title\r\n\r\nNiviz: Configurable quality control image generation and rating\r\n\r\n### Leaders\r\n\r\nJerrold Jeyachandra @jerdra\r\n\r\n### Collaborators\r\n\r\nNone\r\n\r\n### Brainhack Global 2021 Event\r\n\r\nBrainHack Toronto\r\n\r\n### Project Description\r\n\r\nThe process of QCing is universally boring, terrible and inefficient. \r\n\r\n### The Problem with QC\r\n\r\n1. Most pipelines people write and use don't generate QC images, especially those that are as user-friendly as widely established pipelines such as fMRIPREP\r\n\r\n2. Even then, the QC images that are generated do not necessarily match how users end up QC'ing and rating images. \r\n\r\n3. Most of the time users must figure out their own way to record and organize their QC results, this is incredibly variable across individuals. Your collaborator might use differing definitions, organizational principles, and file formats for storing their QC results than you.\r\n\r\n4. Comparing rated images is often slow, manual and therefore painful. Often-times users have doubt about their ratings and would want to compare it to other images with the same rating. Doing this is often a very manual process (i.e lookup similar QC ratings on your spreadsheet, find file, open both images and compare)\r\n\r\n### The Solution - Niviz\r\n\r\nNiviz is a simple, configurable Python-based tool that:\r\n\r\n1. Enables researchers to generate QC images using a simple YAML file for *any* pipeline that outputs NIFTI, GIFTI or CIFTI images\r\n2. Provides a small web application using `niviz-rater` that collects generated QC images (or any set of images organized in a BIDS-style dataset!!!) into an interactive QC interface. In addition, QC can be configured to suit the user's needs using (yet another) simple YAML file.\r\n\r\n### Link to project repository/sources\r\n\r\n#### QC image generation\r\n\r\nhttps://github.com/TIGRab/niviz\r\n\r\n#### QC web application\r\n\r\nhttps://github.com/jerdra/niviz-rater\r\n\r\n### Goals for Brainhack Global\r\n\r\nBoth niviz and niviz-rater are relatively new projects and therefore require a bit of maintenance and organizational effort. The primary goals are as follows:\r\n\r\n####  Niviz\r\n\r\n1. Bug squashing \r\n2. Implementing a YAML schema validation step\r\n3. Documentation: Getting started, tutorials (including OSF dataset)\r\n4. Writing unit-tests\r\n\r\n#### Niviz Rater\r\n\r\n1. Unit tests\r\n2. Several UX feature additions\r\n3. Basic feature additions to one day support collaborative QC rating and analysis (i.e inter-rater reliability)\r\n4. Maintenance (packaging)\r\n5. Documentation: Tutorials, getting started, API  \r\n\r\n### Good first issues\r\n\r\nIssues can be found under:\r\n\r\nhttps://github.com/TIGRLab/niviz/issues\r\n\r\nhttps://github.com/jerdra/niviz-rater/issues\r\n\r\nLook for the `good first issue` label for easy topics!\r\n\r\n### Communication channels\r\n\r\nhttps://mattermost.brainhack.org/brainhack/channels/brainhack-toronto\r\n\r\nWe'll probably create our own channel if this picks up interest :)\r\n\r\n### Skills\r\n\r\nThe repositories are primarily written in Python and Javascript, these components are mostly independent from one another so you don't need to know both!\r\n\r\n#### Python\r\n\r\nIntermediate\r\n- Nibabel\r\n- Nilearn\r\n- Nipype (just the interfaces)\r\n- Image plotting\r\n\r\n#### Git\r\n\r\nIntermediate \r\n\r\n#### Javascript\r\n\r\nFamiliarity with Svelte framework is preferred. I'm still learning myself!\r\n\r\n* Happy to accommodate learning individuals for a few of the smaller issues as long as you're proficient in google-fu and willing to learn :) \r\n\r\n### Onboarding documentation\r\n\r\n[Contributing](https://github.com/TIGRLab/niviz/blob/main/CONTRIBUTING.md)\r\n\r\n### What will participants learn?\r\n\r\nDepending on which repository you contribute to:\r\n\r\n#### Niviz\r\n\r\n1. Python unit testing\r\n2. nipype interface development\r\n3. niworkflows image generation\r\n\r\n\r\n#### Niviz-Rater\r\n\r\n1. Svelte javascript framework\r\n2. `Bottle` for building python web applications\r\n3. Light database work with `peewee`\r\n4. Python packaging\r\n5. Unit testing\r\n\r\n### Data to use\r\n\r\nAs part of contributing to the documentation efforts of this project, we'd like to host some OSF sample data. \r\n\r\n#### Niviz\r\n\r\nSome image data from a pipeline like fMRIPrep\r\n\r\n#### Niviz-Rater\r\n\r\nSome QC image data so that users can play around with writing a YAML specification file and using the QC interface\r\n\r\n### Number of collaborators\r\n\r\n3\r\n\r\n### Credit to collaborators\r\n\r\nProject contributers will be included using the GitHub allcontributors bot. I'm still setting this up :see_no_evil: \r\n\r\n### Image\r\n\r\nLeave this text if you don't have an image yet.\r\n\r\n### Type\r\n\r\ncoding_methods, documentation, visualization\r\n\r\n### Development status\r\n\r\n1_basic structure\r\n\r\n### Topic\r\n\r\ndata_visualisation, other\r\n\r\n### Tools\r\n\r\nNipype, other\r\n\r\n### Programming language\r\n\r\ndocumentation, Python, html_css, javascript\r\n\r\n### Modalities\r\n\r\nDWI, fMRI, MRI\r\n\r\n### Git skills\r\n\r\n1_commit_push, 2_branches_PRs\r\n\r\n### Anything else?\r\n\r\n_No response_\r\n\r\n### Things to do after the project is submitted and ready to review.\r\n\r\n- [X] Add a comment below the main post of your issue saying: `Hi @brainhackorg/project-monitors my project is ready!`\r\n- [x] Twitter-sized summary of your project pitch.",
  "project_description": "\r\n\r\nThe process of QCing is universally boring, terrible and inefficient. \r\n\r\n"
}