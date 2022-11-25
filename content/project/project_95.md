{
  "Title": "Normalisation and artefact correction toolkit for fibre photometry data",
  "link_to_issue": "https://github.com/brainhackorg/global2022/issues/95",
  "issue_number": 95,
  "labels": [
    {
      "name": "australasia_aus",
      "description": "Australasia event",
      "color": "d4c5f9"
    },
    {
      "name": "modality:behavioral",
      "description": "",
      "color": "1d76db"
    },
    {
      "name": "git_skills:0_none",
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
      "name": "project_type:visualisation",
      "description": "",
      "color": "c5def5"
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
      "name": "topic:systems_neuroscience",
      "description": "",
      "color": "006b75"
    }
  ],
  "content": "### Title\n\nNormalisation and artefact correction toolkit for fibre photometry data\n\n### Leaders\n\nChris Nolan (Mattermost: @cnolan | Mastodon: @cnolan@fediscience.org)\n\n### Collaborators\n\nPhil Jean-Richard Dit Bressel\r\nThomas Burton\r\nJ Bertran-Gonzalez\r\nChelsea Goulton\n\n### Brainhack Global 2022 Event\n\nBrainhack Australasia\n\n### Project Description\n\nStudies using optic fibres to record real-time fluorescent biosensors in-vivo are now commonplace, yet despite a large degree of overlap in the techniques used to filter and normalise this data, there is a surprising lack of open tooling around such analysis. This project is an effort to fill this gap by providing flexible Python-based implementations of common normalisation and artefact correction procedures for fluorescent biosensors, along with some basic analysis tools.\n\n### Link to project repository/sources\n\nTBA\n\n### Goals for Brainhack Global\n\n* Generate a comparison of normalisation methods for GCaMP and dLight data\r\n* Create a semi-automated artefact rejection method if required (for uncorrectable artefacts)\r\n* Create an interactive data viewer that can show raw and corrected / normalised data, and allows overlays of rejected signal periods\r\n* Outline a standardised structure for raw and processed data along with the necessary associated metadata \u2014 ideally BIDS-friendly\n\n### Good first issues\n\n1. Install the skeleton package from Github repository (to be added)\r\n2. Test existing basic normalisation method using a variety of fibre photometry data\r\n3. Research and document typical biosensor normalisation methods\r\n\n\n### Communication channels\n\nhttps://mattermost.brainhack.org/brainhack/channels/fibrepy\n\n### Skills\n\nPrimarily, some knowledge of fluorescent biosensor normalisation and analysis procedures will be useful. We'll be predominantly working in Python, but there will be tasks for all levels of Python competency.\r\n\r\nBonus useful skills:\r\n* Signal processing (we'll be filtering and fitting timeseries data)\r\n* Python interactive visualisation (bokeh / holoviews / vispy)\r\n* BIDS experience - while we won't be attempting to add an official BIDS extension for fibre photometry in this project, we will try to produce data structures that are broadly in line with the BIDS format\r\n\n\n### Onboarding documentation\n\n_No response_\n\n### What will participants learn?\n\n* Data manipulation in Python (numpy / pandas)\r\n* Signal filtering in Python\r\n* Basic GitHub collaboration techniques\n\n### Data to use\n\nBYO fibre & behavioural data - we'll create a repository of useful examples.\n\n### Number of collaborators\n\nmore\n\n### Credit to collaborators\n\nProject contributors will be listed on the repository README.\n\n### Image\n\nLeave this text if you don't have an image yet.\n\n### Type\n\ndata_management, method_development, pipeline_development, visualization\n\n### Development status\n\n1_basic structure\n\n### Topic\n\nsystems_neuroscience\n\n### Tools\n\nBIDS\n\n### Programming language\n\nPython\n\n### Modalities\n\nbehavioral, other\n\n### Git skills\n\n0_no_git_skills, 1_commit_push, 2_branches_PRs\n\n### Anything else?\n\nModalities: fibre_photometry\r\n\n\n### Things to do after the project is submitted and ready to review.\n\n- [X] Add a comment below the main post of your issue saying: `Hi @brainhackorg/project-monitors my project is ready!`\n- [ ] Twitter-sized summary of your project pitch.",
  "project_description": "\n\nStudies using optic fibres to record real-time fluorescent biosensors in-vivo are now commonplace, yet despite a large degree of overlap in the techniques used to filter and normalise this data, there is a surprising lack of open tooling around such analysis. This project is an effort to fill this gap by providing flexible Python-based implementations of common normalisation and artefact correction procedures for fluorescent biosensors, along with some basic analysis tools.\n\n"
}
